# Dropdown Button

На странице появляется кнопка.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_dropdown_button items %}
```

`render_dropdown_button()` даёт `<div class="dropdown-button"><button class="button dropdown-toggle">Options</button><ul class="d-menu" data-role="dropdown"><li><a href="#">No items</a></li></ul></div>`.
