# Double Select Box

MetroUI Double Select Box Component

## Call

```python
from metroui5.components import render_double_select_box

render_double_select_box()
```

Empty or invalid: `render_double_select_box()` returns `<div data-role="double-select-box"><select></select><select></select></div>`.

In a template:

```django
{% metroui5_double_select_box left_options right_options %}
```
