# Cutter

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_cutter

render_cutter()
```

Пустое или неверное значение: `render_cutter()` даёт `<div class="cutter" id="cutter-component"><div class="content"></div></div>`.

В шаблоне:

```django
{% metroui5_cutter %}
```
