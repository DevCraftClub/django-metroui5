# Drop Menu

MetroUI Drop Menu Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_drop_menu items %}
```

`render_drop_menu()` returns `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-eea68ab9"></ul>`. An empty call returns `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-5d7ff4ec"></ul>`.
