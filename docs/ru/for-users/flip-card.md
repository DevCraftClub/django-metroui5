# Flip Card

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_flip_card %}
```

`render_flip_card()` даёт `<div class="flip-card" data-role="flip-card"><div class="front"></div><div class="back"></div></div>`.
