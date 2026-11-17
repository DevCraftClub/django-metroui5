# Chips

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_chips

render_chips()
```

Пустое или неверное значение: `render_chips()` даёт `<div class="chip" id="chips-component"><div class="label">Chip</div></div>`.

В шаблоне:

```django
{% metroui5_chips %}
```
