# Modals

MetroUI5 Django provides a comprehensive modal component system for creating overlay dialogs, popups, and interactive content displays.

## Basic Usage

```python
from metroui5.components import render_modal

# Simple modal
modal_html = render_modal(
    title="Confirmation",
    content="Are you sure you want to delete this item?",
    id="confirm-modal"
)
```

## Parameters

### `render_modal(title, content, **attrs)`

- **title** (str): Modal title/header
- **content** (str): Modal content (can be HTML)
- **attrs** (dict): Additional HTML attributes for the modal

## Examples

### Basic Modal

```python
from metroui5.components import render_modal

modal = render_modal(
    title="Welcome",
    content="Welcome to our application!",
    id="welcome-modal"
)
```

### Modal with Custom Classes

```python
modal = render_modal(
    title="User Profile",
    content="""
    <div class="user-info">
        <p><strong>Name:</strong> John Doe</p>
        <p><strong>Email:</strong> john@example.com</p>
        <p><strong>Role:</strong> Administrator</p>
    </div>
    """,
    class="modal modal-large",
    id="profile-modal"
)
```

### Modal with Actions

```python
def create_modal_with_actions():
    content = """
    <p>This action cannot be undone. Are you sure you want to proceed?</p>
    <div class="button-group">
        <button class="button button-danger" onclick="confirmDelete()">Delete</button>
        <button class="button" onclick="Metro.dialog.close('#confirm-modal')">Cancel</button>
    </div>
    """

    return render_modal(
        title="Confirm Delete",
        content=content,
        id="confirm-modal",
        class="modal"
    )

modal = create_modal_with_actions()
```

## MetroUI Modal Classes

MetroUI5 provides several CSS classes for modal styling:

### Size Classes

- `modal-small` - Small modal
- `modal-large` - Large modal
- `modal-wide` - Wide modal
- `modal-tall` - Tall modal

### Style Classes

- `modal-dark` - Dark theme modal
- `modal-light` - Light theme modal
- `modal-rounded` - Rounded corners
- `modal-shadow` - Enhanced shadow

### Position Classes

- `modal-top` - Modal positioned at top
- `modal-center` - Modal centered (default)
- `modal-bottom` - Modal positioned at bottom

## Modal Types

### Confirmation Modal

```python
def create_confirmation_modal(message, action_url):
    content = f"""
    <p>{message}</p>
    <div class="button-group">
        <button class="button button-danger" onclick="window.location.href='{action_url}'">
            Confirm
        </button>
        <button class="button" onclick="Metro.dialog.close('#confirm-modal')">
            Cancel
        </button>
    </div>
    """

    return render_modal(
        title="Confirm Action",
        content=content,
        id="confirm-modal",
        class="modal"
    )

modal = create_confirmation_modal(
    "Are you sure you want to delete this user?",
    "/users/delete/123/"
)
```

### Form Modal

```python
def create_form_modal():
    content = """
    <form id="user-form" method="post">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" class="input" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" class="input" required>
        </div>
        <div class="button-group">
            <button type="submit" class="button button-primary">Save</button>
            <button type="button" class="button" onclick="Metro.dialog.close('#form-modal')">Cancel</button>
        </div>
    </form>
    """

    return render_modal(
        title="Add New User",
        content=content,
        id="form-modal",
        class="modal modal-large"
    )

modal = create_form_modal()
```

### Alert Modal

```python
def create_alert_modal(message, alert_type="info"):
    icon_map = {
        "success": "checkmark",
        "warning": "warning",
        "error": "cross",
        "info": "info"
    }

    icon = icon_map.get(alert_type, "info")

    content = f"""
    <div class="alert alert-{alert_type}">
        <span class="mif-{icon}"></span>
        {message}
    </div>
    <div class="button-group">
        <button class="button" onclick="Metro.dialog.close('#alert-modal')">OK</button>
    </div>
    """

    return render_modal(
        title=f"{alert_type.title()} Alert",
        content=content,
        id="alert-modal",
        class="modal"
    )

success_modal = create_alert_modal("Operation completed successfully!", "success")
error_modal = create_alert_modal("An error occurred. Please try again.", "error")
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_modal title="Confirmation" content="Are you
sure?" id="confirm-modal" %}
```

## Advanced Examples

### Modal with Dynamic Content

```python
def create_dynamic_modal(user_data):
    content = f"""
    <div class="user-details">
        <div class="avatar">
            <img src="{user_data.get('avatar', '/static/default-avatar.png')}" alt="Avatar">
        </div>
        <div class="info">
            <h3>{user_data['name']}</h3>
            <p><strong>Email:</strong> {user_data['email']}</p>
            <p><strong>Role:</strong> {user_data['role']}</p>
            <p><strong>Last Login:</strong> {user_data['last_login']}</p>
        </div>
    </div>
    <div class="button-group">
        <button class="button button-primary" onclick="editUser({user_data['id']})">Edit</button>
        <button class="button" onclick="Metro.dialog.close('#user-modal')">Close</button>
    </div>
    """

    return render_modal(
        title="User Details",
        content=content,
        id="user-modal",
        class="modal modal-large"
    )

user_modal = create_dynamic_modal({
    'id': 123,
    'name': 'John Doe',
    'email': 'john@example.com',
    'role': 'Administrator',
    'last_login': '2024-01-15 10:30 AM',
    'avatar': '/static/avatars/john.jpg'
})
```

### Modal with Loading State

```python
def create_loading_modal():
    content = """
    <div class="loading-content">
        <div class="spinner"></div>
        <p>Loading data, please wait...</p>
    </div>
    """

    return render_modal(
        title="Loading",
        content=content,
        id="loading-modal",
        class="modal modal-small"
    )

loading_modal = create_loading_modal()
```

### Modal with Tabs

```python
def create_tabbed_modal():
    content = """
    <div class="tabs" data-role="tabs">
        <ul class="tabs-nav">
            <li><a href="#tab1">General</a></li>
            <li><a href="#tab2">Settings</a></li>
            <li><a href="#tab3">Advanced</a></li>
        </ul>
        <div class="tabs-content">
            <div id="tab1">
                <p>General settings content...</p>
            </div>
            <div id="tab2">
                <p>Settings content...</p>
            </div>
            <div id="tab3">
                <p>Advanced settings content...</p>
            </div>
        </div>
    </div>
    <div class="button-group">
        <button class="button button-primary">Save</button>
        <button class="button" onclick="Metro.dialog.close('#settings-modal')">Cancel</button>
    </div>
    """

    return render_modal(
        title="Settings",
        content=content,
        id="settings-modal",
        class="modal modal-large"
    )

settings_modal = create_tabbed_modal()
```

## JavaScript Integration

### Opening Modals

```javascript
// Open modal by ID
Metro.dialog.open("#my-modal");

// Open modal with custom options
Metro.dialog.open("#my-modal", {
	width: 600,
	height: 400,
	overlay: true,
	overlayClose: true,
});
```

### Closing Modals

```javascript
// Close modal by ID
Metro.dialog.close("#my-modal");

// Close all modals
Metro.dialog.closeAll();
```

### Modal Events

```javascript
// Listen for modal events
$("#my-modal").on("dialogopen", function () {
	console.log("Modal opened");
});

$("#my-modal").on("dialogclose", function () {
	console.log("Modal closed");
});
```

## Best Practices

1. **Use descriptive titles**: Make modal titles clear and descriptive
2. **Keep content focused**: Don't overload modals with too much content
3. **Provide clear actions**: Always include clear action buttons
4. **Handle keyboard events**: Ensure modals can be closed with Escape key
5. **Make it accessible**: Include proper ARIA labels and focus management
6. **Use appropriate sizing**: Choose modal size based on content
7. **Test on mobile**: Ensure modals work well on mobile devices

## Related Components

- [Dialogs](dialogs.md) - For simpler dialog boxes
- [Alerts](alerts.md) - For alert messages
- [Forms](forms.md) - For form content in modals
- [Buttons](buttons.md) - For modal action buttons
