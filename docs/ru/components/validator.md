# Validator

Компонент Metro validator.

## Вызов

```python
from metroui5.components import render_validator

render_validator()
```

Пустое или неверное значение: `render_validator()` даёт `<form data-role="validator"></form>`.

В шаблоне:

```django
{% metroui5_validator %}
```
