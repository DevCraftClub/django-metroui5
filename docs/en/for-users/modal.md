# Modal

MetroUI Modal Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_modal title="Text" content="Text" %}
```

`render_modal('Text', 'Text')` returns `<div class="modal" data-role="modal"><div class='modal-title'>Text</div><div class='modal-content'>Text</div></div>`. An empty call returns `<div class="modal" data-role="modal"><div class='modal-title'></div><div class='modal-content'></div></div>`.
