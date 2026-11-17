# Tile

MetroUI Tile Component

## Call

```python
from metroui5.components import render_tile

render_tile('Text')
```

Empty or invalid: `render_tile('Text')` returns `<div class="tile tile-medium tile-blue" data-role="tile"><h3 class='tile-title'>Text</h3></div>`. An empty call returns `<div class="tile tile-0 tile-blue" data-role="tile"><h3 class='tile-title'></h3></div>`.

In a template:

```django
{% metroui5_tile title="Text" %}
```
