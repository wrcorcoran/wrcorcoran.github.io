---
layout: page
permalink: /writing/
title: writing
nav: true
nav_order: 3
---

<div class="writing-controls mt-3 mb-4">
  <input type="text" id="writing-search" class="form-control form-control-sm mb-2" placeholder="search...">
  <div>
    <button class="writing-filter-btn active" data-filter="all">all</button>
    <button class="writing-filter-btn" data-filter="technical">technical</button>
    <button class="writing-filter-btn" data-filter="musings">musings</button>
  </div>
</div>

<ul id="writing-list" class="list-unstyled">
{% assign all_posts = site.writing | sort: "date" | reverse %}
{% for post in all_posts %}
  <li class="writing-item mb-3"
      data-category="{{ post.category }}"
      data-title="{{ post.title | downcase }}"
      data-description="{{ post.description | downcase | default: '' }}">
    <div>
      <small class="text-muted mr-2">{{ post.date | date: "%b %Y" }}</small>
      <small class="writing-tag">{{ post.category }}</small>
      <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a>
    </div>
    {% if post.description %}
    <div><small class="text-muted">{{ post.description }}</small></div>
    {% endif %}
  </li>
{% endfor %}
</ul>

<p id="writing-empty" style="display:none;" class="text-muted font-italic">No posts match your filter or search.</p>

<style>
.writing-filter-btn {
  margin-right: 0.3rem;
  padding: 0.2rem 0.65rem;
  font-size: 0.8rem;
  border: 1px solid #aaa;
  border-radius: 3px;
  background: transparent;
  color: #666;
  cursor: pointer;
}
.writing-filter-btn.active,
.writing-filter-btn:hover {
  background: #444;
  color: #fff;
  border-color: #444;
}
.writing-tag {
  display: inline-block;
  font-size: 0.7rem;
  padding: 0.05rem 0.4rem;
  border-radius: 3px;
  background: #eee;
  color: #555;
  margin-right: 0.35rem;
  text-transform: lowercase;
}
html[data-theme="dark"] .writing-filter-btn { border-color: #666; color: #aaa; }
html[data-theme="dark"] .writing-filter-btn.active,
html[data-theme="dark"] .writing-filter-btn:hover { background: #bbb; color: #111; border-color: #bbb; }
html[data-theme="dark"] .writing-tag { background: #333; color: #bbb; }
</style>

<script>
(function () {
  var search = document.getElementById("writing-search");
  var btns = document.querySelectorAll(".writing-filter-btn");
  var items = document.querySelectorAll(".writing-item");
  var empty = document.getElementById("writing-empty");
  var activeFilter = "all";

  function update() {
    var q = search.value.toLowerCase().trim();
    var visible = 0;
    items.forEach(function (item) {
      var catOk = activeFilter === "all" || item.dataset.category === activeFilter;
      var textOk = !q || item.dataset.title.includes(q) || item.dataset.description.includes(q);
      item.style.display = catOk && textOk ? "" : "none";
      if (catOk && textOk) visible++;
    });
    empty.style.display = visible === 0 ? "" : "none";
  }

  btns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      btns.forEach(function (b) { b.classList.remove("active"); });
      btn.classList.add("active");
      activeFilter = btn.dataset.filter;
      update();
    });
  });

  search.addEventListener("input", update);
})();
</script>
