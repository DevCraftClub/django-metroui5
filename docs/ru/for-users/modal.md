# Modal

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_modal title="Text" content="Text" %}
```

`render_modal('Text', 'Text')` даёт `<div class="modal" data-role="modal"><div class='modal-title'>Text</div><div class='modal-content'>Text</div></div>`. Пустой вызов даёт `<div class="modal" data-role="modal"><div class='modal-title'></div><div class='modal-content'></div></div>`.
