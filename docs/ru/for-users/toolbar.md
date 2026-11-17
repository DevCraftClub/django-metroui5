# Toolbar

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_toolbar items %}
```

`render_toolbar([{'text': 'One', 'href': '/one'}])` даёт `<ul class="toolbar" data-role="toolbar"><li><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="toolbar" data-role="toolbar"></ul>`.
