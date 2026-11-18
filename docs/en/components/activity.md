# Activity

A small animated mark that shows work in progress.

## Call

```python
from metroui5.components import render_activity

render_activity(type="ring")
```

`render_activity()` returns `<div class="activity" data-role="activity"></div>`. `render_activity(type="nope")` returns the same div with `data-type="nope"` and does not raise.

In a template:

```django
{% metroui5_activity type="ring" %}
```
