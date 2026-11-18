# Cloak

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_cloak %}
```

`render_cloak()` даёт `<div class="cloak" id="cloak-component"></div>`.
