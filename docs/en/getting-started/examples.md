# Examples

Practical examples of using MetroUI5 Django in various scenarios.

## Simple Page

### View

```python
from django.shortcuts import render
from metroui5.components import render_alert, render_button, render_card


def simple_page(request):
	context = {
		'welcome_alert': render_alert(
			"Welcome to our page!",
			alert_type="info"
		),
		'action_buttons': [
			render_button("Primary button", button_type="primary"),
			render_button("Secondary button", button_type="secondary"),
			render_button("Success", button_type="success"),
		],
		'info_card': render_card(
			header="Information",
			content="This is a simple card with information about the project.",
			footer="Created with MetroUI5 Django"
		)
	}
	return render(request, 'simple_page.html', context)
```

### Template

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }}

<div class="row">
	<div class="cell-md-8">{{ info_card|safe }}</div>
	<div class="cell-md-4">
		<h3>Actions</h3>
		{% for button in action_buttons %}
		<div class="mb-2">{{ button|safe }}</div>
		{% endfor %}
	</div>
</div>
{% endblock %}
```

## Dashboard

### View

```python
from metroui5.components import (
	render_card, render_table, render_progress,
	render_badge, render_tile
)


def dashboard(request):
	# Statistics
	stats = [
		{'label': 'Users', 'value': '1,234', 'color': 'blue'},
		{'label': 'Orders', 'value': '567', 'color': 'green'},
		{'label': 'Revenue', 'value': '$12,345', 'color': 'orange'},
		{'label': 'Products', 'value': '89', 'color': 'red'},
	]

	# Recent orders
	recent_orders = [
		['#1234', 'Ivan Ivanov', 'Product A', '$100', 'Processed'],
		['#1235', 'Petr Petrov', 'Product B', '$200', 'In Transit'],
		['#1236', 'Sidor Sidorov', 'Product C', '$150', 'Delivered'],
	]

	# Task progress
	tasks = [
		{'name': 'Development', 'progress': 75, 'color': 'blue'},
		{'name': 'Testing', 'progress': 45, 'color': 'green'},
		{'name': 'Documentation', 'progress': 90, 'color': 'orange'},
	]

	context = {
		'stats_tiles': [
			render_tile(
				title=stat['label'],
				content=stat['value'],
				color=stat['color'],
				size="small"
			) for stat in stats
		],
		'stats_card': render_card(
			header="Statistics",
			content="<div class='row'>" +
					"".join([f"<div class='cell-md-3'>{tile}</div>" for tile in context['stats_tiles']]) +
					"</div>"
		),
		'orders_table': render_table(
			headers=['Number', 'Customer', 'Product', 'Amount', 'Status'],
			rows=recent_orders
		),
		'tasks_progress': [
			render_progress(
				value=task['progress'],
				color=task['color'],
				**{"data-label": task['name']}
			) for task in tasks
		]
	}

	return render(request, 'dashboard.html', context)
```

### Template

```html
{% extends 'base.html' %} {% block content %}
<h1>Dashboard</h1>

{{ stats_card|safe }}

<div class="row">
	<div class="cell-md-8">
		<h3>Recent Orders</h3>
		{{ orders_table|safe }}
	</div>
	<div class="cell-md-4">
		<h3>Task Progress</h3>
		{% for progress in tasks_progress %} {{ progress|safe }}
		<br />
		{% endfor %}
	</div>
</div>
{% endblock %}
```

## Form with Validation

### Form

```python
from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
	)
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'placeholder': 'Enter email'})
	)
	subject = forms.CharField(
		max_length=200,
		widget=forms.TextInput(attrs={'placeholder': 'Message subject'})
	)
	message = forms.CharField(
		widget=forms.Textarea(attrs={'placeholder': 'Your message', 'rows': 5})
	)
```

### View

```python
from metroui5.forms import render_form, render_form_errors
from metroui5.components import render_alert, render_button


def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Form processing
			success_alert = render_alert(
				"Message sent successfully!",
				alert_type="success"
			)
			return render(request, 'contact_success.html', {
				'alert': success_alert
			})
	else:
		form = ContactForm()

	# Render form with MetroUI5 styles
	form_html = render_form(
		form,
		layout='horizontal',
		submit_text="Send message",
		submit_class="btn btn-primary"
	)

	return render(request, 'contact_form.html', {'form': form_html})
```

### Template

```html
{% extends 'base.html' %} {% block content %}
<div class="row">
	<div class="cell-md-8">
		<h2>Contact Us</h2>
		{{ form|safe }}
	</div>
	<div class="cell-md-4">
		<h3>Contact Information</h3>
		<p><strong>Email:</strong> info@example.com</p>
		<p><strong>Phone:</strong> +7 (123) 456-78-90</p>
		<p><strong>Address:</strong> Example St., 123</p>
	</div>
</div>
{% endblock %}
```

## Navigation Menu

### View

```python
from metroui5.components import render_navigation, render_breadcrumb


def navigation_example(request):
	# Main menu
	nav_items = [
		{'text': 'Home', 'url': '/', 'icon': 'home'},
		{'text': 'About', 'url': '/about/', 'icon': 'info'},
		{'text': 'Services', 'url': '/services/', 'icon': 'cog'},
		{'text': 'Contact', 'url': '/contact/', 'icon': 'mail'},
	]

	# Breadcrumbs
	breadcrumb_items = [
		{'text': 'Home', 'url': '/'},
		{'text': 'Services', 'url': '/services/'},
		{'text': 'Web Development', 'url': None},
	]

	context = {
		'main_navigation': render_navigation(nav_items),
		'breadcrumbs': render_breadcrumb(breadcrumb_items),
	}

	return render(request, 'navigation_example.html', context)
```

### Template

```html
{% extends 'base.html' %} {% block content %} {{ breadcrumbs|safe }}

<div class="row">
	<div class="cell-md-3">{{ main_navigation|safe }}</div>
	<div class="cell-md-9">
		<h1>Web Development</h1>
		<p>Page content...</p>
	</div>
</div>
{% endblock %}
```

## Modal Window

### View

```python
from metroui5.components import render_modal, render_button


def modal_example(request):
	# Button to open modal window
	open_button = render_button(
		"Open modal window",
		button_type="primary",
		**{"data-role": "button", "data-toggle": "modal", "data-target": "#exampleModal"}
	)

	# Modal window
	modal = render_modal(
		title="Modal window example",
		content="""
            <p>This is modal window content.</p>
            <p>You can add any HTML markup.</p>
        """,
		modal_id="exampleModal"
	)

	context = {
		'open_button': open_button,
		'modal': modal,
	}

	return render(request, 'modal_example.html', context)
```

### Template

```html
{% extends 'base.html' %} {% block content %}
<h1>Modal window example</h1>

{{ open_button|safe }} {{ modal|safe }} {% endblock %}
```

## Table with Data

### View

```python
from metroui5.components import render_table, render_button, render_badge


def table_example(request):
	# Table data
	users = [
		{
			'id': 1,
			'name': 'Ivan Ivanov',
			'email': 'ivan@example.com',
			'status': 'Active',
			'actions': 'Actions'
		},
		{
			'id': 2,
			'name': 'Petr Petrov',
			'email': 'petr@example.com',
			'status': 'Inactive',
			'actions': 'Actions'
		},
		{
			'id': 3,
			'name': 'Sidor Sidorov',
			'email': 'sidor@example.com',
			'status': 'Active',
			'actions': 'Actions'
		},
	]

	# Transform data for table
	table_rows = []
	for user in users:
		status_badge = render_badge(
			user['status'],
			badge_type="success" if user['status'] == 'Active' else "alert"
		)

		action_buttons = [
			render_button("Edit", button_type="secondary", size="small"),
			render_button("Delete", button_type="alert", size="small"),
		]

		row = [
			user['id'],
			user['name'],
			user['email'],
			status_badge,
			" ".join([btn for btn in action_buttons])
		]
		table_rows.append(row)

	context = {
		'users_table': render_table(
			headers=['ID', 'Name', 'Email', 'Status', 'Actions'],
			rows=table_rows,
			**{"class": "table-border"}
		)
	}

	return render(request, 'table_example.html', context)
```

### Template

```html
{% extends 'base.html' %} {% block content %}
<h1>Users</h1>

{{ users_table|safe }} {% endblock %}
```

## Comprehensive Example

### View

```python
from metroui5.components import *
from metroui5.forms import render_form


def comprehensive_example(request):
	# Create comprehensive page with various components

	# Alert
	welcome_alert = render_alert(
		"Welcome to comprehensive MetroUI5 example!",
		alert_type="success",
		dismissible=True
	)

	# Information cards
	info_cards = [
		render_card(
			header="Statistics",
			content="<p>Total users: <strong>1,234</strong></p>",
			footer="Updated today"
		),
		render_card(
			header="Quick Actions",
			content="<p>Choose action to continue work</p>",
			footer="Available 24/7"
		),
	]

	# Action buttons
	action_buttons = [
		render_button("Create", button_type="primary", icon="plus"),
		render_button("Edit", button_type="secondary", icon="edit"),
		render_button("Delete", button_type="alert", icon="trash"),
	]

	# Progress bars
	progress_bars = [
		render_progress(75, color="blue", **{"data-label": "Task 1"}),
		render_progress(45, color="green", **{"data-label": "Task 2"}),
		render_progress(90, color="orange", **{"data-label": "Task 3"}),
	]

	# Tiles
	tiles = [
		render_tile("Users", "1,234", "blue", "medium", "users"),
		render_tile("Orders", "567", "green", "medium", "cart"),
		render_tile("Revenue", "$12,345", "orange", "medium", "dollar"),
	]

	context = {
		'welcome_alert': welcome_alert,
		'info_cards': info_cards,
		'action_buttons': action_buttons,
		'progress_bars': progress_bars,
		'tiles': tiles,
	}

	return render(request, 'comprehensive_example.html', context)
```

### Template

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }}

<div class="row">
	<div class="cell-md-8">
		<h2>Information</h2>
		{% for card in info_cards %} {{ card|safe }}
		<br />
		{% endfor %}

		<h3>Task Progress</h3>
		{% for progress in progress_bars %} {{ progress|safe }}
		<br />
		{% endfor %}
	</div>

	<div class="cell-md-4">
		<h3>Quick Actions</h3>
		{% for button in action_buttons %}
		<div class="mb-2">{{ button|safe }}</div>
		{% endfor %}

		<h3>Statistics</h3>
		<div class="row">
			{% for tile in tiles %}
			<div class="cell-md-4">{{ tile|safe }}</div>
			{% endfor %}
		</div>
	</div>
</div>
{% endblock %}
```

## Next Steps

These examples demonstrate the main capabilities of MetroUI5 Django. For more detailed study:

1. Study [components](../components/) to understand all available capabilities
2. Check out the [API reference](../api-reference/) for detailed information
3. Create your own project using these examples as a foundation
4. Experiment with various component combinations
