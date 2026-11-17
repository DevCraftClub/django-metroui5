# Clock

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_clock

render_clock()
```

Пустое или неверное значение: `render_clock()` даёт `<div class="clock" id="clock-component" data-role="clock"></div>`.

В шаблоне:

```django
{% metroui5_clock %}
```
