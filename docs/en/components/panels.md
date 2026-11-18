# Panels

MetroUI5 Django provides a flexible panel component system for creating collapsible content areas, sidebars, and organized content sections.

## Basic Usage

```python
from metroui5.components import render_panel

# Simple panel
panel_html = render_panel(
    title="Panel Title",
    content="Panel content goes here..."
)
```

## Parameters

### `render_panel(title=None, content=None, **attrs)`

- **title** (str, optional): Panel title/header
- **content** (str): Panel content (can be HTML)
- **attrs** (dict): Additional HTML attributes

## Examples

### Basic Panel

```python
from metroui5.components import render_panel

panel = render_panel(
    title="User Information",
    content="""
    <p><strong>Name:</strong> John Doe</p>
    <p><strong>Email:</strong> john@example.com</p>
    <p><strong>Role:</strong> Administrator</p>
    """
)
```

### Panel with Custom Classes

```python
panel = render_panel(
    title="Settings",
    content="Panel content...",
    class="panel panel-primary",
    id="settings-panel"
)
```

### Collapsible Panel

```python
panel = render_panel(
    title="Advanced Options",
    content="Advanced settings content...",
    class="panel panel-collapsible",
    data_role="panel"
)
```

## MetroUI Panel Classes

MetroUI5 provides several CSS classes for panel styling:

### Style Classes

- `panel` - Base panel class
- `panel-primary` - Primary panel style
- `panel-secondary` - Secondary panel style
- `panel-success` - Success panel style
- `panel-warning` - Warning panel style
- `panel-danger` - Danger panel style
- `panel-info` - Info panel style

### Size Classes

- `panel-small` - Small panel
- `panel-large` - Large panel
- `panel-compact` - Compact panel

### Layout Classes

- `panel-collapsible` - Collapsible panel
- `panel-expandable` - Expandable panel
- `panel-fixed` - Fixed height panel
- `panel-scrollable` - Scrollable panel

## Panel Types

### Basic Information Panel

```python
def create_info_panel(title, data):
    """Create information panel with structured data."""

    content = "<div class='info-list'>"
    for key, value in data.items():
        content += f"""
        <div class='info-item'>
            <span class='info-label'>{key}:</span>
            <span class='info-value'>{value}</span>
        </div>
        """
    content += "</div>"

    return render_panel(
        title=title,
        content=content,
        class="panel panel-info"
    )

# Usage
user_data = {
    "Name": "John Doe",
    "Email": "john@example.com",
    "Phone": "+1-555-0123",
    "Department": "Engineering"
}

info_panel = create_info_panel("User Details", user_data)
```

### Collapsible Settings Panel

```python
def create_settings_panel():
    """Create collapsible settings panel."""

    content = """
    <form class="settings-form">
        <div class="form-group">
            <label>Theme:</label>
            <select class="select">
                <option>Light</option>
                <option>Dark</option>
                <option>Auto</option>
            </select>
        </div>
        <div class="form-group">
            <label>Language:</label>
            <select class="select">
                <option>English</option>
                <option>Spanish</option>
                <option>French</option>
            </select>
        </div>
        <div class="form-group">
            <label class="checkbox">
                <input type="checkbox" data-role="checkbox">
                <span class="check"></span>
                Enable notifications
            </label>
        </div>
        <button class="button button-primary">Save Settings</button>
    </form>
    """

    return render_panel(
        title="Settings",
        content=content,
        class="panel panel-collapsible",
        data_role="panel"
    )

settings_panel = create_settings_panel()
```

### Statistics Panel

```python
def create_stats_panel(title, stats):
    """Create statistics panel with metrics."""

    content = "<div class='stats-grid'>"
    for stat in stats:
        content += f"""
        <div class='stat-item'>
            <div class='stat-value'>{stat['value']}</div>
            <div class='stat-label'>{stat['label']}</div>
            <div class='stat-change {stat.get('change_type', 'neutral')}'>
                {stat.get('change', '')}
            </div>
        </div>
        """
    content += "</div>"

    return render_panel(
        title=title,
        content=content,
        class="panel panel-primary"
    )

# Usage
dashboard_stats = [
    {"value": "1,234", "label": "Total Users", "change": "+12%", "change_type": "positive"},
    {"value": "567", "label": "Active Sessions", "change": "+5%", "change_type": "positive"},
    {"value": "89", "label": "Errors", "change": "-3%", "change_type": "negative"},
    {"value": "98.5%", "label": "Uptime", "change": "+0.2%", "change_type": "positive"}
]

stats_panel = create_stats_panel("Dashboard Overview", dashboard_stats)
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_panel title="Panel Title" content="Panel
content..." class="panel panel-primary" %}
```

## Advanced Examples

### Panel with Actions

```python
def create_action_panel(title, content, actions=None):
    """Create panel with action buttons."""

    if actions is None:
        actions = []

    action_buttons = ""
    for action in actions:
        action_buttons += f"""
        <button class="button button-{action.get('type', 'default')}"
                onclick="{action.get('onclick', '')}">
            {action.get('text', 'Action')}
        </button>
        """

    panel_content = f"""
    <div class="panel-content">
        {content}
    </div>
    <div class="panel-actions">
        {action_buttons}
    </div>
    """

    return render_panel(
        title=title,
        content=panel_content,
        class="panel panel-with-actions"
    )

# Usage
actions = [
    {"text": "Edit", "type": "primary", "onclick": "editItem()"},
    {"text": "Delete", "type": "danger", "onclick": "deleteItem()"},
    {"text": "View", "type": "secondary", "onclick": "viewItem()"}
]

action_panel = create_action_panel(
    "User Profile",
    "User profile content...",
    actions
)
```

### Panel with Tabs

```python
def create_tabbed_panel(title, tabs):
    """Create panel with tabbed content."""

    tab_nav = "<ul class='tabs-nav'>"
    tab_content = "<div class='tabs-content'>"

    for i, tab in enumerate(tabs):
        tab_id = f"tab-{i}"
        tab_nav += f"<li><a href='#{tab_id}'>{tab['title']}</a></li>"
        tab_content += f"<div id='{tab_id}'>{tab['content']}</div>"

    tab_nav += "</ul>"
    tab_content += "</div>"

    content = f"""
    <div class="tabs" data-role="tabs">
        {tab_nav}
        {tab_content}
    </div>
    """

    return render_panel(
        title=title,
        content=content,
        class="panel panel-tabbed"
    )

# Usage
tabs = [
    {
        "title": "General",
        "content": "General settings content..."
    },
    {
        "title": "Security",
        "content": "Security settings content..."
    },
    {
        "title": "Notifications",
        "content": "Notification settings content..."
    }
]

tabbed_panel = create_tabbed_panel("User Settings", tabs)
```

### Panel with Progress Indicators

```python
def create_progress_panel(title, tasks):
    """Create panel showing task progress."""

    content = "<div class='task-list'>"
    for task in tasks:
        progress = task.get('progress', 0)
        status_class = "success" if progress == 100 else "warning" if progress > 0 else "default"

        content += f"""
        <div class='task-item'>
            <div class='task-header'>
                <span class='task-name'>{task['name']}</span>
                <span class='task-status badge badge-{status_class}'>{progress}%</span>
            </div>
            <div class='progress-bar'>
                <div class='progress-fill' style='width: {progress}%'></div>
            </div>
        </div>
        """
    content += "</div>"

    return render_panel(
        title=title,
        content=content,
        class="panel panel-progress"
    )

# Usage
tasks = [
    {"name": "Database Migration", "progress": 100},
    {"name": "File Upload", "progress": 75},
    {"name": "Email Setup", "progress": 25},
    {"name": "Security Scan", "progress": 0}
]

progress_panel = create_progress_panel("System Tasks", tasks)
```

### Panel with Data Table

```python
def create_table_panel(title, headers, rows):
    """Create panel with data table."""

    from metroui5.components import render_table

    table = render_table(headers, rows, class="table table-border table-striped")

    return render_panel(
        title=title,
        content=table,
        class="panel panel-table"
    )

# Usage
headers = ["Name", "Email", "Role", "Status"]
rows = [
    ["John Doe", "john@example.com", "Admin", "Active"],
    ["Jane Smith", "jane@example.com", "User", "Active"],
    ["Bob Johnson", "bob@example.com", "Editor", "Inactive"]
]

table_panel = create_table_panel("Users", headers, rows)
```

### Responsive Panel Grid

```python
def create_panel_grid(panels, columns=3):
    """Create responsive grid of panels."""

    grid_class = f"grid grid-columns-{columns}"
    grid_content = f"<div class='{grid_class}'>"

    for panel in panels:
        grid_content += f"<div class='cell'>{panel}</div>"

    grid_content += "</div>"

    return grid_content

# Usage
panels = [
    create_info_panel("Panel 1", {"Key": "Value"}),
    create_info_panel("Panel 2", {"Key": "Value"}),
    create_info_panel("Panel 3", {"Key": "Value"}),
    create_info_panel("Panel 4", {"Key": "Value"})
]

panel_grid = create_panel_grid(panels, columns=2)
```

## JavaScript Integration

### Panel Collapse/Expand

```javascript
// Toggle panel collapse
function togglePanel(panelId) {
	const panel = document.querySelector(`#${panelId}`);
	if (panel) {
		panel.classList.toggle("panel-collapsed");

		const content = panel.querySelector(".panel-content");
		if (content) {
			content.style.display =
				content.style.display === "none" ? "block" : "none";
		}
	}
}

// Auto-collapse panels
document.querySelectorAll(".panel-collapsible").forEach((panel) => {
	const header = panel.querySelector(".panel-header");
	if (header) {
		header.addEventListener("click", function () {
			togglePanel(panel.id);
		});
	}
});
```

### Panel Loading States

```javascript
// Show loading state in panel
function showPanelLoading(panelId) {
	const panel = document.querySelector(`#${panelId}`);
	if (panel) {
		const content = panel.querySelector(".panel-content");
		if (content) {
			content.innerHTML = '<div class="loading-spinner">Loading...</div>';
		}
	}
}

// Update panel content
function updatePanelContent(panelId, newContent) {
	const panel = document.querySelector(`#${panelId}`);
	if (panel) {
		const content = panel.querySelector(".panel-content");
		if (content) {
			content.innerHTML = newContent;
		}
	}
}
```

### Panel Events

```javascript
// Handle panel events
document.querySelectorAll(".panel").forEach((panel) => {
	panel.addEventListener("panel-open", function () {
		console.log("Panel opened:", this.id);
	});

	panel.addEventListener("panel-close", function () {
		console.log("Panel closed:", this.id);
	});

	panel.addEventListener("panel-toggle", function () {
		console.log("Panel toggled:", this.id);
	});
});
```

## Best Practices

1. **Use descriptive titles**: Make panel titles clear and descriptive
2. **Organize content logically**: Group related information together
3. **Use appropriate sizing**: Choose panel sizes that fit your content
4. **Provide clear actions**: Make action buttons obvious and accessible
5. **Handle loading states**: Show loading indicators for dynamic content
6. **Make it responsive**: Ensure panels work well on all screen sizes
7. **Use consistent styling**: Apply consistent classes across your application

## Related Components

- [Cards](cards.md) - For card-based layouts
- [Tabs](tabs.md) - For tabbed content within panels
- [Tables](tables.md) - For data display in panels
- [Progress Bars](progress.md) - For progress indicators in panels


## metroui5_panel

```python
render_panel()
```

Empty or invalid: `render_panel()` returns `<div class="panel" data-role="panel"><div class="panel-content"></div></div>`.

```django
{% metroui5_panel %}
```
