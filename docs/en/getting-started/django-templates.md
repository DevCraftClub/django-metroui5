# Using MetroUI5 Components in Django Templates

This guide shows you how to use MetroUI5 components effectively in Django templates, including both template tags and view-based approaches.

## Template Tags vs View-Based Components

MetroUI5 provides two main ways to use components in Django:

1. **Template Tags** - Use components directly in templates
2. **View-Based** - Create components in views and pass to templates

## Template Tags Approach

### Basic Usage

```html
{% load metroui5 %}

<!-- Basic alert -->
{% metroui5_alert "Welcome to our application!" alert_type="success" %}

<!-- Button with icon -->
{% metroui5_button "Save Changes" button_type="primary" icon="checkmark" %}

<!-- Icon -->
{% metroui5_icon "home" size="2x" %}
```

### Template Tag Examples

#### Alerts

```html
{% load metroui5 %}

<!-- Success alert -->
{% metroui5_alert "Operation completed successfully!" alert_type="success"
dismissible=True %}

<!-- Warning alert -->
{% metroui5_alert "Please review your input" alert_type="warning" %}

<!-- Error alert -->
{% metroui5_alert "An error occurred" alert_type="danger" dismissible=True %}
```

#### Buttons

```html
{% load metroui5 %}

<!-- Primary button -->
{% metroui5_button "Submit" button_type="primary" %}

<!-- Button with icon -->
{% metroui5_button "Download" button_type="success" icon="download" %}

<!-- Outline button -->
{% metroui5_button "Cancel" button_type="secondary" outline=True %}
```

#### Icons

```html
{% load metroui5 %}

<!-- Basic icon -->
{% metroui5_icon "user" %}

<!-- Icon with size -->
{% metroui5_icon "mail" size="3x" %}

<!-- Icon with custom classes -->
{% metroui5_icon "heart" class="icon-red" %}
```

## View-Based Approach

### Creating Components in Views

```python
# views.py
from metroui5.components import render_alert, render_button
from metroui5.templatetags.metroui5 import metroui5_icon

def dashboard_view(request):
    # Create alerts
    welcome_alert = render_alert(
        "Welcome back, {}!".format(request.user.first_name),
        alert_type="success",
        dismissible=True
    )

    # Create buttons
    save_button = render_button(
        "Save Settings",
        button_type="primary",
        icon="checkmark"
    )

    # Create icons
    user_icon = metroui5_icon("user", size="2x", class="icon-primary")

    context = {
        'welcome_alert': welcome_alert,
        'save_button': save_button,
        'user_icon': user_icon,
    }
    return render(request, 'dashboard.html', context)
```

### Using in Templates

```html
<!-- dashboard.html -->
{% load metroui5 %} {% block content %}
<!-- Display alert -->
{{ welcome_alert|safe }}

<!-- Display button -->
{{ save_button|safe }}

<!-- Display icon -->
{{ user_icon|safe }} {% endblock %}
```

## Advanced Patterns

### Conditional Components

```python
# views.py
def profile_view(request):
    components = []

    # Add alerts based on user status
    if not request.user.email_verified:
        components.append(render_alert(
            "Please verify your email address",
            alert_type="warning",
            dismissible=True
        ))

    if request.user.is_new:
        components.append(render_alert(
            "Complete your profile setup",
            alert_type="info",
            dismissible=True
        ))

    # Add action buttons
    action_buttons = [
        render_button("Edit Profile", button_type="primary", icon="edit"),
        render_button("Change Password", button_type="secondary", icon="key"),
    ]

    context = {
        'alerts': components,
        'action_buttons': action_buttons,
    }
    return render(request, 'profile.html', context)
```

```html
<!-- profile.html -->
{% load metroui5 %} {% block content %}
<!-- Display conditional alerts -->
{% for alert in alerts %} {{ alert|safe }} {% endfor %}

<!-- Display action buttons -->
<div class="button-group">
	{% for button in action_buttons %} {{ button|safe }} {% endfor %}
</div>
{% endblock %}
```

### Dynamic Component Lists

```python
# views.py
def navigation_view(request):
    nav_items = [
        {
            "text": "Dashboard",
            "icon": metroui5_icon("dashboard"),
            "url": "/dashboard/",
            "active": request.path == "/dashboard/"
        },
        {
            "text": "Users",
            "icon": metroui5_icon("users"),
            "url": "/users/",
            "active": request.path.startswith("/users/")
        },
        {
            "text": "Settings",
            "icon": metroui5_icon("cog"),
            "url": "/settings/",
            "active": request.path.startswith("/settings/")
        },
    ]

    context = {'nav_items': nav_items}
    return render(request, 'navigation.html', context)
```

```html
<!-- navigation.html -->
{% load metroui5 %}

<nav class="nav nav-horizontal">
	{% for item in nav_items %}
	<a
		href="{{ item.url }}"
		class="nav-item {% if item.active %}active{% endif %}"
	>
		{{ item.icon|safe }} {{ item.text }}
	</a>
	{% endfor %}
</nav>
```

### Form Components

```python
# views.py
def form_view(request):
    if request.method == 'POST':
        # Process form
        submit_button = render_button(
            "Processing...",
            button_type="primary",
            disabled=True
        )
        status_alert = render_alert(
            "Form submitted successfully!",
            alert_type="success"
        )
    else:
        submit_button = render_button(
            "Submit Form",
            button_type="primary",
            icon="checkmark"
        )
        status_alert = None

    context = {
        'submit_button': submit_button,
        'status_alert': status_alert,
    }
    return render(request, 'form.html', context)
```

```html
<!-- form.html -->
{% load metroui5 %} {% block content %} {% if status_alert %} {{
status_alert|safe }} {% endif %}

<form method="post">
	<!-- Form fields -->
	<div class="form-group">
		<label>Name:</label>
		<input type="text" name="name" class="input" required />
	</div>

	<div class="form-group">
		<label>Email:</label>
		<input type="email" name="email" class="input" required />
	</div>

	<!-- Submit button -->
	<div class="form-actions">
		{{ submit_button|safe }} {% metroui5_button "Reset" button_type="secondary"
		type="reset" %}
	</div>
</form>
{% endblock %}
```

### Component Mixing

```python
# views.py
def mixed_components_view(request):
    # Mix template tags and view-based components
    view_alert = render_alert(
        "This alert was created in the view",
        alert_type="info"
    )

    view_button = render_button(
        "View Button",
        button_type="primary"
    )

    context = {
        'view_alert': view_alert,
        'view_button': view_button,
    }
    return render(request, 'mixed.html', context)
```

```html
<!-- mixed.html -->
{% load metroui5 %} {% block content %}
<!-- View-based components -->
{{ view_alert|safe }} {{ view_button|safe }}

<!-- Template tag components -->
{% metroui5_alert "This alert was created with template tags"
alert_type="success" %} {% metroui5_button "Template Button"
button_type="secondary" %}

<!-- Mix both approaches -->
<div class="component-group">
	{{ view_alert|safe }} {% metroui5_button "Template Tag Button"
	button_type="info" %}
</div>
{% endblock %}
```

## Best Practices

### 1. Choose the Right Approach

**Use Template Tags when:**

- Components are static or simple
- You want to keep logic in templates
- Components don't depend on complex view logic

**Use View-Based when:**

- Components depend on user data or permissions
- You need conditional logic
- Components are part of complex business logic

### 2. Consistent Styling

```python
# views.py
def consistent_styling_view(request):
    # Use consistent button styling
    primary_buttons = [
        render_button("Save", button_type="primary", icon="checkmark"),
        render_button("Update", button_type="primary", icon="edit"),
        render_button("Create", button_type="primary", icon="plus"),
    ]

    # Use consistent alert styling
    alerts = [
        render_alert("Success message", alert_type="success"),
        render_alert("Warning message", alert_type="warning"),
        render_alert("Error message", alert_type="danger"),
    ]

    context = {
        'primary_buttons': primary_buttons,
        'alerts': alerts,
    }
    return render(request, 'consistent.html', context)
```

### 3. Component Reusability

```python
# utils.py
from metroui5.components import render_alert, render_button
from metroui5.templatetags.metroui5 import metroui5_icon

def create_status_alert(status, message):
    """Create consistent status alerts."""
    status_map = {
        'success': 'success',
        'error': 'danger',
        'warning': 'warning',
        'info': 'info'
    }

    return render_alert(
        message,
        alert_type=status_map.get(status, 'info'),
        dismissible=True
    )

def create_action_button(text, action_type, icon=None):
    """Create consistent action buttons."""
    type_map = {
        'save': 'primary',
        'delete': 'danger',
        'edit': 'info',
        'cancel': 'secondary'
    }

    return render_button(
        text,
        button_type=type_map.get(action_type, 'default'),
        icon=icon
    )
```

```python
# views.py
from .utils import create_status_alert, create_action_button

def reusable_components_view(request):
    alerts = [
        create_status_alert('success', 'Operation completed'),
        create_status_alert('warning', 'Please review your data'),
    ]

    buttons = [
        create_action_button('Save', 'save', 'checkmark'),
        create_action_button('Delete', 'delete', 'delete'),
        create_action_button('Edit', 'edit', 'edit'),
    ]

    context = {
        'alerts': alerts,
        'buttons': buttons,
    }
    return render(request, 'reusable.html', context)
```

### 4. Performance Considerations

```python
# views.py
def performance_view(request):
    # Cache frequently used components
    if not hasattr(request, '_cached_components'):
        request._cached_components = {
            'user_icon': metroui5_icon("user", class="nav-icon"),
            'home_icon': metroui5_icon("home", class="nav-icon"),
            'settings_icon': metroui5_icon("cog", class="nav-icon"),
        }

    context = {
        'cached_icons': request._cached_components,
    }
    return render(request, 'performance.html', context)
```

## Common Patterns

### 1. Dashboard with Multiple Components

```python
# views.py
def dashboard_view(request):
    # Status alerts
    alerts = []
    if request.user.is_new:
        alerts.append(render_alert(
            "Welcome! Complete your profile.",
            alert_type="info",
            dismissible=True
        ))

    # Action buttons
    action_buttons = [
        render_button("New Project", button_type="primary", icon="plus"),
        render_button("Import Data", button_type="secondary", icon="upload"),
    ]

    # Navigation icons
    nav_icons = {
        'dashboard': metroui5_icon("dashboard", class="nav-icon"),
        'projects': metroui5_icon("folder", class="nav-icon"),
        'settings': metroui5_icon("cog", class="nav-icon"),
    }

    context = {
        'alerts': alerts,
        'action_buttons': action_buttons,
        'nav_icons': nav_icons,
    }
    return render(request, 'dashboard.html', context)
```

### 2. Form with Dynamic Components

```python
# views.py
def dynamic_form_view(request):
    form_data = request.POST if request.method == 'POST' else {}

    # Dynamic submit button based on form state
    if form_data:
        submit_button = render_button(
            "Saving...",
            button_type="primary",
            disabled=True
        )
    else:
        submit_button = render_button(
            "Save Changes",
            button_type="primary",
            icon="checkmark"
        )

    # Dynamic alerts based on form validation
    alerts = []
    if 'email' in form_data and '@' not in form_data['email']:
        alerts.append(render_alert(
            "Please enter a valid email address",
            alert_type="danger"
        ))

    context = {
        'submit_button': submit_button,
        'alerts': alerts,
    }
    return render(request, 'dynamic_form.html', context)
```

This comprehensive guide shows you how to effectively use MetroUI5 components in Django templates, covering both template tags and view-based approaches with practical examples and best practices.
