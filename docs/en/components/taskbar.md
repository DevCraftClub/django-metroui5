# Taskbar

Компонент Metro taskbar.

## Call

```python
from metroui5.components import render_taskbar

render_taskbar()
```

Empty or invalid: `render_taskbar()` returns `<div data-role="task-bar"></div>`.

In a template:

```django
{% metroui5_taskbar %}
```
