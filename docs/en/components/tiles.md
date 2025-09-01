# Tiles

Component for creating information tiles with title, content, and icon.

## Basic Usage

### Simple Tile

```python
from metroui5.components import render_tile

# Basic tile
tile = render_tile("Title", "Content")
```

### Tile with Color and Size

```python
# Tile with color and size
tile = render_tile(
    title="Users",
    content="1,234",
    color="blue",
    size="medium"
)
```

### Tile with Icon

```python
# Tile with icon
tile = render_tile(
    title="Orders",
    content="567",
    color="green",
    size="large",
    icon="cart"
)
```

## Parameters

### `title` (required)

Tile title.

```python
tile = render_tile("Tile Title")
```

### `content` (optional)

Tile content. If not specified, content is not displayed.

```python
tile = render_tile("Title", "Content")
```

### `size` (optional)

Tile size. Available values:

- `"small"` - small
- `"medium"` (default) - medium
- `"large"` - large

```python
tile = render_tile("Title", size="large")
```

### `color` (optional)

Tile color. Available values:

- `"blue"` (default) - blue
- `"green"` - green
- `"orange"` - orange
- `"red"` - red
- `"purple"` - purple
- `"yellow"` - yellow
- `"cyan"` - cyan
- `"gray"` - gray

```python
tile = render_tile("Title", color="green")
```

### `icon` (optional)

Icon for the tile (MetroUI icon name).

```python
tile = render_tile("Title", icon="users")
```

### `**attrs` (optional)

Additional HTML attributes.

```python
tile = render_tile(
    "Title",
    **{"class": "custom-tile", "id": "myTile"}
)
```

## Usage Examples

### In Views

```python
from metroui5.components import render_tile


def dashboard(request):
    context = {
        'stats_tiles': [
            render_tile(
                title="Users",
                content="1,234",
                color="blue",
                size="small",
                icon="users"
            ),
            render_tile(
                title="Orders",
                content="567",
                color="green",
                size="small",
                icon="cart"
            ),
            render_tile(
                title="Revenue",
                content="$12,345",
                color="orange",
                size="small",
                icon="dollar"
            ),
            render_tile(
                title="Products",
                content="89",
                color="red",
                size="small",
                icon="package"
            )
        ]
    }
    return render(request, 'dashboard.html', context)
```

### In Templates

```html
{% extends 'base.html' %} {% block content %}
<div class="row">
	{% for tile in stats_tiles %}
	<div class="cell-md-3">{{ tile|safe }}</div>
	{% endfor %}
</div>
{% endblock %}
```

### Tiles with Different Sizes

```python
def size_examples_view(request):
    context = {
        'size_tiles': [
            render_tile("Small", "Small content", size="small", color="blue"),
            render_tile("Medium", "Medium content", size="medium", color="green"),
            render_tile("Large", "Large content", size="large", color="orange"),
        ]
    }
    return render(request, 'size_examples.html', context)
```

### Color Variations

```python
def color_examples_view(request):
    colors = ["blue", "green", "orange", "red", "purple", "yellow", "cyan", "gray"]

    context = {
        'color_tiles': [
            render_tile(f"{color.title()}", f"{color.title()} tile", color=color)
            for color in colors
        ]
    }
    return render(request, 'color_examples.html', context)
```

### Icon Variations

```python
def icon_examples_view(request):
    icons = ["users", "cart", "dollar", "package", "star", "heart", "home", "cog"]

    context = {
        'icon_tiles': [
            render_tile(f"{icon.title()}", f"{icon.title()} tile", icon=icon)
            for icon in icons
        ]
    }
    return render(request, 'icon_examples.html', context)
```

## Advanced Examples

### Dynamic Tile Generation

```python
def dynamic_tiles_view(request):
    # Generate tiles based on user permissions
    tiles = []

    if request.user.is_staff:
        tiles.append(render_tile(
            title="Admin Panel",
            content="Access to administrative functions",
            color="red",
            icon="cog"
        ))

    if request.user.has_perm('app.view_reports'):
        tiles.append(render_tile(
            title="Reports",
            content="View and generate reports",
            color="blue",
            icon="chart"
        ))

    if request.user.has_perm('app.manage_users'):
        tiles.append(render_tile(
            title="User Management",
            content="Manage user accounts and permissions",
            color="green",
            icon="users"
        ))

    context = {'tiles': tiles}
    return render(request, 'dynamic_tiles.html', context)
```

### Conditional Tile Content

```python
def conditional_tiles_view(request):
    user = request.user

    # Base tile
    base_tile = render_tile(
        f"Welcome, {user.first_name}!",
        "Here's your personalized dashboard."
    )

    # Conditional tiles based on user status
    conditional_tiles = []

    if not user.email_verified:
        conditional_tiles.append(render_tile(
            "Email Verification Required",
            "Please verify your email address to access all features.",
            color="warning",
            icon="mail"
        ))

    if user.is_new:
        conditional_tiles.append(render_tile(
            "Getting Started",
            "Complete your profile setup to get the most out of our platform.",
            color="info",
            icon="user"
        ))

    if user.last_login and user.last_login.date() < timezone.now().date() - timedelta(days=7):
        conditional_tiles.append(render_tile(
            "Welcome Back!",
            "We've missed you. Here's what's new since your last visit.",
            color="success",
            icon="star"
        ))

    context = {
        'base_tile': base_tile,
        'conditional_tiles': conditional_tiles
    }
    return render(request, 'conditional_tiles.html', context)
```

### Interactive Tiles

```python
def interactive_tiles_view(request):
    # Tiles with interactive elements
    interactive_tiles = [
        render_tile(
            "Settings",
            "Click to access your account settings",
            color="blue",
            icon="cog",
            **{"onclick": "openSettings()", "class": "clickable-tile"}
        ),
        render_tile(
            "Notifications",
            "Manage your notification preferences",
            color="green",
            icon="bell",
            **{"onclick": "openNotifications()", "class": "clickable-tile"}
        ),
        render_tile(
            "Help",
            "Get help and support",
            color="orange",
            icon="question",
            **{"onclick": "openHelp()", "class": "clickable-tile"}
        )
    ]

    context = {'interactive_tiles': interactive_tiles}
    return render(request, 'interactive_tiles.html', context)
```

## Tile Layouts

### Grid Layout

```html
<!-- Grid layout for tiles -->
<div class="row">
	<div class="cell-md-3">{{ tile1|safe }}</div>
	<div class="cell-md-3">{{ tile2|safe }}</div>
	<div class="cell-md-3">{{ tile3|safe }}</div>
	<div class="cell-md-3">{{ tile4|safe }}</div>
</div>
```

### Responsive Layout

```html
<!-- Responsive tile layout -->
<div class="row">
	<div class="cell-sm-12 cell-md-6 cell-lg-4">{{ responsive_tile1|safe }}</div>
	<div class="cell-sm-12 cell-md-6 cell-lg-4">{{ responsive_tile2|safe }}</div>
	<div class="cell-sm-12 cell-md-12 cell-lg-4">{{ responsive_tile3|safe }}</div>
</div>
```

### Masonry Layout

```html
<!-- Masonry-style layout -->
<div class="masonry-grid" data-role="masonry">
	<div class="masonry-item">{{ tall_tile|safe }}</div>
	<div class="masonry-item">{{ wide_tile|safe }}</div>
	<div class="masonry-item">{{ small_tile|safe }}</div>
</div>
```

## Customization

### Custom CSS Classes

```css
/* Custom tile styles */
.custom-tile {
	border-radius: 15px;
	box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
	transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.custom-tile:hover {
	transform: translateY(-5px);
	box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
}

.clickable-tile {
	cursor: pointer;
	transition: all 0.3s ease;
}

.clickable-tile:hover {
	transform: scale(1.05);
	box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

/* Custom color variations */
.tile-custom-blue {
	background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
	color: white;
}

.tile-custom-green {
	background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
	color: white;
}

.tile-custom-orange {
	background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
	color: white;
}
```

### Custom JavaScript

```javascript
// Add custom tile interactions
document.addEventListener("DOMContentLoaded", function () {
	// Add click handlers to clickable tiles
	document.querySelectorAll(".clickable-tile").forEach((tile) => {
		tile.addEventListener("click", function () {
			// Add click effect
			this.style.transform = "scale(0.98)";
			setTimeout(() => {
				this.style.transform = "scale(1)";
			}, 150);
		});
	});

	// Add hover effects
	document.querySelectorAll(".tile").forEach((tile) => {
		tile.addEventListener("mouseenter", function () {
			this.style.boxShadow = "0 8px 25px rgba(0, 0, 0, 0.15)";
		});

		tile.addEventListener("mouseleave", function () {
			this.style.boxShadow = "0 4px 15px rgba(0, 0, 0, 0.1)";
		});
	});

	// Add tile counter animation
	document.querySelectorAll(".tile[data-counter]").forEach((tile) => {
		const counter = tile.querySelector(".tile-content");
		if (counter) {
			const targetValue = parseInt(counter.textContent);
			animateCounter(counter, 0, targetValue, 2000);
		}
	});
});

function animateCounter(element, start, end, duration) {
	const startTime = performance.now();

	function updateCounter(currentTime) {
		const elapsed = currentTime - startTime;
		const progress = Math.min(elapsed / duration, 1);

		const current = Math.floor(start + (end - start) * progress);
		element.textContent = current.toLocaleString();

		if (progress < 1) {
			requestAnimationFrame(updateCounter);
		}
	}

	requestAnimationFrame(updateCounter);
}
```

## Best Practices

### 1. Consistent Tile Structure

```python
# Define consistent tile structure
def create_consistent_tile(title, content, color="blue", size="medium", **kwargs):
    """Create a tile with consistent styling and structure."""

    default_attrs = {
        'class': 'tile tile-standard',
        'data-tile-type': 'standard'
    }

    # Merge with custom attributes
    default_attrs.update(kwargs)

    return render_tile(
        title=title,
        content=content,
        color=color,
        size=size,
        **default_attrs
    )

# Usage
def dashboard_view(request):
    context = {
        'welcome_tile': create_consistent_tile(
            "Welcome Back!",
            "We're glad to see you again.",
            color="blue"
        ),
        'stats_tile': create_consistent_tile(
            "Statistics",
            "Your activity summary for today.",
            color="green"
        )
    }
    return render(request, 'dashboard.html', context)
```

### 2. Performance Optimization

```python
# Cache expensive tile content
from django.core.cache import cache

def get_cached_tile_content(user_id, tile_type):
    """Get cached tile content to improve performance."""

    cache_key = f"tile_content_{user_id}_{tile_type}"
    content = cache.get(cache_key)

    if not content:
        # Generate expensive content
        content = generate_expensive_content(user_id, tile_type)

        # Cache for 10 minutes
        cache.set(cache_key, content, 600)

    return content

def optimized_tiles_view(request):
    user_id = request.user.id

    # Get cached content
    stats_content = get_cached_tile_content(user_id, 'stats')
    activity_content = get_cached_tile_content(user_id, 'activity')

    context = {
        'stats_tile': render_tile(
            title="Statistics",
            content=stats_content,
            color="blue"
        ),
        'activity_tile': render_tile(
            title="Recent Activity",
            content=activity_content,
            color="green"
        )
    }
    return render(request, 'optimized_tiles.html', context)
```

### 3. Accessibility

```python
# Create accessible tiles
def create_accessible_tile(title, content, **kwargs):
    """Create a tile with proper accessibility attributes."""

    # Add accessibility attributes
    accessibility_attrs = {
        'role': 'article',
        'aria-labelledby': f"tile-{kwargs.get('id', 'default')}-title",
        'aria-describedby': f"tile-{kwargs.get('id', 'default')}-content"
    }

    # Merge with existing attributes
    if 'attrs' not in kwargs:
        kwargs['attrs'] = {}
    kwargs['attrs'].update(accessibility_attrs)

    return render_tile(
        title=title,
        content=content,
        **kwargs
    )

# Usage
def accessible_tiles_view(request):
    context = {
        'accessible_tile': create_accessible_tile(
            "Important Information",
            "This tile is designed with accessibility in mind.",
            id="important-info"
        )
    }
    return render(request, 'accessible_tiles.html', context)
```

## Troubleshooting

### Common Issues

1. **Tile not displaying**: Check if `render_tile` is imported and `|safe` filter is used
2. **Styles not applying**: Ensure MetroUI5 CSS is loaded and no conflicting CSS rules
3. **Icons not showing**: Check if the icon name is correct and MetroUI icons CSS is loaded
4. **Colors not working**: Verify that the color values are valid and CSS is properly loaded

### Debug Mode

```python
# Enable debug mode for tile issues
METROUI5 = {
    'tile_debug': True,  # Enable tile debugging
    'tile_logging': True,  # Log tile rendering
}
```

## Related Documentation

- [Components](components.md) - Component rendering functions
- [Template Tags](templatetags.md) - Django template integration
- [Icons](icons.md) - Icon usage in tiles
- [Cards](cards.md) - Alternative to tiles for content display
- [CSS Utilities](css.md) - CSS class management
