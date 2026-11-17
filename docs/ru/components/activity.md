# Индикатор работы

Небольшая подвижная метка показывает, что работа ещё идёт.

## Вызов

```python
from metroui5.components import render_activity

render_activity(type="ring")
```

`render_activity()` даёт `<div class="activity" data-role="activity"></div>`. `render_activity(type="nope")` даёт тот же блок с `data-type="nope"` и не вызывает ошибку.

В шаблоне:

```django
{% metroui5_activity type="ring" %}
```
