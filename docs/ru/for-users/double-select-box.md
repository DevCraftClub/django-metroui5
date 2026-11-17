# Double Select Box

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_double_select_box left_options right_options %}
```

`render_double_select_box()` даёт `<div data-role="double-select-box"><select></select><select></select></div>`.
