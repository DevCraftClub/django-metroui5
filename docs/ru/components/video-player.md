# Video Player

Компонент Metro video-player.

## Вызов

```python
from metroui5.components import render_video_player

render_video_player()
```

Пустое или неверное значение: `render_video_player()` даёт `<video data-role="video-player"></video>`.

В шаблоне:

```django
{% metroui5_video_player %}
```
