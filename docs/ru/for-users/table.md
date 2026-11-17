# Table

На странице появляется таблица.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_table headers rows %}
```

`render_table(['Name'], [['One']])` даёт `<table class="table" data-role="table"><tr><th>Name</th></tr><tr><td>One</td></tr></table>`. Пустой вызов даёт `<table class="table" data-role="table"><tr></tr></table>`.
