# Bulls

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_bulls

render_bulls()
```

Пустое или неверное значение: `render_bulls()` даёт `<div class="bull" data-role="bull" data-type="success" data-size="16"></div>`. Пустой вызов даёт `<div class="bull" data-role="bull" data-type="success" data-size="0"></div>`.

В шаблоне:

```django
{% metroui5_bulls %}
```
