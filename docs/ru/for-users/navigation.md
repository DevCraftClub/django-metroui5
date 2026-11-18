# Navigation

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_navigation items %}
```

`render_navigation([{'text': 'One', 'href': '/one'}])` даёт `<ul class="navigation" data-role="navigation"><li><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="navigation" data-role="navigation"></ul>`.
