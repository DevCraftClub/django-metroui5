# MetroUI5 Django Components

Overview of all available components for creating user interfaces.

## Main Components

### 🚨 [Alerts](alerts.md)

Display informational messages, warnings and errors.

**Main features:**

- Various types: info, success, warning, error
- Dismissible alerts
- Customization of styles and attributes

**Usage example:**

```python
from metroui5.components import render_alert

alert = render_alert(
	"Important message!",
	alert_type="warning",
	dismissible=True
)
```

### 🔘 [Buttons](buttons.md)

Creating interactive buttons of various types and sizes.

**Main features:**

- Types: default, primary, secondary, success, alert, warning
- Sizes: small, default, large
- Outline buttons
- Icons

**Usage example:**

```python
from metroui5.components import render_button

button = render_button(
	"Click me!",
	button_type="primary",
	size="large",
	icon="plus"
)
```

### 🃏 [Cards](cards.md)

Information cards with header, content and footer.

**Main features:**

- Header, content and footer
- HTML content
- Style customization

**Usage example:**

```python
from metroui5.components import render_card

card = render_card(
	header="Header",
	content="Card content",
	footer="Footer"
)
```

### 🧱 [Tiles](tiles.md)

Compact information tiles with header, content and icon.

**Main features:**

- Sizes: small, medium, large
- Colors: blue, green, orange, red, purple, yellow, cyan, gray
- MetroUI icons

**Usage example:**

```python
from metroui5.components import render_tile

tile = render_tile(
	title="Users",
	content="1,234",
	color="blue",
	size="small",
	icon="users"
)
```

### 🎨 [Themes](themes.md)

Support for light and dark MetroUI 5 themes with automatic switching.

**Main features:**

- Built-in themes: light, dark, auto
- Theme switcher component
- Automatic system theme detection
- Customization of target element

**Usage example:**

```python
# settings.py
METROUI5 = {
	'theme': 'dark',
	'theme_switcher_enabled': True,
}
```

```html
{% extends "metroui5/layout/base.html" %}
<!-- Dark theme is automatically applied -->
```

### 📝 [Forms](forms.md)

Rendering Django forms with MetroUI5 styles.

**Main features:**

- Layouts: vertical, horizontal
- Submit button customization
- Validation error handling

**Usage example:**

```python
from metroui5.forms import render_form

form_html = render_form(
	form,
	layout='horizontal',
	submit_text="Submit",
	submit_class="btn btn-primary"
)
```

## Additional Components

### 📊 [Tables](tables.md)

Creating HTML tables with data.

**Main features:**

- Headers and data rows
- Style customization
- HTML support in cells

### 🧭 [Navigation](navigation.md)

Navigation menus and elements.

**Main features:**

- Navigation lists
- Active states
- Icons

### 🪟 [Modals](modals.md)

Popup modal windows.

**Main features:**

- Header and content
- Custom IDs
- JavaScript integration

### 📋 [Panels](panels.md)

Information panels with header and content.

**Main features:**

- Header and content
- Various styles
- Customization

### 📈 [Progress Bars](progress.md)

Visualization of task completion progress.

**Main features:**

- Percentage value
- Colors: blue, green, orange, red
- Sizes: default, small, large

### 🪗 [Accordions](accordions.md)

Collapsible content sections.

**Main features:**

- Headers and content
- Open/close states
- Customization

### 📅 [Calendars](calendars.md)

Calendar widgets.

**Main features:**

- Date display
- Events
- Month navigation

### 💬 [Dialogs](dialogs.md)

Dialog windows for interaction.

**Main features:**

- Header and content
- Action buttons
- Customization

### 📋 [Dropdowns](dropdowns.md)

Dropdown menus and lists.

**Main features:**

- List items
- Trigger button
- Customization

### ⌨️ [Input Fields](inputs.md)

HTML input fields of various types.

**Main features:**

- Types: text, email, password, number
- Placeholder text
- Customization

### 📝 [Lists](lists.md)

HTML lists (ul, ol).

**Main features:**

- Types: ul, ol
- List items
- Customization

### 🍽️ [Menus](menus.md)

Context menus.

**Main features:**

- Menu items
- Submenus
- Customization

### 📱 [Sidebars](sidebars.md)

Side navigation panels.

**Main features:**

- Navigation elements
- Grouping
- Customization

### 🏷️ [Tabs](tabs.md)

Tabs for organizing content.

**Main features:**

- Tab headers
- Tab content
- Active states

### 🛠️ [Toolbars](toolbars.md)

Toolbars with tools and actions.

**Main features:**

- Tool elements
- Grouping
- Customization

### 🍞 [Breadcrumbs](breadcrumbs.md)

Navigation breadcrumbs.

**Main features:**

- Navigation elements
- Separators
- Customization

### 📄 [Pagination](pagination.md)

Page navigation.

**Main features:**

- Current page
- Total number of pages
- Navigation buttons

### 🏷️ [Badges](badges.md)

Small information labels.

**Main features:**

- Types: default, success, warning, alert
- Content text
- Customization

### 👤 [Avatars](avatars.md)

User profile images.

**Main features:**

- Image URL
- Sizes: small, medium, large
- Fallback images

### ⭐ [Ratings](ratings.md)

Rating and evaluation systems.

**Main features:**

- Rating value
- Maximum value
- Visual representation

## Combining Components

### Dashboard

```python
from metroui5.components import *


def dashboard_view(request):
	context = {
		# Statistics in tiles
		'stats_tiles': [
			render_tile("Users", "1,234", "blue", "small", "users"),
			render_tile("Orders", "567", "green", "small", "cart"),
			render_tile("Revenue", "$12,345", "orange", "small", "dollar"),
		],

		# Information in cards
		'info_cards': [
			render_card("Recent Orders", "Order list..."),
			render_card("Activity", "Activity chart..."),
		],

		# Actions in buttons
		'action_buttons': [
			render_button("Create", "primary", icon="plus"),
			render_button("Import", "secondary", icon="upload"),
			render_button("Export", "success", icon="download"),
		],

		# Task progress
		'progress_bars': [
			render_progress(75, "blue", **{"data-label": "Task 1"}),
			render_progress(45, "green", **{"data-label": "Task 2"}),
		]
	}

	return render(request, 'dashboard.html', context)
```

### Form with Components

```python
from metroui5.components import *
from metroui5.forms import render_form


def complex_form_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Form processing
			alert = render_alert("Form submitted!", "success")
		else:
			alert = render_alert("Fix errors!", "error")
	else:
		form = ContactForm()
		alert = None

	# Render form
	form_html = render_form(
		form,
		layout='horizontal',
		submit_text="Submit",
		submit_class="btn btn-primary"
	)

	# Create card for form
	form_card = render_card(
		header="Contact Us",
		content=form_html,
		footer="We'll respond within 24 hours"
	)

	context = {
		'alert': alert,
		'form_card': form_card,
	}

	return render(request, 'complex_form.html', context)
```

## Best Practices

### 1. Import only needed components

```python
# Good - import only needed ones
from metroui5.components import render_button, render_card, render_alert

# Bad - import all
from metroui5.components import *
```

### 2. Group related components

```python
# Good - group by purpose
context = {
	'header_components': {
		'alert': render_alert("Message", "info"),
		'breadcrumb': render_breadcrumb(items),
	},
	'main_components': {
		'card': render_card(...),
		'table': render_table(...),
	},
	'footer_components': {
		'buttons': [render_button(...), render_button(...)],
	}
}
```

### 3. Use constants for repeating values

```python
# Good
BUTTON_PRIMARY = "btn btn-primary"
TILE_COLORS = ["blue", "green", "orange", "red"]

tiles = [
	render_tile("Title", "Content", color)
	for color in TILE_COLORS
]

# Bad
tiles = [
	render_tile("Title", "Content", "blue"),
	render_tile("Title", "Content", "green"),
	render_tile("Title", "Content", "orange"),
	render_tile("Title", "Content", "red"),
]
```

### 4. Handle errors

```python
def safe_render_component(component_func, *args, **kwargs):
	"""Safe component rendering with error handling"""
	try:
		return component_func(*args, **kwargs)
	except Exception as e:
		logger.error(f"Component rendering error: {e}")
		return f"<div>Component loading error</div>"


# Usage
button = safe_render_component(render_button, "Text", "primary")
```

## Next Steps

Now that you're familiar with the components:

1. Study the detailed documentation of each component
2. Check out the [examples](../../getting-started/examples.md)
3. Study the [API reference](../../api-reference/) for detailed information
4. Create your own components based on existing ones
5. Build full-featured user interfaces!

## Useful Links

- [Getting Started](../../getting-started/) - usage basics
- [Examples](../../getting-started/examples.md) - practical examples
- [API Reference](../../api-reference/) - detailed documentation
- [GitHub Repository](https://github.com/your-repo/django-metroui5) - source code
