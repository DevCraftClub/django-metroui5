# Bulls

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_bulls %}
```

`render_bulls()` даёт `<div class="bull" data-role="bull" data-type="success" data-size="16"></div>`. Пустой вызов даёт `<div class="bull" data-role="bull" data-type="success" data-size="0"></div>`.
