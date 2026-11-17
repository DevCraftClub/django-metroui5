# Charms

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_charms

render_charms()
```

Пустое или неверное значение: `render_charms()` даёт `<div class="charms right-side" id="charms-component" data-role="charms" />`. Пустой вызов даёт `<div class="charms right-side" id="charms-component" data-role="charms"></div>`.

В шаблоне:

```django
{% metroui5_charms %}
```
