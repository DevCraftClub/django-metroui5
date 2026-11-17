# Sidebar

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_sidebar items %}
```

`render_sidebar([{'text': 'One', 'href': '/one'}])` даёт `<ul class="sidebar" data-role="sidebar"><li><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="sidebar" data-role="sidebar"></ul>`.
