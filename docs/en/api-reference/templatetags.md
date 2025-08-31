# Template Tags

API reference for MetroUI5 Django template tags.

## Overview

The `templatetags` module contains Django template tags for connecting MetroUI5 resources and components in templates.

## Loading Tags

At the beginning of each template, load MetroUI5 tags:

```html
{% load metroui5 %}
```

## Available Tags

### `{% metroui5_css %}`

Connects MetroUI5 CSS files.

#### Usage

```html
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>{% block title %}Title{% endblock %}</title>

	{% metroui5_css %}
</head>
```

#### Result

```html
<link
	href="/static/metroui5/css/metro.all.css"
	rel="stylesheet"
	type="text/css"
/>
```

#### Parameters

This tag doesn't accept parameters.

### `{% metroui5_javascript %}`

Connects MetroUI5 JavaScript files.

#### Usage

```html
<body>
	<div class="container">{% block content %} {% endblock %}</div>

	{% metroui5_javascript %}
</body>
```

#### Result

```html
<script src="/static/metroui5/js/metro.all.js"></script>
```

#### Parameters

This tag doesn't accept parameters.

### `{% metroui5_icons %}`

Connects MetroUI5 icons CSS file.

#### Usage

```html
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>{% block title %}Title{% endblock %}</title>

	{% metroui5_css %} {% metroui5_icons %}
</head>
```

#### Result

```html
<link
	href="/static/metroui5/icons/icons.css"
	rel="stylesheet"
	type="text/css"
/>
```

#### Parameters

This tag doesn't accept parameters.

### `{% metroui5_theme %}`

Connects MetroUI5 theme (if configured).

#### Usage

```html
<head>
	{% metroui5_css %} {% metroui5_theme %}
</head>
```

#### Result

```html
<link
	href="/static/metroui5/themes/dark.css"
	rel="stylesheet"
	type="text/css"
/>
```

#### Parameters

This tag doesn't accept parameters.

## Complete Base Template

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{% block title %}Title{% endblock %}</title>

		{% metroui5_css %} {% metroui5_icons %} {% metroui5_theme %} {% block
		extra_css %}{% endblock %}
	</head>
	<body>
		<div class="container">{% block content %} {% endblock %}</div>

		{% metroui5_javascript %} {% block extra_js %}{% endblock %}
	</body>
</html>
```

## Advanced Capabilities

### Connecting Custom CSS Files

```html
{% load metroui5 %}

<head>
	{% metroui5_css %}

	<!-- Custom CSS files -->
	<link href="{% static 'css/custom.css' %}" rel="stylesheet" type="text/css" />
	<link href="{% static 'css/theme.css' %}" rel="stylesheet" type="text/css" />
</head>
```

### Connecting Custom JavaScript Files

```html
{% load metroui5 %}

<body>
	<!-- Main content -->
	{% block content %}{% endblock %} {% metroui5_javascript %}

	<!-- Custom JavaScript files -->
	<script src="{% static 'js/custom.js' %}"></script>
	<script src="{% static 'js/plugins.js' %}"></script>
</body>
```

### Conditional Resource Connection

```html
{% load metroui5 %}

<head>
	{% metroui5_css %} {% if debug %}
	<!-- Additional styles for development -->
	<link href="{% static 'css/debug.css' %}" rel="stylesheet" type="text/css" />
	{% endif %} {% if user.is_authenticated %}
	<!-- Styles for authenticated users -->
	<link href="{% static 'css/user.css' %}" rel="stylesheet" type="text/css" />
	{% endif %}
</head>
```

## Configuration via settings.py

### Basic Settings

```python
# settings.py

METROUI5 = {
	'CDN_MODE': False,  # Use local files
	'THEME': 'default',  # Default theme
	'VERSION': '5.0.0',  # MetroUI version
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

## Best Practices

### 1. Place CSS in `<head>`

```html
<!-- Good -->
<head>
	{% metroui5_css %} {% metroui5_icons %}
</head>

<!-- Bad -->
<body>
	{% metroui5_css %} {% metroui5_icons %}
</body>
```

### 2. Place JavaScript Before Closing `</body>`

```html
<!-- Good -->
<body>
	<!-- Content -->
	{% metroui5_javascript %}
</body>

<!-- Bad -->
<head>
	{% metroui5_javascript %}
</head>
```

### 3. Use Blocks for Additional Resources

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{% block title %}Title{% endblock %}</title>

		{% metroui5_css %} {% metroui5_icons %} {% block extra_css %}{% endblock %}
	</head>
	<body>
		{% block content %}{% endblock %} {% metroui5_javascript %} {% block
		extra_js %}{% endblock %}
	</body>
</html>
```

### 4. Override Blocks in Child Templates

```html
<!-- base.html -->
{% block extra_css %}{% endblock %}

<!-- child.html -->
{% extends 'base.html' %} {% block extra_css %}
<link
	href="{% static 'css/page-specific.css' %}"
	rel="stylesheet"
	type="text/css"
/>
{% endblock %}
```

## Troubleshooting

### Tags Not Loading

1. Make sure `metroui5` is added to `INSTALLED_APPS`
2. Check that `{% load metroui5 %}` is specified at the beginning of template
3. Restart Django server

### Resources Not Loading

1. Check `METROUI5` settings in `settings.py`
2. Make sure static files are configured correctly
3. Run `python manage.py collectstatic`

### Browser Console Errors

1. Check that all tags are loaded in correct order
2. Make sure there are no conflicts with other CSS/JS files
3. Check Network tab in DevTools

## Testing

### Unit Tests

```python
from django.test import TestCase
from django.template import Template, Context


class TemplateTagsTestCase(TestCase):

	def test_metroui5_css_tag(self):
		"""Test metroui5_css tag"""
		template = Template('{% load metroui5 %}{% metroui5_css %}')
		context = Context({})
		result = template.render(context)

		self.assertIn('metro.all.css', result)
		self.assertIn('rel="stylesheet"', result)

	def test_metroui5_javascript_tag(self):
		"""Test metroui5_javascript tag"""
		template = Template('{% load metroui5 %}{% metroui5_javascript %}')
		context = Context({})
		result = template.render(context)

		self.assertIn('metro.all.js', result)
		self.assertIn('<script', result)

	def test_metroui5_icons_tag(self):
		"""Test metroui5_icons tag"""
		template = Template('{% load metroui5 %}{% metroui5_icons %}')
		context = Context({})
		result = template.render(context)

		self.assertIn('icons.css', result)
		self.assertIn('rel="stylesheet"', result)
```

### Integration Tests

```python
from django.test import TestCase, Client
from django.urls import reverse


class TemplateTagsIntegrationTestCase(TestCase):

	def setUp(self):
		self.client = Client()

	def test_base_template_renders(self):
		"""Test base template rendering"""
		response = self.client.get(reverse('home'))

		# Check that CSS is connected
		self.assertContains(response, 'metro.all.css')

		# Check that JavaScript is connected
		self.assertContains(response, 'metro.all.js')

		# Check that icons are connected
		self.assertContains(response, 'icons.css')
```

## Related Modules

- [Core Functions](core.md) - for getting settings
- [HTML Utilities](html.md) - for generating HTML
- [Components](components.md) - for rendering UI

## Next Steps

Now that you've mastered template tags:

1. Study [core functions](core.md) for understanding settings
2. Check out [HTML utilities](html.md) for HTML generation
3. Study [components](components.md) for creating UI
4. Create your own template tags for specific tasks!
