# Directive

На странице появляется блок из примера.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_directive %}
```

`render_directive()` даёт `<div data-role="directive"></div>`.
