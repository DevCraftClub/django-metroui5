# Components API Reference

Complete reference for all MetroUI5 component rendering functions available in the `metroui5.components` module.

## Overview

The components module provides high-level functions for rendering complete UI components with MetroUI5 styling. Each function returns HTML strings that can be used directly in Django templates or views.

```python
from metroui5.components import (
    render_alert, render_button, render_card, render_tile,
    render_table, render_navigation, render_modal,
    render_progress, render_input, render_panel, render_accordion,
    render_list, render_badge, render_pagination, render_calendar,
    render_dialog, render_dropdown, render_menu, render_sidebar,
    render_tabs, render_toolbar, render_breadcrumb, render_avatar,
    render_rating
)
```

## Alert Components

### `render_alert(content, alert_type="info", dismissible=False, **attrs)`

Renders alert/notification components.

**Parameters:**

- `content` (str): Alert content
- `alert_type` (str): Alert type - "info", "success", "warning", "danger", "error"
- `dismissible` (bool): Whether alert can be dismissed
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

**Example:**

```python
alert_html = render_alert(
    content="Operation completed successfully",
    alert_type="success",
    dismissible=True,
    id="success-alert"
)
```

## Button Components

### `render_button(content, button_type="default", size=None, outline=False, **attrs)`

Renders button components with various styles and sizes.

**Parameters:**

- `content` (str): Button text content
- `button_type` (str): Button style - "default", "primary", "secondary", "success", "danger", "warning", "info"
- `size` (str, optional): Button size - "sm", "lg"
- `outline` (bool): Whether to use outline style
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

**Example:**

```python
button_html = render_button(
    content="Save Changes",
    button_type="primary",
    size="lg",
    onclick="saveForm()"
)
```

## Card Components

### `render_card(header=None, content=None, footer=None, **attrs)`

Renders card components for content display.

**Parameters:**

- `header` (str, optional): Card header content
- `content` (str, optional): Card body content
- `footer` (str, optional): Card footer content
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

**Example:**

```python
card_html = render_card(
    header="Product Card",
    content="<p>Product description here</p>",
    footer='<button class="button">Buy Now</button>'
)
```

## Tile Components

### `render_tile(title, content=None, size="medium", color="blue", icon=None, **attrs)`

Renders MetroUI tile components.

**Parameters:**

- `title` (str): Tile title
- `content` (str, optional): Additional content
- `size` (str): Tile size - "small", "medium", "large", "wide", "tall"
- `color` (str): Tile color
- `icon` (str, optional): MetroUI icon name
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Table Components

### `render_table(headers, rows, **attrs)`

Renders data tables with MetroUI5 styling.

**Parameters:**

- `headers` (list): Table headers
- `rows` (list): Table data rows (each row is a list of cells)
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

**Example:**

```python
table_html = render_table(
    headers=["Name", "Email", "Role"],
    rows=[
        ["John Doe", "john@example.com", "Admin"],
        ["Jane Smith", "jane@example.com", "User"]
    ]
)
```

## Navigation Components

### `render_navigation(items, **attrs)`

Renders navigation menus.

**Parameters:**

- `items` (list): Navigation items (strings or dicts with 'text' and 'url')
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Modal Components

### `render_modal(title, content, **attrs)`

Renders modal dialogs.

**Parameters:**

- `title` (str): Modal title
- `content` (str): Modal content HTML
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Progress Components

### `render_progress(value, max_value=100, color="blue", size="default", **attrs)`

Renders progress bars and indicators.

**Parameters:**

- `value` (int/float): Current progress value
- `max_value` (int/float): Maximum value
- `color` (str): Progress bar color
- `size` (str): Size - "mini", "small", "large", or "default"
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Input Components

### `render_input(input_type="text", placeholder="", **attrs)`

Renders various input field types.

**Parameters:**

- `input_type` (str): Input type - "text", "email", "password", "number", etc.
- `placeholder` (str): Placeholder text
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Panel Components

### `render_panel(title=None, content=None, **attrs)`

Renders collapsible panels.

**Parameters:**

- `title` (str, optional): Panel title
- `content` (str, optional): Panel content HTML
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Accordion Components

### `render_accordion(items, **attrs)`

Renders accordion components with multiple sections.

**Parameters:**

- `items` (list): List of dictionaries with 'title' and 'content' keys
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

**Example:**

```python
accordion_html = render_accordion(
    items=[
        {"title": "Section 1", "content": "Content 1"},
        {"title": "Section 2", "content": "Content 2"}
    ]
)
```

## List Components

### `render_list(items, list_type="ul", **attrs)`

Renders various list types.

**Parameters:**

- `items` (list): List items (strings or dicts with 'text' and 'url')
- `list_type` (str): List type - "ul" or "ol"
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Menu Components

### `render_menu(items, **attrs)`

Renders navigation menus.

**Parameters:**

- `items` (list): Menu items (strings or dicts with 'text' and 'url')
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Sidebar Components

### `render_sidebar(items, **attrs)`

Renders sidebar panels.

**Parameters:**

- `items` (list): Sidebar items (strings or dicts with 'text' and 'url')
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Tab Components

### `render_tabs(tabs, **attrs)`

Renders tabbed interfaces.

**Parameters:**

- `tabs` (list): List of dictionaries with 'title' and 'content' keys
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Toolbar Components

### `render_toolbar(items, **attrs)`

Renders action toolbars.

**Parameters:**

- `items` (list): Toolbar items
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Breadcrumb Components

### `render_breadcrumb(items, **attrs)`

Renders navigation breadcrumbs.

**Parameters:**

- `items` (list): Breadcrumb items (strings or dicts with 'text' and 'url')
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Badge Components

### `render_badge(content, badge_type="default", **attrs)`

Renders badges and labels.

**Parameters:**

- `content` (str): Badge content
- `badge_type` (str): Badge type - "default", "primary", "secondary", "success", "danger", "warning", "info"
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Pagination Components

### `render_pagination(current_page, total_pages, **attrs)`

Renders pagination controls.

**Parameters:**

- `current_page` (int): Current page number
- `total_pages` (int): Total number of pages
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Calendar Components

### `render_calendar(**attrs)`

Renders calendar widgets.

**Parameters:**

- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Dialog Components

### `render_dialog(title, content, **attrs)`

Renders dialog boxes.

**Parameters:**

- `title` (str): Dialog title
- `content` (str): Dialog content HTML
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Dropdown Components

### `render_dropdown(items, button_text="Dropdown", **attrs)`

Renders dropdown select lists.

**Parameters:**

- `items` (list): Dropdown items (strings or dicts with 'text' and 'url')
- `button_text` (str): Button text for dropdown trigger
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Avatar Components

### `render_avatar(image_url, size="medium", **attrs)`

Renders user avatars.

**Parameters:**

- `image_url` (str): Avatar image URL
- `size` (str): Avatar size - "mini", "small", "medium", "large"
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Rating Components

### `render_rating(value, max_value=5, **attrs)`

Renders star ratings.

**Parameters:**

- `value` (int/float): Rating value
- `max_value` (int): Maximum rating value
- `**attrs`: Additional HTML attributes

**Returns:** HTML string

## Form Functions (Available in `metroui5.forms`)

For form-related functions, import from the forms module:

```python
from metroui5.forms import (
    render_form, render_field, render_formset,
    render_form_errors, render_formset_errors, render_label
)
```

### `render_form(form, **kwargs)`

Renders Django forms with MetroUI5 styling.

### `render_field(field, **kwargs)`

Renders individual form fields.

### `render_formset(formset, **kwargs)`

Renders Django formsets.

## Common Parameters

All component functions accept these common parameters:

### HTML Attributes

- `id` (str): Element ID
- `class` (str): CSS classes
- `style` (str): Inline styles
- `data-*` (str): Data attributes

### Event Handlers

- `onclick` (str): Click handler
- `onchange` (str): Change handler
- `onsubmit` (str): Submit handler

## Usage Examples

### Basic Component Usage

```python
from metroui5.components import render_button, render_alert

# Simple button
button = render_button("Click Me", button_type="primary")

# Alert with custom styling
alert = render_alert(
    "Success message",
    alert_type="success",
    **{"class": "my-custom-alert", "data-timeout": "5000"}
)
```

### Complex Component Composition

```python
from metroui5.components import render_card, render_button, render_badge

# Card with multiple elements
card_content = f"""
    <p>Product description here</p>
    {render_badge("New", badge_type="success")}
    <div class="mt-3">
        {render_button("Add to Cart", button_type="primary")}
        {render_button("View Details", button_type="secondary", outline=True)}
    </div>
"""

product_card = render_card(
    header="Product Name",
    content=card_content
)
```

### Form Integration

```python
from django import forms
from metroui5.forms import render_form
from metroui5.components import render_button

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

def contact_view(request):
    form = ContactForm()

    form_html = render_form(form)
    submit_button = render_button(
        "Send Message",
        button_type="primary",
        type="submit"
    )

    return render(request, 'contact.html', {
        'form_html': form_html,
        'submit_button': submit_button
    })
```

## Related Documentation

- [Forms API](forms.md) - Form rendering functions
- [Template Tags](templatetags.md) - Django template tag equivalents
- [HTML Utilities](html.md) - Low-level HTML generation
- [CSS Utilities](css.md) - CSS class management
