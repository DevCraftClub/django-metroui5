# App Bar

MetroUI App Bar Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_app_bar menu_items static_items %}
```

`render_app_bar()` returns `<nav class="app-bar" id="app_bar-component" data-role="appbar"></nav>`.
