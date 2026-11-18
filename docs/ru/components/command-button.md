# Command Button

На странице появляется кнопка.

## Вызов

```python
from metroui5.components import render_command_button

render_command_button()
```

Пустое или неверное значение: `render_command_button()` даёт `<button class="command-button" id="command-button-component" type="button"></button>`.

В шаблоне:

```django
{% metroui5_command_button %}
```
