# Audio Button

На странице появляется кнопка.

В шаблоне страницы, после `{% load metroui5 %}`:

```django
{% metroui5_audio_button %}
```

`render_audio_button()` даёт `<button class="button" data-role="audio-button"></button>`.
