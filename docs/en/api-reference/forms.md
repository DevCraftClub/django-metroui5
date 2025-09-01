# Forms

MetroUI5 Django provides comprehensive form rendering utilities for creating MetroUI-styled forms with proper validation, error handling, and responsive design.

## Basic Usage

```python
from metroui5.forms import render_form, render_field, render_formset

# Render a complete form
form_html = render_form(form)

# Render a single field
field_html = render_field(form['username'])

# Render a formset
formset_html = render_formset(formset)
```

## Functions

### `render_form(form, **kwargs)`

Renders a complete Django form with MetroUI styling.

**Parameters:**

- `form`: Django form instance
- `**kwargs`: Additional rendering options

**Returns:**

- `str`: Rendered form HTML

**Example:**

```python
from metroui5.forms import render_form
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

form = UserForm()
form_html = render_form(form)
```

### `render_field(field, **kwargs)`

Renders a single form field with MetroUI styling.

**Parameters:**

- `field`: Django form field instance
- `**kwargs`: Additional rendering options

**Returns:**

- `str`: Rendered field HTML

**Example:**

```python
from metroui5.forms import render_field

# Render specific field
username_field = form['username']
field_html = render_field(username_field, label_class="field-label", input_class="input")
```

### `render_formset(formset, **kwargs)`

Renders a Django formset with MetroUI styling.

**Parameters:**

- `formset`: Django formset instance
- `**kwargs`: Additional rendering options

**Returns:**

- `str`: Rendered formset HTML

**Example:**

```python
from metroui5.forms import render_formset
from django.forms import formset_factory

UserFormSet = formset_factory(UserForm, extra=3)
formset = UserFormSet()
formset_html = render_formset(formset)
```

### `render_form_errors(form, type="all", **kwargs)`

Renders form errors with MetroUI styling.

**Parameters:**

- `form`: Django form instance
- `type` (str): Error type ("all", "field", "non_field")
- `**kwargs`: Additional rendering options

**Returns:**

- `str`: Rendered errors HTML

**Example:**

```python
from metroui5.forms import render_form_errors

# Render all errors
errors_html = render_form_errors(form)

# Render only field errors
field_errors = render_form_errors(form, type="field")

# Render only non-field errors
non_field_errors = render_form_errors(form, type="non_field")
```

### `render_formset_errors(formset, **kwargs)`

Renders formset errors with MetroUI styling.

**Parameters:**

- `formset`: Django formset instance
- `**kwargs`: Additional rendering options

**Returns:**

- `str`: Rendered formset errors HTML

**Example:**

```python
from metroui5.forms import render_formset_errors

formset_errors = render_formset_errors(formset)
```

### `render_label(field, **kwargs)`

Renders a form field label with MetroUI styling.

**Parameters:**

- `field`: Django form field instance
- `**kwargs`: Additional rendering options

**Returns:**

- `str`: Rendered label HTML

**Example:**

```python
from metroui5.forms import render_label

label_html = render_label(form['email'], class="field-label")
```

## Form Rendering Options

### Basic Form Rendering

```python
# Simple form
form_html = render_form(form)

# Form with custom classes
form_html = render_form(
    form,
    form_class="form-custom",
    field_class="field-custom",
    label_class="label-custom"
)
```

### Field-Specific Rendering

```python
# Render field with custom options
field_html = render_field(
    form['username'],
    label_class="field-label",
    input_class="input input-large",
    help_text_class="help-text",
    error_class="error-message"
)
```

### Formset Rendering

```python
# Render formset with management form
formset_html = render_formset(
    formset,
    formset_class="formset-custom",
    form_class="form-inline",
    add_button_text="Add Another",
    remove_button_text="Remove"
)
```

## Advanced Usage

### Custom Form Layout

```python
def render_custom_form(form, layout="vertical"):
    """Render form with custom layout options."""

    if layout == "horizontal":
        return render_form(
            form,
            form_class="form form-horizontal",
            field_class="field field-horizontal",
            label_class="label label-horizontal"
        )
    elif layout == "inline":
        return render_form(
            form,
            form_class="form form-inline",
            field_class="field field-inline"
        )
    else:
        return render_form(
            form,
            form_class="form form-vertical",
            field_class="field field-vertical"
        )

# Usage
vertical_form = render_custom_form(form, "vertical")
horizontal_form = render_custom_form(form, "horizontal")
inline_form = render_custom_form(form, "inline")
```

### Conditional Field Rendering

```python
def render_conditional_fields(form, user_permissions):
    """Render fields based on user permissions."""

    rendered_fields = []

    for field_name, field in form.fields.items():
        # Check if user has permission to see this field
        if hasattr(field, 'permission_required'):
            if field.permission_required not in user_permissions:
                continue

        # Render field with conditional styling
        field_html = render_field(
            form[field_name],
            disabled=field_name in ['readonly_field1', 'readonly_field2'],
            readonly=field_name in ['readonly_field1', 'readonly_field2']
        )
        rendered_fields.append(field_html)

    return "\n".join(rendered_fields)

# Usage
user_perms = ['can_edit', 'can_view']
fields_html = render_conditional_fields(form, user_perms)
```

### Dynamic Form Validation

```python
def render_form_with_validation(form, validation_rules):
    """Render form with custom validation rules."""

    form_html = render_form(form)

    # Add validation JavaScript
    validation_js = """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const form = document.querySelector('#%s');
        if (form) {
            form.addEventListener('submit', function(e) {
                if (!validateForm(form, %s)) {
                    e.preventDefault();
                }
            });
        }
    });
    </script>
    """ % (form.auto_id, validation_rules)

    return form_html + validation_js

# Usage
validation_rules = {
    'username': {'required': True, 'min_length': 3},
    'email': {'required': True, 'email': True},
    'password': {'required': True, 'min_length': 8}
}

form_with_validation = render_form_with_validation(form, validation_rules)
```

### Responsive Form Layout

```python
def render_responsive_form(form, breakpoints=None):
    """Render form with responsive layout."""

    if breakpoints is None:
        breakpoints = {
            'mobile': {'columns': 1, 'stack': True},
            'tablet': {'columns': 2, 'stack': False},
            'desktop': {'columns': 3, 'stack': False}
        }

    form_class = "form form-responsive"

    # Add responsive classes
    for breakpoint, config in breakpoints.items():
        if config['columns'] > 1:
            form_class += f" form-{breakpoint}-columns-{config['columns']}"
        if config['stack']:
            form_class += f" form-{breakpoint}-stack"

    return render_form(form, form_class=form_class)

# Usage
responsive_form = render_responsive_form(form)
```

## Form Field Types

### Text Input Fields

```python
# Text input
text_field = render_field(
    form['username'],
    input_class="input",
    placeholder="Enter username"
)

# Email input
email_field = render_field(
    form['email'],
    input_class="input",
    type="email",
    placeholder="Enter email address"
)

# Password input
password_field = render_field(
    form['password'],
    input_class="input",
    type="password",
    placeholder="Enter password"
)
```

### Select Fields

```python
# Dropdown select
select_field = render_field(
    form['country'],
    input_class="select",
    data_role="select"
)

# Multi-select
multi_select_field = render_field(
    form['languages'],
    input_class="select",
    multiple=True,
    data_role="select"
)
```

### Checkbox and Radio Fields

```python
# Checkbox
checkbox_field = render_field(
    form['agree_terms'],
    input_class="checkbox",
    data_role="checkbox"
)

# Radio buttons
radio_field = render_field(
    form['gender'],
    input_class="radio",
    data_role="radio"
)
```

### Textarea Fields

```python
# Textarea
textarea_field = render_field(
    form['description'],
    input_class="textarea",
    rows=5,
    placeholder="Enter description..."
)
```

## Error Handling

### Field-Level Errors

```python
def render_field_with_errors(field):
    """Render field with error handling."""

    field_html = render_field(field)

    if field.errors:
        error_html = render_form_errors(field.form, type="field")
        return field_html + error_html

    return field_html

# Usage
field_with_errors = render_field_with_errors(form['username'])
```

### Form-Level Errors

```python
def render_form_with_error_summary(form):
    """Render form with error summary at top."""

    # Render non-field errors first
    non_field_errors = render_form_errors(form, type="non_field")

    # Render form
    form_html = render_form(form)

    return non_field_errors + form_html

# Usage
form_with_summary = render_form_with_error_summary(form)
```

## Best Practices

1. **Use semantic field names**: Choose descriptive field names
2. **Provide helpful labels**: Make labels clear and descriptive
3. **Include placeholder text**: Use placeholders to guide users
4. **Handle errors gracefully**: Display errors clearly and helpfully
5. **Make forms accessible**: Include proper ARIA labels and focus management
6. **Test thoroughly**: Test forms with various input combinations
7. **Use consistent styling**: Apply consistent classes across your application

## Related Functions

- [Components](components.md) - For form-related components
- [HTML Utilities](html.md) - For HTML element generation
- [Renderers](renderers.md) - For advanced form rendering
