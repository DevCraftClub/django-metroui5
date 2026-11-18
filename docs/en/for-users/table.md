# Table

MetroUI Table Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_table headers rows %}
```

`render_table(['Name'], [['One']])` returns `<table class="table" data-role="table"><tr><th>Name</th></tr><tr><td>One</td></tr></table>`. An empty call returns `<table class="table" data-role="table"><tr></tr></table>`.
