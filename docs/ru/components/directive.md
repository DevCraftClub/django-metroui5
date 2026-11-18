# Directive

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_directive

render_directive()
```

Пустое или неверное значение: `render_directive()` даёт `<div data-role="directive"></div>`.

В шаблоне:

```django
{% metroui5_directive %}
```
