# Color Selector

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_color_selector

render_color_selector()
```

Пустое или неверное значение: `render_color_selector()` даёт `<div class="" id="color-selector-component" data-role="color-selector"></div>`.

В шаблоне:

```django
{% metroui5_color_selector %}
```
