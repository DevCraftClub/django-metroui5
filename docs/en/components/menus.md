# Menus

Component for creating navigation menus, context menus, and dropdown menu systems.

## Basic Usage

### Simple Menu

```python
from metroui5.components import render_menu

# Basic menu
menu_items = [
    {"text": "Home", "url": "/"},
    {"text": "About", "url": "/about/"},
    {"text": "Contact", "url": "/contact/"}
]

menu_html = render_menu(items=menu_items)
```

### Menu with Icons

```python
# Menu with icons
menu_items = [
    {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Users", "url": "/users/", "icon": "users"},
    {"text": "Settings", "url": "/settings/", "icon": "cog"}
]

menu_html = render_menu(items=menu_items, show_icons=True)
```

### Nested Menu

```python
# Menu with submenus
menu_items = [
    {"text": "Home", "url": "/"},
    {
        "text": "Products",
        "children": [
            {"text": "Laptops", "url": "/products/laptops/"},
            {"text": "Phones", "url": "/products/phones/"}
        ]
    },
    {"text": "Contact", "url": "/contact/"}
]

menu_html = render_menu(items=menu_items)
```

## Rendered Output

### Basic Menu

```html
<!-- Input -->
render_menu(items=[{"text": "Home", "url": "/"}, {"text": "About", "url":
"/about/"}])

<!-- Output -->
<ul class="menu" data-role="menu">
	<li class="menu-item">
		<a href="/" class="menu-link">Home</a>
	</li>
	<li class="menu-item">
		<a href="/about/" class="menu-link">About</a>
	</li>
</ul>
```

### Menu with Icons

```html
<!-- Input -->
render_menu(items=[{"text": "Home", "url": "/", "icon": "home"}],
show_icons=True)

<!-- Output -->
<ul class="menu menu-with-icons" data-role="menu">
	<li class="menu-item">
		<a href="/" class="menu-link">
			<span class="mif-home"></span>
			Home
		</a>
	</li>
</ul>
```

### Nested Menu

```html
<!-- Input -->
render_menu(items=[{"text": "Products", "children": [{"text": "Laptops", "url":
"/laptops/"}]}])

<!-- Output -->
<ul class="menu" data-role="menu">
	<li class="menu-item has-children">
		<a href="#" class="menu-link">Products</a>
		<ul class="menu-submenu">
			<li class="menu-item">
				<a href="/laptops/" class="menu-link">Laptops</a>
			</li>
		</ul>
	</li>
</ul>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic menu -->
{% metroui5_menu items=menu_items %}

<!-- Menu with icons -->
{% metroui5_menu items=menu_items show_icons=True %}

<!-- Custom menu -->
{% metroui5_menu items=menu_items class="menu-vertical" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_menu

def menu_view(request):
    # Create navigation menu
    nav_items = [
        {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard"},
        {"text": "Users", "url": "/users/", "icon": "users"},
        {
            "text": "Reports",
            "icon": "chart",
            "children": [
                {"text": "Sales", "url": "/reports/sales/"},
                {"text": "Analytics", "url": "/reports/analytics/"}
            ]
        }
    ]

    menu_html = render_menu(
        items=nav_items,
        show_icons=True,
        class="menu-primary"
    )

    context = {
        'menu_html': menu_html,
        'nav_items': nav_items
    }
    return render(request, 'menu.html', context)
```

```html
<!-- menu.html -->
{% load metroui5 %} {% block content %}
<!-- Direct HTML output -->
{{ menu_html|safe }}

<!-- Or use template tag -->
{% metroui5_menu items=nav_items show_icons=True %} {% endblock %}
```

## Parameters

### `items` (required)

List of menu items with text, URL, and optional properties.

**Format**:

```python
items = [
    {
        "text": "Menu Item",
        "url": "/path/",
        "icon": "icon-name",  # Optional
        "active": True,       # Optional
        "children": []        # Optional for submenus
    }
]
```

### `show_icons` (optional)

Whether to display icons in menu items.

**Default**: `False`

**Example**:

```python
menu_html = render_menu(items=items, show_icons=True)
```

### `orientation` (optional)

Menu orientation: horizontal or vertical.

**Default**: `"horizontal"`

**Example**:

```python
menu_html = render_menu(items=items, orientation="vertical")
```

### `id` (optional)

Unique identifier for the menu element.

**Example**:

```python
menu_html = render_menu(items=items, id="main-menu")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
menu_html = render_menu(items=items, class="menu-primary")
```

## Advanced Examples

### Context Menu

```python
def create_context_menu(actions):
    """Create right-click context menu."""

    context_items = []
    for action in actions:
        context_items.append({
            "text": action["text"],
            "onclick": action["function"],
            "icon": action.get("icon"),
            "disabled": action.get("disabled", False)
        })

    return render_menu(
        items=context_items,
        class="menu-context",
        show_icons=True
    )
```

### Breadcrumb Menu

```python
def create_breadcrumb_menu(path_items):
    """Create breadcrumb navigation menu."""

    breadcrumb_items = []
    for i, item in enumerate(path_items):
        breadcrumb_items.append({
            "text": item["text"],
            "url": item["url"] if i < len(path_items) - 1 else None,
            "active": i == len(path_items) - 1
        })

    return render_menu(
        items=breadcrumb_items,
        class="menu-breadcrumb",
        orientation="horizontal"
    )
```

### User Menu

```python
def create_user_menu(user):
    """Create user profile menu."""

    user_items = [
        {"text": f"Welcome, {user.first_name}", "disabled": True},
        {"text": "Profile", "url": "/profile/", "icon": "user"},
        {"text": "Settings", "url": "/settings/", "icon": "cog"},
        {"text": "Logout", "url": "/logout/", "icon": "exit"}
    ]

    return render_menu(
        items=user_items,
        class="menu-user",
        show_icons=True
    )
```

### Sidebar Menu

```python
def create_sidebar_menu(sections):
    """Create sidebar navigation menu."""

    sidebar_items = []
    for section in sections:
        if section.get("children"):
            sidebar_items.append({
                "text": section["title"],
                "icon": section.get("icon"),
                "children": section["children"]
            })
        else:
            sidebar_items.append({
                "text": section["title"],
                "url": section["url"],
                "icon": section.get("icon")
            })

    return render_menu(
        items=sidebar_items,
        orientation="vertical",
        class="menu-sidebar",
        show_icons=True
    )
```

## Styling

### CSS Classes

#### Base Classes

- `menu` - Base menu class
- `menu-primary` - Primary menu style
- `menu-secondary` - Secondary menu style

#### Orientation Classes

- `menu-horizontal` - Horizontal menu layout
- `menu-vertical` - Vertical menu layout

#### Feature Classes

- `menu-with-icons` - Menu with icon support
- `menu-collapsible` - Collapsible menu sections

#### Type Classes

- `menu-context` - Context menu style
- `menu-breadcrumb` - Breadcrumb menu style
- `menu-sidebar` - Sidebar menu style

### Custom Styling

```css
/* Custom menu styling */
.menu-custom {
	background: #f8f9fa;
	border: 1px solid #dee2e6;
	border-radius: 6px;
	padding: 10px 0;
}

.menu-custom .menu-item {
	margin: 0;
}

.menu-custom .menu-link {
	padding: 12px 20px;
	color: #495057;
	text-decoration: none;
	display: block;
	transition: all 0.3s ease;
}

.menu-custom .menu-link:hover {
	background: #007acc;
	color: white;
}

.menu-custom .menu-link.active {
	background: #0056b3;
	color: white;
	font-weight: bold;
}

/* Submenu styling */
.menu-custom .menu-submenu {
	background: #ffffff;
	border-left: 3px solid #007acc;
	margin-left: 20px;
}
```

## JavaScript Integration

### Menu Events

```javascript
// Handle menu item clicks
$(".menu").on("click", ".menu-link", function (e) {
	const menuItem = $(this);
	const hasChildren = menuItem.parent().hasClass("has-children");

	if (hasChildren) {
		e.preventDefault();
		toggleSubmenu(menuItem);
	} else {
		handleMenuClick(menuItem);
	}
});

function toggleSubmenu(menuLink) {
	const submenu = menuLink.siblings(".menu-submenu");
	submenu.slideToggle();
	menuLink.parent().toggleClass("expanded");
}

function handleMenuClick(menuLink) {
	// Remove active class from all items
	$(".menu-link").removeClass("active");

	// Add active class to clicked item
	menuLink.addClass("active");

	// Track menu navigation
	const url = menuLink.attr("href");
	console.log("Navigating to:", url);
}
```

### Context Menu

```javascript
// Show context menu on right click
$(document).on("contextmenu", ".context-target", function (e) {
	e.preventDefault();

	const contextMenu = $(".menu-context");
	contextMenu.css({
		display: "block",
		left: e.pageX,
		top: e.pageY,
	});

	// Hide context menu when clicking elsewhere
	$(document).one("click", function () {
		contextMenu.hide();
	});
});
```

### Dynamic Menu Loading

```javascript
// Load menu items dynamically
function loadMenuItems(menuId, url) {
	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			updateMenu(menuId, data.items);
		},
		error: function (xhr, status, error) {
			console.error("Error loading menu:", error);
		},
	});
}

function updateMenu(menuId, items) {
	const menu = $(`#${menuId}`);
	menu.empty();

	items.forEach((item) => {
		const menuItem = createMenuItem(item);
		menu.append(menuItem);
	});
}

function createMenuItem(item) {
	const icon = item.icon ? `<span class="mif-${item.icon}"></span>` : "";
	const link = `<a href="${item.url}" class="menu-link">${icon}${item.text}</a>`;
	return `<li class="menu-item">${link}</li>`;
}
```

## Best Practices

### 1. Menu Structure

```python
# Consistent menu item structure
def create_menu_item(text, url=None, icon=None, children=None, **kwargs):
    """Create standardized menu item."""
    item = {"text": text}
    if url:
        item["url"] = url
    if icon:
        item["icon"] = icon
    if children:
        item["children"] = children
    item.update(kwargs)
    return item
```

### 2. Active State Management

```python
# Determine active menu items
def set_active_menu_item(menu_items, current_path):
    """Set active state for current page."""
    for item in menu_items:
        if item.get("url") == current_path:
            item["active"] = True
        elif item.get("children"):
            set_active_menu_item(item["children"], current_path)
```

### 3. Permission-Based Menus

```python
# Filter menu items based on permissions
def filter_menu_by_permissions(menu_items, user):
    """Filter menu items based on user permissions."""
    filtered_items = []
    for item in menu_items:
        if has_permission(user, item.get("permission")):
            if item.get("children"):
                item["children"] = filter_menu_by_permissions(item["children"], user)
            filtered_items.append(item)
    return filtered_items
```

## Related Components

- [Navigation](navigation.md) - For navigation systems
- [Buttons](buttons.md) - For menu triggers
- [Icons](icons.md) - For menu item icons
- [Dropdowns](dropdowns.md) - For dropdown menus


## metroui5_menu

```python
render_menu([{'text': 'One', 'href': '/one'}])
```

Empty or invalid: `render_menu([{'text': 'One', 'href': '/one'}])` returns `<ul class="menu" data-role="menu"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="menu" data-role="menu"></ul>`.

```django
{% metroui5_menu items %}
```
