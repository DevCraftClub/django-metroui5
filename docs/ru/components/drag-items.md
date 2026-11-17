# Drag Items

На странице появляется список.

## Вызов

```python
from metroui5.components import render_drag_items

render_drag_items()
```

Пустое или неверное значение: `render_drag_items()` даёт `<ul data-role="drag-items"></ul>`.

В шаблоне:

```django
{% metroui5_drag_items items %}
```
