# Alert

MetroUI Alert Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_alert content="Text" %}
```

`render_alert('Text')` returns `<div class="alert alert-info" role="alert">Text</div>`. An empty call returns `<div class="alert alert-info" role="alert"></div>`.
