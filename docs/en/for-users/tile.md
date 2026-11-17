# Tile

MetroUI Tile Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_tile title="Text" %}
```

`render_tile('Text')` returns `<div class="tile tile-medium tile-blue" data-role="tile"><h3 class='tile-title'>Text</h3></div>`. An empty call returns `<div class="tile tile-0 tile-blue" data-role="tile"><h3 class='tile-title'></h3></div>`.
