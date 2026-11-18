# Cloak

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_cloak

render_cloak()
```

Пустое или неверное значение: `render_cloak()` даёт `<div class="cloak" id="cloak-component"></div>`.

В шаблоне:

```django
{% metroui5_cloak %}
```
