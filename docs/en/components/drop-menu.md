# Drop Menu

MetroUI Drop Menu Component

## Call

```python
from metroui5.components import render_drop_menu

render_drop_menu()
```

Empty or invalid: `render_drop_menu()` returns `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-eea68ab9"></ul>`. An empty call returns `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-5d7ff4ec"></ul>`.

In a template:

```django
{% metroui5_drop_menu items %}
```
