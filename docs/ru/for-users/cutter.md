# Cutter

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_cutter %}
```

`render_cutter()` даёт `<div class="cutter" id="cutter-component"><div class="content"></div></div>`.
