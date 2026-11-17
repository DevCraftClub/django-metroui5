# Audio Player

На странице появляется блок из примера.

## Вызов

```python
from metroui5.components import render_audio_player

render_audio_player()
```

Пустое или неверное значение: `render_audio_player()` даёт `<audio class="" data-role="audio-player"></audio>`.

В шаблоне:

```django
{% metroui5_audio_player %}
```
