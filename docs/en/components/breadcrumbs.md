# Breadcrumbs

Component for creating navigation breadcrumbs that show the current page location within a navigational hierarchy.

## Basic Usage

### Simple Breadcrumbs

```python
from metroui5.components import render_breadcrumb

# Basic breadcrumbs
breadcrumb_items = [
    {"text": "Home", "url": "/"},
    {"text": "Products", "url": "/products/"},
    {"text": "Laptops", "url": "/products/laptops/"},
    {"text": "Gaming Laptops"}  # Current page (no URL)
]

breadcrumb_html = render_breadcrumb(items=breadcrumb_items)
```

### Breadcrumbs with Icons

```python
# Breadcrumbs with icons
breadcrumb_items = [
    {"text": "Home", "url": "/", "icon": "home"},
    {"text": "Dashboard", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Users", "url": "/users/", "icon": "users"},
    {"text": "Profile", "icon": "user"}
]

breadcrumb_html = render_breadcrumb(items=breadcrumb_items, show_icons=True)
```

### Custom Breadcrumbs

```python
# Custom breadcrumbs with separator
breadcrumb_html = render_breadcrumb(
    items=breadcrumb_items,
    separator="→",
    class="breadcrumb-custom",
    id="page-breadcrumb"
)
```

## Rendered Output

### Basic Breadcrumbs

```html
<!-- Input -->
render_breadcrumb(items=[{"text": "Home", "url": "/"}, {"text": "Products",
"url": "/products/"}, {"text": "Laptops"}])

<!-- Output -->
<nav class="breadcrumb" aria-label="breadcrumb">
	<ol class="breadcrumb-list">
		<li class="breadcrumb-item">
			<a href="/" class="breadcrumb-link">Home</a>
		</li>
		<li class="breadcrumb-separator">/</li>
		<li class="breadcrumb-item">
			<a href="/products/" class="breadcrumb-link">Products</a>
		</li>
		<li class="breadcrumb-separator">/</li>
		<li class="breadcrumb-item active" aria-current="page">
			<span class="breadcrumb-text">Laptops</span>
		</li>
	</ol>
</nav>
```

### Breadcrumbs with Icons

```html
<!-- Input -->
render_breadcrumb(items=[{"text": "Home", "url": "/", "icon": "home"}, {"text":
"Profile", "icon": "user"}], show_icons=True)

<!-- Output -->
<nav class="breadcrumb breadcrumb-with-icons" aria-label="breadcrumb">
	<ol class="breadcrumb-list">
		<li class="breadcrumb-item">
			<a href="/" class="breadcrumb-link">
				<span class="mif-home"></span>
				Home
			</a>
		</li>
		<li class="breadcrumb-separator">/</li>
		<li class="breadcrumb-item active" aria-current="page">
			<span class="breadcrumb-text">
				<span class="mif-user"></span>
				Profile
			</span>
		</li>
	</ol>
</nav>
```

### Breadcrumbs with Custom Separator

```html
<!-- Input -->
render_breadcrumb(items=breadcrumb_items, separator="→")

<!-- Output -->
<nav class="breadcrumb" aria-label="breadcrumb">
	<ol class="breadcrumb-list">
		<li class="breadcrumb-item">
			<a href="/" class="breadcrumb-link">Home</a>
		</li>
		<li class="breadcrumb-separator">→</li>
		<li class="breadcrumb-item active" aria-current="page">
			<span class="breadcrumb-text">Profile</span>
		</li>
	</ol>
</nav>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic breadcrumbs -->
{% metroui5_breadcrumb items=breadcrumb_items %}

<!-- Breadcrumbs with icons -->
{% metroui5_breadcrumb items=breadcrumb_items show_icons=True %}

<!-- Custom breadcrumbs -->
{% metroui5_breadcrumb items=breadcrumb_items separator="→"
class="breadcrumb-custom" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_breadcrumb

def product_detail_view(request, category_slug, product_slug):
    # Build breadcrumb trail
    breadcrumb_items = [
        {"text": "Home", "url": "/", "icon": "home"},
        {"text": "Products", "url": "/products/", "icon": "grid"},
        {"text": category.name, "url": f"/products/{category_slug}/", "icon": "folder"},
        {"text": product.name, "icon": "box"}  # Current page
    ]

    breadcrumb_html = render_breadcrumb(
        items=breadcrumb_items,
        show_icons=True,
        class="breadcrumb-product"
    )

    context = {
        'breadcrumb_html': breadcrumb_html,
        'breadcrumb_items': breadcrumb_items,
        'product': product
    }
    return render(request, 'product_detail.html', context)
```

```html
<!-- product_detail.html -->
{% load metroui5 %} {% block content %}
<!-- Direct HTML output -->
{{ breadcrumb_html|safe }}

<!-- Or use template tag -->
{% metroui5_breadcrumb items=breadcrumb_items show_icons=True %}

<div class="product-details">
	<h1>{{ product.name }}</h1>
	<!-- Product content -->
</div>
{% endblock %}
```

## Parameters

### `items` (required)

List of breadcrumb items representing the navigation path.

**Format**:

```python
items = [
    {
        "text": "Page Name",
        "url": "/path/",       # Optional (omit for current page)
        "icon": "icon-name",   # Optional
        "title": "Tooltip"     # Optional
    }
]
```

### `show_icons` (optional)

Whether to display icons in breadcrumb items.

**Default**: `False`

**Example**:

```python
breadcrumb_html = render_breadcrumb(items=items, show_icons=True)
```

### `separator` (optional)

Character or string to use as separator between items.

**Default**: `"/"`

**Example**:

```python
breadcrumb_html = render_breadcrumb(items=items, separator="→")
```

### `max_items` (optional)

Maximum number of items to display (with ellipsis for overflow).

**Example**:

```python
breadcrumb_html = render_breadcrumb(items=items, max_items=4)
```

### `id` (optional)

Unique identifier for the breadcrumb element.

**Example**:

```python
breadcrumb_html = render_breadcrumb(items=items, id="page-breadcrumb")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
breadcrumb_html = render_breadcrumb(items=items, class="breadcrumb-custom")
```

## Advanced Examples

### Dynamic Breadcrumbs

```python
def create_dynamic_breadcrumb(request, current_object=None):
    """Create breadcrumbs based on current URL and object."""

    breadcrumb_items = [{"text": "Home", "url": "/", "icon": "home"}]

    # Build breadcrumbs from URL path
    path_parts = request.path.strip('/').split('/')
    current_path = ""

    for part in path_parts[:-1]:  # Exclude current page
        current_path += f"/{part}"
        breadcrumb_items.append({
            "text": part.replace('-', ' ').title(),
            "url": current_path + "/"
        })

    # Add current page
    if current_object:
        breadcrumb_items.append({
            "text": str(current_object),
            "icon": get_object_icon(current_object)
        })

    return render_breadcrumb(
        items=breadcrumb_items,
        show_icons=True,
        class="breadcrumb-dynamic"
    )
```

### Hierarchical Breadcrumbs

```python
def create_hierarchical_breadcrumb(category):
    """Create breadcrumbs for hierarchical categories."""

    breadcrumb_items = [{"text": "Home", "url": "/", "icon": "home"}]

    # Build hierarchy from category parents
    ancestors = []
    current = category
    while current.parent:
        ancestors.append(current.parent)
        current = current.parent

    # Reverse to get root-to-leaf order
    ancestors.reverse()

    for ancestor in ancestors:
        breadcrumb_items.append({
            "text": ancestor.name,
            "url": ancestor.get_absolute_url(),
            "icon": "folder"
        })

    # Add current category
    breadcrumb_items.append({
        "text": category.name,
        "icon": "folder-open"
    })

    return render_breadcrumb(
        items=breadcrumb_items,
        show_icons=True,
        separator="→"
    )
```

### Truncated Breadcrumbs

```python
def create_truncated_breadcrumb(items, max_display=4):
    """Create breadcrumbs with ellipsis for long paths."""

    if len(items) <= max_display:
        return render_breadcrumb(items=items)

    # Keep first item, last items, and add ellipsis
    truncated_items = [items[0]]

    if len(items) > max_display:
        truncated_items.append({
            "text": "...",
            "class": "breadcrumb-ellipsis",
            "title": f"Hidden {len(items) - max_display + 1} levels"
        })

    # Add last few items
    truncated_items.extend(items[-(max_display-2):])

    return render_breadcrumb(
        items=truncated_items,
        class="breadcrumb-truncated"
    )
```

### Contextual Breadcrumbs

```python
def create_contextual_breadcrumb(request, context_type="default"):
    """Create breadcrumbs based on context type."""

    breadcrumb_configs = {
        "admin": [
            {"text": "Admin", "url": "/admin/", "icon": "cog"},
            {"text": "Dashboard", "url": "/admin/dashboard/", "icon": "dashboard"}
        ],
        "user": [
            {"text": "My Account", "url": "/account/", "icon": "user"},
            {"text": "Profile", "url": "/account/profile/", "icon": "id-card"}
        ],
        "default": [
            {"text": "Home", "url": "/", "icon": "home"}
        ]
    }

    base_items = breadcrumb_configs.get(context_type, breadcrumb_configs["default"])

    # Add current page info
    current_page = get_current_page_info(request)
    if current_page:
        base_items.append(current_page)

    return render_breadcrumb(
        items=base_items,
        show_icons=True,
        class=f"breadcrumb-{context_type}"
    )
```

## Styling

### CSS Classes

#### Base Classes

- `breadcrumb` - Base breadcrumb container
- `breadcrumb-primary` - Primary breadcrumb style
- `breadcrumb-secondary` - Secondary breadcrumb style

#### Feature Classes

- `breadcrumb-with-icons` - Breadcrumbs with icon support
- `breadcrumb-truncated` - Truncated breadcrumbs with ellipsis
- `breadcrumb-compact` - Compact breadcrumb style

#### Context Classes

- `breadcrumb-admin` - Admin context breadcrumbs
- `breadcrumb-user` - User context breadcrumbs
- `breadcrumb-product` - Product page breadcrumbs

### Custom Styling

```css
/* Custom breadcrumb styling */
.breadcrumb-custom {
	background: #f8f9fa;
	border: 1px solid #dee2e6;
	border-radius: 6px;
	padding: 12px 16px;
	margin-bottom: 20px;
}

.breadcrumb-custom .breadcrumb-list {
	display: flex;
	align-items: center;
	list-style: none;
	margin: 0;
	padding: 0;
	flex-wrap: wrap;
}

.breadcrumb-custom .breadcrumb-item {
	display: flex;
	align-items: center;
}

.breadcrumb-custom .breadcrumb-link {
	color: #007acc;
	text-decoration: none;
	padding: 4px 8px;
	border-radius: 4px;
	transition: all 0.3s ease;
	display: flex;
	align-items: center;
	gap: 6px;
}

.breadcrumb-custom .breadcrumb-link:hover {
	background: #e3f2fd;
	color: #0056b3;
}

.breadcrumb-custom .breadcrumb-item.active .breadcrumb-text {
	color: #495057;
	font-weight: 500;
	padding: 4px 8px;
	display: flex;
	align-items: center;
	gap: 6px;
}

.breadcrumb-custom .breadcrumb-separator {
	color: #6c757d;
	margin: 0 8px;
	font-size: 14px;
}

/* Responsive breadcrumbs */
@media (max-width: 768px) {
	.breadcrumb-custom .breadcrumb-list {
		flex-direction: column;
		align-items: flex-start;
	}

	.breadcrumb-custom .breadcrumb-separator {
		display: none;
	}

	.breadcrumb-custom .breadcrumb-item {
		margin-bottom: 4px;
	}
}

/* Truncated breadcrumbs */
.breadcrumb-ellipsis {
	color: #6c757d;
	cursor: help;
	padding: 4px 8px;
}

.breadcrumb-ellipsis:hover {
	background: #f8f9fa;
	border-radius: 4px;
}
```

## JavaScript Integration

### Breadcrumb Navigation

```javascript
// Handle breadcrumb clicks with analytics
$(".breadcrumb").on("click", ".breadcrumb-link", function (e) {
	const link = $(this);
	const breadcrumbText = link.text().trim();
	const url = link.attr("href");

	// Track breadcrumb navigation
	trackBreadcrumbClick(breadcrumbText, url);

	// Allow normal navigation
	return true;
});

function trackBreadcrumbClick(text, url) {
	// Analytics tracking
	if (typeof gtag !== "undefined") {
		gtag("event", "breadcrumb_click", {
			breadcrumb_text: text,
			destination_url: url,
		});
	}
}
```

### Dynamic Breadcrumb Updates

```javascript
// Update breadcrumbs dynamically
function updateBreadcrumbs(newItems) {
	const breadcrumb = $(".breadcrumb");
	const list = breadcrumb.find(".breadcrumb-list");

	list.empty();

	newItems.forEach((item, index) => {
		// Add breadcrumb item
		const itemElement = createBreadcrumbItem(
			item,
			index === newItems.length - 1
		);
		list.append(itemElement);

		// Add separator (except for last item)
		if (index < newItems.length - 1) {
			list.append('<li class="breadcrumb-separator">/</li>');
		}
	});
}

function createBreadcrumbItem(item, isLast) {
	const icon = item.icon ? `<span class="mif-${item.icon}"></span>` : "";

	if (isLast || !item.url) {
		return `
			<li class="breadcrumb-item active" aria-current="page">
				<span class="breadcrumb-text">${icon}${item.text}</span>
			</li>
		`;
	} else {
		return `
			<li class="breadcrumb-item">
				<a href="${item.url}" class="breadcrumb-link">${icon}${item.text}</a>
			</li>
		`;
	}
}
```

### Responsive Breadcrumbs

```javascript
// Handle responsive breadcrumb behavior
function handleResponsiveBreadcrumbs() {
	const breadcrumb = $(".breadcrumb");
	const items = breadcrumb.find(".breadcrumb-item");
	const windowWidth = $(window).width();

	if (windowWidth < 768) {
		// Mobile: Show only last few items
		showMobileBreadcrumbs(items);
	} else {
		// Desktop: Show all items
		items.show();
		breadcrumb.find(".breadcrumb-mobile-toggle").remove();
	}
}

function showMobileBreadcrumbs(items) {
	const maxMobileItems = 2;

	if (items.length <= maxMobileItems) {
		return; // Show all if few items
	}

	// Hide middle items
	items.slice(1, -1).hide();

	// Add toggle button
	const toggleButton = `
		<li class="breadcrumb-mobile-toggle">
			<button class="breadcrumb-toggle-btn" onclick="toggleHiddenBreadcrumbs()">
				<span class="mif-more"></span>
			</button>
		</li>
	`;

	items.eq(0).after(toggleButton);
}

function toggleHiddenBreadcrumbs() {
	const hiddenItems = $(".breadcrumb-item:hidden");
	hiddenItems.toggle();
}

// Handle window resize
$(window).on("resize", handleResponsiveBreadcrumbs);
$(document).ready(handleResponsiveBreadcrumbs);
```

## Best Practices

### 1. Consistent Structure

```python
# Use consistent breadcrumb structure
def build_breadcrumb_path(request, current_object=None):
	"""Build consistent breadcrumb structure."""
	items = [{"text": "Home", "url": "/", "icon": "home"}]

	# Add path-based items
	path_items = extract_path_items(request.path)
	items.extend(path_items)

	# Add current object
	if current_object:
		items.append({
			"text": str(current_object),
			"icon": get_model_icon(current_object._meta.model)
		})

	return items
```

### 2. SEO Optimization

```python
# Create SEO-friendly breadcrumbs
def create_seo_breadcrumb(items):
	"""Create breadcrumbs with structured data."""
	breadcrumb_html = render_breadcrumb(items=items)

	# Add JSON-LD structured data
	structured_data = {
		"@context": "https://schema.org",
		"@type": "BreadcrumbList",
		"itemListElement": [
			{
				"@type": "ListItem",
				"position": i + 1,
				"name": item["text"],
				"item": request.build_absolute_uri(item.get("url", ""))
			}
			for i, item in enumerate(items) if item.get("url")
		]
	}

	return breadcrumb_html, structured_data
```

### 3. Accessibility

```python
# Ensure breadcrumb accessibility
def create_accessible_breadcrumb(items):
	return render_breadcrumb(
		items=items,
		**{
			"aria-label": "breadcrumb navigation",
			"role": "navigation"
		}
	)
```

## Related Components

- [Navigation](navigation.md) - For main navigation systems
- [Menus](menus.md) - For dropdown navigation menus
- [Icons](icons.md) - For breadcrumb icons
- [Links](links.md) - For breadcrumb link styling
