# Avatar

MetroUI Avatar Components

## Call

```python
from metroui5.components import render_avatar

render_avatar('Text')
```

Empty or invalid: `render_avatar('Text')` returns `<img class="avatar" data-role="avatar" src="Text" alt="Avatar">`. An empty call returns `<img class="avatar" data-role="avatar" src="" alt="Avatar">`.

In a template:

```django
{% metroui5_avatar image_url="Text" %}
```
