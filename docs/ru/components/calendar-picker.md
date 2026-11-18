# Calendar Picker

На странице появляется поле.

## Вызов

```python
from metroui5.components import render_calendar_picker

render_calendar_picker()
```

Пустое или неверное значение: `render_calendar_picker()` даёт `<input class="" data-role="calendar-picker" type="text"></input>`.

В шаблоне:

```django
{% metroui5_calendar_picker %}
```
