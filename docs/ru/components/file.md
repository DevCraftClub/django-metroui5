# File

На странице появляется поле.

## Вызов

```python
from metroui5.components import render_file

render_file()
```

Пустое или неверное значение: `render_file()` даёт `<input class="" type="file" data-role="file"></input>`.

В шаблоне:

```django
{% metroui5_file %}
```
