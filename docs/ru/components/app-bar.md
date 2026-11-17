# App Bar

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_app_bar

render_app_bar()
```

Пустое или неверное значение: `render_app_bar()` даёт `<nav class="app-bar" id="app_bar-component" data-role="appbar"></nav>`.

В шаблоне:

```django
{% metroui5_app_bar menu_items static_items %}
```
