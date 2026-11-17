# Badges

MetroUI5 Django provides a flexible badge component system for displaying status indicators, counts, labels, and small pieces of information.

## Basic Usage

```python
from metroui5.components import render_badge

# Simple badge
badge_html = render_badge("New")
```

## Parameters

### `render_badge(content, badge_type="default", **attrs)`

- **content** (str): Badge text content
- **badge_type** (str): Badge type/style (default, primary, success, warning, danger, info)
- **attrs** (dict): Additional HTML attributes

## Examples

### Basic Badges

```python
from metroui5.components import render_badge

# Default badge
badge = render_badge("Default")

# Primary badge
badge = render_badge("Primary", badge_type="primary")

# Success badge
badge = render_badge("Success", badge_type="success")

# Warning badge
badge = render_badge("Warning", badge_type="warning")

# Danger badge
badge = render_badge("Danger", badge_type="danger")

# Info badge
badge = render_badge("Info", badge_type="info")
```

### Badge with Custom Attributes

```python
badge = render_badge(
    "Custom",
    badge_type="primary",
    id="custom-badge",
    class="badge-large"
)
```

### Badge with Icons

```python
def create_icon_badge(content, badge_type="default", icon=None):
    """Create badge with icon."""

    if icon:
        content = f'<span class="mif-{icon}"></span> {content}'

    return render_badge(content, badge_type)

# Usage
icon_badge = create_icon_badge("5", "danger", "mail")
```

## MetroUI Badge Classes

MetroUI5 provides several CSS classes for badge styling:

### Type Classes

- `badge` - Base badge class
- `badge-primary` - Primary badge style
- `badge-secondary` - Secondary badge style
- `badge-success` - Success badge style (green)
- `badge-warning` - Warning badge style (yellow)
- `badge-danger` - Danger badge style (red)
- `badge-info` - Info badge style (blue)
- `badge-light` - Light badge style
- `badge-dark` - Dark badge style

### Size Classes

- `badge-small` - Small badge
- `badge-large` - Large badge
- `badge-mini` - Mini badge

### Style Classes

- `badge-rounded` - Rounded badge
- `badge-pill` - Pill-shaped badge
- `badge-outline` - Outline badge
- `badge-glow` - Glowing badge

## Badge Types

### Status Badges

```python
def create_status_badge(status):
    """Create status badge based on status value."""

    status_map = {
        "active": ("Active", "success"),
        "inactive": ("Inactive", "default"),
        "pending": ("Pending", "warning"),
        "error": ("Error", "danger"),
        "completed": ("Completed", "success"),
        "cancelled": ("Cancelled", "danger"),
        "processing": ("Processing", "info")
    }

    text, badge_type = status_map.get(status.lower(), ("Unknown", "default"))
    return render_badge(text, badge_type)

# Usage
active_badge = create_status_badge("active")
pending_badge = create_status_badge("pending")
error_badge = create_status_badge("error")
```

### Count Badges

```python
def create_count_badge(count, max_count=None, badge_type="primary"):
    """Create count badge with optional max limit."""

    if max_count and count > max_count:
        display_count = f"{max_count}+"
        badge_type = "warning"
    else:
        display_count = str(count)

    return render_badge(display_count, badge_type)

# Usage
message_count = create_count_badge(5)
notification_count = create_count_badge(12, max_count=10)
```

### Priority Badges

```python
def create_priority_badge(priority):
    """Create priority badge."""

    priority_map = {
        "high": ("High", "danger"),
        "medium": ("Medium", "warning"),
        "low": ("Low", "info"),
        "critical": ("Critical", "danger"),
        "normal": ("Normal", "default")
    }

    text, badge_type = priority_map.get(priority.lower(), ("Unknown", "default"))
    return render_badge(text, badge_type)

# Usage
high_priority = create_priority_badge("high")
critical_priority = create_priority_badge("critical")
```

### Category Badges

```python
def create_category_badge(category, color_map=None):
    """Create category badge with custom color mapping."""

    if color_map is None:
        color_map = {
            "frontend": "primary",
            "backend": "success",
            "database": "warning",
            "devops": "info",
            "design": "danger"
        }

    badge_type = color_map.get(category.lower(), "default")
    return render_badge(category.title(), badge_type)

# Usage
frontend_badge = create_category_badge("frontend")
backend_badge = create_category_badge("backend")
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_badge "New" badge_type="primary" %}
```

## Advanced Examples

### Badge with Tooltip

```python
def create_tooltip_badge(content, badge_type="default", tooltip=""):
    """Create badge with tooltip."""

    return render_badge(
        content,
        badge_type,
        class="badge-tooltip",
        data_tooltip=tooltip,
        data_tooltip_position="top"
    )

# Usage
tooltip_badge = create_tooltip_badge(
    "Beta",
    "warning",
    "This feature is in beta testing"
)
```

### Animated Badge

```python
def create_animated_badge(content, badge_type="default", animation="pulse"):
    """Create badge with animation."""

    return render_badge(
        content,
        badge_type,
        class=f"badge badge-{animation}"
    )

# Usage
pulse_badge = create_animated_badge("Live", "danger", "pulse")
```

### Badge with Close Button

```python
def create_dismissible_badge(content, badge_type="default", onclose=""):
    """Create badge with close button."""

    close_button = f'<button type="button" class="badge-close" onclick="{onclose}">&times;</button>'
    content_with_close = f"{content}{close_button}"

    return render_badge(
        content_with_close,
        badge_type,
        class="badge-dismissible"
    )

# Usage
dismissible_badge = create_dismissible_badge(
    "Dismissible",
    "info",
    "closeBadge(this)"
)
```

### Badge Group

```python
def create_badge_group(badges, separator=" "):
    """Create group of badges."""

    badge_htmls = []
    for badge in badges:
        if isinstance(badge, dict):
            badge_html = render_badge(
                badge['content'],
                badge.get('type', 'default'),
                **badge.get('attrs', {})
            )
        else:
            badge_html = render_badge(badge)
        badge_htmls.append(badge_html)

    return separator.join(badge_htmls)

# Usage
badge_group = create_badge_group([
    {"content": "Python", "type": "primary"},
    {"content": "Django", "type": "success"},
    {"content": "MetroUI5", "type": "info"}
])
```

### Conditional Badge

```python
def create_conditional_badge(condition, true_content, false_content, true_type="success", false_type="default"):
    """Create badge that changes based on condition."""

    if condition:
        return render_badge(true_content, true_type)
    else:
        return render_badge(false_content, false_type)

# Usage
online_badge = create_conditional_badge(
    user.is_online,
    "Online",
    "Offline",
    "success",
    "default"
)
```

### Badge with Progress

```python
def create_progress_badge(content, progress, badge_type="info"):
    """Create badge showing progress."""

    progress_html = f"""
    <div class="badge-progress">
        <span class="badge-content">{content}</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress}%"></div>
        </div>
    </div>
    """

    return render_badge(
        progress_html,
        badge_type,
        class="badge-progress-container"
    )

# Usage
progress_badge = create_progress_badge("Upload", 75, "primary")
```

### Badge in Navigation

```python
def create_nav_with_badges(nav_items):
    """Create navigation with badges."""

    nav_html = "<nav class='nav nav-horizontal'>"

    for item in nav_items:
        badge_html = ""
        if item.get('badge'):
            badge_html = render_badge(
                item['badge']['content'],
                item['badge'].get('type', 'primary')
            )

        nav_html += f"""
        <a href="{item['url']}" class="nav-item">
            <span class="mif-{item['icon']}"></span>
            {item['text']}
            {badge_html}
        </a>
        """

    nav_html += "</nav>"
    return nav_html

# Usage
nav_items = [
    {"text": "Home", "url": "/", "icon": "home"},
    {"text": "Messages", "url": "/messages/", "icon": "mail", "badge": {"content": "5", "type": "danger"}},
    {"text": "Notifications", "url": "/notifications/", "icon": "bell", "badge": {"content": "12", "type": "warning"}},
    {"text": "Settings", "url": "/settings/", "icon": "cog"}
]

nav_with_badges = create_nav_with_badges(nav_items)
```

### Badge in Cards

```python
def create_card_with_badge(title, content, badge_content, badge_type="primary"):
    """Create card with badge in header."""

    badge_html = render_badge(badge_content, badge_type)

    return f"""
    <div class="card">
        <div class="card-header">
            <h3>{title} {badge_html}</h3>
        </div>
        <div class="card-content">
            {content}
        </div>
    </div>
    """

# Usage
card_with_badge = create_card_with_badge(
    "Project Status",
    "Project is progressing well...",
    "Active",
    "success"
)
```

### Badge in Tables

```python
def create_table_with_badges(headers, rows_with_badges):
    """Create table with badge columns."""

    from metroui5.components import render_table

    # Process rows to include badge HTML
    processed_rows = []
    for row in rows_with_badges:
        processed_row = []
        for i, cell in enumerate(row):
            if isinstance(cell, dict) and 'badge' in cell:
                badge_html = render_badge(
                    cell['badge']['content'],
                    cell['badge'].get('type', 'default')
                )
                processed_row.append(badge_html)
            else:
                processed_row.append(cell)
        processed_rows.append(processed_row)

    return render_table(headers, processed_rows, class="table table-border")

# Usage
headers = ["Name", "Status", "Priority", "Category"]
rows_with_badges = [
    ["Task 1", {"badge": {"content": "Active", "type": "success"}},
     {"badge": {"content": "High", "type": "danger"}},
     {"badge": {"content": "Frontend", "type": "primary"}}],
    ["Task 2", {"badge": {"content": "Pending", "type": "warning"}},
     {"badge": {"content": "Medium", "type": "warning"}},
     {"badge": {"content": "Backend", "type": "success"}}]
]

table_with_badges = create_table_with_badges(headers, rows_with_badges)
```

## JavaScript Integration

### Dynamic Badge Updates

```javascript
// Update badge content
function updateBadge(badgeId, newContent, newType) {
	const badge = document.querySelector(`#${badgeId}`);
	if (badge) {
		badge.textContent = newContent;
		badge.className = `badge badge-${newType}`;
	}
}

// Animate badge count
function animateBadgeCount(badgeId, targetCount) {
	const badge = document.querySelector(`#${badgeId}`);
	if (badge) {
		const currentCount = parseInt(badge.textContent) || 0;
		const increment = targetCount > currentCount ? 1 : -1;

		const animate = () => {
			if (currentCount !== targetCount) {
				currentCount += increment;
				badge.textContent = currentCount;
				setTimeout(animate, 50);
			}
		};

		animate();
	}
}
```

### Badge Events

```javascript
// Handle badge clicks
document.querySelectorAll(".badge").forEach((badge) => {
	badge.addEventListener("click", function () {
		console.log("Badge clicked:", this.textContent);

		// Add click effect
		this.style.transform = "scale(1.1)";
		setTimeout(() => {
			this.style.transform = "scale(1)";
		}, 200);
	});
});

// Handle dismissible badges
document
	.querySelectorAll(".badge-dismissible .badge-close")
	.forEach((closeBtn) => {
		closeBtn.addEventListener("click", function () {
			const badge = this.parentElement;
			badge.style.opacity = "0";
			setTimeout(() => {
				badge.remove();
			}, 300);
		});
	});
```

### Badge Filtering

```javascript
// Filter elements by badge type
function filterByBadge(badgeType) {
	const elements = document.querySelectorAll(".badge");

	elements.forEach((element) => {
		if (
			badgeType === "all" ||
			element.classList.contains(`badge-${badgeType}`)
		) {
			element.style.display = "inline-block";
		} else {
			element.style.display = "none";
		}
	});
}
```

## Best Practices

1. **Use appropriate colors**: Choose badge colors that convey the right meaning
2. **Keep text concise**: Use short, clear text for badge content
3. **Maintain consistency**: Use consistent badge styles throughout your application
4. **Consider accessibility**: Ensure badges have sufficient contrast and are readable
5. **Use sparingly**: Don't overuse badges as they can clutter the interface
6. **Provide context**: Use badges to enhance, not replace, important information
7. **Test on mobile**: Ensure badges are visible and readable on mobile devices

## Related Components

- [Alerts](alerts.md) - For status messages with badges
- [Navigation](navigation.md) - For navigation items with badges
- [Cards](cards.md) - For cards with badge headers
- [Tables](tables.md) - For table cells with badge indicators


## metroui5_badge

```python
render_badge('Text')
```

Empty or invalid: `render_badge('Text')` returns `<span class="badge">Text</span>`. An empty call returns `<span class="badge"></span>`.

```django
{% metroui5_badge content="Text" %}
```
