# Template

Компонент Metro template.

## Call

```python
from metroui5.components import render_template

render_template()
```

Empty or invalid: `render_template()` returns `<div data-role="template"></div>`.

In a template:

```django
{% metroui5_template %}
```
