# Menu

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_menu items %}
```

`render_menu([{'text': 'One', 'href': '/one'}])` даёт `<ul class="menu" data-role="menu"><li><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="menu" data-role="menu"></ul>`.
