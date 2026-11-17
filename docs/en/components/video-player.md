# Video Player

Компонент Metro video-player.

## Call

```python
from metroui5.components import render_video_player

render_video_player()
```

Empty or invalid: `render_video_player()` returns `<video data-role="video-player"></video>`.

In a template:

```django
{% metroui5_video_player %}
```
