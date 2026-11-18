# Rating

На странице появляется поле.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_rating value="Text" %}
```

`render_rating(0)` даёт `<input class="rating" data-role="rating" data-value="0" data-stars="5">`. Пустой вызов даёт `<input class="rating" data-role="rating" data-value="0" data-stars="0">`.
