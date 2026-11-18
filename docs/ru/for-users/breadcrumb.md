# Breadcrumb

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_breadcrumb items %}
```

`render_breadcrumb([{'text': 'One', 'href': '/one'}])` даёт `<ul class="breadcrumbs" id="breadcrumb-component"><li class="active"><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="breadcrumbs" id="breadcrumb-component"></ul>`.
