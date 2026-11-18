# Pagination

MetroUI Pagination Component

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_pagination current_page="Text" total_pages %}
```

`render_pagination('Text', ['One'])` raises TypeError: '>' not supported between instances of 'str' and 'int'. An empty call raises TypeError: '>' not supported between instances of 'str' and 'int'.
