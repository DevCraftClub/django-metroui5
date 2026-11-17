# Navigation

MetroUI5 Django provides a flexible navigation component system for creating various types of navigation menus and navigation structures.

## Basic Usage

```python
from metroui5.components import render_navigation

# Simple navigation menu
items = [
    {"text": "Home", "url": "/", "icon": "home"},
    {"text": "About", "url": "/about/", "icon": "info"},
    {"text": "Contact", "url": "/contact/", "icon": "mail"}
]

nav_html = render_navigation(items)
```

## Parameters

### `render_navigation(items, **attrs)`

- **items** (list): List of navigation items, each containing:
  - `text` (str): Display text for the navigation item
  - `url` (str): URL for the navigation item
  - `icon` (str, optional): MetroUI icon name
  - `active` (bool, optional): Whether this item is currently active
  - `disabled` (bool, optional): Whether this item is disabled
- **attrs** (dict): Additional HTML attributes for the navigation container

## Examples

### Basic Navigation

```python
from metroui5.components import render_navigation

items = [
    {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Users", "url": "/users/", "icon": "users"},
    {"text": "Settings", "url": "/settings/", "icon": "cog"},
    {"text": "Reports", "url": "/reports/", "icon": "chart"}
]

nav = render_navigation(items)
```

### Navigation with Active State

```python
items = [
    {"text": "Home", "url": "/", "icon": "home"},
    {"text": "Products", "url": "/products/", "icon": "box", "active": True},
    {"text": "About", "url": "/about/", "icon": "info"},
    {"text": "Contact", "url": "/contact/", "icon": "mail"}
]

nav = render_navigation(items, class="nav nav-horizontal")
```

### Navigation with Custom Classes

```python
nav = render_navigation(
    items=[
        {"text": "Home", "url": "/", "icon": "home"},
        {"text": "About", "url": "/about/", "icon": "info"},
        {"text": "Contact", "url": "/contact/", "icon": "mail"}
    ],
    class="nav nav-horizontal nav-dark",
    id="main-navigation"
)
```

## MetroUI Navigation Classes

MetroUI5 provides several CSS classes for navigation styling:

### Layout Classes

- `nav` - Base navigation class
- `nav-horizontal` - Horizontal navigation
- `nav-vertical` - Vertical navigation
- `nav-expand` - Expandable navigation

### Style Classes

- `nav-dark` - Dark theme navigation
- `nav-light` - Light theme navigation
- `nav-compact` - Compact navigation
- `nav-large` - Large navigation

### Position Classes

- `nav-top` - Top navigation
- `nav-bottom` - Bottom navigation
- `nav-left` - Left navigation
- `nav-right` - Right navigation

## Navigation Types

### Horizontal Navigation

```python
nav = render_navigation(
    items=[
        {"text": "Home", "url": "/", "icon": "home"},
        {"text": "Products", "url": "/products/", "icon": "box"},
        {"text": "Services", "url": "/services/", "icon": "wrench"},
        {"text": "Contact", "url": "/contact/", "icon": "mail"}
    ],
    class="nav nav-horizontal"
)
```

### Vertical Navigation

```python
nav = render_navigation(
    items=[
        {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard"},
        {"text": "Users", "url": "/users/", "icon": "users"},
        {"text": "Settings", "url": "/settings/", "icon": "cog"},
        {"text": "Reports", "url": "/reports/", "icon": "chart"}
    ],
    class="nav nav-vertical"
)
```

### Breadcrumb Navigation

```python
breadcrumb_items = [
    {"text": "Home", "url": "/"},
    {"text": "Products", "url": "/products/"},
    {"text": "Electronics", "url": "/products/electronics/"},
    {"text": "Smartphones", "url": None, "active": True}
]

breadcrumb = render_navigation(
    breadcrumb_items,
    class="breadcrumb"
)
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_navigation items=navigation_items class="nav
nav-horizontal" %}
```

## Advanced Examples

### Navigation with Dropdowns

```python
def create_dropdown_nav():
    items = [
        {"text": "Home", "url": "/", "icon": "home"},
        {
            "text": "Products",
            "url": "#",
            "icon": "box",
            "dropdown": [
                {"text": "Electronics", "url": "/products/electronics/"},
                {"text": "Clothing", "url": "/products/clothing/"},
                {"text": "Books", "url": "/products/books/"}
            ]
        },
        {"text": "About", "url": "/about/", "icon": "info"}
    ]
    return render_navigation(items, class="nav nav-horizontal")

nav = create_dropdown_nav()
```

### Responsive Navigation

```python
nav = render_navigation(
    items=[
        {"text": "Home", "url": "/", "icon": "home"},
        {"text": "Products", "url": "/products/", "icon": "box"},
        {"text": "Services", "url": "/services/", "icon": "wrench"},
        {"text": "Contact", "url": "/contact/", "icon": "mail"}
    ],
    class="nav nav-horizontal nav-responsive",
    data_role="navigation"
)
```

### Navigation with Badges

```python
def create_nav_with_badges():
    items = [
        {"text": "Home", "url": "/", "icon": "home"},
        {"text": "Messages", "url": "/messages/", "icon": "mail", "badge": "5"},
        {"text": "Notifications", "url": "/notifications/", "icon": "bell", "badge": "12"},
        {"text": "Settings", "url": "/settings/", "icon": "cog"}
    ]
    return render_navigation(items, class="nav nav-horizontal")

nav = create_nav_with_badges()
```

### Conditional Navigation

```python
def get_navigation_items(user):
    base_items = [
        {"text": "Home", "url": "/", "icon": "home"},
        {"text": "About", "url": "/about/", "icon": "info"}
    ]

    if user.is_authenticated:
        base_items.extend([
            {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard"},
            {"text": "Profile", "url": "/profile/", "icon": "user"},
            {"text": "Logout", "url": "/logout/", "icon": "exit"}
        ])
    else:
        base_items.extend([
            {"text": "Login", "url": "/login/", "icon": "enter"},
            {"text": "Register", "url": "/register/", "icon": "user-plus"}
        ])

    return render_navigation(base_items, class="nav nav-horizontal")

nav = get_navigation_items(request.user)
```

## Best Practices

1. **Use descriptive text**: Make navigation labels clear and descriptive
2. **Include icons**: Use MetroUI icons to improve visual recognition
3. **Highlight active state**: Always indicate the current page
4. **Keep it simple**: Don't overload navigation with too many items
5. **Make it responsive**: Ensure navigation works on all screen sizes
6. **Use consistent styling**: Apply consistent classes across your application

## Related Components

- [Menus](menus.md) - For dropdown and context menus
- [Breadcrumbs](breadcrumbs.md) - For breadcrumb navigation
- [Sidebars](sidebars.md) - For sidebar navigation
- [Tabs](tabs.md) - For tabbed navigation


## metroui5_navigation

```python
render_navigation([{'text': 'One', 'href': '/one'}])
```

Empty or invalid: `render_navigation([{'text': 'One', 'href': '/one'}])` returns `<ul class="navigation" data-role="navigation"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="navigation" data-role="navigation"></ul>`.

```django
{% metroui5_navigation items %}
```
