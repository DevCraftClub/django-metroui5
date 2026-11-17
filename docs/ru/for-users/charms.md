# Charms

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_charms %}
```

`render_charms()` даёт `<div class="charms right-side" id="charms-component" data-role="charms" />`. Пустой вызов даёт `<div class="charms right-side" id="charms-component" data-role="charms"></div>`.
