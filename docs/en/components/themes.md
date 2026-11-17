# MetroUI 5 Themes

MetroUI 5 supports built-in `light` and `dark` themes for components. You can switch themes according to
system preferences or use the built-in theme switcher.

## About Themes

MetroUI 5 supports built-in `light` and `dark` themes for components. By default, the theme is set to `light`. To
change the theme, add the `.dark-side` class to the `<html>` tag for global application or to a specific `<element>` for
local application.

### Global Application

```html
<!-- Globally -->
<html class="dark-side">
	<div data-role="calendar"></div>
</html>
```

### Local Application

```html
<!-- Locally -->
<div class="dark-side">
	<div data-role="calendar"></div>
</div>
```

## Theme Configuration

### Basic Settings

```python
# settings.py
METROUI5 = {
    'theme': 'light',  # 'light', 'dark', or 'auto'
    'theme_target': 'html',  # Target element for theme class
    'theme_switcher_enabled': False,  # Enable built-in theme switcher
}
```

### Available Theme Values

- **`light`** - light theme (default)
- **`dark`** - dark theme
- **`auto`** - automatic detection based on system settings

### Target Element

- **`html`** - apply theme to `<html>` tag (default)
- **`body`** - apply theme to `<body>` tag
- **Any CSS selector** - for example `#app`, `.container`

## Automatic Theme Detection

You can use the `prefers-color-scheme` function to determine if the user has requested the use of light
or dark color theme in the system. To use this function, add the `metroui:theme` meta tag with content `auto`
in the `<head>` of the page.

```html
<meta name="metroui:theme" content="auto" />
```

You can also use `light` and `dark` values to set a specific theme.

## Theme Switcher

MetroUI 5 has a built-in theme switcher that allows you to switch between `light` and `dark` themes. You can
use the `theme-switcher` component to add a control element for switching between light and dark themes.

### Enabling Theme Switcher

```python
# settings.py
METROUI5 = {
    'theme_switcher_enabled': True,  # Enable theme switcher
}
```

### Switcher Modes

You can use the `data-mode` attribute to set the theme switcher mode.

#### Switch Mode

```html
<input type="checkbox" data-role="theme-switcher" />
```

#### Button Mode

```html
<input type="checkbox" data-role="theme-switcher" data-mode="button" />
```

### Using in Templates

#### Basic Theme Switcher

```html
{% load metroui5 %}

<!-- Full theme switcher with container -->
{% metroui5_theme_switcher %}
```

#### Switch Mode

```html
{% load metroui5 %}

<!-- Only checkbox in switch mode -->
{% metroui5_theme_switcher_switch %}
```

#### Button Mode

```html
{% load metroui5 %}

<!-- Only checkbox in button mode -->
{% metroui5_theme_switcher_button %}
```

## Template Tags

### `metroui5_theme_meta`

Returns meta tag for theme configuration.

```html
{% load metroui5 %}
<head>
	{% metroui5_theme_meta %}
</head>
```

### `metroui5_theme_switcher`

Renders the complete theme switcher component.

```html
{% load metroui5 %}

<!-- Basic theme switcher -->
{% metroui5_theme_switcher %}

<!-- With custom attributes -->
{% metroui5_theme_switcher class="custom-switcher" id="theme-toggle" %}
```

### `metroui5_theme_switcher_switch`

Renders only the switch part of the theme switcher.

```html
{% load metroui5 %}

<!-- Switch only -->
{% metroui5_theme_switcher_switch %}

<!-- With custom styling -->
{% metroui5_theme_switcher_switch class="switch-custom" %}
```

### `metroui5_theme_switcher_button`

Renders only the button part of the theme switcher.

```html
{% load metroui5 %}

<!-- Button only -->
{% metroui5_theme_switcher_button %}

<!-- With custom text -->
{% metroui5_theme_switcher_button light_text="☀️" dark_text="🌙" %}
```

## Usage Examples

### Basic Theme Implementation

```python
# views.py
from django.shortcuts import render

def themed_view(request):
    context = {
        'page_title': 'Themed Page',
        'content': 'This page supports light and dark themes'
    }
    return render(request, 'themed_page.html', context)
```

```html
<!-- themed_page.html -->
{% load metroui5 %}

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>{{ page_title }}</title>
		{% metroui5_theme_meta %} {% metroui5_css %}
	</head>
	<body>
		<header>
			<h1>{{ page_title }}</h1>
			<!-- Theme switcher in header -->
			{% metroui5_theme_switcher class="header-switcher" %}
		</header>

		<main>
			<p>{{ content }}</p>
		</main>

		{% metroui5_javascript %}
	</body>
</html>
```

### Conditional Theme Styling

```python
# views.py
def conditional_theme_view(request):
    # Check user preference
    user_theme = request.session.get('theme', 'light')

    context = {
        'user_theme': user_theme,
        'is_dark': user_theme == 'dark'
    }
    return render(request, 'conditional_theme.html', context)
```

```html
<!-- conditional_theme.html -->
{% load metroui5 %}

<div class="content {% if is_dark %}dark-content{% endif %}">
	<h2>Theme-Aware Content</h2>

	{% if is_dark %}
	<p class="dark-text">This content is optimized for dark theme</p>
	{% else %}
	<p class="light-text">This content is optimized for light theme</p>
	{% endif %}

	<!-- Theme switcher -->
	{% metroui5_theme_switcher %}
</div>
```

### Dynamic Theme Switching

```python
# views.py
from django.http import JsonResponse

def switch_theme(request):
    if request.method == 'POST':
        new_theme = request.POST.get('theme', 'light')
        request.session['theme'] = new_theme

        return JsonResponse({
            'success': True,
            'theme': new_theme
        })

    return JsonResponse({'success': False})
```

```html
<!-- theme_switcher.html -->
{% load metroui5 %}

<div class="theme-controls">
	<button onclick="switchTheme('light')" class="btn btn-light">Light</button>
	<button onclick="switchTheme('dark')" class="btn btn-dark">Dark</button>
	<button onclick="switchTheme('auto')" class="btn btn-auto">Auto</button>
</div>

<script>
	function switchTheme(theme) {
		fetch("/switch-theme/", {
			method: "POST",
			headers: {
				"Content-Type": "application/x-www-form-urlencoded",
				"X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
					.value,
			},
			body: "theme=" + theme,
		})
			.then((response) => response.json())
			.then((data) => {
				if (data.success) {
					// Apply theme change
					document.documentElement.className =
						theme === "dark" ? "dark-side" : "";
					localStorage.setItem("theme", theme);
				}
			});
	}
</script>
```

## CSS Customization

### Custom Theme Classes

```css
/* Light theme styles */
.light-side {
	--bg-color: #ffffff;
	--text-color: #333333;
	--border-color: #e0e0e0;
}

/* Dark theme styles */
.dark-side {
	--bg-color: #1a1a1a;
	--text-color: #ffffff;
	--border-color: #404040;
}

/* Theme-aware components */
.themed-card {
	background-color: var(--bg-color);
	color: var(--text-color);
	border: 1px solid var(--border-color);
}

.themed-button {
	background-color: var(--bg-color);
	color: var(--text-color);
	border: 1px solid var(--border-color);
}
```

### Component-Specific Themes

```css
/* Custom calendar theme */
.dark-side .calendar {
	background-color: #2d2d2d;
	color: #ffffff;
}

.dark-side .calendar-header {
	background-color: #404040;
	border-bottom: 1px solid #555555;
}

/* Custom form theme */
.dark-side .form-control {
	background-color: #333333;
	color: #ffffff;
	border-color: #555555;
}

.dark-side .form-control:focus {
	border-color: #007acc;
	box-shadow: 0 0 0 0.2rem rgba(0, 122, 204, 0.25);
}
```

## JavaScript Integration

### Theme Detection

```javascript
// Check current theme
function getCurrentTheme() {
	return document.documentElement.classList.contains("dark-side")
		? "dark"
		: "light";
}

// Check system preference
function getSystemTheme() {
	return window.matchMedia("(prefers-color-scheme: dark)").matches
		? "dark"
		: "light";
}

// Apply theme
function applyTheme(theme) {
	if (theme === "dark") {
		document.documentElement.classList.add("dark-side");
	} else {
		document.documentElement.classList.remove("dark-side");
	}

	// Save to localStorage
	localStorage.setItem("theme", theme);

	// Dispatch custom event
	document.dispatchEvent(
		new CustomEvent("themeChanged", { detail: { theme } })
	);
}
```

### Theme Change Listeners

```javascript
// Listen for theme changes
document.addEventListener("themeChanged", function (event) {
	const theme = event.detail.theme;
	console.log("Theme changed to:", theme);

	// Update UI elements
	updateThemeDependentElements(theme);
});

// Listen for system theme changes
window
	.matchMedia("(prefers-color-scheme: dark)")
	.addEventListener("change", function (event) {
		const newTheme = event.matches ? "dark" : "light";
		if (localStorage.getItem("theme") === "auto") {
			applyTheme(newTheme);
		}
	});

function updateThemeDependentElements(theme) {
	// Update charts, maps, or other theme-dependent components
	if (window.chartInstances) {
		window.chartInstances.forEach((chart) => {
			chart.update({
				options: {
					theme: theme,
				},
			});
		});
	}
}
```

## Best Practices

### 1. Consistent Theme Application

```python
# Use consistent theme configuration
THEME_CONFIG = {
    'default': 'light',
    'target': 'html',
    'persist': True,
    'auto_detect': True
}

# Apply in all views
def themed_view(request):
    context = {
        'theme_config': THEME_CONFIG,
        'current_theme': request.session.get('theme', THEME_CONFIG['default'])
    }
    return render(request, 'themed_template.html', context)
```

### 2. Performance Optimization

```python
# Cache theme-specific content
from django.core.cache import cache

def get_theme_content(request, theme):
    cache_key = f"theme_content_{theme}"
    content = cache.get(cache_key)

    if not content:
        # Generate theme-specific content
        content = generate_theme_content(theme)
        cache.set(cache_key, content, 3600)  # Cache for 1 hour

    return content
```

### 3. Accessibility

```html
<!-- Ensure theme switcher is accessible -->
<div class="theme-switcher" role="group" aria-label="Theme selection">
	<button
		onclick="switchTheme('light')"
		class="btn btn-light"
		aria-pressed="false"
		aria-label="Switch to light theme"
	>
		☀️ Light
	</button>
	<button
		onclick="switchTheme('dark')"
		class="btn btn-dark"
		aria-pressed="false"
		aria-label="Switch to dark theme"
	>
		🌙 Dark
	</button>
</div>
```

## Troubleshooting

### Common Issues

1. **Theme not applying**: Check if the target element exists and the class is being added correctly
2. **Theme switcher not working**: Verify that `theme_switcher_enabled` is set to `True` in settings
3. **Styles not updating**: Ensure CSS variables are properly defined for both themes
4. **Performance issues**: Use caching for theme-specific content and minimize DOM manipulation

### Debug Mode

```python
# Enable debug mode for theme issues
METROUI5 = {
    'theme_debug': True,  # Enable theme debugging
    'theme_logging': True,  # Log theme changes
}
```

## Related Documentation

- [Components](components.md) - Component rendering functions
- [Template Tags](templatetags.md) - Django template integration
- [CSS Utilities](css.md) - CSS class management
- [JavaScript Integration](../getting-started/javascript.md) - Client-side functionality


## metroui5_theme_switcher

```python
render_theme_switcher()
```

Empty or invalid: `render_theme_switcher()` returns `<input data-role="theme-switcher">`.

```django
{% metroui5_theme_switcher %}
```
