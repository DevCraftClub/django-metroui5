# App Bar

MetroUI App Bar Component

## Call

```python
from metroui5.components import render_app_bar

render_app_bar()
```

Empty or invalid: `render_app_bar()` returns `<nav class="app-bar" id="app_bar-component" data-role="appbar"></nav>`.

In a template:

```django
{% metroui5_app_bar menu_items static_items %}
```
