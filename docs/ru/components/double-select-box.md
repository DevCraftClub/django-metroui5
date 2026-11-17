# Double Select Box

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_double_select_box

render_double_select_box()
```

Пустое или неверное значение: `render_double_select_box()` даёт `<div data-role="double-select-box"><select></select><select></select></div>`.

В шаблоне:

```django
{% metroui5_double_select_box left_options right_options %}
```
