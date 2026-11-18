# Alert

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_alert content="Text" %}
```

`render_alert('Text')` даёт `<div class="alert alert-info" role="alert">Text</div>`. Пустой вызов даёт `<div class="alert alert-info" role="alert"></div>`.
