# Sidebar

MetroUI Sidebar Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_sidebar items %}
```

`render_sidebar([{'text': 'One', 'href': '/one'}])` returns `<ul class="sidebar" data-role="sidebar"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="sidebar" data-role="sidebar"></ul>`.
