# Cards

Component for creating information cards with header, content, and footer.

## Basic Usage

### Simple Card

```python
from metroui5.components import render_card

# Basic card
card = render_card("Title", "Card content")
```

### Card with Footer

```python
# Card with header, content, and footer
card = render_card(
    header="Card Title",
    content="Main card content",
    footer="Card footer"
)
```

### Content-Only Card

```python
# Card without header and footer
card = render_card(content="Content only")
```

## Parameters

### `header` (optional)

Card header. If not specified, header is not displayed.

```python
card = render_card(header="Title", content="Content")
```

### `content` (optional)

Main card content. If not specified, content is not displayed.

```python
card = render_card(header="Title", content="Content")
```

### `footer` (optional)

Card footer. If not specified, footer is not displayed.

```python
card = render_card(
    header="Title",
    content="Content",
    footer="Footer"
)
```

### `**attrs` (optional)

Additional HTML attributes.

```python
card = render_card(
    header="Title",
    content="Content",
    **{"class": "custom-card", "id": "myCard"}
)
```

## Usage Examples

### In Views

```python
from metroui5.components import render_card


def dashboard(request):
    context = {
        'info_card': render_card(
            header="Information",
            content="This is an information card with important data.",
            footer="Updated today"
        ),
        'stats_card': render_card(
            header="Statistics",
            content="""
                <div class="row">
                    <div class="cell-md-6">
                        <strong>Users:</strong> 1,234
                    </div>
                    <div class="cell-md-6">
                        <strong>Orders:</strong> 567
                    </div>
                </div>
            """,
            footer="Last updated: 5 minutes ago"
        ),
        'action_card': render_card(
            header="Quick Actions",
            content="""
                <div class="button-group">
                    <button class="button primary">Create New</button>
                    <button class="button secondary">Import Data</button>
                </div>
            """,
            footer="Click any button to proceed"
        )
    }
    return render(request, 'dashboard.html', context)
```

### In Templates

```html
<!-- dashboard.html -->
{% load metroui5 %} {% block content %}
<div class="row">
	<!-- Information card -->
	<div class="cell-md-4">{{ info_card|safe }}</div>

	<!-- Statistics card -->
	<div class="cell-md-4">{{ stats_card|safe }}</div>

	<!-- Action card -->
	<div class="cell-md-4">{{ action_card|safe }}</div>
</div>
{% endblock %}
```

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic card -->
{% metroui5_card header="Card Title" content="Card content" %}

<!-- Card with footer -->
{% metroui5_card header="Important Notice" content="This is an important message
for all users." footer="Please read carefully" %}

<!-- Custom styled card -->
{% metroui5_card header="Custom Card" content="This card has custom styling"
class="card-custom" id="custom-card" %}
```

## Advanced Examples

### Dynamic Card Generation

```python
def dynamic_cards_view(request):
    # Generate cards based on user permissions
    cards = []

    if request.user.is_staff:
        cards.append(render_card(
            header="Admin Panel",
            content="Access to administrative functions",
            footer="Restricted access"
        ))

    if request.user.has_perm('app.view_reports'):
        cards.append(render_card(
            header="Reports",
            content="View and generate reports",
            footer="Data updated hourly"
        ))

    if request.user.has_perm('app.manage_users'):
        cards.append(render_card(
            header="User Management",
            content="Manage user accounts and permissions",
            footer="Real-time updates"
        ))

    context = {'cards': cards}
    return render(request, 'dynamic_cards.html', context)
```

### Conditional Card Content

```python
def conditional_cards_view(request):
    user = request.user

    # Base card
    base_card = render_card(
        header=f"Welcome, {user.first_name}!",
        content="Here's your personalized dashboard."
    )

    # Conditional cards based on user status
    conditional_cards = []

    if not user.email_verified:
        conditional_cards.append(render_card(
            header="Email Verification Required",
            content="Please verify your email address to access all features.",
            footer="Check your inbox"
        ))

    if user.is_new:
        conditional_cards.append(render_card(
            header="Getting Started",
            content="Complete your profile setup to get the most out of our platform.",
            footer="Takes only 2 minutes"
        ))

    if user.last_login and user.last_login.date() < timezone.now().date() - timedelta(days=7):
        conditional_cards.append(render_card(
            header="Welcome Back!",
            content="We've missed you. Here's what's new since your last visit.",
            footer="Stay updated"
        ))

    context = {
        'base_card': base_card,
        'conditional_cards': conditional_cards
    }
    return render(request, 'conditional_cards.html', context)
```

### Interactive Cards

```python
def interactive_cards_view(request):
    # Cards with interactive elements
    interactive_cards = [
        render_card(
            header="Settings",
            content="""
                <div class="form-group">
                    <label>Notifications:</label>
                    <input type="checkbox" data-role="switch" checked>
                </div>
                <div class="form-group">
                    <label>Theme:</label>
                    <select data-role="select">
                        <option value="light">Light</option>
                        <option value="dark">Dark</option>
                    </select>
                </div>
            """,
            footer="<button class='button primary'>Save Changes</button>"
        ),
        render_card(
            header="Quick Actions",
            content="""
                <div class="button-group">
                    <button class="button primary" onclick="createProject()">New Project</button>
                    <button class="button secondary" onclick="importData()">Import</button>
                    <button class="button alert" onclick="exportData()">Export</button>
                </div>
            """,
            footer="Click any button to proceed"
        )
    ]

    context = {'interactive_cards': interactive_cards}
    return render(request, 'interactive_cards.html', context)
```

## Card Layouts

### Grid Layout

```html
<!-- Grid layout for cards -->
<div class="row">
	<div class="cell-md-3">{{ card1|safe }}</div>
	<div class="cell-md-3">{{ card2|safe }}</div>
	<div class="cell-md-3">{{ card3|safe }}</div>
	<div class="cell-md-3">{{ card4|safe }}</div>
</div>
```

### Masonry Layout

```html
<!-- Masonry-style layout -->
<div class="masonry-grid" data-role="masonry">
	<div class="masonry-item">{{ tall_card|safe }}</div>
	<div class="masonry-item">{{ wide_card|safe }}</div>
	<div class="masonry-item">{{ small_card|safe }}</div>
</div>
```

### Responsive Layout

```html
<!-- Responsive card layout -->
<div class="row">
	<div class="cell-sm-12 cell-md-6 cell-lg-4">{{ responsive_card1|safe }}</div>
	<div class="cell-sm-12 cell-md-6 cell-lg-4">{{ responsive_card2|safe }}</div>
	<div class="cell-sm-12 cell-md-12 cell-lg-4">{{ responsive_card3|safe }}</div>
</div>
```

## Customization

### Custom CSS Classes

```css
/* Custom card styles */
.custom-card {
	border-radius: 15px;
	box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
	transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.custom-card:hover {
	transform: translateY(-5px);
	box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
}

.custom-card .card-header {
	background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
	color: white;
	border-radius: 15px 15px 0 0;
}

.custom-card .card-content {
	padding: 2rem;
	line-height: 1.6;
}

.custom-card .card-footer {
	background-color: #f8f9fa;
	border-top: 1px solid #e9ecef;
	border-radius: 0 0 15px 15px;
}
```

### Custom JavaScript

```javascript
// Add custom card interactions
document.addEventListener("DOMContentLoaded", function () {
	// Add click handlers to cards
	document.querySelectorAll(".card").forEach((card) => {
		card.addEventListener("click", function () {
			// Add click effect
			this.style.transform = "scale(0.98)";
			setTimeout(() => {
				this.style.transform = "scale(1)";
			}, 150);
		});
	});

	// Add hover effects
	document.querySelectorAll(".card").forEach((card) => {
		card.addEventListener("mouseenter", function () {
			this.style.boxShadow = "0 8px 25px rgba(0, 0, 0, 0.15)";
		});

		card.addEventListener("mouseleave", function () {
			this.style.boxShadow = "0 4px 15px rgba(0, 0, 0, 0.1)";
		});
	});
});
```

## Best Practices

### 1. Consistent Card Structure

```python
# Define consistent card structure
def create_consistent_card(title, content, footer=None, **kwargs):
    """Create a card with consistent styling and structure."""

    default_attrs = {
        'class': 'card card-standard',
        'data-card-type': 'standard'
    }

    # Merge with custom attributes
    default_attrs.update(kwargs)

    return render_card(
        header=title,
        content=content,
        footer=footer,
        **default_attrs
    )

# Usage
def dashboard_view(request):
    context = {
        'welcome_card': create_consistent_card(
            "Welcome Back!",
            "We're glad to see you again.",
            footer="Last login: 2 hours ago"
        ),
        'stats_card': create_consistent_card(
            "Statistics",
            "Your activity summary for today.",
            footer="Updated every 5 minutes"
        )
    }
    return render(request, 'dashboard.html', context)
```

### 2. Performance Optimization

```python
# Cache expensive card content
from django.core.cache import cache

def get_cached_card_content(user_id, card_type):
    """Get cached card content to improve performance."""

    cache_key = f"card_content_{user_id}_{card_type}"
    content = cache.get(cache_key)

    if not content:
        # Generate expensive content
        content = generate_expensive_content(user_id, card_type)

        # Cache for 10 minutes
        cache.set(cache_key, content, 600)

    return content

def optimized_cards_view(request):
    user_id = request.user.id

    # Get cached content
    stats_content = get_cached_card_content(user_id, 'stats')
    activity_content = get_cached_card_content(user_id, 'activity')

    context = {
        'stats_card': render_card(
            header="Statistics",
            content=stats_content,
            footer="Cached data"
        ),
        'activity_card': render_card(
            header="Recent Activity",
            content=activity_content,
            footer="Cached data"
        )
    }
    return render(request, 'optimized_cards.html', context)
```

### 3. Accessibility

```python
# Create accessible cards
def create_accessible_card(title, content, footer=None, **kwargs):
    """Create a card with proper accessibility attributes."""

    # Add accessibility attributes
    accessibility_attrs = {
        'role': 'article',
        'aria-labelledby': f"card-{kwargs.get('id', 'default')}-header",
        'aria-describedby': f"card-{kwargs.get('id', 'default')}-content"
    }

    # Merge with existing attributes
    if 'attrs' not in kwargs:
        kwargs['attrs'] = {}
    kwargs['attrs'].update(accessibility_attrs)

    return render_card(
        header=title,
        content=content,
        footer=footer,
        **kwargs
    )

# Usage
def accessible_cards_view(request):
    context = {
        'accessible_card': create_accessible_card(
            "Important Information",
            "This card is designed with accessibility in mind.",
            footer="Accessible footer",
            id="important-info"
        )
    }
    return render(request, 'accessible_cards.html', context)
```

## Related Documentation

- [Components](components.md) - Component rendering functions
- [Template Tags](templatetags.md) - Django template integration
- [Layout](layout.md) - Page layout components
- [CSS Utilities](css.md) - CSS class management
