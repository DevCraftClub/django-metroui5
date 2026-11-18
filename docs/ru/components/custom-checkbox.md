# Custom Checkbox

На странице появляется поле.

## Вызов

```python
from metroui5.components import render_custom_checkbox

render_custom_checkbox()
```

Пустое или неверное значение: `render_custom_checkbox()` даёт `<input data-role="custom-checkbox" data-state-on="✓" data-state-off="✗" data-caption-position="right" type="checkbox" id="custom_checkbox-component">`.

В шаблоне:

```django
{% metroui5_custom_checkbox %}
```
