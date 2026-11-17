# Activity

Shows that the page is still busy.

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_activity type="ring" %}
```

With no `type`, the mark still appears. An unknown `type` stays on the mark and does not break the page.
