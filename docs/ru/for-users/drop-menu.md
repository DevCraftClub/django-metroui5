# Drop Menu

На странице появляется кнопка.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_drop_menu items %}
```

`render_drop_menu()` даёт `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-eea68ab9"></ul>`. Пустой вызов даёт `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-5d7ff4ec"></ul>`.
