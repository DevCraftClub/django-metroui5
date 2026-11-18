# App Bar

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_app_bar menu_items static_items %}
```

`render_app_bar()` даёт `<nav class="app-bar" id="app_bar-component" data-role="appbar"></nav>`.
