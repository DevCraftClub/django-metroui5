# Carousel

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_carousel slides %}
```

`render_carousel()` даёт `<div class="carousel" id="carousel-component" data-role="carousel"></div>`.
