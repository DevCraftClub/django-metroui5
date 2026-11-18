# Drag Items

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_drag_items items %}
```

`render_drag_items()` даёт `<ul data-role="drag-items"></ul>`.
