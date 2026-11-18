# Catalog Menu

MetroUI Catalog Menu Component

## Call

```python
from metroui5.components import render_catalog_menu

render_catalog_menu()
```

Empty or invalid: `render_catalog_menu()` returns `<nav class="catalog-menu" id="catalog_menu-component" data-role="catalog-menu"></nav>`.

In a template:

```django
{% metroui5_catalog_menu items %}
```
