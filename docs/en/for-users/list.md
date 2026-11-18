# List

MetroUI List Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_list items %}
```

`render_list([{'text': 'One', 'href': '/one'}])` returns `<ul class="list" data-role="list"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="list" data-role="list"></ul>`.
