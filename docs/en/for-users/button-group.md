# Button Group

MetroUI Button Group Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_button_group buttons targets %}
```

`render_button_group(['One'])` returns `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="button"><button>One</button></div>`. An empty call returns `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="[]"></div>`.
