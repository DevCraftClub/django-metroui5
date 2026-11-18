# Chart Card

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_chart_card %}
```

`render_chart_card()` даёт `<div class="chart-card" id="chart_card-component"><div class="content"></div><div class="chart"></div></div>`.
