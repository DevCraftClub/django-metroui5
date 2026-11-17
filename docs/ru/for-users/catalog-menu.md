# Catalog Menu

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_catalog_menu items %}
```

`render_catalog_menu()` даёт `<nav class="catalog-menu" id="catalog_menu-component" data-role="catalog-menu"></nav>`.
