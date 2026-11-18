# Charms

MetroUI Charms Component

## Call

```python
from metroui5.components import render_charms

render_charms()
```

Empty or invalid: `render_charms()` returns `<div class="charms right-side" id="charms-component" data-role="charms" />`. An empty call returns `<div class="charms right-side" id="charms-component" data-role="charms"></div>`.

In a template:

```django
{% metroui5_charms %}
```
