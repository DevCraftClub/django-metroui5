# Color Picker

На странице появляется поле.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_color_picker %}
```

`render_color_picker()` даёт `<input class="" type="text" data-role="color-picker" id="color-picker-component"></input>`.
