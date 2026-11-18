# Dropdown Button

MetroUI Dropdown Button Component

## Call

```python
from metroui5.components import render_dropdown_button

render_dropdown_button()
```

Empty or invalid: `render_dropdown_button()` returns `<div class="dropdown-button"><button class="button dropdown-toggle">Options</button><ul class="d-menu" data-role="dropdown"><li><a href="#">No items</a></li></ul></div>`.

In a template:

```django
{% metroui5_dropdown_button items %}
```
