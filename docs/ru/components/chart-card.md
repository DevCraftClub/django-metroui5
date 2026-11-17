# Chart Card

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_chart_card

render_chart_card()
```

Пустое или неверное значение: `render_chart_card()` даёт `<div class="chart-card" id="chart_card-component"><div class="content"></div><div class="chart"></div></div>`.

В шаблоне:

```django
{% metroui5_chart_card %}
```
