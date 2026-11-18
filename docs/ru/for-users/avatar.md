# Avatar

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_avatar image_url="Text" %}
```

`render_avatar('Text')` даёт `<img class="avatar" data-role="avatar" src="Text" alt="Avatar">`. Пустой вызов даёт `<img class="avatar" data-role="avatar" src="" alt="Avatar">`.
