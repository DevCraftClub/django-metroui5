# Validator

Компонент Metro validator.

## Call

```python
from metroui5.components import render_validator

render_validator()
```

Empty or invalid: `render_validator()` returns `<form data-role="validator"></form>`.

In a template:

```django
{% metroui5_validator %}
```
