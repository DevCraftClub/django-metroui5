# Chat

MetroUI Chat Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_chat messages %}
```

`render_chat()` returns `<div class="chat" id="chat-789d3d5a" data-role="chat"></div>`. An empty call returns `<div class="chat" id="chat-e6e07fed" data-role="chat"></div>`.
