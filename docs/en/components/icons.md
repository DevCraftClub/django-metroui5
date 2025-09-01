# Icons

MetroUI5 Django provides a comprehensive icon system using MetroUI's built-in icon font, allowing you to easily add icons throughout your application.

## Basic Usage

```python
from metroui5.templatetags.metroui5 import metroui5_icon

# Simple icon
icon_html = metroui5_icon("home")
```

## Rendered Output

### Basic Icon

```html
<!-- Input -->
metroui5_icon("home")

<!-- Output -->
<span class="mif home"></span>
```

### Icon with Size

```html
<!-- Input -->
metroui5_icon("user", size="2x")

<!-- Output -->
<span class="mif user mif-2x"></span>
```

### Icon with Custom Classes

```html
<!-- Input -->
metroui5_icon("mail", class="icon-primary", id="mail-icon")

<!-- Output -->
<span class="mif mail icon-primary" id="mail-icon"></span>
```

## Template Usage

```html
{% load metroui5 %}

<!-- Basic icon -->
{% metroui5_icon "home" %}

<!-- Icon with size -->
{% metroui5_icon "user" size="2x" %}

<!-- Icon with custom attributes -->
{% metroui5_icon "mail" class="icon-primary" id="mail-icon" %}
```

## Parameters

### `metroui5_icon(icon_name, size=None, **kwargs)`

- **icon_name** (str): Name of the MetroUI icon
- **size** (str, optional): Icon size (1x, 2x, 3x, 4x, 5x)
- **kwargs**: Additional HTML attributes

## Examples

### Basic Icons

```html
{% load metroui5 %}

<!-- Navigation icons -->
{% metroui5_icon "home" %} {% metroui5_icon "user" %} {% metroui5_icon
"settings" %} {% metroui5_icon "mail" %} {% metroui5_icon "phone" %}
```

### Icons with Sizes

```html
<!-- Different sizes -->
{% metroui5_icon "star" size="1x" %} {% metroui5_icon "star" size="2x" %} {%
metroui5_icon "star" size="3x" %} {% metroui5_icon "star" size="4x" %} {%
metroui5_icon "star" size="5x" %}
```

### Icons with Custom Styling

```html
<!-- Icons with custom classes -->
{% metroui5_icon "heart" class="icon-red" %} {% metroui5_icon "checkmark"
class="icon-green" %} {% metroui5_icon "warning" class="icon-yellow" %} {%
metroui5_icon "info" class="icon-blue" %}
```

## MetroUI Icon Classes

MetroUI5 provides several CSS classes for icon styling:

### Size Classes

- `mif-1x` - 1x size (default)
- `mif-2x` - 2x size
- `mif-Nx` - Nx size (number instead of N)
- `mif-10x` - 10x size (max size)

### Color Classes

- `icon-primary` - Primary color
- `icon-secondary` - Secondary color
- `icon-success` - Success color (green)
- `icon-warning` - Warning color (yellow)
- `icon-danger` - Danger color (red)
- `icon-info` - Info color (blue)
- `icon-light` - Light color
- `icon-dark` - Dark color

### Style Classes

- `icon-spin` - Spinning animation
- `icon-pulse` - Pulsing animation
- `icon-bounce` - Bouncing animation
- `icon-flip` - Flipping animation

## Common Icon Categories

### Navigation Icons

```html
{% load metroui5 %}

<!-- Main navigation -->
{% metroui5_icon "home" %} {% metroui5_icon "dashboard" %} {% metroui5_icon
"menu" %} {% metroui5_icon "back" %} {% metroui5_icon "forward" %} {%
metroui5_icon "up" %} {% metroui5_icon "down" %} {% metroui5_icon "left" %} {%
metroui5_icon "right" %}
```

### User Interface Icons

```html
<!-- UI elements -->
{% metroui5_icon "user" %} {% metroui5_icon "users" %} {% metroui5_icon
"settings" %} {% metroui5_icon "cog" %} {% metroui5_icon "gear" %} {%
metroui5_icon "search" %} {% metroui5_icon "filter" %} {% metroui5_icon "sort"
%}
```

### Communication Icons

```html
<!-- Communication -->
{% metroui5_icon "mail" %} {% metroui5_icon "phone" %} {% metroui5_icon "chat"
%} {% metroui5_icon "comment" %} {% metroui5_icon "bell" %} {% metroui5_icon
"notification" %}
```

### File and Document Icons

```html
<!-- Files and documents -->
{% metroui5_icon "file" %} {% metroui5_icon "folder" %} {% metroui5_icon
"download" %} {% metroui5_icon "upload" %} {% metroui5_icon "attachment" %} {%
metroui5_icon "document" %} {% metroui5_icon "image" %} {% metroui5_icon "video"
%}
```

### Action Icons

```html
<!-- Actions -->
{% metroui5_icon "plus" %} {% metroui5_icon "minus" %} {% metroui5_icon "edit"
%} {% metroui5_icon "delete" %} {% metroui5_icon "save" %} {% metroui5_icon
"copy" %} {% metroui5_icon "cut" %} {% metroui5_icon "paste" %}
```

### Status Icons

```html
<!-- Status indicators -->
{% metroui5_icon "checkmark" %} {% metroui5_icon "cross" %} {% metroui5_icon
"warning" %} {% metroui5_icon "info" %} {% metroui5_icon "question" %} {%
metroui5_icon "exclamation" %}
```

## Django Template Usage

### Using in Views

```python
# views.py
from metroui5.templatetags.metroui5 import metroui5_icon

def my_view(request):
    # Create icons in view
    home_icon = metroui5_icon("home", size="2x")
    user_icon = metroui5_icon("user", class="icon-primary")

    context = {
        'home_icon': home_icon,
        'user_icon': user_icon,
        'navigation_icons': [
            metroui5_icon("dashboard", class="nav-icon"),
            metroui5_icon("settings", class="nav-icon"),
            metroui5_icon("logout", class="nav-icon"),
        ]
    }
    return render(request, 'my_template.html', context)
```

```html
<!-- my_template.html -->
{% load metroui5 %}

<!-- Direct HTML output -->
{{ home_icon|safe }} {{ user_icon|safe }}

<!-- Loop through icons -->
{% for icon in navigation_icons %} {{ icon|safe }} {% endfor %}
```

### Icons in Navigation

```python
# views.py
def navigation_view(request):
    nav_items = [
        {"text": "Home", "icon": metroui5_icon("home"), "url": "/"},
        {"text": "Dashboard", "icon": metroui5_icon("dashboard"), "url": "/dashboard/"},
        {"text": "Settings", "icon": metroui5_icon("cog"), "url": "/settings/"},
    ]

    context = {'nav_items': nav_items}
    return render(request, 'navigation.html', context)
```

```html
<!-- navigation.html -->
{% load metroui5 %}

<nav class="nav nav-horizontal">
	{% for item in nav_items %}
	<a href="{{ item.url }}" class="nav-item">
		{{ item.icon|safe }} {{ item.text }}
	</a>
	{% endfor %}
</nav>
```

### Conditional Icons

```python
# views.py
def status_view(request):
    items = [
        {"name": "Task 1", "status": "completed"},
        {"name": "Task 2", "status": "pending"},
        {"name": "Task 3", "status": "failed"},
    ]

    for item in items:
        if item["status"] == "completed":
            item["icon"] = metroui5_icon("checkmark", class="icon-success")
        elif item["status"] == "pending":
            item["icon"] = metroui5_icon("clock", class="icon-warning")
        else:
            item["icon"] = metroui5_icon("cross", class="icon-danger")

    context = {'items': items}
    return render(request, 'status.html', context)
```

```html
<!-- status.html -->
{% load metroui5 %}

<ul class="list">
	{% for item in items %}
	<li class="list-item">{{ item.icon|safe }} {{ item.name }}</li>
	{% endfor %}
</ul>
```

## Advanced Examples

### Icons in Buttons

```html
{% load metroui5 %}

<!-- Button with icon -->
<button class="button button-primary">{% metroui5_icon "save" %} Save</button>

<!-- Icon-only button -->
<button class="button button-mini">{% metroui5_icon "edit" %}</button>

<!-- Button with icon and text -->
<a href="#" class="button button-success">
	{% metroui5_icon "download" size="2x" %} Download File
</a>
```

### Icons in Navigation

```html
{% load metroui5 %}

<nav class="nav nav-horizontal">
	<a href="/" class="nav-item"> {% metroui5_icon "home" %} Home </a>
	<a href="/about/" class="nav-item"> {% metroui5_icon "info" %} About </a>
	<a href="/contact/" class="nav-item"> {% metroui5_icon "mail" %} Contact </a>
</nav>
```

### Icons in Lists

```html
{% load metroui5 %}

<ul class="list">
	<li>{% metroui5_icon "user" class="icon-primary" %} John Doe</li>
	<li>{% metroui5_icon "mail" class="icon-info" %} john@example.com</li>
	<li>{% metroui5_icon "phone" class="icon-success" %} +1-555-0123</li>
</ul>
```

### Animated Icons

```html
{% load metroui5 %}

<!-- Spinning loading icon -->
{% metroui5_icon "spinner" class="icon-spin" %}

<!-- Pulsing notification icon -->
{% metroui5_icon "bell" class="icon-pulse" %}

<!-- Bouncing success icon -->
{% metroui5_icon "checkmark" class="icon-bounce" %}
```

### Icons with Tooltips

```html
{% load metroui5 %}

<!-- Icon with tooltip -->
<span class="tooltip" data-tooltip="Click to edit">
	{% metroui5_icon "edit" class="icon-primary" %}
</span>

<!-- Icon with custom tooltip -->
<span
	class="tooltip"
	data-tooltip="Delete this item"
	data-tooltip-position="top"
>
	{% metroui5_icon "delete" class="icon-danger" %}
</span>
```

### Responsive Icons

```html
{% load metroui5 %}

<!-- Responsive icon sizes -->
<div class="icon-responsive">
	{% metroui5_icon "home" size="2x" class="icon-mobile-small icon-tablet-medium
	icon-desktop-large" %}
</div>
```

### Icons in Cards

```html
{% load metroui5 %}

<div class="card">
	<div class="card-header">
		<h3>{% metroui5_icon "user" class="icon-primary" %} User Profile</h3>
	</div>
	<div class="card-content">
		<p>{% metroui5_icon "mail" %} user@example.com</p>
		<p>{% metroui5_icon "phone" %} +1-555-0123</p>
	</div>
</div>
```

### Icons in Alerts

```html
{% load metroui5 %}

<!-- Success alert with icon -->
<div class="alert alert-success">
	{% metroui5_icon "checkmark" class="icon-success" %} Operation completed
	successfully!
</div>

<!-- Warning alert with icon -->
<div class="alert alert-warning">
	{% metroui5_icon "warning" class="icon-warning" %} Please review your input.
</div>

<!-- Error alert with icon -->
<div class="alert alert-danger">
	{% metroui5_icon "cross" class="icon-danger" %} An error occurred.
</div>
```

## Custom Icon Styling

### CSS Customization

```css
/* Custom icon colors */
.icon-custom-red {
	color: #ff4444;
}

.icon-custom-blue {
	color: #4444ff;
}

.icon-custom-green {
	color: #44ff44;
}

/* Custom icon sizes */
.icon-tiny {
	font-size: 0.5em;
}

.icon-huge {
	font-size: 4em;
}

/* Custom icon effects */
.icon-glow {
	text-shadow: 0 0 10px currentColor;
}

.icon-shadow {
	text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
```

### Using Custom Classes

```html
{% load metroui5 %}

<!-- Custom colored icons -->
{% metroui5_icon "heart" class="icon-custom-red" %} {% metroui5_icon "star"
class="icon-custom-blue" %} {% metroui5_icon "leaf" class="icon-custom-green" %}

<!-- Custom sized icons -->
{% metroui5_icon "home" class="icon-tiny" %} {% metroui5_icon "home"
class="icon-huge" %}

<!-- Icons with effects -->
{% metroui5_icon "star" class="icon-glow" %} {% metroui5_icon "heart"
class="icon-shadow" %}
```

## JavaScript Integration

### Dynamic Icon Updates

```javascript
// Change icon dynamically
function changeIcon(element, newIcon) {
	const iconElement = element.querySelector(".mif");
	if (iconElement) {
		// Remove old icon class
		const oldClasses = Array.from(iconElement.classList).filter((cls) =>
			cls.startsWith("mif-")
		);
		oldClasses.forEach((cls) => iconElement.classList.remove(cls));

		// Add new icon class
		iconElement.classList.add(`mif-${newIcon}`);
	}
}

// Example usage
const button = document.querySelector("#my-button");
changeIcon(button, "checkmark");
```

### Icon Animations

```javascript
// Add animation to icon
function animateIcon(iconElement, animation) {
	iconElement.classList.add(`icon-${animation}`);

	// Remove animation after completion
	setTimeout(() => {
		iconElement.classList.remove(`icon-${animation}`);
	}, 1000);
}

// Example usage
const icon = document.querySelector(".mif-heart");
animateIcon(icon, "bounce");
```

### Icon Click Events

```javascript
// Handle icon clicks
document.querySelectorAll(".mif").forEach((icon) => {
	icon.addEventListener("click", function () {
		const iconName = this.classList[1]; // Get icon name from class
		console.log(`Clicked icon: ${iconName}`);

		// Add click effect
		this.style.transform = "scale(1.2)";
		setTimeout(() => {
			this.style.transform = "scale(1)";
		}, 200);
	});
});
```

## Best Practices

1. **Use semantic icons**: Choose icons that clearly represent their function
2. **Maintain consistency**: Use the same icon for the same action throughout your app
3. **Consider accessibility**: Provide text alternatives for icon-only buttons
4. **Use appropriate sizes**: Choose icon sizes that fit well with your content
5. **Limit animations**: Use animations sparingly to avoid overwhelming users
6. **Test on mobile**: Ensure icons are visible and usable on mobile devices
7. **Use color meaningfully**: Use colors to convey status or importance

## Icon Reference

MetroUI5 includes hundreds of icons. Here are some commonly used ones:

### Basic Icons

- `home`, `user`, `settings`, `search`, `menu`, `close`, `checkmark`, `cross`
- `plus`, `minus`, `edit`, `delete`, `save`, `copy`, `cut`, `paste`
- `mail`, `phone`, `chat`, `bell`, `notification`, `comment`

### File Icons

- `file`, `folder`, `document`, `image`, `video`, `audio`, `archive`
- `download`, `upload`, `attachment`, `link`, `bookmark`

### Navigation Icons

- `back`, `forward`, `up`, `down`, `left`, `right`, `arrow-up`, `arrow-down`
- `arrow-left`, `arrow-right`, `chevron-up`, `chevron-down`

### Status Icons

- `warning`, `info`, `question`, `exclamation`, `checkmark`, `cross`
- `star`, `heart`, `like`, `dislike`, `flag`, `bookmark`

## Related Components

- [Buttons](buttons.md) - For buttons with icons
- [Navigation](navigation.md) - For navigation with icons
- [Alerts](alerts.md) - For alerts with status icons
- [Cards](cards.md) - For cards with header icons
