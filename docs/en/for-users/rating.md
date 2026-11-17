# Rating

MetroUI Rating Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_rating value="Text" %}
```

`render_rating(0)` returns `<input class="rating" data-role="rating" data-value="0" data-stars="5">`. An empty call returns `<input class="rating" data-role="rating" data-value="0" data-stars="0">`.
