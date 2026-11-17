# Tabs

На странице появляется список.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_tabs tabs %}
```

`render_tabs([{'title': 'One', 'content': 'Text'}])` даёт `<ul data-role="tabs"><li><a href="#tab-0">One</a></li></ul><div class="tabs-targets"><div id="tab-0">Text</div></div>`. Пустой вызов даёт `<ul data-role="tabs"></ul><div class="tabs-targets"></div>`.
