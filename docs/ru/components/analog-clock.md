# Analog Clock

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_analog_clock

render_analog_clock()
```

Пустое или неверное значение: `render_analog_clock()` даёт `<div class="analog-clock" data-role="analog-clock"></div>`.

В шаблоне:

```django
{% metroui5_analog_clock %}
```
