# Carousel

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_carousel

render_carousel()
```

Пустое или неверное значение: `render_carousel()` даёт `<div class="carousel" id="carousel-component" data-role="carousel"></div>`.

В шаблоне:

```django
{% metroui5_carousel slides %}
```
