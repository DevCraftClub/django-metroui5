# Alerts

Component for displaying informational messages, warnings and errors.

## Basic Usage

### Simple Alert

```python
from metroui5.components import render_alert

# Basic alert
alert = render_alert("This is an informational message")
```

### Alert with Type

```python
# Various alert types
info_alert = render_alert("Information", alert_type="info")
success_alert = render_alert("Success!", alert_type="success")
warning_alert = render_alert("Warning!", alert_type="warning")
error_alert = render_alert("Error!", alert_type="error")
```

### Dismissible Alert

```python
# Alert with close capability
dismissible_alert = render_alert(
	"This message can be closed",
	alert_type="info",
	dismissible=True
)
```

## Rendered Output

### Basic Alert

```html
<!-- Input -->
render_alert("This is an alert message")

<!-- Output -->
<div class="alert alert-info" role="alert">This is an alert message</div>
```

### Dismissible Alert

```html
<!-- Input -->
render_alert("This alert can be dismissed", alert_type="warning",
dismissible=True)

<!-- Output -->
<div class="alert alert-warning alert-dismissible" role="alert">
	This alert can be dismissed
	<button
		type="button"
		class="button button-mini"
		data-role="close"
		aria-label="Close"
	>
		&times;
	</button>
</div>
```

### Alert with Icon

```html
<!-- Input -->
render_alert("Success! Operation completed.", alert_type="success",
icon="checkmark")

<!-- Output -->
<div class="alert alert-success" role="alert">
	<span class="mif-checkmark"></span>
	Success! Operation completed.
</div>
```

## Parameters

### `content` (required)

Message text for display.

```python
alert = render_alert("Your message here")
```

### `alert_type` (optional)

Alert type that determines style and color. Available values:

- `"info"` (default) - blue
- `"success"` - green
- `"warning"` - yellow/orange
- `"error"` - red

```python
alert = render_alert("Message", alert_type="success")
```

### `dismissible` (optional)

If `True`, adds close button. Default `False`.

```python
alert = render_alert("Dismissible message", dismissible=True)
```

### `**attrs` (optional)

Additional HTML attributes.

```python
alert = render_alert(
	"Custom alert",
	**{"class": "custom-alert", "id": "myAlert"}
)
```

## Usage Examples

### In View

```python
from metroui5.components import render_alert


def dashboard(request):
	context = {
		'welcome_alert': render_alert(
			"Welcome to the dashboard!",
			alert_type="success"
		),
		'info_alert': render_alert(
			"System updated to version 2.0",
			alert_type="info",
			dismissible=True
		),
		'warning_alert': render_alert(
			"Don't forget to save changes before exiting",
			alert_type="warning"
		)
	}
	return render(request, 'dashboard.html', context)
```

### In Template

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }} {{
info_alert|safe }} {{ warning_alert|safe }}

<h2>Main content</h2>
<p>Page content...</p>
{% endblock %}
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic alert -->
{% metroui5_alert "This is an alert message" alert_type="info" %}

<!-- Dismissible alert -->
{% metroui5_alert "This alert can be dismissed" alert_type="warning"
dismissible=True %}

<!-- Alert with custom classes -->
{% metroui5_alert "Custom styled alert" alert_type="success"
class="alert-custom" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_alert

def my_view(request):
    # Create alert in view
    alert_html = render_alert(
        "Welcome to our application!",
        alert_type="success",
        dismissible=True
    )

    context = {
        'alert_html': alert_html,
        'user_alerts': [
            render_alert("Profile updated successfully", "success"),
            render_alert("Please verify your email", "warning"),
        ]
    }
    return render(request, 'my_template.html', context)
```

```html
<!-- my_template.html -->
{% load metroui5 %}

<!-- Direct HTML output -->
{{ alert_html|safe }}

<!-- Loop through alerts -->
{% for alert in user_alerts %} {{ alert|safe }} {% endfor %}
```

### Conditional Alerts

```python
# views.py
def dashboard_view(request):
    alerts = []

    if not request.user.email_verified:
        alerts.append(render_alert(
            "Please verify your email address",
            alert_type="warning",
            dismissible=True
        ))

    if request.user.is_new:
        alerts.append(render_alert(
            "Welcome! Complete your profile setup.",
            alert_type="info",
            dismissible=True
        ))

    context = {'alerts': alerts}
    return render(request, 'dashboard.html', context)
```

```html
<!-- dashboard.html -->
{% load metroui5 %} {% block content %}
<!-- Display conditional alerts -->
{% for alert in alerts %} {{ alert|safe }} {% endfor %}

<!-- Main dashboard content -->
<h1>Dashboard</h1>
<!-- ... -->
{% endblock %}
```

### Dynamic Alerts

```python
def form_processing(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			# Processing successful
			alert = render_alert(
				"Form submitted successfully!",
				alert_type="success"
			)
		else:
			# Has errors
			alert = render_alert(
				"Please fix errors in the form.",
				alert_type="error"
			)
	else:
		form = MyForm()
		alert = None

	return render(request, 'form.html', {
		'form': form,
		'alert': alert
	})
```

### Conditional Display

```html
{% if alert %} {{ alert|safe }} {% endif %} {% if messages %} {% for message in
messages %} {% if message.tags == 'success' %} {{ render_alert(message,
alert_type="success")|safe }} {% elif message.tags == 'error' %} {{
render_alert(message, alert_type="error")|safe }} {% elif message.tags ==
'warning' %} {{ render_alert(message, alert_type="warning")|safe }} {% else %}
{{ render_alert(message, alert_type="info")|safe }} {% endif %} {% endfor %} {%
endif %}
```

## Customization

### Additional CSS Classes

```python
alert = render_alert(
	"Custom style",
	**{"class": "alert-custom my-alert"}
)
```

### Attributes for JavaScript

```python
alert = render_alert(
	"Interactive alert",
	**{
		"data-auto-hide": "5000",
		"data-animation": "fade",
		"onclick": "handleAlertClick()"
	}
)
```

### Styling via CSS

```css
/* Custom styles for alerts */
.alert-custom {
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.my-alert {
	font-weight: bold;
	text-transform: uppercase;
}
```

## Best Practices

### 1. Use Correct Types

- `info` - for general information
- `success` - for successful operations
- `warning` - for warnings
- `error` - for errors

### 2. Keep Messages Concise

```python
# Good
alert = render_alert("File uploaded successfully", alert_type="success")

# Bad
alert = render_alert("File was successfully uploaded to the system and saved in the database", alert_type="success")
```

### 3. Use Dismissible for Important Messages

```python
# Important message that user can close
alert = render_alert(
	"Don't forget to save changes!",
	alert_type="warning",
	dismissible=True
)
```

### 4. Group Related Alerts

```python
def process_form(request):
	alerts = []

	if form.is_valid():
		alerts.append(render_alert("Form valid", "success"))

		if user.is_new:
			alerts.append(render_alert("Welcome!", "info"))

	context = {'alerts': alerts}
	return render(request, 'form.html', context)
```

## Troubleshooting

### Alert Not Displaying

1. Check that `render_alert` function is imported
2. Make sure `|safe` filter is used in template
3. Check browser console for JavaScript errors

### Styles Not Applying

1. Make sure MetroUI5 CSS is loaded
2. Check that there are no conflicting CSS rules
3. Use browser inspector to check applied styles

### JavaScript Not Working

1. Check that MetroUI5 JavaScript is loaded
2. Make sure there are no conflicts with other scripts
3. Check browser console for errors

## Related Components

- [Buttons](buttons.md) - for actions in alerts
- [Cards](cards.md) - for grouping information
- [Forms](forms.md) - for displaying validation errors

## Next Steps

Now that you've mastered alerts:

1. Study other [components](../) for creating complete interfaces
2. Check out [examples](../../getting-started/examples.md)
3. Study [API reference](../../api-reference/) for detailed information


## metroui5_alert

```python
render_alert('Text')
```

Empty or invalid: `render_alert('Text')` returns `<div class="alert alert-info" role="alert">Text</div>`. An empty call returns `<div class="alert alert-info" role="alert"></div>`.

```django
{% metroui5_alert content="Text" %}
```
