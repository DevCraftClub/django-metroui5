# Tabs

MetroUI Tabs Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_tabs tabs %}
```

`render_tabs([{'title': 'One', 'content': 'Text'}])` returns `<ul data-role="tabs"><li><a href="#tab-0">One</a></li></ul><div class="tabs-targets"><div id="tab-0">Text</div></div>`. An empty call returns `<ul data-role="tabs"></ul><div class="tabs-targets"></div>`.
