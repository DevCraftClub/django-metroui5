# HTML Utilities

API reference for MetroUI5 Django HTML utilities module.

## Overview

The `html` module contains functions for generating HTML tags, links, scripts and other HTML elements.

## Functions

### `render_tag(tag, attrs=None, content=None, close=True)`

Creates HTML tag with specified attributes and content.

#### Parameters

- `tag` (str) - HTML tag name
- `attrs` (dict, optional) - tag attributes
- `content` (str, optional) - tag content
- `close` (bool, optional) - whether to close tag. Default `True`

#### Returns

HTML string

#### Examples

```python
from metroui5.html import render_tag

# Simple div
div_tag = render_tag("div", {"class": "container"}, "Content")
# Result: <div class="container">Content</div>

# Tag without content
hr_tag = render_tag("hr", {"class": "divider"}, close=False)
# Result: <hr class="divider">

# Tag with multiple attributes
button_tag = render_tag(
	"button",
	{"class": "btn", "type": "submit", "id": "submitBtn"},
	"Submit"
)
# Result: <button class="btn" type="submit" id="submitBtn">Submit</button>
```

### `render_link_tag(url, **attrs)`

Creates HTML `<link>` tag for connecting external resources.

#### Parameters

- `url` (str) - resource URL
- `**attrs` - additional attributes

#### Returns

HTML string for `<link>` tag

#### Examples

```python
from metroui5.html import render_link_tag

# CSS file
css_link = render_link_tag(
	"/static/css/style.css",
	rel="stylesheet",
	type="text/css"
)
# Result: <link href="/static/css/style.css" rel="stylesheet" type="text/css">

# Icon
icon_link = render_link_tag(
	"/favicon.ico",
	rel="icon",
	type="image/x-icon"
)
# Result: <link href="/favicon.ico" rel="icon" type="image/x-icon">

# Preload
preload_link = render_link_tag(
	"/static/js/app.js",
	rel="preload",
	as="script"
)
# Result: <link href="/static/js/app.js" rel="preload" as="script">
```

### `render_script_tag(url, **attrs)`

Creates HTML `<script>` tag for connecting JavaScript files.

#### Parameters

- `url` (str) - JavaScript file URL
- `**attrs` - additional attributes

#### Returns

HTML string for `<script>` tag

#### Examples

```python
from metroui5.html import render_script_tag

# Regular script
script_tag = render_script_tag("/static/js/app.js")
# Result: <script src="/static/js/app.js"></script>

# Script with attributes
script_tag = render_script_tag(
	"/static/js/app.js",
	defer=True,
	async=True
)
# Result: <script src="/static/js/app.js" defer async></script>

# Script with type
script_tag = render_script_tag(
	"/static/js/app.js",
	type="module"
)
# Result: <script src="/static/js/app.js" type="module"></script>
```

### `render_custom_css_files(css_files)`

Generates HTML `<link>` tags for custom CSS files.

#### Parameters

- `css_files` (list) - list of CSS file URLs

#### Returns

HTML string with `<link>` tags

#### Examples

```python
from metroui5.html import render_custom_css_files

# CSS files list
css_files = [
	"/static/css/custom.css",
	"/static/css/theme.css",
	"/static/css/responsive.css"
]

# Generate HTML
css_html = render_custom_css_files(css_files)
# Result:
# <link href="/static/css/custom.css" rel="stylesheet" type="text/css">
# <link href="/static/css/theme.css" rel="stylesheet" type="text/css">
# <link href="/static/css/responsive.css" rel="stylesheet" type="text/css">
```

### `render_custom_javascript_files(js_files)`

Generates HTML `<script>` tags for custom JavaScript files.

#### Parameters

- `js_files` (list) - list of JavaScript file URLs

#### Returns

HTML string with `<script>` tags

#### Examples

```python
from metroui5.html import render_custom_javascript_files

# JavaScript files list
js_files = [
	"/static/js/custom.js",
	"/static/js/plugins.js",
	"/static/js/analytics.js"
]

# Generate HTML
js_html = render_custom_javascript_files(js_files)
# Result:
# <script src="/static/js/custom.js"></script>
# <script src="/static/js/plugins.js"></script>
# <script src="/static/js/analytics.js"></script>
```

## Usage Examples

### Creating Custom Components

```python
from metroui5.html import render_tag


def render_custom_alert(message, alert_type="info"):
	"""Creates custom alert"""
	classes = f"alert alert-{alert_type} custom-alert"

	return render_tag(
		"div",
		{"class": classes, "role": "alert"},
		f"""
            <span class="alert-icon">!</span>
            <span class="alert-message">{message}</span>
            <button class="alert-close" onclick="this.parentElement.remove()">×</button>
        """
	)


# Usage
alert = render_custom_alert("Important message!", "warning")
```

### Generating Navigation Menu

```python
from metroui5.html import render_tag


def render_nav_menu(items):
	"""Creates navigation menu"""
	menu_items = []

	for item in items:
		if item.get('active'):
			classes = "nav-item active"
		else:
			classes = "nav-item"

		link = render_tag(
			"a",
			{"href": item['url'], "class": "nav-link"},
			item['text']
		)

		menu_item = render_tag("li", {"class": classes}, link)
		menu_items.append(menu_item)

	return render_tag("ul", {"class": "nav-menu"}, "".join(menu_items))


# Usage
nav_items = [
	{"text": "Home", "url": "/", "active": True},
	{"text": "About", "url": "/about/", "active": False},
	{"text": "Contact", "url": "/contact/", "active": False},
]

nav_menu = render_nav_menu(nav_items)
```

### Creating Table

```python
from metroui5.html import render_tag


def render_data_table(headers, rows, table_class="table"):
	"""Creates HTML table"""
	# Headers
	header_cells = []
	for header in headers:
		th = render_tag("th", {}, header)
		header_cells.append(th)

	header_row = render_tag("tr", {}, "".join(header_cells))

	# Data rows
	data_rows = []
	for row in rows:
		cells = []
		for cell in row:
			td = render_tag("td", {}, str(cell))
			cells.append(td)
		tr = render_tag("tr", {}, "".join(cells))
		data_rows.append(tr)

	# Assemble table
	thead = render_tag("thead", {}, header_row)
	tbody = render_tag("tbody", {}, "".join(data_rows))

	return render_tag("table", {"class": table_class}, thead + tbody)


# Usage
headers = ["Name", "Email", "Status"]
rows = [
	["Ivan", "ivan@example.com", "Active"],
	["Petr", "petr@example.com", "Inactive"],
]

table = render_data_table(headers, rows, "table table-striped")
```

### Generating Forms

```python
from metroui5.html import render_tag


def render_form_field(field_name, field_type="text", **attrs):
	"""Creates form field"""
	default_attrs = {
		"name": field_name,
		"id": field_name,
		"type": field_type,
		"class": "form-control"
	}

	# Combine attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("input", final_attrs, close=False)


def render_form_group(label_text, field_html, help_text=None):
	"""Creates form group with label and field"""
	label = render_tag("label", {"for": "field", "class": "form-label"}, label_text)

	group_content = label + field_html

	if help_text:
		help_element = render_tag("div", {"class": "form-text"}, help_text)
		group_content += help_element

	return render_tag("div", {"class": "form-group"}, group_content)


# Usage
name_field = render_form_field("name", placeholder="Enter name")
email_field = render_form_field("email", "email", placeholder="Enter email")

name_group = render_form_group("Name:", name_field, "Enter your full name")
email_group = render_form_group("Email:", email_field, "Will be used for contact")

form = render_tag("form", {"method": "post"}, name_group + email_group)
```

## Customization

### Creating Custom HTML Utilities

```python
from metroui5.html import render_tag


def render_icon(icon_name, size="16px", color="currentColor"):
	"""Creates SVG icon"""
	svg_attrs = {
		"width": size,
		"height": size,
		"fill": color,
		"viewBox": "0 0 24 24"
	}

	# Here you can add SVG path for icon
	path = render_tag("path", {
		"d": "M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"},
					  close=False)

	return render_tag("svg", svg_attrs, path)


def render_badge(text, badge_type="default"):
	"""Creates badge"""
	classes = f"badge badge-{badge_type}"
	return render_tag("span", {"class": classes}, text)


# Usage
star_icon = render_icon("star", "24px", "#ffd700")
badge = render_badge("New", "success")
```

### Extending Existing Functions

```python
from metroui5.html import render_tag


def render_enhanced_tag(tag, attrs=None, content=None, close=True, **kwargs):
	"""Enhanced version of render_tag with additional capabilities"""

	# Add data attributes
	if 'data' in kwargs:
		for key, value in kwargs['data'].items():
			if attrs is None:
				attrs = {}
			attrs[f"data-{key}"] = value

	# Add aria attributes
	if 'aria' in kwargs:
		for key, value in kwargs['aria'].items():
			if attrs is None:
				attrs = {}
			attrs[f"aria-{key}"] = value

	# Add events
	if 'events' in kwargs:
		for event, handler in kwargs['events'].items():
			if attrs is None:
				attrs = {}
			attrs[f"on{event}"] = handler

	return render_tag(tag, attrs, content, close)


# Usage
enhanced_div = render_enhanced_tag(
	"div",
	{"class": "enhanced-element"},
	"Content",
	data={"id": "123", "type": "info"},
	aria={"label": "Description", "hidden": "false"},
	events={"click": "handleClick()", "mouseover": "handleHover()"}
)
```

## Best Practices

### 1. Use Semantic Tags

```python
# Good
article = render_tag("article", {"class": "blog-post"}, content)
section = render_tag("section", {"class": "content"}, section_content)

# Bad
div = render_tag("div", {"class": "blog-post"}, content)
div = render_tag("div", {"class": "content"}, section_content)
```

### 2. Add Accessibility Attributes

```python
# Good
button = render_tag(
	"button",
	{
		"class": "btn",
		"aria-label": "Close modal window",
		"aria-expanded": "false"
	},
	"Close"
)

# Bad
button = render_tag("button", {"class": "btn"}, "Close")
```

### 3. Use Constants for Repeating Values

```python
# Good
FORM_CLASSES = "form-control"
BUTTON_CLASSES = "btn btn-primary"

name_field = render_tag("input", {"class": FORM_CLASSES, "name": "name"})
submit_button = render_tag("button", {"class": BUTTON_CLASSES, "type": "submit"}, "Submit")

# Bad
name_field = render_tag("input", {"class": "form-control", "name": "name"})
submit_button = render_tag("button", {"class": "btn btn-primary", "type": "submit"}, "Submit")
```

### 4. Handle Errors

```python
def safe_render_tag(tag, attrs=None, content=None, close=True):
	"""Safe version of render_tag with error handling"""
	try:
		return render_tag(tag, attrs, content, close)
	except Exception as e:
		logger.error(f"Error rendering tag {tag}: {e}")
		# Return fallback
		return f"<{tag}>Rendering error</{tag}>"
```

## Testing

### Unit Tests

```python
from django.test import TestCase
from metroui5.html import render_tag, render_link_tag, render_script_tag


class HTMLTestCase(TestCase):

	def test_render_tag_basic(self):
		"""Test basic tag rendering"""
		result = render_tag("div", {"class": "test"}, "content")
		expected = '<div class="test">content</div>'
		self.assertEqual(result, expected)

	def test_render_tag_no_close(self):
		"""Test tag without closing"""
		result = render_tag("hr", {"class": "divider"}, close=False)
		expected = '<hr class="divider">'
		self.assertEqual(result, expected)

	def test_render_link_tag(self):
		"""Test link tag rendering"""
		result = render_link_tag("/style.css", rel="stylesheet")
		expected = '<link href="/style.css" rel="stylesheet">'
		self.assertEqual(result, expected)

	def test_render_script_tag(self):
		"""Test script tag rendering"""
		result = render_script_tag("/app.js", defer=True)
		expected = '<script src="/app.js" defer></script>'
		self.assertEqual(result, expected)
```

## Related Modules

- [Core Functions](core.md) - for getting settings
- [CSS Utilities](css.md) - for working with CSS classes
- [Components](components.md) - for rendering UI components

## Next Steps

Now that you've mastered HTML utilities:

1. Study [CSS utilities](css.md) for working with styles
2. Check out [components](components.md) for creating UI
3. Create your own HTML utilities for specific tasks
4. Integrate HTML utilities into your Django views!
