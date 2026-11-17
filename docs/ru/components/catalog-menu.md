# Catalog Menu

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_catalog_menu

render_catalog_menu()
```

Пустое или неверное значение: `render_catalog_menu()` даёт `<nav class="catalog-menu" id="catalog_menu-component" data-role="catalog-menu"></nav>`.

В шаблоне:

```django
{% metroui5_catalog_menu items %}
```
