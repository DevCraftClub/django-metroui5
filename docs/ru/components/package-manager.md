# Package Manager

Компонент Metro package-manager.

## Вызов

```python
from metroui5.components import render_package_manager

render_package_manager()
```

Пустое или неверное значение: `render_package_manager()` даёт `<div data-role="package-manager"></div>`.

В шаблоне:

```django
{% metroui5_package_manager %}
```
