# Navigation

MetroUI Navigation Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_navigation items %}
```

`render_navigation([{'text': 'One', 'href': '/one'}])` returns `<ul class="navigation" data-role="navigation"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="navigation" data-role="navigation"></ul>`.
