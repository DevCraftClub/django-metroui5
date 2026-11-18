# Avatar

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_avatar

render_avatar('Text')
```

Пустое или неверное значение: `render_avatar('Text')` даёт `<img class="avatar" data-role="avatar" src="Text" alt="Avatar">`. Пустой вызов даёт `<img class="avatar" data-role="avatar" src="" alt="Avatar">`.

В шаблоне:

```django
{% metroui5_avatar image_url="Text" %}
```
