#!/usr/bin/env python3
"""Sync published Notion pages to Jekyll _writing/ collection."""

import os
import re
import requests
from pathlib import Path
from datetime import datetime

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
WRITING_DIR = REPO_ROOT / "_writing"
IMG_DIR = REPO_ROOT / "assets" / "img" / "writing"

WRITING_DIR.mkdir(exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Notion API helpers
# ---------------------------------------------------------------------------

def notion_post(path, body=None):
    resp = requests.post(
        f"https://api.notion.com/v1/{path}",
        headers=HEADERS,
        json=body or {},
    )
    resp.raise_for_status()
    return resp.json()


def notion_get(path, params=None):
    resp = requests.get(
        f"https://api.notion.com/v1/{path}",
        headers=HEADERS,
        params=params or {},
    )
    resp.raise_for_status()
    return resp.json()


def query_database(filter_body=None, start_cursor=None):
    body = {}
    if filter_body:
        body["filter"] = filter_body
    if start_cursor:
        body["start_cursor"] = start_cursor
    return notion_post(f"databases/{NOTION_DATABASE_ID}/query", body)


def get_block_children(block_id, start_cursor=None):
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return notion_get(f"blocks/{block_id}/children", params)


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def get_prop(props, name):
    p = props.get(name, {})
    ptype = p.get("type")
    if ptype == "title":
        return "".join(rt["plain_text"] for rt in p.get("title", []))
    if ptype == "rich_text":
        return "".join(rt["plain_text"] for rt in p.get("rich_text", []))
    if ptype == "select":
        sel = p.get("select")
        return sel["name"] if sel else ""
    if ptype == "date":
        d = p.get("date")
        return d["start"] if d else ""
    if ptype == "multi_select":
        return [item["name"] for item in p.get("multi_select", [])]
    return ""


def download_image(url, slug, block_id):
    ext = url.split("?")[0].rsplit(".", 1)[-1].lower()
    if ext not in {"jpg", "jpeg", "png", "gif", "webp", "svg"}:
        ext = "jpg"
    img_dir = IMG_DIR / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{block_id.replace('-', '')[:8]}.{ext}"
    local_path = img_dir / filename
    if not local_path.exists():
        r = requests.get(url, stream=True, timeout=30)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return f"/assets/img/writing/{slug}/{filename}"


# ---------------------------------------------------------------------------
# Block → Markdown conversion
# ---------------------------------------------------------------------------

def rich_text_to_md(rich_texts):
    result = ""
    for rt in rich_texts:
        if rt.get("type") == "equation":
            result += f"${rt['equation']['expression']}$"
            continue
        text = rt.get("plain_text", "")
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


def blocks_to_md(blocks, slug, indent=0):
    lines = []
    prefix = "  " * indent

    for block in blocks:
        btype = block["type"]
        data = block.get(btype, {})
        children = block.get("_children", [])

        if btype == "paragraph":
            text = rich_text_to_md(data.get("rich_text", []))
            lines.append(f"{prefix}{text}" if text else "")

        elif btype in ("heading_1", "heading_2", "heading_3"):
            level = int(btype[-1]) + 1  # H1→##, H2→###, H3→####
            text = rich_text_to_md(data.get("rich_text", []))
            lines.append(f"{prefix}{'#' * level} {text}")

        elif btype == "bulleted_list_item":
            text = rich_text_to_md(data.get("rich_text", []))
            lines.append(f"{prefix}- {text}")
            if children:
                lines.extend(blocks_to_md(children, slug, indent + 1))

        elif btype == "numbered_list_item":
            text = rich_text_to_md(data.get("rich_text", []))
            lines.append(f"{prefix}1. {text}")
            if children:
                lines.extend(blocks_to_md(children, slug, indent + 1))

        elif btype == "code":
            lang = data.get("language", "")
            text = rich_text_to_md(data.get("rich_text", []))
            lines += [f"```{lang}", text, "```"]

        elif btype == "equation":
            lines += ["$$", data.get("expression", ""), "$$"]

        elif btype == "quote":
            text = rich_text_to_md(data.get("rich_text", []))
            lines.append(f"> {text}")

        elif btype == "callout":
            text = rich_text_to_md(data.get("rich_text", []))
            lines.append(f"> {text}")

        elif btype == "divider":
            lines.append("---")

        elif btype == "image":
            url = (
                data["file"]["url"]
                if data.get("type") == "file"
                else data.get("external", {}).get("url", "")
            )
            caption = rich_text_to_md(data.get("caption", []))
            if url:
                try:
                    local_path = download_image(url, slug, block["id"])
                    lines.append(f"![{caption or 'image'}]({local_path})")
                except Exception as e:
                    print(f"  Warning: image download failed ({block['id']}): {e}")
                    lines.append(f"<!-- image download failed: {block['id']} -->")

        elif btype == "table" and children:
            for ri, row in enumerate(children):
                cells = row.get("table_row", {}).get("cells", [])
                row_md = "| " + " | ".join(rich_text_to_md(c) for c in cells) + " |"
                lines.append(row_md)
                if ri == 0:
                    lines.append("| " + " | ".join("---" for _ in cells) + " |")

        elif btype == "toggle":
            text = rich_text_to_md(data.get("rich_text", []))
            lines.append(f"**{text}**")
            if children:
                lines.extend(blocks_to_md(children, slug, indent + 1))

        lines.append("")

    return lines


def fetch_blocks(block_id):
    blocks, cursor = [], None
    while True:
        resp = get_block_children(block_id, cursor)
        for block in resp.get("results", []):
            if block.get("has_children"):
                block["_children"] = fetch_blocks(block["id"])
            blocks.append(block)
        if not resp.get("has_more"):
            break
        cursor = resp["next_cursor"]
    return blocks


# ---------------------------------------------------------------------------
# Main sync
# ---------------------------------------------------------------------------

def sync():
    pages, cursor = [], None
    filter_body = {"property": "Status", "select": {"equals": "Published"}}

    while True:
        resp = query_database(filter_body, cursor)
        pages.extend(resp.get("results", []))
        if not resp.get("has_more"):
            break
        cursor = resp["next_cursor"]

    print(f"Found {len(pages)} published page(s)")

    for page in pages:
        props = page["properties"]
        title = get_prop(props, "Name")
        category = get_prop(props, "Category")
        description = get_prop(props, "Description")
        date_str = get_prop(props, "Date")
        slug = get_prop(props, "Slug") or slugify(title)
        projects = get_prop(props, "Project")

        if not date_str:
            print(f"  Skipping '{title}' — no Date set")
            continue
        if not slug:
            print(f"  Skipping page with no title and no slug")
            continue

        date = datetime.fromisoformat(date_str).date()
        filename = f"{date}-{slug}.md"
        filepath = WRITING_DIR / filename

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
