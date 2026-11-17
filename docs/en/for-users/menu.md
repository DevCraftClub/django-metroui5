# Menu

MetroUI Menu Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_menu items %}
```

`render_menu([{'text': 'One', 'href': '/one'}])` returns `<ul class="menu" data-role="menu"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="menu" data-role="menu"></ul>`.
