# Tile

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_tile title="Text" %}
```

`render_tile('Text')` даёт `<div class="tile tile-medium tile-blue" data-role="tile"><h3 class='tile-title'>Text</h3></div>`. Пустой вызов даёт `<div class="tile tile-0 tile-blue" data-role="tile"><h3 class='tile-title'></h3></div>`.
