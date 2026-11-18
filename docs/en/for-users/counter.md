# Counter

MetroUI Counter Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_counter %}
```

`render_counter()` returns `<div data-role="counter" data-value="0" data-from="0" data-duration="2000" data-prefix="" data-suffix="" data-delimiter="," data-size="16" data-start-on-viewport="false" data-counter-deferred="0" data-timeout="0" id="cou...`. An empty call returns `<div data-role="counter" data-value="0" data-from="0" data-duration="0" data-prefix="" data-suffix="" data-delimiter="," data-size="0" data-start-on-viewport="false" data-counter-deferred="0" data-timeout="0" id="counter...`.
