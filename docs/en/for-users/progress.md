# Progress

MetroUI Progress Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_progress value="Text" %}
```

`render_progress(0)` returns `<div class="progress progress-blue" data-role="progress" data-value="0" data-max="100"></div>`. An empty call returns `<div class="progress progress-blue progress-0" data-role="progress" data-value="0" data-max="0"></div>`.
