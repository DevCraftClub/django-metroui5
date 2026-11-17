# Dropdown Button

На странице появляется кнопка.

## Вызов

```python
from metroui5.components import render_dropdown_button

render_dropdown_button()
```

Пустое или неверное значение: `render_dropdown_button()` даёт `<div class="dropdown-button"><button class="button dropdown-toggle">Options</button><ul class="d-menu" data-role="dropdown"><li><a href="#">No items</a></li></ul></div>`.

В шаблоне:

```django
{% metroui5_dropdown_button items %}
```
