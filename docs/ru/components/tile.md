# Tile

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_tile

render_tile('Text')
```

Пустое или неверное значение: `render_tile('Text')` даёт `<div class="tile tile-medium tile-blue" data-role="tile"><h3 class='tile-title'>Text</h3></div>`. Пустой вызов даёт `<div class="tile tile-0 tile-blue" data-role="tile"><h3 class='tile-title'></h3></div>`.

В шаблоне:

```django
{% metroui5_tile title="Text" %}
```
