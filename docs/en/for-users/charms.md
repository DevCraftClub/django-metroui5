# Charms

MetroUI Charms Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_charms %}
```

`render_charms()` returns `<div class="charms right-side" id="charms-component" data-role="charms" />`. An empty call returns `<div class="charms right-side" id="charms-component" data-role="charms"></div>`.
