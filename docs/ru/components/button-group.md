# Button Group

На странице появляется кнопка.

## Вызов

```python
from metroui5.components import render_button_group

render_button_group(['One'])
```

Пустое или неверное значение: `render_button_group(['One'])` даёт `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="button"><button>One</button></div>`. Пустой вызов даёт `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="[]"></div>`.

В шаблоне:

```django
{% metroui5_button_group buttons targets %}
```
