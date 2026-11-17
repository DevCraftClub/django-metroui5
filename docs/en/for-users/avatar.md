# Avatar

MetroUI Avatar Components

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_avatar image_url="Text" %}
```

`render_avatar('Text')` returns `<img class="avatar" data-role="avatar" src="Text" alt="Avatar">`. An empty call returns `<img class="avatar" data-role="avatar" src="" alt="Avatar">`.
