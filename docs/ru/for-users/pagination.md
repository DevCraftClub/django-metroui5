# Pagination

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_pagination current_page="Text" total_pages %}
```

`render_pagination('Text', ['One'])` вызывает TypeError: '>' not supported between instances of 'str' and 'int'. Пустой вызов вызывает TypeError: '>' not supported between instances of 'str' and 'int'.
