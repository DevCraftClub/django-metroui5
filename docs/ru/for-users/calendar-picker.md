# Calendar Picker

На странице появляется поле.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_calendar_picker %}
```

`render_calendar_picker()` даёт `<input class="" data-role="calendar-picker" type="text"></input>`.
