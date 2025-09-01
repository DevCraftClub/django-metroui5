# Dropdowns

Component for creating dropdown menus and select lists with various options and interactive features.

## Basic Usage

### Simple Dropdown

```python
from metroui5.components import render_dropdown

# Basic dropdown
dropdown_html = render_dropdown(
    options=["Option 1", "Option 2", "Option 3"]
)
```

### Dropdown with Values

```python
# Dropdown with specific values
options = [
    {"text": "Home", "value": "home"},
    {"text": "About", "value": "about"},
    {"text": "Contact", "value": "contact"}
]

dropdown_html = render_dropdown(
    options=options,
    selected="home"
)
```

### Custom Dropdown

```python
# Custom dropdown with styling
dropdown_html = render_dropdown(
    options=options,
    id="main-dropdown",
    class="dropdown-primary",
    placeholder="Select an option..."
)
```

## Rendered Output

### Basic Dropdown

```html
<!-- Input -->
render_dropdown(options=["Option 1", "Option 2", "Option 3"])

<!-- Output -->
<select class="dropdown" data-role="dropdown">
	<option value="Option 1">Option 1</option>
	<option value="Option 2">Option 2</option>
	<option value="Option 3">Option 3</option>
</select>
```

### Dropdown with Values

```html
<!-- Input -->
render_dropdown(options=[{"text": "Home", "value": "home"}, {"text": "About",
"value": "about"}], selected="home")

<!-- Output -->
<select class="dropdown" data-role="dropdown">
	<option value="home" selected>Home</option>
	<option value="about">About</option>
</select>
```

### Dropdown with Placeholder

```html
<!-- Input -->
render_dropdown(options=options, placeholder="Choose option...")

<!-- Output -->
<select class="dropdown" data-role="dropdown">
	<option value="" disabled selected>Choose option...</option>
	<option value="home">Home</option>
	<option value="about">About</option>
</select>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic dropdown -->
{% metroui5_dropdown options=dropdown_options %}

<!-- Dropdown with selection -->
{% metroui5_dropdown options=dropdown_options selected="home" %}

<!-- Custom dropdown -->
{% metroui5_dropdown options=dropdown_options placeholder="Select..."
class="dropdown-large" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_dropdown

def dropdown_view(request):
    # Create dropdown options
    category_options = [
        {"text": "Technology", "value": "tech"},
        {"text": "Sports", "value": "sports"},
        {"text": "News", "value": "news"}
    ]

    dropdown_html = render_dropdown(
        options=category_options,
        selected=request.GET.get('category', ''),
        placeholder="Select category...",
        id="category-dropdown"
    )

    context = {
        'dropdown_html': dropdown_html,
        'category_options': category_options
    }
    return render(request, 'dropdown.html', context)
```

```html
<!-- dropdown.html -->
{% load metroui5 %} {% block content %}
<!-- Direct HTML output -->
{{ dropdown_html|safe }}

<!-- Or use template tag -->
{% metroui5_dropdown options=category_options selected=selected_category %} {%
endblock %}
```

## Parameters

### `options` (required)

List of options for the dropdown. Can be strings or dictionaries.

**Format**:

```python
# Simple strings
options = ["Option 1", "Option 2", "Option 3"]

# Dictionaries with text and value
options = [
    {"text": "Display Text", "value": "actual_value"},
    {"text": "Another Option", "value": "another_value"}
]
```

### `selected` (optional)

Value of the initially selected option.

**Example**:

```python
dropdown_html = render_dropdown(options=options, selected="home")
```

### `placeholder` (optional)

Placeholder text when no option is selected.

**Example**:

```python
dropdown_html = render_dropdown(options=options, placeholder="Choose...")
```

### `id` (optional)

Unique identifier for the dropdown element.

**Example**:

```python
dropdown_html = render_dropdown(options=options, id="my-dropdown")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
dropdown_html = render_dropdown(options=options, class="dropdown-large")
```

### `multiple` (optional)

Allow multiple selections.

**Example**:

```python
dropdown_html = render_dropdown(options=options, multiple=True)
```

## Advanced Examples

### Grouped Dropdown

```python
def create_grouped_dropdown(groups):
    """Create dropdown with option groups."""

    dropdown_html = '<select class="dropdown" data-role="dropdown">'

    for group in groups:
        dropdown_html += f'<optgroup label="{group["label"]}">'
        for option in group["options"]:
            dropdown_html += f'<option value="{option["value"]}">{option["text"]}</option>'
        dropdown_html += '</optgroup>'

    dropdown_html += '</select>'
    return dropdown_html
```

### Searchable Dropdown

```python
def create_searchable_dropdown(options, searchable=True):
    """Create dropdown with search functionality."""

    return render_dropdown(
        options=options,
        class="dropdown-search" if searchable else "dropdown",
        **{"data-search": "true"} if searchable else {}
    )
```

### Dynamic Dropdown

```python
def create_dynamic_dropdown(options, ajax_url=None):
    """Create dropdown that loads options dynamically."""

    return render_dropdown(
        options=options,
        class="dropdown-dynamic",
        **{"data-ajax-url": ajax_url} if ajax_url else {}
    )
```

## Styling

### CSS Classes

#### Base Classes

- `dropdown` - Base dropdown class
- `dropdown-primary` - Primary dropdown style
- `dropdown-secondary` - Secondary dropdown style

#### Size Classes

- `dropdown-small` - Small dropdown
- `dropdown-large` - Large dropdown
- `dropdown-mini` - Mini dropdown

#### Feature Classes

- `dropdown-search` - Searchable dropdown
- `dropdown-multi` - Multiple selection dropdown

### Custom Styling

```css
/* Custom dropdown styling */
.dropdown-custom {
	border: 2px solid #007acc;
	border-radius: 6px;
	padding: 10px;
	font-size: 16px;
	background: white;
}

.dropdown-custom:focus {
	outline: none;
	border-color: #005a99;
	box-shadow: 0 0 5px rgba(0, 122, 204, 0.3);
}

/* Dropdown arrow customization */
.dropdown-custom::after {
	content: "▼";
	position: absolute;
	right: 10px;
	pointer-events: none;
}
```

## JavaScript Integration

### Basic Events

```javascript
// Handle dropdown change
$(".dropdown").on("change", function () {
	const selectedValue = $(this).val();
	console.log("Selected:", selectedValue);
	handleDropdownChange(selectedValue);
});

function handleDropdownChange(value) {
	// Process the selected value
	updateContent(value);
}
```

### Dynamic Loading

```javascript
// Load dropdown options via AJAX
function loadDropdownOptions(dropdownId, url) {
	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			updateDropdownOptions(dropdownId, data.options);
		},
		error: function (xhr, status, error) {
			console.error("Error loading options:", error);
		},
	});
}

function updateDropdownOptions(dropdownId, options) {
	const dropdown = $(`#${dropdownId}`);
	dropdown.empty();

	options.forEach((option) => {
		dropdown.append(`<option value="${option.value}">${option.text}</option>`);
	});
}
```

## Best Practices

### 1. Option Structure

```python
# Consistent option format
def format_dropdown_options(items, text_field='name', value_field='id'):
    """Format items for dropdown use."""
    return [
        {"text": getattr(item, text_field), "value": getattr(item, value_field)}
        for item in items
    ]
```

### 2. Default Selection

```python
# Handle default selections
def create_dropdown_with_default(options, default_value=None):
    return render_dropdown(
        options=options,
        selected=default_value or options[0]['value'] if options else None
    )
```

## Related Components

- [Forms](forms.md) - For form integration
- [Buttons](buttons.md) - For dropdown triggers
- [Navigation](navigation.md) - For navigation dropdowns
