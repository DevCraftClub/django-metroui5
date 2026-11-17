# Dropdown Button

MetroUI Dropdown Button Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_dropdown_button items %}
```

`render_dropdown_button()` returns `<div class="dropdown-button"><button class="button dropdown-toggle">Options</button><ul class="d-menu" data-role="dropdown"><li><a href="#">No items</a></li></ul></div>`.
