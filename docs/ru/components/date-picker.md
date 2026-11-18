# Date Picker

На странице появляется поле.

## Вызов

```python
from metroui5.components import render_date_picker

render_date_picker()
```

Пустое или неверное значение: `render_date_picker()` даёт `<input class="date-picker" type="text" data-role="date-picker">`.

В шаблоне:

```django
{% metroui5_date_picker %}
```
