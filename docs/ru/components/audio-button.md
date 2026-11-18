# Audio Button

На странице появляется кнопка.

## Вызов

```python
from metroui5.components import render_audio_button

render_audio_button()
```

Пустое или неверное значение: `render_audio_button()` даёт `<button class="button" data-role="audio-button"></button>`.

В шаблоне:

```django
{% metroui5_audio_button %}
```
