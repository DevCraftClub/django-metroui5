# Basic Usage

Basics of using MetroUI5 Django in your projects.

## Loading Template Tags

At the beginning of each template, load MetroUI5 tags:

```html
{% load metroui5 %}
```

## Connecting Resources

### CSS Files

```html
{% metroui5_css %}
```

### JavaScript Files

```html
{% metroui5_javascript %}
```

### Icons

```html
{% metroui5_icons %}
```

### Complete Base Template

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{% block title %}Title{% endblock %}</title>

		{% metroui5_css %} {% metroui5_icons %}
	</head>
	<body>
		<div class="container">{% block content %} {% endblock %}</div>

		{% metroui5_javascript %}
	</body>
</html>
```

## Using Components

### In Views

```python
from metroui5.components import render_button, render_card, render_alert


def dashboard(request):
	context = {
		'welcome_alert': render_alert(
			"Welcome to the dashboard!",
			alert_type="success"
		),
		'action_button': render_button(
			"Create new project",
			button_type="primary",
			size="large"
		),
		'info_card': render_card(
			header="Information",
			content="This is a card with information",
			footer="Additional actions"
		)
	}
	return render(request, 'dashboard.html', context)
```

### In Templates

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }}

<div class="row">
	<div class="cell-md-6">{{ action_button|safe }}</div>
	<div class="cell-md-6">{{ info_card|safe }}</div>
</div>
{% endblock %}
```

## Working with Forms

### Form Rendering

```python
from metroui5.forms import render_form


def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Form processing
			pass
	else:
		form = ContactForm()

	form_html = render_form(form, layout='horizontal')
	return render(request, 'contact.html', {'form': form_html})
```

### Rendering Individual Field

```python
from metroui5.forms import render_field


def custom_form(request):
	form = CustomForm()

	# Render only specific fields
	name_field = render_field(form['name'], placeholder="Enter name")
	email_field = render_field(form['email'], placeholder="Enter email")

	context = {
		'name_field': name_field,
		'email_field': email_field,
	}
	return render(request, 'custom_form.html', context)
```

## Using Utilities

### HTML Utilities

```python
from metroui5.html import render_tag, render_link_tag

# Creating HTML tag
div_tag = render_tag("div", {"class": "container"}, "Content")

# Creating link
link = render_link_tag("https://example.com", text="Example", target="_blank")
```

### CSS Utilities

```python
from metroui5.css import merge_css_classes, add_css_class

# Combining CSS classes
classes = merge_css_classes("btn", "btn-primary", "btn-large")

# Adding class
new_classes = add_css_class(classes, "btn-block")
```

## Configuration via settings.py

### Basic Settings

```python
METROUI5 = {
	'CDN_MODE': False,
	'THEME': 'default',
	'VERSION': '5.0.0',
}
```

### Custom Files

```python
METROUI5 = {
	'CUSTOM_CSS_FILES': [
		'css/custom.css',
		'css/theme.css',
	],
	'CUSTOM_JS_FILES': [
		'js/custom.js',
		'js/plugins.js',
	],
}
```

### CDN Settings

```python
METROUI5 = {
	'CDN_MODE': True,
	'CDN_URL': 'https://cdn.metroui.org.ua/current',
	'THEME': 'default',
}
```

## Working with Renderers

### Custom Form Renderer

```python
from metroui5.renderers import get_form_renderer


def custom_form_view(request):
	form = MyForm()

	# Get custom renderer
	renderer = get_form_renderer(
		form,
		layout='horizontal',
		label_class='custom-label',
		field_class='custom-field'
	)

	form_html = renderer.render()
	return render(request, 'form.html', {'form': form_html})
```

### Field Renderer

```python
from metroui5.renderers import get_field_renderer


def field_view(request):
	form = MyForm()
	field = form['username']

	# Render field with custom settings
	renderer = get_field_renderer(
		field,
		widget_class='custom-input',
		help_text_class='custom-help'
	)

	field_html = renderer.render()
	return render(request, 'field.html', {'field': field_html})
```

## Best Practices

### 1. Use Base Template

Always create a base template with connected MetroUI5 resources.

### 2. Group Components

```python
# Good
context = {
	'header_components': {
		'alert': render_alert("Message", "info"),
		'breadcrumb': render_breadcrumb(breadcrumb_items),
	},
	'main_components': {
		'card': render_card(...),
		'table': render_table(...),
	}
}
```

### 3. Use Constants for Repeating Values

```python
# settings.py
METROUI5_DEFAULT_BUTTON_CLASS = "btn btn-primary"

# views.py
from django.conf import settings

button = render_button(
	"Text",
	**{"class": settings.METROUI5_DEFAULT_BUTTON_CLASS}
)
```

### 4. Handle Errors

```python
try:
	component_html = render_component(...)
except Exception as e:
	# Error logging
	logger.error(f"Component rendering error: {e}")
	component_html = "<div>Component loading error</div>"
```

## Debugging

### Checking Loaded Resources

In browser check:

1. **Network** tab - CSS and JS files are loaded
2. **Console** - no JavaScript errors
3. **Elements** - CSS classes are applied

### Logging

```python
import logging

logger = logging.getLogger(__name__)


def debug_view(request):
	logger.debug("Rendering component")
	component = render_component(...)
	logger.debug(f"Component created: {component}")
	return render(request, 'debug.html', {'component': component})
```

## Next Steps

Now that you've mastered basic usage:

1. Study [examples](examples.md) for more complex scenarios
2. Check out available [components](../components/)
3. Study [API reference](../api-reference/) for detailed information
4. Create your first project with MetroUI5!
