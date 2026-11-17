# Button Group

На странице появляется кнопка.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_button_group buttons targets %}
```

`render_button_group(['One'])` даёт `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="button"><button>One</button></div>`. Пустой вызов даёт `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="[]"></div>`.
