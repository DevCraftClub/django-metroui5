# Custom Checkbox

На странице появляется поле.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_custom_checkbox %}
```

`render_custom_checkbox()` даёт `<input data-role="custom-checkbox" data-state-on="✓" data-state-off="✗" data-caption-position="right" type="checkbox" id="custom_checkbox-component">`.
