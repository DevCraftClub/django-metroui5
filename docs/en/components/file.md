# File

MetroUI File Component

## Call

```python
from metroui5.components import render_file

render_file()
```

Empty or invalid: `render_file()` returns `<input class="" type="file" data-role="file"></input>`.

In a template:

```django
{% metroui5_file %}
```
