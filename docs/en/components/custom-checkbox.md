# Custom Checkbox

MetroUI Custom Checkbox Component

## Call

```python
from metroui5.components import render_custom_checkbox

render_custom_checkbox()
```

Empty or invalid: `render_custom_checkbox()` returns `<input data-role="custom-checkbox" data-state-on="✓" data-state-off="✗" data-caption-position="right" type="checkbox" id="custom_checkbox-component">`.

In a template:

```django
{% metroui5_custom_checkbox %}
```
