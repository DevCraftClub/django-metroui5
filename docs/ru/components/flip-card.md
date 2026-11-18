# Flip Card

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_flip_card

render_flip_card()
```

Пустое или неверное значение: `render_flip_card()` даёт `<div class="flip-card" data-role="flip-card"><div class="front"></div><div class="back"></div></div>`.

В шаблоне:

```django
{% metroui5_flip_card %}
```
