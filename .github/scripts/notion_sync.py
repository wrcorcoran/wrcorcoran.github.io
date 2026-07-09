#!/usr/bin/env python3
"""Sync published Notion pages to Jekyll _writing/ collection."""

import os
import re
import requests
from pathlib import Path
from datetime import datetime
from notion_client import Client

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
WRITING_DIR = REPO_ROOT / "_writing"
IMG_DIR = REPO_ROOT / "assets" / "img" / "writing"

WRITING_DIR.mkdir(exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def rich_text_to_md(rich_texts):
    result = ""
    for rt in rich_texts:
        if rt.get("type") == "equation":
            result += f"${rt['equation']['expression']}$"
            continue
        text = rt["plain_text"]
        ann = rt.get("annotations", {})
        href = rt.get("href")
        if ann.get("code"):
            text = f"`{text}`"
        if ann.get("bold"):
            text = f"**{text}**"
        if ann.get("italic"):
            text = f"*{text}*"
        if ann.get("strikethrough"):
            text = f"~~{text}~~"
        if href:
            text = f"[{text}]({href})"
        result += text
    return result


def download_image(url, slug, block_id):
    ext = url.split("?")[0].rsplit(".", 1)[-1].lower()
    if ext not in {"jpg", "jpeg", "png", "gif", "webp", "svg"}:
        ext = "jpg"
    img_dir = IMG_DIR / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{block_id.replace('-', '')[:8]}.{ext}"
    local_path = img_dir / filename
    if not local_path.exists():
        resp = requests.get(url, stream=True, timeout=30)
        resp.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
    return f"/assets/img/writing/{slug}/{filename}"


def blocks_to_md(blocks, slug, indent=0):
    lines = []
    prefix = "  " * indent

    for block in blocks:
        btype = block["type"]
        children = block.get("_children", [])

        if btype == "paragraph":
            text = rich_text_to_md(block["paragraph"]["rich_text"])
            lines.append(f"{prefix}{text}" if text else "")

        elif btype in ("heading_1", "heading_2", "heading_3"):
            level = int(btype[-1]) + 1  # Notion H1→##, H2→###, H3→####
            text = rich_text_to_md(block[btype]["rich_text"])
            lines.append(f"{prefix}{'#' * level} {text}")

        elif btype == "bulleted_list_item":
            text = rich_text_to_md(block["bulleted_list_item"]["rich_text"])
            lines.append(f"{prefix}- {text}")
            if children:
                lines.extend(blocks_to_md(children, slug, indent + 1))

        elif btype == "numbered_list_item":
            text = rich_text_to_md(block["numbered_list_item"]["rich_text"])
            lines.append(f"{prefix}1. {text}")
            if children:
                lines.extend(blocks_to_md(children, slug, indent + 1))

        elif btype == "code":
            lang = block["code"].get("language", "")
            text = rich_text_to_md(block["code"]["rich_text"])
            lines += [f"```{lang}", text, "```"]

        elif btype == "equation":
            expr = block["equation"]["expression"]
            lines += ["$$", expr, "$$"]

        elif btype == "quote":
            text = rich_text_to_md(block["quote"]["rich_text"])
            lines.append(f"> {text}")

        elif btype == "callout":
            text = rich_text_to_md(block["callout"]["rich_text"])
            lines.append(f"> {text}")

        elif btype == "divider":
            lines.append("---")

        elif btype == "image":
            img = block["image"]
            url = img["file"]["url"] if img["type"] == "file" else img["external"]["url"]
            caption = rich_text_to_md(img.get("caption", []))
            try:
                local_path = download_image(url, slug, block["id"])
                lines.append(f"![{caption or 'image'}]({local_path})")
            except Exception as e:
                print(f"  Warning: failed to download image {block['id']}: {e}")
                lines.append(f"<!-- image download failed: {block['id']} -->")

        elif btype == "table" and children:
            for ri, row in enumerate(children):
                cells = row["table_row"]["cells"]
                row_md = "| " + " | ".join(rich_text_to_md(c) for c in cells) + " |"
                lines.append(row_md)
                if ri == 0:
                    lines.append("| " + " | ".join("---" for _ in cells) + " |")

        elif btype == "toggle":
            text = rich_text_to_md(block["toggle"]["rich_text"])
            lines.append(f"**{text}**")
            if children:
                lines.extend(blocks_to_md(children, slug, indent + 1))

        lines.append("")  # blank line after each block

    return lines


def fetch_blocks(block_id):
    blocks, cursor = [], None
    while True:
        kwargs = {"block_id": block_id}
        if cursor:
            kwargs["start_cursor"] = cursor
        resp = notion.blocks.children.list(**kwargs)
        for block in resp["results"]:
            if block.get("has_children") and block["type"] != "table":
                block["_children"] = fetch_blocks(block["id"])
            elif block.get("has_children"):
                block["_children"] = fetch_blocks(block["id"])
            blocks.append(block)
        if not resp.get("has_more"):
            break
        cursor = resp["next_cursor"]
    return blocks


def prop(props, name):
    p = props.get(name, {})
    ptype = p.get("type")
    if ptype == "title":
        return "".join(rt["plain_text"] for rt in p["title"])
    if ptype == "rich_text":
        return "".join(rt["plain_text"] for rt in p["rich_text"])
    if ptype == "select":
        return p["select"]["name"] if p.get("select") else ""
    if ptype == "date":
        return p["date"]["start"] if p.get("date") else ""
    if ptype == "multi_select":
        return [item["name"] for item in p.get("multi_select", [])]
    return ""


def sync():
    pages, cursor = [], None
    while True:
        kwargs = {
            "database_id": NOTION_DATABASE_ID,
            "filter": {"property": "Status", "select": {"equals": "Published"}},
        }
        if cursor:
            kwargs["start_cursor"] = cursor
        resp = notion.databases.query(**kwargs)
        pages.extend(resp["results"])
        if not resp.get("has_more"):
            break
        cursor = resp["next_cursor"]

    print(f"Found {len(pages)} published page(s)")

    for page in pages:
        props = page["properties"]
        title = prop(props, "Name")
        category = prop(props, "Category")
        description = prop(props, "Description")
        date_str = prop(props, "Date")
        slug = prop(props, "Slug") or slugify(title)
        projects = prop(props, "Project")

        if not date_str:
            print(f"  Skipping '{title}' — no Date set")
            continue
        if not slug:
            print(f"  Skipping page with no title and no slug")
            continue

        date = datetime.fromisoformat(date_str).date()
        filename = f"{date}-{slug}.md"
        filepath = WRITING_DIR / filename

        # Build frontmatter
        title_safe = title.replace('"', '\\"')
        desc_safe = description.replace('"', '\\"')
        fm = [
            "---",
            "layout: writing_post",
            f'title: "{title_safe}"',
            f"date: {date}",
            f"category: {category}",
            f'description: "{desc_safe}"',
        ]
        if projects:
            fm.append("project:")
            for p in projects:
                fm.append(f"  - {p}")
        fm += ["---", ""]

        blocks = fetch_blocks(page["id"])
        content = blocks_to_md(blocks, slug)
        new_text = "\n".join(fm + content) + "\n"

        if filepath.exists() and filepath.read_text() == new_text:
            print(f"  Unchanged: {filename}")
            continue

        filepath.write_text(new_text)
        print(f"  Written: {filename}")


if __name__ == "__main__":
    sync()
