# Кнопка действий

Одна главная кнопка открывает меньшие действия.

## Вызов

```python
from metroui5.components import render_action_button

render_action_button([{"icon": "mif-share", "href": "/share"}])
```

Пустой список всё равно даёт главную кнопку с плюсом и `<ul class="actions"></ul>`. `None` вызывает `TypeError`.

В шаблоне:

```django
{% metroui5_action_button actions %}
```

`actions` — тот же список. `main_icon` по умолчанию `mif-plus`.
