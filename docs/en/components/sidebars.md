# Sidebars

Component for creating navigation sidebars, side panels, and collapsible side content areas.

## Basic Usage

### Simple Sidebar

```python
from metroui5.components import render_sidebar

# Basic sidebar
sidebar_html = render_sidebar(
    content="<p>Sidebar content here</p>"
)
```

### Sidebar with Menu

```python
# Sidebar with navigation menu
menu_items = [
    {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Users", "url": "/users/", "icon": "users"},
    {"text": "Settings", "url": "/settings/", "icon": "cog"}
]

sidebar_html = render_sidebar(
    menu_items=menu_items,
    title="Navigation"
)
```

### Collapsible Sidebar

```python
# Collapsible sidebar
sidebar_html = render_sidebar(
    content="<p>Collapsible content</p>",
    collapsible=True,
    collapsed=False,
    position="left"
)
```

## Rendered Output

### Basic Sidebar

```html
<!-- Input -->
render_sidebar(content="
<p>Sidebar content</p>
")

<!-- Output -->
<div class="sidebar" data-role="sidebar">
	<div class="sidebar-content">
		<p>Sidebar content</p>
	</div>
</div>
```

### Sidebar with Menu

```html
<!-- Input -->
render_sidebar(menu_items=[{"text": "Home", "url": "/", "icon": "home"}],
title="Navigation")

<!-- Output -->
<div class="sidebar sidebar-with-menu" data-role="sidebar">
	<div class="sidebar-header">
		<h3>Navigation</h3>
	</div>
	<div class="sidebar-content">
		<ul class="sidebar-menu">
			<li class="sidebar-menu-item">
				<a href="/" class="sidebar-menu-link">
					<span class="mif-home"></span>
					Home
				</a>
			</li>
		</ul>
	</div>
</div>
```

### Collapsible Sidebar

```html
<!-- Input -->
render_sidebar(content="Content", collapsible=True, position="left")

<!-- Output -->
<div
	class="sidebar sidebar-collapsible sidebar-left"
	data-role="sidebar"
	data-collapsible="true"
>
	<button class="sidebar-toggle" data-role="sidebar-toggle">☰</button>
	<div class="sidebar-content">Content</div>
</div>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic sidebar -->
{% metroui5_sidebar content="
<p>Content</p>
" %}

<!-- Sidebar with menu -->
{% metroui5_sidebar menu_items=sidebar_menu title="Navigation" %}

<!-- Collapsible sidebar -->
{% metroui5_sidebar content="Content" collapsible=True position="right" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_sidebar

def sidebar_view(request):
    # Create navigation sidebar
    nav_items = [
        {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard", "active": True},
        {"text": "Users", "url": "/users/", "icon": "users"},
        {"text": "Reports", "url": "/reports/", "icon": "chart"},
        {"text": "Settings", "url": "/settings/", "icon": "cog"}
    ]

    sidebar_html = render_sidebar(
        menu_items=nav_items,
        title="Main Menu",
        position="left",
        collapsible=True
    )

    context = {
        'sidebar_html': sidebar_html,
        'nav_items': nav_items
    }
    return render(request, 'sidebar.html', context)
```

```html
<!-- sidebar.html -->
{% load metroui5 %} {% block content %}
<!-- Direct HTML output -->
{{ sidebar_html|safe }}

<!-- Or use template tag -->
{% metroui5_sidebar menu_items=nav_items title="Navigation" position="left" %}
{% endblock %}
```

## Parameters

### `content` (optional)

HTML content to display in the sidebar.

**Example**:

```python
sidebar_html = render_sidebar(content="<p>Custom content</p>")
```

### `menu_items` (optional)

List of menu items for navigation sidebar.

**Format**:

```python
menu_items = [
    {
        "text": "Menu Item",
        "url": "/path/",
        "icon": "icon-name",  # Optional
        "active": True,       # Optional
        "children": []        # Optional for submenus
    }
]
```

### `title` (optional)

Title displayed in the sidebar header.

**Example**:

```python
sidebar_html = render_sidebar(title="Navigation Menu")
```

### `position` (optional)

Position of the sidebar: left or right.

**Default**: `"left"`

**Example**:

```python
sidebar_html = render_sidebar(content="Content", position="right")
```

### `collapsible` (optional)

Whether the sidebar can be collapsed.

**Default**: `False`

**Example**:

```python
sidebar_html = render_sidebar(content="Content", collapsible=True)
```

### `collapsed` (optional)

Initial collapsed state (if collapsible).

**Default**: `False`

**Example**:

```python
sidebar_html = render_sidebar(content="Content", collapsible=True, collapsed=True)
```

### `width` (optional)

Width of the sidebar.

**Example**:

```python
sidebar_html = render_sidebar(content="Content", width="300px")
```

### `id` (optional)

Unique identifier for the sidebar element.

**Example**:

```python
sidebar_html = render_sidebar(content="Content", id="main-sidebar")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
sidebar_html = render_sidebar(content="Content", class="sidebar-custom")
```

## Advanced Examples

### Multi-Level Navigation Sidebar

```python
def create_nav_sidebar(nav_sections):
    """Create sidebar with grouped navigation."""

    menu_items = []
    for section in nav_sections:
        if section.get("children"):
            menu_items.append({
                "text": section["title"],
                "icon": section.get("icon"),
                "children": section["children"]
            })
        else:
            menu_items.append({
                "text": section["title"],
                "url": section["url"],
                "icon": section.get("icon")
            })

    return render_sidebar(
        menu_items=menu_items,
        title="Navigation",
        position="left",
        collapsible=True,
        class="sidebar-navigation"
    )
```

### Filter Sidebar

```python
def create_filter_sidebar(filters):
    """Create sidebar with filter options."""

    filter_content = "<div class='sidebar-filters'>"

    for filter_group in filters:
        filter_content += f"<h4>{filter_group['title']}</h4>"
        filter_content += "<div class='filter-group'>"

        for option in filter_group['options']:
            checked = "checked" if option.get('selected') else ""
            filter_content += f"""
            <label class="filter-option">
                <input type="checkbox" name="{filter_group['name']}"
                       value="{option['value']}" {checked}>
                {option['text']}
            </label>
            """

        filter_content += "</div>"

    filter_content += "</div>"

    return render_sidebar(
        content=filter_content,
        title="Filters",
        position="left",
        class="sidebar-filters"
    )
```

### User Profile Sidebar

```python
def create_profile_sidebar(user):
    """Create user profile sidebar."""

    profile_content = f"""
    <div class="user-profile">
        <div class="user-avatar">
            <img src="{user.avatar_url}" alt="{user.name}">
        </div>
        <div class="user-info">
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            <p class="user-role">{user.role}</p>
        </div>
        <div class="user-stats">
            <div class="stat">
                <span class="stat-value">{user.posts_count}</span>
                <span class="stat-label">Posts</span>
            </div>
            <div class="stat">
                <span class="stat-value">{user.followers_count}</span>
                <span class="stat-label">Followers</span>
            </div>
        </div>
    </div>
    """

    return render_sidebar(
        content=profile_content,
        title="Profile",
        position="right",
        class="sidebar-profile"
    )
```

### Widget Sidebar

```python
def create_widget_sidebar(widgets):
    """Create sidebar with multiple widgets."""

    widget_content = ""

    for widget in widgets:
        widget_content += f"""
        <div class="sidebar-widget">
            <h4 class="widget-title">{widget['title']}</h4>
            <div class="widget-content">
                {widget['content']}
            </div>
        </div>
        """

    return render_sidebar(
        content=widget_content,
        title="Widgets",
        position="right",
        class="sidebar-widgets"
    )
```

## Styling

### CSS Classes

#### Base Classes

- `sidebar` - Base sidebar class
- `sidebar-primary` - Primary sidebar style
- `sidebar-secondary` - Secondary sidebar style

#### Position Classes

- `sidebar-left` - Left-positioned sidebar
- `sidebar-right` - Right-positioned sidebar

#### Feature Classes

- `sidebar-collapsible` - Collapsible sidebar
- `sidebar-collapsed` - Collapsed state
- `sidebar-with-menu` - Sidebar with menu items

#### Type Classes

- `sidebar-navigation` - Navigation sidebar
- `sidebar-filters` - Filter sidebar
- `sidebar-widgets` - Widget sidebar

### Custom Styling

```css
/* Custom sidebar styling */
.sidebar-custom {
	background: #f8f9fa;
	border-right: 1px solid #dee2e6;
	box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
	width: 280px;
	height: 100vh;
	position: fixed;
	left: 0;
	top: 0;
	z-index: 1000;
}

.sidebar-custom .sidebar-header {
	background: #007acc;
	color: white;
	padding: 20px;
	border-bottom: 1px solid #005a99;
}

.sidebar-custom .sidebar-content {
	padding: 20px;
	height: calc(100vh - 80px);
	overflow-y: auto;
}

.sidebar-custom .sidebar-menu-item {
	margin-bottom: 5px;
}

.sidebar-custom .sidebar-menu-link {
	display: block;
	padding: 12px 15px;
	color: #495057;
	text-decoration: none;
	border-radius: 6px;
	transition: all 0.3s ease;
}

.sidebar-custom .sidebar-menu-link:hover {
	background: #007acc;
	color: white;
}

.sidebar-custom .sidebar-menu-link.active {
	background: #0056b3;
	color: white;
}

/* Collapsed sidebar */
.sidebar-custom.sidebar-collapsed {
	width: 60px;
}

.sidebar-custom.sidebar-collapsed .sidebar-content {
	padding: 10px;
}

.sidebar-custom.sidebar-collapsed .sidebar-menu-link {
	text-align: center;
	padding: 15px 5px;
}

.sidebar-custom.sidebar-collapsed .sidebar-menu-link span:not(.mif) {
	display: none;
}
```

## JavaScript Integration

### Sidebar Toggle

```javascript
// Toggle sidebar collapse
function toggleSidebar(sidebarId) {
	const sidebar = $(`#${sidebarId}`);
	sidebar.toggleClass("sidebar-collapsed");

	// Save state to localStorage
	const isCollapsed = sidebar.hasClass("sidebar-collapsed");
	localStorage.setItem("sidebar-collapsed", isCollapsed);
}

// Initialize sidebar state from localStorage
$(document).ready(function () {
	const isCollapsed = localStorage.getItem("sidebar-collapsed") === "true";
	if (isCollapsed) {
		$(".sidebar").addClass("sidebar-collapsed");
	}

	// Handle toggle button clicks
	$(".sidebar-toggle").on("click", function () {
		const sidebar = $(this).closest(".sidebar");
		toggleSidebar(sidebar.attr("id"));
	});
});
```

### Responsive Sidebar

```javascript
// Handle responsive sidebar behavior
function handleResponsiveSidebar() {
	const sidebar = $(".sidebar");
	const windowWidth = $(window).width();

	if (windowWidth < 768) {
		// Mobile: Hide sidebar by default
		sidebar.addClass("sidebar-mobile");
		sidebar.addClass("sidebar-collapsed");
	} else {
		// Desktop: Show sidebar
		sidebar.removeClass("sidebar-mobile");
		const savedState = localStorage.getItem("sidebar-collapsed") === "true";
		sidebar.toggleClass("sidebar-collapsed", savedState);
	}
}

// Handle window resize
$(window).on("resize", handleResponsiveSidebar);

// Initialize on page load
$(document).ready(handleResponsiveSidebar);
```

### Sidebar Menu Navigation

```javascript
// Handle sidebar menu clicks
$(".sidebar-menu").on("click", ".sidebar-menu-link", function (e) {
	const menuLink = $(this);
	const hasChildren = menuLink.parent().hasClass("has-children");

	if (hasChildren) {
		e.preventDefault();
		toggleSubmenu(menuLink);
	} else {
		setActiveMenuItem(menuLink);
	}
});

function toggleSubmenu(menuLink) {
	const submenu = menuLink.siblings(".sidebar-submenu");
	const parent = menuLink.parent();

	submenu.slideToggle();
	parent.toggleClass("expanded");
}

function setActiveMenuItem(menuLink) {
	// Remove active class from all items
	$(".sidebar-menu-link").removeClass("active");

	// Add active class to clicked item
	menuLink.addClass("active");

	// Update breadcrumb or page title
	const itemText = menuLink.text().trim();
	updatePageTitle(itemText);
}
```

## Best Practices

### 1. Responsive Design

```python
# Create responsive sidebar
def create_responsive_sidebar(menu_items, mobile_collapsed=True):
    return render_sidebar(
        menu_items=menu_items,
        collapsible=True,
        collapsed=mobile_collapsed,
        class="sidebar-responsive"
    )
```

### 2. State Management

```python
# Preserve sidebar state
def get_sidebar_state(request):
    return {
        'collapsed': request.session.get('sidebar_collapsed', False),
        'active_item': request.path
    }
```

### 3. Permission-Based Menu

```python
# Filter menu items by user permissions
def create_authorized_sidebar(user, all_menu_items):
    authorized_items = []
    for item in all_menu_items:
        if user.has_perm(item.get('permission', 'view')):
            authorized_items.append(item)

    return render_sidebar(
        menu_items=authorized_items,
        title="Navigation",
        collapsible=True
    )
```

## Related Components

- [Menus](menus.md) - For sidebar menu items
- [Navigation](navigation.md) - For navigation systems
- [Icons](icons.md) - For sidebar menu icons
- [Panels](panels.md) - For sidebar content panels


## metroui5_sidebar

```python
render_sidebar([{'text': 'One', 'href': '/one'}])
```

Empty or invalid: `render_sidebar([{'text': 'One', 'href': '/one'}])` returns `<ul class="sidebar" data-role="sidebar"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="sidebar" data-role="sidebar"></ul>`.

```django
{% metroui5_sidebar items %}
```
