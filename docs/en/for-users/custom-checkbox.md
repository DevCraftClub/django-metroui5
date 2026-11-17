# Custom Checkbox

MetroUI Custom Checkbox Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_custom_checkbox %}
```

`render_custom_checkbox()` returns `<input data-role="custom-checkbox" data-state-on="✓" data-state-off="✗" data-caption-position="right" type="checkbox" id="custom_checkbox-component">`.
