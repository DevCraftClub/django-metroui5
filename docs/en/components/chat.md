# Chat

MetroUI Chat Component

## Call

```python
from metroui5.components import render_chat

render_chat()
```

Empty or invalid: `render_chat()` returns `<div class="chat" id="chat-789d3d5a" data-role="chat"></div>`. An empty call returns `<div class="chat" id="chat-e6e07fed" data-role="chat"></div>`.

In a template:

```django
{% metroui5_chat messages %}
```
