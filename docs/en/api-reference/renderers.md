# Renderers API Reference

MetroUI5 Django provides renderer classes for form and field rendering with MetroUI5 styling.

## Overview

The renderers module provides classes for rendering Django forms, fields, and formsets with MetroUI5 markup. Each renderer handles the conversion of Django form objects to HTML with proper MetroUI5 classes and attributes.

```python
from metroui5.renderers import BaseRenderer, FieldRenderer, FormRenderer, FormsetRenderer
from metroui5.css import merge_css_classes
from metroui5.html import render_tag
```

## Base Classes

### `BaseRenderer`

Base class for all MetroUI renderers with common functionality.

**Methods:**

#### `__init__(self, form_or_field, **kwargs)`

Initialize renderer with configuration options.

**Parameters:**

- `form_or_field`: Django form, field, or formset instance
- `**kwargs`: Renderer configuration options

#### `get_widget_attrs(self, widget)`

Gets widget attributes with MetroUI classes.

**Parameters:**

- `widget`: Django form widget instance

**Returns:** Dictionary of widget attributes

**Example:**

```python
class CustomRenderer(BaseRenderer):
    def render(self, **kwargs):
        widget_attrs = self.get_widget_attrs(self.field.field.widget)
        return render_tag("input", widget_attrs, close=False)
```

#### `get_field_classes(self, field)`

Gets CSS classes for form field.

**Parameters:**

- `field`: Django form field instance

**Returns:** String of CSS classes

**Example:**

```python
class FormRenderer(BaseRenderer):
    def render_field(self, field, **kwargs):
        field_classes = self.get_field_classes(field)
        
        return render_tag(
            "div",
            {"class": f"form-field {field_classes}"},
            field.as_widget(attrs=self.get_widget_attrs(field.field.widget))
        )
```

#### `render_errors(self, errors)`

Renders field errors.

**Parameters:**

- `errors`: List of error messages

**Returns:** HTML string

#### `render_help_text(self, help_text)`

Renders help text for field.

**Parameters:**

- `help_text`: Help text string

**Returns:** HTML string

## Field Renderer

### `FieldRenderer`

Renderer for individual form fields.

**Inherits from:** `BaseRenderer`

**Methods:**

#### `render(self)`

Renders form field in MetroUI markup.

**Returns:** HTML string

**Example:**

```python
from metroui5.renderers import FieldRenderer

# Render a single field
field_renderer = FieldRenderer(field, layout="horizontal")
field_html = field_renderer.render()
```

#### `render_label(self)`

Renders field label.

**Returns:** HTML string

#### `render_widget(self)`

Renders field widget.

**Returns:** HTML string

## Form Renderer

### `FormRenderer`

Renderer for Django forms.

**Inherits from:** `BaseRenderer`

**Methods:**

#### `render(self)`

Renders form in MetroUI markup.

**Returns:** HTML string

**Example:**

```python
from metroui5.renderers import FormRenderer

# Render a complete form
form_renderer = FormRenderer(form, layout="horizontal")
form_html = form_renderer.render()
```

#### `render_non_field_errors(self)`

Renders form errors (not related to fields).

**Returns:** HTML string

#### `render_hidden_fields(self)`

Renders hidden form fields.

**Returns:** HTML string

#### `render_visible_fields(self)`

Renders visible form fields.

**Returns:** HTML string

#### `render_errors(self, type="all")`

Renders form errors.

**Parameters:**

- `type` (str): Error type - "all", "non_field"

**Returns:** HTML string

## Formset Renderer

### `FormsetRenderer`

Renderer for Django formsets.

**Inherits from:** `BaseRenderer`

**Methods:**

#### `render(self)`

Renders formset in MetroUI markup.

**Returns:** HTML string

**Example:**

```python
from metroui5.renderers import FormsetRenderer

# Render a formset
formset_renderer = FormsetRenderer(formset)
formset_html = formset_renderer.render()
```

#### `render_formset_errors(self)`

Renders formset errors.

**Returns:** HTML string

#### `render_management_form(self)`

Renders formset management form.

**Returns:** HTML string

#### `render_errors(self)`

Renders formset errors.

**Returns:** HTML string

## Configuration Options

All renderers accept these configuration options:

### Layout Options

- `layout` (str): Form layout - "vertical" (default) or "horizontal"
- `size` (str): Input size - "mini", "small", "large"

### CSS Classes

- `horizontal_label_class` (str): CSS class for horizontal layout labels
- `horizontal_field_class` (str): CSS class for horizontal layout fields
- `horizontal_field_offset_class` (str): CSS class for horizontal layout field offsets
- `wrapper_class` (str): CSS class for field wrapper
- `inline_wrapper_class` (str): CSS class for inline field wrapper

### Behavior Options

- `set_placeholder` (bool): Whether to set placeholder text
- `required_css_class` (str): CSS class for required fields
- `error_css_class` (str): CSS class for fields with errors
- `success_css_class` (str): CSS class for fields with success state

## Usage Examples

### Basic Field Rendering

```python
from metroui5.renderers import FieldRenderer

def render_custom_field(field, **kwargs):
    """Render a field with custom styling."""
    renderer = FieldRenderer(field, **kwargs)
    return renderer.render()

# Usage
field_html = render_custom_field(
    form['username'],
    layout="horizontal",
    size="large"
)
```

### Custom Form Renderer

```python
from metroui5.renderers import FormRenderer

class CustomFormRenderer(FormRenderer):
    def render(self):
        """Custom form rendering with additional styling."""
        form_html = super().render()
        
        # Add custom wrapper
        return render_tag(
            "div",
            {"class": "custom-form-wrapper"},
            form_html
        )

# Usage
custom_renderer = CustomFormRenderer(form, layout="horizontal")
form_html = custom_renderer.render()
```

### Formset with Custom Styling

```python
from metroui5.renderers import FormsetRenderer

class StyledFormsetRenderer(FormsetRenderer):
    def render(self):
        """Render formset with custom styling."""
        formset_html = super().render()
        
        # Add formset container
        return render_tag(
            "div",
            {"class": "styled-formset", "data-role": "formset"},
            formset_html
        )

# Usage
styled_renderer = StyledFormsetRenderer(formset)
formset_html = styled_renderer.render()
```

### Field with Custom Widget Attributes

```python
from metroui5.renderers import FieldRenderer

class EnhancedFieldRenderer(FieldRenderer):
    def get_widget_attrs(self, widget):
        """Get widget attributes with enhancements."""
        attrs = super().get_widget_attrs(widget)
        
        # Add custom attributes
        attrs.update({
            "data-role": "input",
            "data-validate": "true"
        })
        
        return attrs

# Usage
enhanced_renderer = EnhancedFieldRenderer(field)
field_html = enhanced_renderer.render()
```

## Best Practices

### 1. Consistent Configuration

```python
# Define common renderer configuration
COMMON_RENDERER_CONFIG = {
    "layout": "horizontal",
    "size": "medium",
    "wrapper_class": "form-group",
    "error_css_class": "has-error",
    "success_css_class": "has-success"
}

# Use in renderers
renderer = FormRenderer(form, **COMMON_RENDERER_CONFIG)
```

### 2. Custom Error Handling

```python
class SafeFieldRenderer(FieldRenderer):
    def render(self):
        """Render field with error handling."""
        try:
            return super().render()
        except Exception as e:
            # Log error and return fallback
            logger.error(f"Field rendering error: {e}")
            return f'<div class="field-error">Field unavailable</div>'
```

### 3. Performance Optimization

```python
from functools import lru_cache

class CachedFormRenderer(FormRenderer):
    @lru_cache(maxsize=128)
    def get_cached_field_classes(self, field_id):
        """Cache field classes for better performance."""
        field = self.form.fields.get(field_id)
        if field:
            return self.get_field_classes(field)
        return ""
```

## Related Documentation

- [Forms API](forms.md) - Form rendering functions
- [CSS Utilities](css.md) - CSS class management
- [HTML Utilities](html.md) - HTML generation utilities
- [Template Tags](templatetags.md) - Django template integration
