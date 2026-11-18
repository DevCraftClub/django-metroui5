# Button Group

MetroUI Button Group Component

## Call

```python
from metroui5.components import render_button_group

render_button_group(['One'])
```

Empty or invalid: `render_button_group(['One'])` returns `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="button"><button>One</button></div>`. An empty call returns `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="[]"></div>`.

In a template:

```django
{% metroui5_button_group buttons targets %}
```
