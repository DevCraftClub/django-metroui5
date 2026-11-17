# Drop Menu

На странице появляется кнопка.

## Вызов

```python
from metroui5.components import render_drop_menu

render_drop_menu()
```

Пустое или неверное значение: `render_drop_menu()` даёт `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-eea68ab9"></ul>`. Пустой вызов даёт `<button class="button menu-toggle">Menu</button><ul data-role="dropmenu" id="dropmenu-5d7ff4ec"></ul>`.

В шаблоне:

```django
{% metroui5_drop_menu items %}
```
