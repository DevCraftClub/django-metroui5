# Badge

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_badge content="Text" %}
```

`render_badge('Text')` даёт `<span class="badge">Text</span>`. Пустой вызов даёт `<span class="badge"></span>`.
