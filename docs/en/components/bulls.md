# Bulls

MetroUI Bulls Component

## Call

```python
from metroui5.components import render_bulls

render_bulls()
```

Empty or invalid: `render_bulls()` returns `<div class="bull" data-role="bull" data-type="success" data-size="16"></div>`. An empty call returns `<div class="bull" data-role="bull" data-type="success" data-size="0"></div>`.

In a template:

```django
{% metroui5_bulls %}
```
