# Color Picker

На странице появляется поле.

## Вызов

```python
from metroui5.components import render_color_picker

render_color_picker()
```

Пустое или неверное значение: `render_color_picker()` даёт `<input class="" type="text" data-role="color-picker" id="color-picker-component"></input>`.

В шаблоне:

```django
{% metroui5_color_picker %}
```
