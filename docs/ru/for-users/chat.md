# Chat

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_chat messages %}
```

`render_chat()` даёт `<div class="chat" id="chat-789d3d5a" data-role="chat"></div>`. Пустой вызов даёт `<div class="chat" id="chat-e6e07fed" data-role="chat"></div>`.
