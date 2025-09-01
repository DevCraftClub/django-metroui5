# CSS Utilities

MetroUI5 Django provides CSS utility functions for managing CSS classes and styles.

## Basic Usage

```python
from metroui5.css import merge_css_classes, add_css_class, remove_css_class

# Merge CSS classes
classes = merge_css_classes("button", "button-primary", "button-large")

# Add CSS class
button_with_primary = add_css_class("button", "button-primary")

# Remove CSS class
button_without_primary = remove_css_class("button button-primary", "button-primary")
```

## Available Functions

### `merge_css_classes(*args)`

Merges multiple CSS classes into a single string, handling duplicates and empty values.

**Parameters:**

- `*args`: Variable number of CSS class strings, lists, or tuples

**Returns:**

- `str`: Merged CSS classes string

**Example:**

```python
from metroui5.css import merge_css_classes

# Basic merging
classes = merge_css_classes("button", "button-primary", "button-large")
# Result: "button button-primary button-large"

# Handle duplicates
classes = merge_css_classes("button", "button", "button-primary")
# Result: "button button-primary"

# Handle empty values
classes = merge_css_classes("button", "", None, "button-primary")
# Result: "button button-primary"

# Mix strings and lists
classes = merge_css_classes("button", ["button-primary", "button-large"])
# Result: "button button-primary button-large"
```

### `add_css_class(classes, new_class)`

Adds a new CSS class to existing ones.

**Parameters:**

- `classes`: Existing CSS classes (string, list, or tuple)
- `new_class` (str): New CSS class to add

**Returns:**

- `str`: String with updated CSS classes

**Example:**

```python
from metroui5.css import add_css_class

# Add class to existing classes
button_with_primary = add_css_class("button", "button-primary")
# Result: "button button-primary"

# Add class to list of classes
button_with_size = add_css_class(["button", "button-primary"], "button-large")
# Result: "button button-primary button-large"

# Handle duplicates (won't add if already present)
button_no_duplicate = add_css_class("button button-primary", "button-primary")
# Result: "button button-primary"
```

### `remove_css_class(classes, class_to_remove)`

Removes CSS class from existing ones.

**Parameters:**

- `classes`: Existing CSS classes (string, list, or tuple)
- `class_to_remove` (str): CSS class to remove

**Returns:**

- `str`: String with updated CSS classes

**Example:**

```python
from metroui5.css import remove_css_class

# Remove class from existing classes
button_without_primary = remove_css_class("button button-primary", "button-primary")
# Result: "button"

# Remove class from list of classes
button_without_size = remove_css_class(["button", "button-primary", "button-large"], "button-large")
# Result: "button button-primary"

# Handle non-existent class (no change)
button_unchanged = remove_css_class("button button-primary", "button-large")
# Result: "button button-primary"
```

## Internal Functions

### `_css_class_list(classes)`

Converts CSS classes to a list (internal utility function).

**Parameters:**

- `classes`: CSS classes as string, list, or tuple

**Returns:**

- `list`: List of CSS classes

**Note:** This is an internal function used by other CSS utilities.

## Usage Examples

### Basic Class Management

```python
from metroui5.css import merge_css_classes, add_css_class, remove_css_class

# Start with base classes
base_classes = "button"

# Add primary style
button_classes = add_css_class(base_classes, "button-primary")

# Add size
button_classes = add_css_class(button_classes, "button-large")

# Remove size
button_classes = remove_css_class(button_classes, "button-large")

print(button_classes)  # Output: "button button-primary"
```

### Dynamic Class Building

```python
from metroui5.css import merge_css_classes

def build_button_classes(button_type="default", size=None, disabled=False):
    """Build button CSS classes dynamically."""
    classes = ["button"]

    if button_type != "default":
        classes.append(f"button-{button_type}")

    if size:
        classes.append(f"button-{size}")

    if disabled:
        classes.append("button-disabled")

    return merge_css_classes(*classes)

# Usage
primary_button = build_button_classes("primary", "large")
# Result: "button button-primary button-large"

disabled_button = build_button_classes("secondary", disabled=True)
# Result: "button button-secondary button-disabled"
```

### Component Class Management

```python
from metroui5.css import merge_css_classes, add_css_class

class ComponentCSSManager:
    def __init__(self, base_class):
        self.base_class = base_class
        self.classes = [base_class]

    def add_modifier(self, modifier):
        """Add a modifier class."""
        if modifier:
            self.classes.append(f"{self.base_class}-{modifier}")
        return self

    def add_state(self, state):
        """Add a state class."""
        if state:
            self.classes.append(f"{self.base_class}-{state}")
        return self

    def get_classes(self):
        """Get final CSS classes string."""
        return merge_css_classes(*self.classes)

# Usage
button_css = ComponentCSSManager("button")
button_css.add_modifier("primary").add_state("hover")
final_classes = button_css.get_classes()
# Result: "button button-primary button-hover"
```

### Form Field Classes

```python
from metroui5.css import merge_css_classes, add_css_class

def get_field_classes(field_type="text", size="medium", has_error=False):
    """Get CSS classes for form fields."""
    base_classes = ["form-control", f"form-control-{field_type}"]

    if size != "medium":
        base_classes.append(f"form-control-{size}")

    if has_error:
        base_classes.append("form-control-error")

    return merge_css_classes(*base_classes)

# Usage
text_field = get_field_classes("text", "large")
# Result: "form-control form-control-text form-control-large"

error_field = get_field_classes("email", has_error=True)
# Result: "form-control form-control-email form-control-error"
```

## Best Practices

### 1. Consistent Naming

```python
# Use consistent class naming patterns
def get_button_classes(variant="default", size="medium"):
    """Get button classes with consistent naming."""
    classes = ["btn"]

    if variant != "default":
        classes.append(f"btn-{variant}")

    if size != "medium":
        classes.append(f"btn-{size}")

    return merge_css_classes(*classes)
```

### 2. Handle Edge Cases

```python
def safe_add_class(existing_classes, new_class):
    """Safely add CSS class with error handling."""
    if not new_class or not isinstance(new_class, str):
        return existing_classes

    try:
        return add_css_class(existing_classes, new_class)
    except Exception:
        return existing_classes
```

### 3. Performance Optimization

```python
# Cache frequently used class combinations
from functools import lru_cache

@lru_cache(maxsize=128)
def get_cached_button_classes(variant, size):
    """Cache button class combinations for better performance."""
    return get_button_classes(variant, size)
```

## Related Documentation

- [Components](components.md) - Component rendering functions
- [HTML Utilities](html.md) - HTML generation utilities
- [Template Tags](templatetags.md) - Django template integration
