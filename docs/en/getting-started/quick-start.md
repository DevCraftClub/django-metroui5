# Quick Start

This section will help you quickly get started with MetroUI5 Django.

## Minimal Setup

### 1. Installation

```bash
pip install django-metroui5
```

### 2. Adding to Django Project

Add `metroui5` to `INSTALLED_APPS` in your `settings.py`:

```python
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'metroui5',  # Add this line
]
```

### 3. Static Files Configuration

Make sure you have static files configured in `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	BASE_DIR / "static",
]
```

### 4. Creating Base Template

Create `templates/base.html`:

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{% block title %}MetroUI5 Django{% endblock %}</title>

		{% metroui5_css %} {% metroui5_icons %}
	</head>
	<body>
		<div class="container">{% block content %} {% endblock %}</div>

		{% metroui5_javascript %}
	</body>
</html>
```

### 5. First Component

In your view (View):

```python
from metroui5.components import render_button


def home(request):
	button_html = render_button("Click me!", button_type="primary")
	return render(request, 'home.html', {'button': button_html})
```

In `home.html` template:

```html
{% extends 'base.html' %} {% block content %} {{ button|safe }} {% endblock %}
```

## CDN or Local Files

MetroUI5 Django supports two operating modes:

### Local Files (default)

The package automatically copies MetroUI5 files to your static directory.

### CDN Mode

Use the official CDN for quick start:

```python
# settings.py
METROUI5 = {
	'use_cdn': True,  # Enable CDN mode

	# Optionally: override CDN URLs
	'cdn_js_url': 'https://your-cdn.com/metro.js',
	'cdn_css_url': 'https://your-cdn.com/metro.css',
	'cdn_icons_url': 'https://your-cdn.com/icons.css',
}
```

**Available CDN files:**

- JavaScript: `https://cdn.metroui.org.ua/current/metro.js`
- CSS: `https://cdn.metroui.org.ua/current/metro.css`
- Icons: `https://cdn.metroui.org.ua/current/icons.css`

## What's Next?

- Study [installation](installation.md) for detailed setup
- Check out [basic usage](basic-usage.md)
- Look at [examples](examples.md) for inspiration
- Study available [components](../components/)

## Quick Check

If everything is configured correctly, you should see:

1. MetroUI5 styles are loaded (check in DevTools)
2. Button displays with MetroUI5 styles
3. No JavaScript errors in browser console

## Troubleshooting

### Static files not loading

```bash
python manage.py collectstatic
```

### Template tags not working

Make sure `metroui5` is added to `INSTALLED_APPS` and restart the server.

### Styles not applying

Check that MetroUI5 CSS files are loading in the `<head>` of the page.
