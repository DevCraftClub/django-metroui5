# Tabs

Component for creating tabbed interfaces with multiple content panels and navigation tabs.

## Basic Usage

### Simple Tabs

```python
from metroui5.components import render_tabs

# Basic tabs
tab_items = [
    {"title": "Tab 1", "content": "Content for tab 1"},
    {"title": "Tab 2", "content": "Content for tab 2"},
    {"title": "Tab 3", "content": "Content for tab 3"}
]

tabs_html = render_tabs(items=tab_items)
```

### Tabs with Icons

```python
# Tabs with icons
tab_items = [
    {"title": "Home", "content": "Home content", "icon": "home"},
    {"title": "Profile", "content": "Profile content", "icon": "user"},
    {"title": "Settings", "content": "Settings content", "icon": "cog"}
]

tabs_html = render_tabs(items=tab_items, show_icons=True)
```

### Custom Tabs

```python
# Custom tabs with active tab
tabs_html = render_tabs(
    items=tab_items,
    active_tab=1,
    orientation="horizontal",
    id="main-tabs"
)
```

## Rendered Output

### Basic Tabs

```html
<!-- Input -->
render_tabs(items=[{"title": "Tab 1", "content": "Content 1"}, {"title": "Tab
2", "content": "Content 2"}])

<!-- Output -->
<div class="tabs" data-role="tabs">
	<ul class="tabs-nav">
		<li class="tab-nav-item active">
			<a href="#tab-0" class="tab-nav-link">Tab 1</a>
		</li>
		<li class="tab-nav-item">
			<a href="#tab-1" class="tab-nav-link">Tab 2</a>
		</li>
	</ul>
	<div class="tabs-content">
		<div id="tab-0" class="tab-panel active">Content 1</div>
		<div id="tab-1" class="tab-panel">Content 2</div>
	</div>
</div>
```

### Tabs with Icons

```html
<!-- Input -->
render_tabs(items=[{"title": "Home", "content": "Home content", "icon":
"home"}], show_icons=True)

<!-- Output -->
<div class="tabs tabs-with-icons" data-role="tabs">
	<ul class="tabs-nav">
		<li class="tab-nav-item active">
			<a href="#tab-0" class="tab-nav-link">
				<span class="mif-home"></span>
				Home
			</a>
		</li>
	</ul>
	<div class="tabs-content">
		<div id="tab-0" class="tab-panel active">Home content</div>
	</div>
</div>
```

### Vertical Tabs

```html
<!-- Input -->
render_tabs(items=tab_items, orientation="vertical")

<!-- Output -->
<div class="tabs tabs-vertical" data-role="tabs">
	<ul class="tabs-nav tabs-nav-vertical">
		<li class="tab-nav-item active">
			<a href="#tab-0" class="tab-nav-link">Tab 1</a>
		</li>
	</ul>
	<div class="tabs-content">
		<div id="tab-0" class="tab-panel active">Content 1</div>
	</div>
</div>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic tabs -->
{% metroui5_tabs items=tab_items %}

<!-- Tabs with icons -->
{% metroui5_tabs items=tab_items show_icons=True %}

<!-- Custom tabs -->
{% metroui5_tabs items=tab_items active_tab=2 orientation="vertical" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_tabs

def tabs_view(request):
    # Create content tabs
    content_tabs = [
        {
            "title": "Overview",
            "content": "<p>Project overview and summary</p>",
            "icon": "chart"
        },
        {
            "title": "Details",
            "content": "<p>Detailed project information</p>",
            "icon": "info"
        },
        {
            "title": "Team",
            "content": "<p>Team members and roles</p>",
            "icon": "users"
        }
    ]

    tabs_html = render_tabs(
        items=content_tabs,
        show_icons=True,
        active_tab=0,
        id="project-tabs"
    )

    context = {
        'tabs_html': tabs_html,
        'content_tabs': content_tabs
    }
    return render(request, 'tabs.html', context)
```

```html
<!-- tabs.html -->
{% load metroui5 %} {% block content %}
<!-- Direct HTML output -->
{{ tabs_html|safe }}

<!-- Or use template tag -->
{% metroui5_tabs items=content_tabs show_icons=True %} {% endblock %}
```

## Parameters

### `items` (required)

List of tab items with title and content.

**Format**:

```python
items = [
    {
        "title": "Tab Title",
        "content": "Tab content HTML",
        "icon": "icon-name",    # Optional
        "disabled": False,      # Optional
        "closable": False       # Optional
    }
]
```

### `active_tab` (optional)

Index of the initially active tab.

**Default**: `0`

**Example**:

```python
tabs_html = render_tabs(items=items, active_tab=2)
```

### `show_icons` (optional)

Whether to display icons in tab titles.

**Default**: `False`

**Example**:

```python
tabs_html = render_tabs(items=items, show_icons=True)
```

### `orientation` (optional)

Tab orientation: horizontal or vertical.

**Default**: `"horizontal"`

**Example**:

```python
tabs_html = render_tabs(items=items, orientation="vertical")
```

### `closable` (optional)

Whether tabs can be closed.

**Default**: `False`

**Example**:

```python
tabs_html = render_tabs(items=items, closable=True)
```

### `id` (optional)

Unique identifier for the tabs container.

**Example**:

```python
tabs_html = render_tabs(items=items, id="main-tabs")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
tabs_html = render_tabs(items=items, class="tabs-custom")
```

## Advanced Examples

### Dynamic Tabs

```python
def create_dynamic_tabs(base_tabs, user_tabs=None):
    """Create tabs with dynamic user-specific content."""

    all_tabs = base_tabs.copy()

    if user_tabs:
        all_tabs.extend(user_tabs)

    return render_tabs(
        items=all_tabs,
        closable=True,
        class="tabs-dynamic"
    )
```

### Form Tabs

```python
def create_form_tabs(form_sections):
    """Create tabs for multi-step form."""

    form_tabs = []
    for i, section in enumerate(form_sections):
        form_tabs.append({
            "title": section["title"],
            "content": section["form_html"],
            "icon": section.get("icon"),
            "data-step": i + 1
        })

    return render_tabs(
        items=form_tabs,
        show_icons=True,
        class="tabs-form"
    )
```

### Content Management Tabs

```python
def create_content_tabs(content_types):
    """Create tabs for different content types."""

    content_tabs = []
    for content_type in content_types:
        content_tabs.append({
            "title": content_type["name"],
            "content": f"""
            <div class="content-section">
                <h3>{content_type["name"]}</h3>
                <div class="content-list">
                    {render_content_list(content_type["items"])}
                </div>
            </div>
            """,
            "icon": content_type.get("icon"),
            "count": len(content_type["items"])
        })

    return render_tabs(
        items=content_tabs,
        show_icons=True,
        class="tabs-content-management"
    )
```

### Dashboard Tabs

```python
def create_dashboard_tabs(dashboard_sections):
    """Create dashboard with tabbed sections."""

    dashboard_tabs = []
    for section in dashboard_sections:
        dashboard_tabs.append({
            "title": section["title"],
            "content": f"""
            <div class="dashboard-section">
                {render_dashboard_widgets(section["widgets"])}
            </div>
            """,
            "icon": section.get("icon")
        })

    return render_tabs(
        items=dashboard_tabs,
        show_icons=True,
        class="tabs-dashboard"
    )
```

## Styling

### CSS Classes

#### Base Classes

- `tabs` - Base tabs container
- `tabs-primary` - Primary tabs style
- `tabs-secondary` - Secondary tabs style

#### Orientation Classes

- `tabs-horizontal` - Horizontal tab layout
- `tabs-vertical` - Vertical tab layout

#### Feature Classes

- `tabs-with-icons` - Tabs with icon support
- `tabs-closable` - Closable tabs
- `tabs-scrollable` - Scrollable tab navigation

#### Type Classes

- `tabs-form` - Form-style tabs
- `tabs-dashboard` - Dashboard-style tabs
- `tabs-content` - Content management tabs

### Custom Styling

```css
/* Custom tabs styling */
.tabs-custom {
	border: 1px solid #dee2e6;
	border-radius: 6px;
	overflow: hidden;
}

.tabs-custom .tabs-nav {
	background: #f8f9fa;
	border-bottom: 1px solid #dee2e6;
	margin: 0;
	padding: 0;
	list-style: none;
	display: flex;
}

.tabs-custom .tab-nav-item {
	margin: 0;
}

.tabs-custom .tab-nav-link {
	display: block;
	padding: 15px 20px;
	color: #495057;
	text-decoration: none;
	border-right: 1px solid #dee2e6;
	transition: all 0.3s ease;
}

.tabs-custom .tab-nav-link:hover {
	background: #e9ecef;
	color: #007acc;
}

.tabs-custom .tab-nav-item.active .tab-nav-link {
	background: #007acc;
	color: white;
	border-bottom: 2px solid #0056b3;
}

.tabs-custom .tabs-content {
	padding: 20px;
}

.tabs-custom .tab-panel {
	display: none;
}

.tabs-custom .tab-panel.active {
	display: block;
}

/* Vertical tabs */
.tabs-custom.tabs-vertical {
	display: flex;
}

.tabs-custom.tabs-vertical .tabs-nav {
	flex-direction: column;
	width: 200px;
	border-right: 1px solid #dee2e6;
	border-bottom: none;
}

.tabs-custom.tabs-vertical .tab-nav-link {
	border-right: none;
	border-bottom: 1px solid #dee2e6;
}

.tabs-custom.tabs-vertical .tabs-content {
	flex: 1;
}
```

## JavaScript Integration

### Tab Navigation

```javascript
// Handle tab clicks
$(".tabs").on("click", ".tab-nav-link", function (e) {
	e.preventDefault();

	const tabLink = $(this);
	const tabsContainer = tabLink.closest(".tabs");
	const targetId = tabLink.attr("href");

	// Update active tab navigation
	tabsContainer.find(".tab-nav-item").removeClass("active");
	tabLink.parent().addClass("active");

	// Update active tab content
	tabsContainer.find(".tab-panel").removeClass("active");
	tabsContainer.find(targetId).addClass("active");

	// Trigger tab change event
	tabsContainer.trigger("tab-changed", [targetId]);
});
```

### Dynamic Tab Management

```javascript
// Add new tab
function addTab(tabsId, title, content, icon = null) {
	const tabs = $(`#${tabsId}`);
	const tabsNav = tabs.find(".tabs-nav");
	const tabsContent = tabs.find(".tabs-content");
	const tabIndex = tabs.find(".tab-nav-item").length;
	const tabId = `tab-${tabIndex}`;

	// Add navigation item
	const iconHtml = icon ? `<span class="mif-${icon}"></span>` : "";
	const navItem = `
        <li class="tab-nav-item">
            <a href="#${tabId}" class="tab-nav-link">
                ${iconHtml}${title}
                <button class="tab-close" onclick="closeTab('${tabId}')">&times;</button>
            </a>
        </li>
    `;
	tabsNav.append(navItem);

	// Add content panel
	const contentPanel = `
        <div id="${tabId}" class="tab-panel">
            ${content}
        </div>
    `;
	tabsContent.append(contentPanel);

	// Activate new tab
	switchTab(tabsId, tabId);
}

// Close tab
function closeTab(tabId) {
	const tabPanel = $(`#${tabId}`);
	const tabsContainer = tabPanel.closest(".tabs");
	const tabNavItem = tabsContainer.find(`a[href="#${tabId}"]`).parent();

	// Remove tab navigation and content
	tabNavItem.remove();
	tabPanel.remove();

	// Activate first remaining tab if closed tab was active
	if (tabPanel.hasClass("active")) {
		const firstTab = tabsContainer.find(".tab-nav-link").first();
		if (firstTab.length) {
			firstTab.click();
		}
	}
}

// Switch to specific tab
function switchTab(tabsId, tabId) {
	const tabs = $(`#${tabsId}`);
	const targetLink = tabs.find(`a[href="#${tabId}"]`);
	targetLink.click();
}
```

### Tab Content Loading

```javascript
// Load tab content via AJAX
function loadTabContent(tabId, url) {
	const tabPanel = $(`#${tabId}`);

	// Show loading state
	tabPanel.html('<div class="loading">Loading...</div>');

	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			tabPanel.html(data);
		},
		error: function (xhr, status, error) {
			tabPanel.html('<div class="error">Error loading content</div>');
			console.error("Error loading tab content:", error);
		},
	});
}

// Lazy load tab content
$(".tabs").on("tab-changed", function (e, tabId) {
	const tabPanel = $(tabId);
	const loadUrl = tabPanel.data("load-url");

	if (loadUrl && !tabPanel.data("loaded")) {
		loadTabContent(tabId.substring(1), loadUrl);
		tabPanel.data("loaded", true);
	}
});
```

## Best Practices

### 1. Tab Content Structure

```python
# Consistent tab structure
def create_tab_item(title, content, icon=None, **kwargs):
    """Create standardized tab item."""
    tab = {"title": title, "content": content}
    if icon:
        tab["icon"] = icon
    tab.update(kwargs)
    return tab
```

### 2. Responsive Tabs

```python
# Create responsive tabs that work on mobile
def create_responsive_tabs(items, mobile_accordion=True):
    return render_tabs(
        items=items,
        class="tabs-responsive" + (" tabs-mobile-accordion" if mobile_accordion else "")
    )
```

### 3. State Persistence

```python
# Remember active tab across page loads
def create_stateful_tabs(items, request):
    active_tab = int(request.GET.get('tab', 0))
    return render_tabs(
        items=items,
        active_tab=active_tab,
        class="tabs-stateful"
    )
```

## Related Components

- [Navigation](navigation.md) - For tab navigation
- [Panels](panels.md) - For tab content panels
- [Icons](icons.md) - For tab icons
- [Forms](forms.md) - For tabbed forms


## metroui5_tabs

```python
render_tabs([{'title': 'One', 'content': 'Text'}])
```

Empty or invalid: `render_tabs([{'title': 'One', 'content': 'Text'}])` returns `<ul data-role="tabs"><li><a href="#tab-0">One</a></li></ul><div class="tabs-targets"><div id="tab-0">Text</div></div>`. An empty call returns `<ul data-role="tabs"></ul><div class="tabs-targets"></div>`.

```django
{% metroui5_tabs tabs %}
```
