# Package Manager

Компонент Metro package-manager.

## Call

```python
from metroui5.components import render_package_manager

render_package_manager()
```

Empty or invalid: `render_package_manager()` returns `<div data-role="package-manager"></div>`.

In a template:

```django
{% metroui5_package_manager %}
```
