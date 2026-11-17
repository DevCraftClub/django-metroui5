# Buttons

Component for creating interactive buttons of various types and sizes.

## Basic Usage

### Simple Button

```python
from metroui5.components import render_button

# Basic button
button = render_button("Click me")
```

### Button with Type

```python
# Different button types
primary_button = render_button("Primary", button_type="primary")
secondary_button = render_button("Secondary", button_type="secondary")
success_button = render_button("Success", button_type="success")
alert_button = render_button("Error", button_type="alert")
```

### Button with Size

```python
# Different sizes
small_button = render_button("Small", size="small")
default_button = render_button("Default", size="default")
large_button = render_button("Large", size="large")
```

## Rendered Output

### Basic Button

```html
<!-- Input -->
render_button("Click me")

<!-- Output -->
<button type="button" class="button">Click me</button>
```

### Primary Button

```html
<!-- Input -->
render_button("Primary Button", button_type="primary")

<!-- Output -->
<button type="button" class="button primary">Primary Button</button>
```

### Button with Icon

```html
<!-- Input -->
render_button("Save", button_type="success", icon="checkmark")

<!-- Output -->
<button type="button" class="button success">
	<span class="mif-checkmark"></span>
	Save
</button>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic button -->
{% metroui5_button "Click me" %}

<!-- Primary button -->
{% metroui5_button "Primary Button" button_type="primary" %}

<!-- Button with icon -->
{% metroui5_button "Save" button_type="success" icon="checkmark" %}

<!-- Button with custom attributes -->
{% metroui5_button "Custom" button_type="primary" class="my-button"
id="save-btn" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_button

def my_view(request):
    # Create buttons in view
    save_button = render_button(
        "Save Changes",
        button_type="primary",
        icon="checkmark"
    )

    cancel_button = render_button(
        "Cancel",
        button_type="secondary",
        outline=True
    )

    context = {
        'save_button': save_button,
        'cancel_button': cancel_button
    }
    return render(request, 'my_template.html', context)
```

### Using in Templates

```html
<!-- my_template.html -->
{% load metroui5 %}

<!-- Direct HTML output -->
{{ save_button|safe }} {{ cancel_button|safe }}

<!-- Loop through buttons -->
{% for button in action_buttons %} {{ button|safe }} {% endfor %}
```

### Form Buttons

```python
# views.py
def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form
            pass

    # Create submit button
    submit_button = render_button(
        "Submit Form",
        button_type="primary",
        icon="checkmark"
    )

    context = {'submit_button': submit_button}
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

	<!-- Submit button -->
	<div class="form-actions">
		{{ submit_button|safe }} {% metroui5_button "Reset" button_type="secondary"
		type="reset" %}
	</div>
</form>
{% endblock %}
```

## Parameters

### `content` (required)

Text or content of the button.

```python
button = render_button("Button text")
```

### `button_type` (optional)

Button type that determines style and color. Available values:

- `"default"` (default) - standard
- `"primary"` - primary (blue)
- `"secondary"` - secondary (gray)
- `"success"` - success (green)
- `"alert"` - error (red)
- `"warning"` - warning (yellow)

```python
button = render_button("Button", button_type="primary")
```

### `size` (optional)

Button size. Available values:

- `"small"` - small
- `"default"` (default) - normal
- `"large"` - large

```python
button = render_button("Button", size="large")
```

### `outline` (optional)

If `True`, creates an outline button. Default is `False`.

```python
button = render_button("Outline", outline=True)
```

### `icon` (optional)

Icon for the button (MetroUI icon name).

```python
button = render_button("With icon", icon="plus")
```

### `**attrs` (optional)

Additional HTML attributes.

```python
button = render_button(
    "Custom",
    **{"class": "custom-btn", "id": "myButton", "onclick": "handleClick()"}
)
```

## Usage Examples

### In Views

```python
from metroui5.components import render_button


def dashboard(request):
    context = {
        'action_buttons': [
            render_button("Create", button_type="primary", icon="plus"),
            render_button("Edit", button_type="secondary", icon="edit"),
            render_button("Delete", button_type="alert", icon="trash"),
        ],
        'size_buttons': [
            render_button("Small", size="small"),
            render_button("Default", size="default"),
            render_button("Large", size="large"),
        ],
        'outline_buttons': [
            render_button("Primary", button_type="primary", outline=True),
            render_button("Success", button_type="success", outline=True),
        ]
    }
    return render(request, 'dashboard.html', context)
```

### In Templates

```html
<!-- dashboard.html -->
{% extends 'base.html' %} {% block content %}
<h3>Actions</h3>
<div class="button-group">
	{% for button in action_buttons %} {{ button|safe }} {% endfor %}
</div>

<h3>Sizes</h3>
<div class="button-group">
	{% for button in size_buttons %} {{ button|safe }} {% endfor %}
</div>

<h3>Outline Buttons</h3>
<div class="button-group">
	{% for button in outline_buttons %} {{ button|safe }} {% endfor %}
</div>
{% endblock %}
```

### Custom Styling

```css
/* Custom styles for buttons */
.btn-custom {
	border-radius: 20px;
	text-transform: uppercase;
	font-weight: bold;
}

.my-button {
	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
	transition: all 0.3s ease;
}

.my-button:hover {
	transform: translateY(-2px);
	box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}
```

### Button Groups

```python
def button_group_view(request):
    context = {
        'button_group': [
            render_button("First", button_type="primary"),
            render_button("Second", button_type="secondary"),
            render_button("Third", button_type="success"),
        ]
    }
    return render(request, 'button_group.html', context)
```

```html
<!-- button_group.html -->
{% extends 'base.html' %} {% block content %}
<div class="vertical-button-group">
	{% for button in button_group %}
	<div class="mb-2">{{ button|safe }}</div>
	{% endfor %}
</div>
{% endblock %}
```

## Advanced Examples

### Dynamic Button Generation

```python
def dynamic_buttons_view(request):
    # Generate buttons based on user permissions
    buttons = []

    if request.user.is_staff:
        buttons.append(render_button(
            "Admin Panel",
            button_type="primary",
            icon="cog"
        ))

    if request.user.has_perm('app.create_project'):
        buttons.append(render_button(
            "New Project",
            button_type="success",
            icon="plus"
        ))

    if request.user.has_perm('app.delete_project'):
        buttons.append(render_button(
            "Delete Project",
            button_type="alert",
            icon="trash"
        ))

    context = {'buttons': buttons}
    return render(request, 'dynamic_buttons.html', context)
```

### Conditional Button Display

```python
def conditional_buttons_view(request):
    user = request.user

    # Base button
    base_button = render_button(
        "Welcome",
        button_type="primary"
    )

    # Conditional buttons
    conditional_buttons = []

    if not user.email_verified:
        conditional_buttons.append(render_button(
            "Verify Email",
            button_type="warning",
            icon="mail"
        ))

    if user.is_new:
        conditional_buttons.append(render_button(
            "Complete Profile",
            button_type="info",
            icon="user"
        ))

    context = {
        'base_button': base_button,
        'conditional_buttons': conditional_buttons
    }
    return render(request, 'conditional_buttons.html', context)
```

### Interactive Buttons

```python
def interactive_buttons_view(request):
    # Buttons with JavaScript functionality
    interactive_buttons = [
        render_button(
            "Load Data",
            button_type="primary",
            icon="download",
            **{"onclick": "loadData()", "data-loading": "Loading..."}
        ),
        render_button(
            "Save Changes",
            button_type="success",
            icon="checkmark",
            **{"onclick": "saveChanges()", "data-save": "true"}
        ),
        render_button(
            "Reset Form",
            button_type="secondary",
            icon="refresh",
            **{"onclick": "resetForm()", "type": "reset"}
        )
    ]

    context = {'interactive_buttons': interactive_buttons}
    return render(request, 'interactive_buttons.html', context)
```

## Button States

### Loading State

```python
def loading_button_view(request):
    loading_button = render_button(
        "Processing...",
        button_type="primary",
        icon="spinner",
        **{"disabled": True, "class": "loading"}
    )

    context = {'loading_button': loading_button}
    return render(request, 'loading_button.html', context)
```

### Disabled State

```python
def disabled_button_view(request):
    disabled_button = render_button(
        "Unavailable",
        button_type="secondary",
        **{"disabled": True, "title": "This action is not available"}
    )

    context = {'disabled_button': disabled_button}
    return render(request, 'disabled_button.html', context)
```

## Best Practices

### 1. Consistent Button Styling

```python
# Define consistent button styling
BUTTON_STYLES = {
    'primary': {'button_type': 'primary', 'icon': 'checkmark'},
    'secondary': {'button_type': 'secondary', 'icon': 'arrow-right'},
    'danger': {'button_type': 'alert', 'icon': 'trash'},
    'success': {'button_type': 'success', 'icon': 'plus'}
}

def create_consistent_button(text, style, **kwargs):
    """Create a button with consistent styling."""

    button_style = BUTTON_STYLES.get(style, BUTTON_STYLES['primary'])
    button_style.update(kwargs)

    return render_button(text, **button_style)

# Usage
def consistent_buttons_view(request):
    context = {
        'save_button': create_consistent_button("Save", "primary"),
        'cancel_button': create_consistent_button("Cancel", "secondary"),
        'delete_button': create_consistent_button("Delete", "danger"),
        'add_button': create_consistent_button("Add", "success")
    }
    return render(request, 'consistent_buttons.html', context)
```

### 2. Button Accessibility

```python
def create_accessible_button(text, button_type="default", **kwargs):
    """Create a button with proper accessibility attributes."""

    # Add accessibility attributes
    accessibility_attrs = {
        'aria-label': kwargs.get('aria_label', text),
        'role': 'button',
        'tabindex': '0'
    }

    # Merge with existing attributes
    if 'attrs' not in kwargs:
        kwargs['attrs'] = {}
    kwargs['attrs'].update(accessibility_attrs)

    return render_button(text, button_type=button_type, **kwargs)

# Usage
def accessible_buttons_view(request):
    context = {
        'accessible_button': create_accessible_button(
            "Submit",
            button_type="primary",
            aria_label="Submit the form"
        )
    }
    return render(request, 'accessible_buttons.html', context)
```

### 3. Performance Optimization

```python
# Cache button HTML for repeated use
from django.core.cache import cache

def get_cached_button(button_key, text, **kwargs):
    """Get cached button HTML to improve performance."""

    cache_key = f"button_{button_key}"
    button_html = cache.get(cache_key)

    if not button_html:
        button_html = render_button(text, **kwargs)
        cache.set(cache_key, button_html, 3600)  # Cache for 1 hour

    return button_html

# Usage
def optimized_buttons_view(request):
    context = {
        'submit_button': get_cached_button('submit', 'Submit', button_type='primary'),
        'cancel_button': get_cached_button('cancel', 'Cancel', button_type='secondary')
    }
    return render(request, 'optimized_buttons.html', context)
```

## Troubleshooting

### Common Issues

1. **Button not displaying**: Check if `render_button` is imported and `|safe` filter is used
2. **Styles not applying**: Ensure MetroUI5 CSS is loaded and no conflicting CSS rules
3. **JavaScript not working**: Verify onclick handlers are properly set and JavaScript is loaded
4. **Icon not showing**: Check if the icon name is correct and MetroUI icons CSS is loaded

### Debug Mode

```python
# Enable debug mode for button issues
METROUI5 = {
    'button_debug': True,  # Enable button debugging
    'button_logging': True,  # Log button rendering
}
```

## Related Documentation

- [Components](components.md) - Component rendering functions
- [Template Tags](templatetags.md) - Django template integration
- [Icons](icons.md) - Icon usage in buttons
- [Forms](forms.md) - Form button integration
- [CSS Utilities](css.md) - CSS class management


## metroui5_button

```python
render_button()
```

Empty or invalid: `render_button()` returns `<button class="button" type="button"></button>`.

```django
{% metroui5_button %}
```
