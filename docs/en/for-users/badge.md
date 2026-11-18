# Badge

MetroUI Badge Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_badge content="Text" %}
```

`render_badge('Text')` returns `<span class="badge">Text</span>`. An empty call returns `<span class="badge"></span>`.
