# Chat

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_chat

render_chat()
```

Пустое или неверное значение: `render_chat()` даёт `<div class="chat" id="chat-789d3d5a" data-role="chat"></div>`. Пустой вызов даёт `<div class="chat" id="chat-e6e07fed" data-role="chat"></div>`.

В шаблоне:

```django
{% metroui5_chat messages %}
```
