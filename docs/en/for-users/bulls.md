# Bulls

MetroUI Bulls Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_bulls %}
```

`render_bulls()` returns `<div class="bull" data-role="bull" data-type="success" data-size="16"></div>`. An empty call returns `<div class="bull" data-role="bull" data-type="success" data-size="0"></div>`.
