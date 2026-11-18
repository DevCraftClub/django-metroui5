# List

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_list items %}
```

`render_list([{'text': 'One', 'href': '/one'}])` даёт `<ul class="list" data-role="list"><li><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="list" data-role="list"></ul>`.
