# Progress

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_progress value="Text" %}
```

`render_progress(0)` даёт `<div class="progress progress-blue" data-role="progress" data-value="0" data-max="100"></div>`. Пустой вызов даёт `<div class="progress progress-blue progress-0" data-role="progress" data-value="0" data-max="0"></div>`.
