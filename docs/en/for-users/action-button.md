# Action button

A plus button. A click shows the smaller actions next to it.

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_action_button actions %}
```

`actions` is the list you already passed into the page. An empty list keeps the plus and leaves the action list empty.
