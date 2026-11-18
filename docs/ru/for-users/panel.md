# Panel

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_panel %}
```

`render_panel()` даёт `<div class="panel" data-role="panel"><div class="panel-content"></div></div>`.
