# Toolbar

MetroUI Toolbar Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_toolbar items %}
```

`render_toolbar([{'text': 'One', 'href': '/one'}])` returns `<ul class="toolbar" data-role="toolbar"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="toolbar" data-role="toolbar"></ul>`.
