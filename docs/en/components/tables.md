# Tables

MetroUI5 Django provides a comprehensive table component system for displaying tabular data with various styling options and interactive features.

## Basic Usage

```python
from metroui5.components import render_table

# Simple table
headers = ["Name", "Email", "Role"]
rows = [
    ["John Doe", "john@example.com", "Admin"],
    ["Jane Smith", "jane@example.com", "User"],
    ["Bob Johnson", "bob@example.com", "Editor"]
]

table_html = render_table(headers, rows)
```

## Parameters

### `render_table(headers, rows, **attrs)`

- **headers** (list): List of column headers
- **rows** (list): List of rows, where each row is a list of cell values
- **attrs** (dict): Additional HTML attributes for the table

## Examples

### Basic Table

```python
from metroui5.components import render_table

headers = ["ID", "Name", "Status", "Actions"]
rows = [
    ["1", "Project Alpha", "Active", "Edit | Delete"],
    ["2", "Project Beta", "Pending", "Edit | Delete"],
    ["3", "Project Gamma", "Completed", "Edit | Delete"]
]

table = render_table(headers, rows)
```

### Table with Custom Classes

```python
table = render_table(
    headers=["Name", "Email", "Role"],
    rows=[
        ["John Doe", "john@example.com", "Admin"],
        ["Jane Smith", "jane@example.com", "User"]
    ],
    class="table table-border table-striped table-hover"
)
```

### Table with Additional Attributes

```python
table = render_table(
    headers=["Product", "Price", "Stock"],
    rows=[
        ["Laptop", "$999", "15"],
        ["Mouse", "$25", "50"],
        ["Keyboard", "$75", "30"]
    ],
    id="products-table",
    data_role="table",
    data_sort="true"
)
```

## MetroUI Table Classes

MetroUI5 provides several CSS classes for table styling:

### Basic Classes

- `table` - Base table class
- `table-border` - Adds borders to table cells
- `table-striped` - Alternating row colors
- `table-hover` - Hover effects on rows
- `table-compact` - Compact table with reduced padding

### Size Classes

- `table-small` - Small table
- `table-large` - Large table

### Color Classes

- `table-dark` - Dark theme table
- `table-light` - Light theme table

## Interactive Features

### Sortable Tables

```python
table = render_table(
    headers=["Name", "Age", "City"],
    rows=[
        ["Alice", "25", "New York"],
        ["Bob", "30", "Los Angeles"],
        ["Charlie", "28", "Chicago"]
    ],
    data_role="table",
    data_sort="true"
)
```

### Responsive Tables

```python
table = render_table(
    headers=["Name", "Email", "Phone", "Address"],
    rows=[
        ["John Doe", "john@example.com", "+1-555-0123", "123 Main St"],
        ["Jane Smith", "jane@example.com", "+1-555-0124", "456 Oak Ave"]
    ],
    class="table table-border table-responsive"
)
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_table headers=headers rows=rows class="table
table-border" %}
```

## Advanced Examples

### Table with Actions

```python
def create_action_buttons(row_id):
    return f"""
    <button class="button button-small button-primary" onclick="editRow({row_id})">
        Edit
    </button>
    <button class="button button-small button-danger" onclick="deleteRow({row_id})">
        Delete
    </button>
    """

headers = ["ID", "Name", "Email", "Actions"]
rows = [
    ["1", "John Doe", "john@example.com", create_action_buttons(1)],
    ["2", "Jane Smith", "jane@example.com", create_action_buttons(2)]
]

table = render_table(headers, rows, class="table table-border")
```

### Table with Status Indicators

```python
def get_status_badge(status):
    color_map = {
        "active": "success",
        "pending": "warning",
        "inactive": "danger"
    }
    color = color_map.get(status.lower(), "default")
    return f'<span class="badge badge-{color}">{status}</span>'

headers = ["Name", "Status", "Last Login"]
rows = [
    ["John Doe", get_status_badge("Active"), "2024-01-15"],
    ["Jane Smith", get_status_badge("Pending"), "2024-01-14"],
    ["Bob Johnson", get_status_badge("Inactive"), "2024-01-10"]
]

table = render_table(headers, rows, class="table table-border")
```

## Best Practices

1. **Use appropriate headers**: Make sure column headers are descriptive and clear
2. **Keep tables responsive**: Use `table-responsive` class for tables with many columns
3. **Add sorting when needed**: Enable sorting for tables with sortable data
4. **Use consistent styling**: Apply consistent classes across your application
5. **Consider accessibility**: Ensure proper ARIA labels and semantic markup

## Related Components

- [Cards](cards.md) - For card-based layouts
- [Lists](lists.md) - For list-based data display
- [Pagination](pagination.md) - For paginated table data


## metroui5_table

```python
render_table(['Name'], [['One']])
```

Empty or invalid: `render_table(['Name'], [['One']])` returns `<table class="table" data-role="table"><tr><th>Name</th></tr><tr><td>One</td></tr></table>`. An empty call returns `<table class="table" data-role="table"><tr></tr></table>`.

```django
{% metroui5_table headers rows %}
```
