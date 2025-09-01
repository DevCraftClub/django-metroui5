# Dialogs

Component for creating modal dialogs and popup windows for user interactions, confirmations, and content display.

## Basic Usage

### Simple Dialog

```python
from metroui5.components import render_dialog

# Basic dialog
dialog_html = render_dialog(
    title="Confirmation",
    content="Are you sure you want to proceed?"
)
```

### Dialog with Actions

```python
# Dialog with action buttons
dialog_html = render_dialog(
    title="Delete Item",
    content="This action cannot be undone. Are you sure?",
    actions=[
        {"text": "Cancel", "class": "button-secondary"},
        {"text": "Delete", "class": "button-danger"}
    ]
)
```

### Custom Dialog

```python
# Custom dialog with specific options
dialog_html = render_dialog(
    title="User Information",
    content="<p>Name: John Doe</p><p>Email: john@example.com</p>",
    id="user-dialog",
    class="dialog-large",
    close_button=True,
    overlay=True
)
```

## Rendered Output

### Basic Dialog

```html
<!-- Input -->
render_dialog(title="Confirmation", content="Are you sure?")

<!-- Output -->
<div class="dialog" data-role="dialog" id="dialog-1">
	<div class="dialog-title">Confirmation</div>
	<div class="dialog-content">Are you sure?</div>
	<div class="dialog-actions">
		<button class="button" data-role="close">OK</button>
	</div>
</div>
```

### Dialog with Actions

```html
<!-- Input -->
render_dialog(title="Delete", content="Confirm deletion", actions=[{"text":
"Cancel"}, {"text": "Delete"}])

<!-- Output -->
<div class="dialog" data-role="dialog" id="dialog-2">
	<div class="dialog-title">Delete</div>
	<div class="dialog-content">Confirm deletion</div>
	<div class="dialog-actions">
		<button class="button button-secondary">Cancel</button>
		<button class="button button-danger">Delete</button>
	</div>
</div>
```

### Dialog with Overlay

```html
<!-- Input -->
render_dialog(title="Modal", content="Content", overlay=True)

<!-- Output -->
<div class="dialog-overlay" data-role="overlay">
	<div class="dialog" data-role="dialog" id="dialog-3">
		<div class="dialog-title">Modal</div>
		<div class="dialog-content">Content</div>
		<div class="dialog-actions">
			<button class="button" data-role="close">OK</button>
		</div>
	</div>
</div>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic dialog -->
{% metroui5_dialog title="Confirmation" content="Are you sure?" %}

<!-- Dialog with actions -->
{% metroui5_dialog title="Delete" content="Confirm deletion"
actions=action_buttons %}

<!-- Custom dialog -->
{% metroui5_dialog title="Info" content="Information" class="dialog-custom" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_dialog

def confirmation_view(request):
    # Create confirmation dialog
    confirm_dialog = render_dialog(
        title="Confirm Action",
        content="This action will affect your data. Continue?",
        actions=[
            {"text": "Cancel", "class": "button-secondary", "onclick": "cancelAction()"},
            {"text": "Continue", "class": "button-primary", "onclick": "proceedAction()"}
        ],
        id="confirm-dialog"
    )

    context = {
        'confirm_dialog': confirm_dialog,
        'action_buttons': [
            {"text": "Cancel", "class": "button-secondary"},
            {"text": "Continue", "class": "button-primary"}
        ]
    }
    return render(request, 'confirmation.html', context)
```

```html
<!-- confirmation.html -->
{% load metroui5 %} {% block content %}
<!-- Direct HTML output -->
{{ confirm_dialog|safe }}

<!-- Or use template tag -->
{% metroui5_dialog title="Confirm Action" content="Continue?"
actions=action_buttons %} {% endblock %}
```

## Parameters

### `title` (optional)

Title displayed in the dialog header.

**Default**: None

**Example**:

```python
dialog_html = render_dialog(title="Important Notice")
```

### `content` (required)

Content to display in the dialog body. Can be HTML.

**Example**:

```python
dialog_html = render_dialog(content="Simple text content")
dialog_html = render_dialog(content="<p>HTML content</p>")
```

### `actions` (optional)

List of action buttons for the dialog.

**Format**:

```python
actions = [
    {
        "text": "Button Text",
        "class": "button-primary",  # Optional
        "onclick": "function()",    # Optional
        "id": "button-id"           # Optional
    }
]
```

**Example**:

```python
actions = [
    {"text": "Cancel", "class": "button-secondary"},
    {"text": "Save", "class": "button-primary", "onclick": "saveData()"}
]
dialog_html = render_dialog(content="Save changes?", actions=actions)
```

### `id` (optional)

Unique identifier for the dialog element.

**Default**: Auto-generated ID

**Example**:

```python
dialog_html = render_dialog(id="my-dialog", content="Content")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
dialog_html = render_dialog(class="dialog-large", content="Content")
```

### `close_button` (optional)

Whether to show a close button.

**Default**: `True`

**Example**:

```python
dialog_html = render_dialog(close_button=False, content="Content")
```

### `overlay` (optional)

Whether to show an overlay background.

**Default**: `False`

**Example**:

```python
dialog_html = render_dialog(overlay=True, content="Modal content")
```

### `width` (optional)

Width of the dialog.

**Default**: Auto

**Example**:

```python
dialog_html = render_dialog(width="500px", content="Content")
```

### `height` (optional)

Height of the dialog.

**Default**: Auto

**Example**:

```python
dialog_html = render_dialog(height="300px", content="Content")
```

## Advanced Examples

### Confirmation Dialog

```python
def create_confirmation_dialog(message, on_confirm, on_cancel=None):
    """Create a confirmation dialog."""

    actions = [
        {"text": "Cancel", "class": "button-secondary"}
    ]

    if on_cancel:
        actions[0]["onclick"] = on_cancel

    actions.append({
        "text": "Confirm",
        "class": "button-danger",
        "onclick": on_confirm
    })

    return render_dialog(
        title="Confirmation",
        content=message,
        actions=actions,
        overlay=True,
        class="dialog-confirmation"
    )
```

### Form Dialog

```python
def create_form_dialog(title, form_html, submit_url):
    """Create dialog with form content."""

    actions = [
        {"text": "Cancel", "class": "button-secondary", "onclick": "closeDialog()"},
        {"text": "Submit", "class": "button-primary", "onclick": f"submitForm('{submit_url}')"}
    ]

    return render_dialog(
        title=title,
        content=form_html,
        actions=actions,
        overlay=True,
        class="dialog-form",
        width="600px"
    )
```

### Alert Dialog

```python
def create_alert_dialog(message, alert_type="info"):
    """Create alert-style dialog."""

    type_classes = {
        "info": "dialog-info",
        "success": "dialog-success",
        "warning": "dialog-warning",
        "error": "dialog-error"
    }

    return render_dialog(
        title="Alert",
        content=f'<div class="alert alert-{alert_type}">{message}</div>',
        class=type_classes.get(alert_type, "dialog-info"),
        close_button=True
    )
```

### Loading Dialog

```python
def create_loading_dialog(message="Loading..."):
    """Create loading dialog."""

    content = f"""
    <div class="loading-dialog">
        <div class="spinner"></div>
        <p>{message}</p>
    </div>
    """

    return render_dialog(
        content=content,
        class="dialog-loading",
        close_button=False,
        overlay=True
    )
```

### Multi-Step Dialog

```python
def create_multi_step_dialog(steps):
    """Create dialog with multiple steps."""

    step_content = ""
    for i, step in enumerate(steps):
        step_content += f"""
        <div class="dialog-step" id="step-{i}" style="display: {'block' if i == 0 else 'none'};">
            <h3>{step['title']}</h3>
            <div>{step['content']}</div>
        </div>
        """

    actions = [
        {"text": "Previous", "class": "button-secondary", "onclick": "previousStep()", "id": "prev-btn", "style": "display: none;"},
        {"text": "Next", "class": "button-primary", "onclick": "nextStep()", "id": "next-btn"},
        {"text": "Finish", "class": "button-success", "onclick": "finishSteps()", "id": "finish-btn", "style": "display: none;"}
    ]

    return render_dialog(
        title="Multi-Step Process",
        content=step_content,
        actions=actions,
        overlay=True,
        class="dialog-multi-step",
        width="700px"
    )
```

## Styling

### CSS Classes

#### Base Classes

- `dialog` - Base dialog class
- `dialog-primary` - Primary dialog style
- `dialog-secondary` - Secondary dialog style

#### Size Classes

- `dialog-small` - Small dialog
- `dialog-large` - Large dialog
- `dialog-fullscreen` - Fullscreen dialog

#### Type Classes

- `dialog-info` - Information dialog
- `dialog-success` - Success dialog
- `dialog-warning` - Warning dialog
- `dialog-error` - Error dialog

#### Layout Classes

- `dialog-centered` - Centered dialog
- `dialog-top` - Top-aligned dialog
- `dialog-bottom` - Bottom-aligned dialog

### Custom Styling

```css
/* Custom dialog styling */
.dialog-custom {
	border-radius: 12px;
	box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
	border: none;
}

.dialog-custom .dialog-title {
	background: linear-gradient(135deg, #007acc, #005a99);
	color: white;
	padding: 20px;
	border-radius: 12px 12px 0 0;
	font-size: 1.2em;
	font-weight: bold;
}

.dialog-custom .dialog-content {
	padding: 30px;
	line-height: 1.6;
}

.dialog-custom .dialog-actions {
	padding: 20px;
	border-top: 1px solid #eee;
	text-align: right;
}

/* Overlay styling */
.dialog-overlay {
	background: rgba(0, 0, 0, 0.5);
	backdrop-filter: blur(5px);
}

/* Loading dialog */
.dialog-loading .loading-dialog {
	text-align: center;
	padding: 40px;
}

.dialog-loading .spinner {
	width: 40px;
	height: 40px;
	border: 4px solid #f3f3f3;
	border-top: 4px solid #007acc;
	border-radius: 50%;
	animation: spin 1s linear infinite;
	margin: 0 auto 20px;
}

@keyframes spin {
	0% {
		transform: rotate(0deg);
	}
	100% {
		transform: rotate(360deg);
	}
}
```

## JavaScript Integration

### Basic Dialog Events

```javascript
// Initialize dialog
$(document).ready(function () {
	$(".dialog").dialog({
		onShow: function () {
			console.log("Dialog shown");
		},
		onHide: function () {
			console.log("Dialog hidden");
		},
		onAction: function (action) {
			console.log("Action clicked:", action);
		},
	});
});
```

### Dialog Management

```javascript
// Show dialog
function showDialog(dialogId) {
	const dialog = $(`#${dialogId}`).data("dialog");
	if (dialog) {
		dialog.show();
	}
}

// Hide dialog
function hideDialog(dialogId) {
	const dialog = $(`#${dialogId}`).data("dialog");
	if (dialog) {
		dialog.hide();
	}
}

// Close all dialogs
function closeAllDialogs() {
	$(".dialog").each(function () {
		const dialog = $(this).data("dialog");
		if (dialog) {
			dialog.hide();
		}
	});
}
```

### Dynamic Content Loading

```javascript
// Load content dynamically
function loadDialogContent(dialogId, url) {
	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			const dialog = $(`#${dialogId}`);
			dialog.find(".dialog-content").html(data);
			showDialog(dialogId);
		},
		error: function (xhr, status, error) {
			console.error("Error loading content:", error);
			showErrorDialog("Failed to load content");
		},
	});
}

// Update dialog content
function updateDialogContent(dialogId, content) {
	const dialog = $(`#${dialogId}`);
	dialog.find(".dialog-content").html(content);
}
```

### Form Handling

```javascript
// Handle form submission in dialog
function handleDialogForm(dialogId, formData) {
	$.ajax({
		url: "/api/submit-form/",
		method: "POST",
		data: formData,
		success: function (response) {
			if (response.success) {
				hideDialog(dialogId);
				showSuccessDialog("Form submitted successfully");
			} else {
				showErrorDialog(response.error);
			}
		},
		error: function (xhr, status, error) {
			showErrorDialog("An error occurred");
		},
	});
}

// Validate dialog form
function validateDialogForm(dialogId) {
	const dialog = $(`#${dialogId}`);
	const form = dialog.find("form");
	const inputs = form.find(
		"input[required], select[required], textarea[required]"
	);

	let isValid = true;
	inputs.each(function () {
		if (!$(this).val().trim()) {
			$(this).addClass("input-error");
			isValid = false;
		} else {
			$(this).removeClass("input-error");
		}
	});

	return isValid;
}
```

### Multi-Step Dialog Navigation

```javascript
// Handle multi-step dialog navigation
let currentStep = 0;
const totalSteps = $(".dialog-step").length;

function nextStep() {
	if (currentStep < totalSteps - 1) {
		$(`#step-${currentStep}`).hide();
		currentStep++;
		$(`#step-${currentStep}`).show();
		updateStepButtons();
	}
}

function previousStep() {
	if (currentStep > 0) {
		$(`#step-${currentStep}`).hide();
		currentStep--;
		$(`#step-${currentStep}`).show();
		updateStepButtons();
	}
}

function updateStepButtons() {
	const prevBtn = $("#prev-btn");
	const nextBtn = $("#next-btn");
	const finishBtn = $("#finish-btn");

	prevBtn.toggle(currentStep > 0);
	nextBtn.toggle(currentStep < totalSteps - 1);
	finishBtn.toggle(currentStep === totalSteps - 1);
}

function finishSteps() {
	// Process final step
	const formData = collectFormData();
	handleDialogForm("multi-step-dialog", formData);
}
```

### Dialog Actions

```javascript
// Handle dialog action clicks
function handleDialogAction(action, dialogId) {
	switch (action) {
		case "confirm":
			hideDialog(dialogId);
			executeConfirmedAction();
			break;
		case "cancel":
			hideDialog(dialogId);
			break;
		case "save":
			if (validateDialogForm(dialogId)) {
				saveDialogData(dialogId);
			}
			break;
		default:
			console.log("Unknown action:", action);
	}
}

// Execute confirmed action
function executeConfirmedAction() {
	// Perform the action that was confirmed
	console.log("Action confirmed and executed");
}

// Save dialog data
function saveDialogData(dialogId) {
	const dialog = $(`#${dialogId}`);
	const formData = new FormData(dialog.find("form")[0]);

	$.ajax({
		url: "/api/save-data/",
		method: "POST",
		data: formData,
		processData: false,
		contentType: false,
		success: function (response) {
			hideDialog(dialogId);
			showSuccessDialog("Data saved successfully");
		},
		error: function (xhr, status, error) {
			showErrorDialog("Failed to save data");
		},
	});
}
```

### Utility Functions

```javascript
// Show success dialog
function showSuccessDialog(message) {
    const dialog = render_dialog(
        title="Success",
        content=message,
        class="dialog-success"
    );
    $('body').append(dialog);
    showDialog('success-dialog');
}

// Show error dialog
function showErrorDialog(message) {
    const dialog = render_dialog(
        title="Error",
        content=message,
        class="dialog-error"
    );
    $('body').append(dialog);
    showDialog('error-dialog');
}

// Show confirmation dialog
function showConfirmationDialog(message, onConfirm) {
    const dialog = render_dialog(
        title="Confirmation",
        content=message,
        actions=[
            {"text": "Cancel", "class": "button-secondary"},
            {"text": "Confirm", "class": "button-danger", "onclick": onConfirm}
        ]
    );
    $('body').append(dialog);
    showDialog('confirm-dialog');
}
```

## Best Practices

### 1. Dialog Naming

```python
# Use descriptive dialog IDs
def create_user_dialog(user_id):
    return render_dialog(
        id=f"user-dialog-{user_id}",
        title="User Details",
        content=get_user_content(user_id)
    )
```

### 2. Action Handling

```python
# Consistent action structure
def create_standard_actions(primary_action, secondary_action=None):
    actions = []
    if secondary_action:
        actions.append(secondary_action)
    actions.append(primary_action)
    return actions
```

### 3. Content Validation

```python
# Validate dialog content
def validate_dialog_content(content):
    """Validate dialog content for security."""
    if not content or len(content.strip()) == 0:
        raise ValueError("Dialog content cannot be empty")
    return content.strip()
```

### 4. Accessibility

```python
# Ensure dialogs are accessible
def create_accessible_dialog(title, content, actions=None):
    return render_dialog(
        title=title,
        content=content,
        actions=actions,
        **{
            "aria-label": title,
            "role": "dialog",
            "aria-modal": "true"
        }
    )
```

## Related Components

- [Modals](modals.md) - For modal dialogs and overlays
- [Forms](forms.md) - For form content in dialogs
- [Alerts](alerts.md) - For alert-style dialogs
- [Buttons](buttons.md) - For dialog action buttons
