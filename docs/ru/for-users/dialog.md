# Dialog

На странице появляется кнопка.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_dialog %}
```

`render_dialog()` даёт `<div class="dialog" id="dialog-component" data-role="dialog"><div class="dialog-actions"><button class="button js-dialog-close" data-action="ok">OK</button><button class="button js-dialog-close" data-action="cancel">Canc...`.
