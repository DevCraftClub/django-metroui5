# Accordion

A list of headings. A click opens the text under that heading.

In the page template, after `{% load metroui5 %}`:

```django
{% metroui5_accordion items %}
```

`items` is the list you already passed into the page. An empty list leaves an empty accordion frame, with no text inside.
