# Breadcrumb

MetroUI Breadcrumb Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_breadcrumb items %}
```

`render_breadcrumb([{'text': 'One', 'href': '/one'}])` returns `<ul class="breadcrumbs" id="breadcrumb-component"><li class="active"><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="breadcrumbs" id="breadcrumb-component"></ul>`.
