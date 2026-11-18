# Dropdown

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_dropdown items %}
```

`render_dropdown()` даёт `<div class="dropdown-toggle">Click me<div class="dropdown" data-role="dropdown"></div></div>`.
