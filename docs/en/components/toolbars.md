# Toolbars

Component for creating action toolbars, button groups, and navigation bars with various tools and controls.

## Basic Usage

### Simple Toolbar

```python
from metroui5.components import render_toolbar

# Basic toolbar
toolbar_items = [
    {"text": "New", "icon": "plus"},
    {"text": "Save", "icon": "checkmark"},
    {"text": "Delete", "icon": "delete"}
]

toolbar_html = render_toolbar(items=toolbar_items)
```

### Toolbar with Groups

```python
# Toolbar with grouped items
toolbar_groups = [
    {
        "items": [
            {"text": "New", "icon": "plus", "onclick": "createNew()"},
            {"text": "Open", "icon": "folder", "onclick": "openFile()"}
        ]
    },
    {
        "items": [
            {"text": "Save", "icon": "checkmark", "onclick": "saveFile()"},
            {"text": "Save As", "icon": "save", "onclick": "saveAsFile()"}
        ]
    }
]

toolbar_html = render_toolbar(groups=toolbar_groups)
```

### Custom Toolbar

```python
# Custom toolbar with positioning
toolbar_html = render_toolbar(
    items=toolbar_items,
    position="top",
    class="toolbar-primary",
    id="main-toolbar"
)
```

## Rendered Output

### Basic Toolbar

```html
<!-- Input -->
render_toolbar(items=[{"text": "New", "icon": "plus"}, {"text": "Save", "icon":
"checkmark"}])

<!-- Output -->
<div class="toolbar" data-role="toolbar">
	<div class="toolbar-group">
		<button class="toolbar-button" type="button">
			<span class="mif-plus"></span>
			New
		</button>
		<button class="toolbar-button" type="button">
			<span class="mif-checkmark"></span>
			Save
		</button>
	</div>
</div>
```

### Toolbar with Groups

```html
<!-- Input -->
render_toolbar(groups=[{"items": [{"text": "New", "icon": "plus"}]}, {"items":
[{"text": "Save", "icon": "save"}]}])

<!-- Output -->
<div class="toolbar" data-role="toolbar">
	<div class="toolbar-group">
		<button class="toolbar-button" type="button">
			<span class="mif-plus"></span>
			New
		</button>
	</div>
	<div class="toolbar-group">
		<button class="toolbar-button" type="button">
			<span class="mif-save"></span>
			Save
		</button>
	</div>
</div>
```

### Toolbar with Dropdown

```html
<!-- Input -->
render_toolbar(items=[{"text": "Actions", "dropdown": [{"text": "Edit"},
{"text": "Delete"}]}])

<!-- Output -->
<div class="toolbar" data-role="toolbar">
	<div class="toolbar-group">
		<div class="toolbar-dropdown">
			<button class="toolbar-button dropdown-toggle" type="button">
				Actions
				<span class="mif-chevron-down"></span>
			</button>
			<ul class="dropdown-menu">
				<li><a href="#" class="dropdown-item">Edit</a></li>
				<li><a href="#" class="dropdown-item">Delete</a></li>
			</ul>
		</div>
	</div>
</div>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic toolbar -->
{% metroui5_toolbar items=toolbar_items %}

<!-- Toolbar with groups -->
{% metroui5_toolbar groups=toolbar_groups %}

<!-- Custom toolbar -->
{% metroui5_toolbar items=toolbar_items position="bottom"
class="toolbar-secondary" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_toolbar

def toolbar_view(request):
    # Create action toolbar
    action_items = [
        {"text": "New Post", "icon": "plus", "onclick": "createPost()", "class": "button-primary"},
        {"text": "Edit", "icon": "edit", "onclick": "editPost()", "disabled": True},
        {"text": "Delete", "icon": "delete", "onclick": "deletePost()", "class": "button-danger"}
    ]

    toolbar_html = render_toolbar(
        items=action_items,
        position="top",
        class="toolbar-actions",
        id="post-toolbar"
    )

    context = {
        'toolbar_html': toolbar_html,
        'action_items': action_items
    }
    return render(request, 'toolbar.html', context)
```

```html
<!-- toolbar.html -->
{% load metroui5 %} {% block content %}
<!-- Direct HTML output -->
{{ toolbar_html|safe }}

<!-- Or use template tag -->
{% metroui5_toolbar items=action_items position="top" %} {% endblock %}
```

## Parameters

### `items` (optional)

List of toolbar items (buttons, dropdowns, etc.).

**Format**:

```python
items = [
    {
        "text": "Button Text",
        "icon": "icon-name",      # Optional
        "onclick": "function()",  # Optional
        "class": "button-class",  # Optional
        "disabled": False,        # Optional
        "dropdown": []            # Optional for dropdown items
    }
]
```

### `groups` (optional)

List of toolbar groups, each containing items.

**Format**:

```python
groups = [
    {
        "items": [...],           # List of items
        "separator": True         # Optional separator after group
    }
]
```

### `position` (optional)

Position of the toolbar: top, bottom, left, right.

**Default**: `"top"`

**Example**:

```python
toolbar_html = render_toolbar(items=items, position="bottom")
```

### `orientation` (optional)

Toolbar orientation: horizontal or vertical.

**Default**: `"horizontal"`

**Example**:

```python
toolbar_html = render_toolbar(items=items, orientation="vertical")
```

### `id` (optional)

Unique identifier for the toolbar element.

**Example**:

```python
toolbar_html = render_toolbar(items=items, id="main-toolbar")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
toolbar_html = render_toolbar(items=items, class="toolbar-custom")
```

## Advanced Examples

### Editor Toolbar

```python
def create_editor_toolbar():
    """Create toolbar for text editor."""

    editor_groups = [
        {
            "items": [
                {"text": "Bold", "icon": "bold", "onclick": "toggleBold()"},
                {"text": "Italic", "icon": "italic", "onclick": "toggleItalic()"},
                {"text": "Underline", "icon": "underline", "onclick": "toggleUnderline()"}
            ]
        },
        {
            "items": [
                {"text": "Align Left", "icon": "align-left", "onclick": "alignLeft()"},
                {"text": "Align Center", "icon": "align-center", "onclick": "alignCenter()"},
                {"text": "Align Right", "icon": "align-right", "onclick": "alignRight()"}
            ]
        },
        {
            "items": [
                {"text": "Insert Link", "icon": "link", "onclick": "insertLink()"},
                {"text": "Insert Image", "icon": "image", "onclick": "insertImage()"}
            ]
        }
    ]

    return render_toolbar(
        groups=editor_groups,
        class="toolbar-editor",
        id="editor-toolbar"
    )
```

### Data Table Toolbar

```python
def create_table_toolbar(selected_count=0):
    """Create toolbar for data table operations."""

    table_items = [
        {"text": "Add New", "icon": "plus", "onclick": "addRecord()", "class": "button-primary"},
        {"text": "Refresh", "icon": "refresh", "onclick": "refreshTable()"},
        {
            "text": "Export",
            "icon": "download",
            "dropdown": [
                {"text": "Export CSV", "onclick": "exportCSV()"},
                {"text": "Export Excel", "onclick": "exportExcel()"},
                {"text": "Export PDF", "onclick": "exportPDF()"}
            ]
        }
    ]

    if selected_count > 0:
        table_items.extend([
            {"text": f"Edit ({selected_count})", "icon": "edit", "onclick": "editSelected()"},
            {"text": f"Delete ({selected_count})", "icon": "delete", "onclick": "deleteSelected()", "class": "button-danger"}
        ])

    return render_toolbar(
        items=table_items,
        class="toolbar-table",
        id="table-toolbar"
    )
```

### Media Toolbar

```python
def create_media_toolbar():
    """Create toolbar for media player."""

    media_items = [
        {"text": "Play", "icon": "play", "onclick": "playMedia()", "id": "play-btn"},
        {"text": "Pause", "icon": "pause", "onclick": "pauseMedia()", "id": "pause-btn", "style": "display:none"},
        {"text": "Stop", "icon": "stop", "onclick": "stopMedia()"},
        {"text": "Previous", "icon": "previous", "onclick": "previousTrack()"},
        {"text": "Next", "icon": "next", "onclick": "nextTrack()"},
        {"text": "Volume", "icon": "volume", "onclick": "toggleMute()"}
    ]

    return render_toolbar(
        items=media_items,
        class="toolbar-media",
        orientation="horizontal"
    )
```

### Filter Toolbar

```python
def create_filter_toolbar(filters):
    """Create toolbar with filter controls."""

    filter_items = [
        {"text": "All", "onclick": "filterAll()", "class": "filter-btn active"},
        {"text": "Active", "onclick": "filterActive()", "class": "filter-btn"},
        {"text": "Inactive", "onclick": "filterInactive()", "class": "filter-btn"},
        {"text": "Clear Filters", "icon": "clear", "onclick": "clearFilters()"}
    ]

    return render_toolbar(
        items=filter_items,
        class="toolbar-filters",
        position="top"
    )
```

## Styling

### CSS Classes

#### Base Classes

- `toolbar` - Base toolbar class
- `toolbar-primary` - Primary toolbar style
- `toolbar-secondary` - Secondary toolbar style

#### Position Classes

- `toolbar-top` - Top-positioned toolbar
- `toolbar-bottom` - Bottom-positioned toolbar
- `toolbar-left` - Left-positioned toolbar
- `toolbar-right` - Right-positioned toolbar

#### Orientation Classes

- `toolbar-horizontal` - Horizontal toolbar layout
- `toolbar-vertical` - Vertical toolbar layout

#### Type Classes

- `toolbar-editor` - Editor-style toolbar
- `toolbar-table` - Table operations toolbar
- `toolbar-media` - Media controls toolbar

### Custom Styling

```css
/* Custom toolbar styling */
.toolbar-custom {
	background: #f8f9fa;
	border: 1px solid #dee2e6;
	border-radius: 6px;
	padding: 10px;
	display: flex;
	align-items: center;
	gap: 10px;
}

.toolbar-custom .toolbar-group {
	display: flex;
	align-items: center;
	gap: 5px;
	padding: 0 10px;
	border-right: 1px solid #dee2e6;
}

.toolbar-custom .toolbar-group:last-child {
	border-right: none;
}

.toolbar-custom .toolbar-button {
	background: white;
	border: 1px solid #ced4da;
	border-radius: 4px;
	padding: 8px 12px;
	color: #495057;
	cursor: pointer;
	transition: all 0.3s ease;
	display: flex;
	align-items: center;
	gap: 5px;
}

.toolbar-custom .toolbar-button:hover {
	background: #e9ecef;
	border-color: #007acc;
	color: #007acc;
}

.toolbar-custom .toolbar-button:active,
.toolbar-custom .toolbar-button.active {
	background: #007acc;
	border-color: #0056b3;
	color: white;
}

.toolbar-custom .toolbar-button:disabled {
	background: #f8f9fa;
	border-color: #e9ecef;
	color: #6c757d;
	cursor: not-allowed;
	opacity: 0.6;
}

/* Vertical toolbar */
.toolbar-custom.toolbar-vertical {
	flex-direction: column;
	align-items: stretch;
}

.toolbar-custom.toolbar-vertical .toolbar-group {
	border-right: none;
	border-bottom: 1px solid #dee2e6;
	padding: 10px 0;
}
```

## JavaScript Integration

### Toolbar Events

```javascript
// Handle toolbar button clicks
$(".toolbar").on("click", ".toolbar-button", function (e) {
	const button = $(this);
	const onclick = button.data("onclick");

	if (onclick && typeof window[onclick] === "function") {
		window[onclick]();
	}

	// Toggle active state for toggle buttons
	if (button.hasClass("toggle-btn")) {
		button.toggleClass("active");
	}
});

// Handle dropdown toggles
$(".toolbar").on("click", ".dropdown-toggle", function (e) {
	e.preventDefault();
	const dropdown = $(this).closest(".toolbar-dropdown");
	dropdown.find(".dropdown-menu").toggle();
});
```

### Dynamic Toolbar Updates

```javascript
// Update toolbar state
function updateToolbarState(toolbarId, updates) {
	const toolbar = $(`#${toolbarId}`);

	Object.keys(updates).forEach((buttonId) => {
		const button = toolbar.find(`#${buttonId}`);
		const update = updates[buttonId];

		if (update.disabled !== undefined) {
			button.prop("disabled", update.disabled);
		}

		if (update.active !== undefined) {
			button.toggleClass("active", update.active);
		}

		if (update.text !== undefined) {
			button.find(".button-text").text(update.text);
		}

		if (update.visible !== undefined) {
			button.toggle(update.visible);
		}
	});
}

// Example usage
updateToolbarState("editor-toolbar", {
	"bold-btn": { active: true },
	"save-btn": { disabled: false },
	"delete-btn": { visible: false },
});
```

### Responsive Toolbar

```javascript
// Handle responsive toolbar behavior
function handleResponsiveToolbar() {
	const toolbar = $(".toolbar");
	const windowWidth = $(window).width();

	if (windowWidth < 768) {
		// Mobile: Convert to vertical or collapsed
		toolbar.addClass("toolbar-mobile");
		collapseToolbarGroups();
	} else {
		// Desktop: Show full toolbar
		toolbar.removeClass("toolbar-mobile");
		expandToolbarGroups();
	}
}

function collapseToolbarGroups() {
	$(".toolbar-group").each(function () {
		const group = $(this);
		const buttons = group.find(".toolbar-button");

		if (buttons.length > 3) {
			// Hide extra buttons and show "more" dropdown
			buttons.slice(3).hide();
			group.append('<button class="toolbar-button more-btn">More...</button>');
		}
	});
}

function expandToolbarGroups() {
	$(".toolbar-button").show();
	$(".more-btn").remove();
}

// Handle window resize
$(window).on("resize", handleResponsiveToolbar);
$(document).ready(handleResponsiveToolbar);
```

### Toolbar Context Menu

```javascript
// Add context menu to toolbar
$(".toolbar").on("contextmenu", ".toolbar-button", function (e) {
	e.preventDefault();

	const button = $(this);
	const contextMenu = createToolbarContextMenu(button);

	showContextMenu(contextMenu, e.pageX, e.pageY);
});

function createToolbarContextMenu(button) {
	const isVisible = button.is(":visible");
	const isDisabled = button.is(":disabled");

	return [
		{
			text: isVisible ? "Hide Button" : "Show Button",
			onclick: () => button.toggle(),
		},
		{
			text: isDisabled ? "Enable Button" : "Disable Button",
			onclick: () => button.prop("disabled", !isDisabled),
		},
		{
			text: "Reset Toolbar",
			onclick: () => resetToolbar(button.closest(".toolbar")),
		},
	];
}
```

## Best Practices

### 1. Button Grouping

```python
# Group related actions together
def create_grouped_toolbar(action_groups):
	groups = []
	for group_name, actions in action_groups.items():
		groups.append({
			"items": actions,
			"separator": True
		})

	return render_toolbar(groups=groups)
```

### 2. State Management

```python
# Track toolbar state consistently
def create_stateful_toolbar(items, state=None):
	if state:
		for item in items:
			item_id = item.get('id')
			if item_id in state:
				item.update(state[item_id])

	return render_toolbar(items=items)
```

### 3. Responsive Design

```python
# Create responsive toolbar
def create_responsive_toolbar(items, mobile_limit=3):
	return render_toolbar(
		items=items,
		class="toolbar-responsive",
		**{"data-mobile-limit": mobile_limit}
	)
```

### 4. Accessibility

```python
# Ensure toolbar accessibility
def create_accessible_toolbar(items):
	for item in items:
		if not item.get('aria-label'):
			item['aria-label'] = item.get('text', 'Toolbar button')

	return render_toolbar(
		items=items,
		**{
			"role": "toolbar",
			"aria-label": "Main toolbar"
		}
	)
```

## Related Components

- [Buttons](buttons.md) - For toolbar button elements
- [Dropdowns](dropdowns.md) - For toolbar dropdown menus
- [Icons](icons.md) - For toolbar button icons
- [Navigation](navigation.md) - For navigation toolbars


## metroui5_toolbar

```python
render_toolbar([{'text': 'One', 'href': '/one'}])
```

Empty or invalid: `render_toolbar([{'text': 'One', 'href': '/one'}])` returns `<ul class="toolbar" data-role="toolbar"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="toolbar" data-role="toolbar"></ul>`.

```django
{% metroui5_toolbar items %}
```
