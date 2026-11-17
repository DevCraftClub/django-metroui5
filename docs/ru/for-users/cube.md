# Cube

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_cube show_axis cells numbers rules %}
```

`render_cube()` даёт `<div data-role="cube" data-show-axis="false" data-axis-style="arrow" data-cells="4" data-numbers="false" data-flash-interval="1000" data-auto-restart="0" data-cell-click="false" class="cube" id="cube-component"></div>`. Пустой вызов даёт `<div data-role="cube" data-show-axis="[]" data-axis-style="arrow" data-cells="[]" data-numbers="[]" data-flash-interval="1000" data-auto-restart="0" data-cell-click="false" data-rules="[]" class="cube" id="cube-component...`.
