# Action button

One main button that opens smaller actions.

## Call

```python
from metroui5.components import render_action_button

render_action_button([{"icon": "mif-share", "href": "/share"}])
```

An empty list still returns the main plus button and `<ul class="actions"></ul>`. `None` raises `TypeError`.

In a template:

```django
{% metroui5_action_button actions %}
```

`actions` is the same list. `main_icon` defaults to `mif-plus`.
