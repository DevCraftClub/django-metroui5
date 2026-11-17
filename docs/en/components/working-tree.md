# Working Tree

Компонент Metro working-tree.

## Call

```python
from metroui5.components import render_working_tree

render_working_tree()
```

Empty or invalid: `render_working_tree()` returns `<ul data-role="working-tree"></ul>`.

In a template:

```django
{% metroui5_working_tree %}
```
