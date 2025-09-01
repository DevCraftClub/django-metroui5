# Input Fields

MetroUI5 Django provides a comprehensive input field component system for creating various types of form inputs with MetroUI styling and functionality.

## Basic Usage

```python
from metroui5.components import render_input

# Simple text input
input_html = render_input(input_type="text", placeholder="Enter text...")
```

## Parameters

### `render_input(input_type="text", placeholder="", **attrs)`

- **input_type** (str): Input type (text, email, password, number, etc.)
- **placeholder** (str): Placeholder text
- **attrs** (dict): Additional HTML attributes

## Examples

### Basic Input Fields

```python
from metroui5.components import render_input

# Text input
text_input = render_input(
    input_type="text",
    placeholder="Enter your name",
    class="input"
)

# Email input
email_input = render_input(
    input_type="email",
    placeholder="Enter your email",
    class="input"
)

# Password input
password_input = render_input(
    input_type="password",
    placeholder="Enter your password",
    class="input"
)
```

### Input with Custom Attributes

```python
input_field = render_input(
    input_type="text",
    placeholder="Search...",
    id="search-input",
    class="input input-large",
    data_role="input",
    autocomplete="off"
)
```

### Input with Validation

```python
input_field = render_input(
    input_type="text",
    placeholder="Enter username",
    class="input",
    required=True,
    minlength="3",
    maxlength="20",
    pattern="[a-zA-Z0-9_]+"
)
```

## MetroUI Input Classes

MetroUI5 provides several CSS classes for input styling:

### Size Classes

- `input-small` - Small input
- `input-large` - Large input
- `input-mini` - Mini input

### Style Classes

- `input-rounded` - Rounded input
- `input-outlined` - Outlined input
- `input-filled` - Filled input
- `input-clear` - Clear input

### State Classes

- `input-success` - Success state
- `input-error` - Error state
- `input-warning` - Warning state
- `input-disabled` - Disabled state

## Input Types

### Text Inputs

```python
# Basic text input
text_input = render_input(
    input_type="text",
    placeholder="Enter text",
    class="input"
)

# Search input
search_input = render_input(
    input_type="search",
    placeholder="Search...",
    class="input input-search"
)

# URL input
url_input = render_input(
    input_type="url",
    placeholder="Enter URL",
    class="input"
)
```

### Numeric Inputs

```python
# Number input
number_input = render_input(
    input_type="number",
    placeholder="Enter number",
    class="input",
    min="0",
    max="100"
)

# Range input
range_input = render_input(
    input_type="range",
    class="input input-range",
    min="0",
    max="100",
    value="50"
)
```

### Date and Time Inputs

```python
# Date input
date_input = render_input(
    input_type="date",
    class="input",
    data_role="datepicker"
)

# Time input
time_input = render_input(
    input_type="time",
    class="input",
    data_role="timepicker"
)

# Datetime input
datetime_input = render_input(
    input_type="datetime-local",
    class="input",
    data_role="datetimepicker"
)
```

### File Inputs

```python
# File input
file_input = render_input(
    input_type="file",
    class="input input-file",
    accept="image/*,.pdf,.doc,.docx"
)

# Multiple file input
multiple_file_input = render_input(
    input_type="file",
    class="input input-file",
    multiple=True,
    accept="image/*"
)
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_input type="text" placeholder="Enter text..."
class="input" %}
```

## Advanced Examples

### Input with Icon

```python
def create_input_with_icon(input_type="text", placeholder="", icon="search"):
    """Create input field with icon."""

    return f"""
    <div class="input-group">
        <span class="input-group-addon">
            <span class="mif-{icon}"></span>
        </span>
        {render_input(
            input_type=input_type,
            placeholder=placeholder,
            class="input"
        )}
    </div>
    """

# Usage
search_input = create_input_with_icon("text", "Search...", "search")
email_input = create_input_with_icon("email", "Enter email", "mail")
```

### Input with Validation States

```python
def create_validated_input(field_name, value="", is_valid=None, error_message=""):
    """Create input with validation state."""

    input_class = "input"

    if is_valid is True:
        input_class += " input-success"
    elif is_valid is False:
        input_class += " input-error"

    input_html = render_input(
        input_type="text",
        name=field_name,
        value=value,
        class=input_class
    )

    if is_valid is False and error_message:
        error_html = f'<div class="error-message">{error_message}</div>'
        return input_html + error_html

    return input_html

# Usage
valid_input = create_validated_input("username", "john_doe", True)
invalid_input = create_validated_input("email", "invalid-email", False, "Please enter a valid email")
```

### Responsive Input

```python
def create_responsive_input(input_type="text", placeholder="", breakpoints=None):
    """Create responsive input field."""

    if breakpoints is None:
        breakpoints = {
            'mobile': {'size': 'small'},
            'tablet': {'size': 'default'},
            'desktop': {'size': 'large'}
        }

    input_class = "input"

    # Add responsive classes
    for breakpoint, config in breakpoints.items():
        if config['size'] != 'default':
            input_class += f" input-{breakpoint}-{config['size']}"

    return render_input(
        input_type=input_type,
        placeholder=placeholder,
        class=input_class
    )

# Usage
responsive_input = create_responsive_input("text", "Enter text...")
```

### Input with Auto-complete

```python
def create_autocomplete_input(field_name, placeholder="", options=None):
    """Create input with auto-complete functionality."""

    if options is None:
        options = []

    input_html = render_input(
        input_type="text",
        name=field_name,
        placeholder=placeholder,
        class="input",
        data_role="autocomplete",
        data_source=options
    )

    return input_html

# Usage
countries = ["USA", "Canada", "UK", "Germany", "France", "Japan"]
country_input = create_autocomplete_input("country", "Select country", countries)
```

### Input with Mask

```python
def create_masked_input(input_type="text", placeholder="", mask="", pattern=""):
    """Create input with input mask."""

    return render_input(
        input_type=input_type,
        placeholder=placeholder,
        class="input",
        data_role="input",
        data_mask=mask,
        data_pattern=pattern
    )

# Usage
phone_input = create_masked_input("tel", "(___) ___-____", "(999) 999-9999")
date_input = create_masked_input("text", "__/__/____", "99/99/9999")
```

### Input with Character Counter

```python
def create_counter_input(input_type="text", placeholder="", max_length=100):
    """Create input with character counter."""

    input_html = render_input(
        input_type=input_type,
        placeholder=placeholder,
        class="input",
        maxlength=max_length,
        data_role="input"
    )

    counter_html = f"""
    <div class="input-counter">
        <span class="counter-current">0</span>
        <span class="counter-separator">/</span>
        <span class="counter-max">{max_length}</span>
    </div>
    """

    return f"""
    <div class="input-with-counter">
        {input_html}
        {counter_html}
    </div>
    """

# Usage
counter_input = create_counter_input("text", "Enter description...", 200)
```

## JavaScript Integration

### Input Validation

```javascript
// Validate input on blur
document.querySelectorAll(".input").forEach((input) => {
	input.addEventListener("blur", function () {
		validateInput(this);
	});
});

function validateInput(input) {
	const value = input.value.trim();
	const type = input.type;

	// Remove existing validation classes
	input.classList.remove("input-success", "input-error");

	if (value === "") {
		if (input.hasAttribute("required")) {
			input.classList.add("input-error");
		}
		return;
	}

	// Type-specific validation
	if (type === "email" && !isValidEmail(value)) {
		input.classList.add("input-error");
		return;
	}

	if (type === "url" && !isValidUrl(value)) {
		input.classList.add("input-error");
		return;
	}

	input.classList.add("input-success");
}

function isValidEmail(email) {
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	return emailRegex.test(email);
}

function isValidUrl(url) {
	try {
		new URL(url);
		return true;
	} catch {
		return false;
	}
}
```

### Input Events

```javascript
// Handle input events
document.querySelectorAll(".input").forEach((input) => {
	input.addEventListener("input", function () {
		// Update character counter
		updateCounter(this);

		// Trigger custom events
		this.dispatchEvent(
			new CustomEvent("metroui-input-change", {
				detail: { value: this.value },
			})
		);
	});
});

function updateCounter(input) {
	const counter = input.parentNode.querySelector(".input-counter");
	if (counter) {
		const current = input.value.length;
		const max = input.maxLength;
		counter.querySelector(".counter-current").textContent = current;
	}
}
```

## Best Practices

1. **Use appropriate input types**: Choose the correct HTML5 input type
2. **Provide helpful placeholders**: Use descriptive placeholder text
3. **Include proper validation**: Add client-side and server-side validation
4. **Make inputs accessible**: Include proper labels and ARIA attributes
5. **Use consistent styling**: Apply consistent classes across your application
6. **Handle edge cases**: Account for empty values and invalid input
7. **Test thoroughly**: Test inputs with various data types and edge cases

## Related Components

- [Forms](forms.md) - For complete form handling
- [Buttons](buttons.md) - For input-related buttons
- [Alerts](alerts.md) - For validation messages
- [Cards](cards.md) - For containing input fields
