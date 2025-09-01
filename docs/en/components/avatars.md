# Avatars

Component for creating user avatars, profile pictures, and image placeholders with various sizes and styles.

## Basic Usage

### Simple Avatar

```python
from metroui5.components import render_avatar

# Basic avatar with image
avatar_html = render_avatar(
    src="/static/images/user.jpg",
    alt="John Doe"
)
```

### Avatar with Initials

```python
# Avatar with user initials
avatar_html = render_avatar(
    initials="JD",
    background_color="#007acc"
)
```

### Avatar with Icon

```python
# Avatar with default icon
avatar_html = render_avatar(
    icon="user",
    size="large"
)
```

## Rendered Output

### Basic Avatar

```html
<!-- Input -->
render_avatar(src="/static/images/user.jpg", alt="John Doe")

<!-- Output -->
<div class="avatar">
	<img src="/static/images/user.jpg" alt="John Doe" class="avatar-image" />
</div>
```

### Avatar with Initials

```html
<!-- Input -->
render_avatar(initials="JD", background_color="#007acc")

<!-- Output -->
<div class="avatar avatar-initials" style="background-color: #007acc;">
	<span class="avatar-text">JD</span>
</div>
```

### Avatar with Icon

```html
<!-- Input -->
render_avatar(icon="user", size="large")

<!-- Output -->
<div class="avatar avatar-icon avatar-large">
	<span class="mif-user"></span>
</div>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic avatar -->
{% metroui5_avatar src="/static/images/user.jpg" alt="User" %}

<!-- Avatar with initials -->
{% metroui5_avatar initials="JD" background_color="#007acc" %}

<!-- Avatar with icon -->
{% metroui5_avatar icon="user" size="medium" %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_avatar

def profile_view(request):
    user = request.user

    # Create user avatar
    if user.profile_picture:
        avatar_html = render_avatar(
            src=user.profile_picture.url,
            alt=f"{user.first_name} {user.last_name}",
            size="large"
        )
    else:
        # Fallback to initials
        initials = f"{user.first_name[0]}{user.last_name[0]}" if user.first_name and user.last_name else "U"
        avatar_html = render_avatar(
            initials=initials,
            background_color=get_user_color(user.id),
            size="large"
        )

    context = {
        'avatar_html': avatar_html,
        'user': user
    }
    return render(request, 'profile.html', context)
```

```html
<!-- profile.html -->
{% load metroui5 %} {% block content %}
<div class="profile-header">
	<!-- Direct HTML output -->
	{{ avatar_html|safe }}

	<!-- Or use template tag -->
	{% if user.profile_picture %} {% metroui5_avatar src=user.profile_picture.url
	alt=user.get_full_name size="large" %} {% else %} {% metroui5_avatar
	initials=user.initials background_color=user.avatar_color %} {% endif %}

	<h1>{{ user.get_full_name }}</h1>
</div>
{% endblock %}
```

## Parameters

### `src` (optional)

URL of the avatar image.

**Example**:

```python
avatar_html = render_avatar(src="/static/images/avatar.jpg")
```

### `alt` (optional)

Alternative text for the avatar image.

**Example**:

```python
avatar_html = render_avatar(src="/images/user.jpg", alt="John Doe")
```

### `initials` (optional)

Text to display when no image is available.

**Example**:

```python
avatar_html = render_avatar(initials="JD")
```

### `icon` (optional)

Icon to display when no image or initials are provided.

**Default**: `"user"`

**Example**:

```python
avatar_html = render_avatar(icon="person")
```

### `size` (optional)

Size of the avatar: small, medium, large, xlarge.

**Default**: `"medium"`

**Example**:

```python
avatar_html = render_avatar(size="large")
```

### `shape` (optional)

Shape of the avatar: circle, square, rounded.

**Default**: `"circle"`

**Example**:

```python
avatar_html = render_avatar(shape="square")
```

### `background_color` (optional)

Background color for initials or icon avatars.

**Example**:

```python
avatar_html = render_avatar(initials="JD", background_color="#28a745")
```

### `text_color` (optional)

Text color for initials.

**Default**: `"white"`

**Example**:

```python
avatar_html = render_avatar(initials="JD", text_color="#000")
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
avatar_html = render_avatar(class="avatar-bordered")
```

### `id` (optional)

Unique identifier for the avatar element.

**Example**:

```python
avatar_html = render_avatar(id="user-avatar")
```

## Advanced Examples

### User Avatar with Fallbacks

```python
def create_user_avatar(user, size="medium"):
    """Create user avatar with multiple fallbacks."""

    # Try profile picture first
    if hasattr(user, 'profile') and user.profile.picture:
        return render_avatar(
            src=user.profile.picture.url,
            alt=user.get_full_name(),
            size=size
        )

    # Fallback to initials
    if user.first_name and user.last_name:
        initials = f"{user.first_name[0]}{user.last_name[0]}".upper()
        return render_avatar(
            initials=initials,
            background_color=generate_user_color(user.id),
            size=size
        )

    # Final fallback to icon
    return render_avatar(
        icon="user",
        size=size,
        background_color="#6c757d"
    )
```

### Avatar Group

```python
def create_avatar_group(users, max_display=3):
    """Create group of avatars with overflow indicator."""

    avatars = []
    display_users = users[:max_display]

    for user in display_users:
        avatars.append(create_user_avatar(user, size="small"))

    # Add overflow indicator
    if len(users) > max_display:
        overflow_count = len(users) - max_display
        avatars.append(render_avatar(
            initials=f"+{overflow_count}",
            size="small",
            background_color="#dee2e6",
            text_color="#495057"
        ))

    return avatars
```

### Status Avatar

```python
def create_status_avatar(user, online_status=None):
    """Create avatar with online status indicator."""

    avatar_html = create_user_avatar(user)

    if online_status:
        status_class = f"avatar-status-{online_status}"  # online, away, busy, offline
        avatar_html = avatar_html.replace(
            'class="avatar"',
            f'class="avatar avatar-with-status {status_class}"'
        )

    return avatar_html
```

### Editable Avatar

```python
def create_editable_avatar(user, editable=True):
    """Create avatar with edit functionality."""

    avatar_html = create_user_avatar(user, size="large")

    if editable:
        edit_overlay = """
        <div class="avatar-edit-overlay">
            <button class="avatar-edit-btn" onclick="editAvatar()">
                <span class="mif-camera"></span>
            </button>
        </div>
        """
        avatar_html = avatar_html.replace("</div>", f"{edit_overlay}</div>")

    return avatar_html
```

### Team Avatar List

```python
def create_team_avatars(team_members):
    """Create list of team member avatars."""

    team_avatars = []

    for member in team_members:
        member_avatar = {
            "avatar": create_user_avatar(member.user),
            "name": member.user.get_full_name(),
            "role": member.role,
            "status": member.status
        }
        team_avatars.append(member_avatar)

    return team_avatars
```

## Styling

### CSS Classes

#### Base Classes

- `avatar` - Base avatar container
- `avatar-image` - Avatar with image
- `avatar-initials` - Avatar with initials
- `avatar-icon` - Avatar with icon

#### Size Classes

- `avatar-small` - Small avatar (32px)
- `avatar-medium` - Medium avatar (48px) - default
- `avatar-large` - Large avatar (64px)
- `avatar-xlarge` - Extra large avatar (96px)

#### Shape Classes

- `avatar-circle` - Circular avatar (default)
- `avatar-square` - Square avatar
- `avatar-rounded` - Rounded square avatar

#### Feature Classes

- `avatar-bordered` - Avatar with border
- `avatar-with-status` - Avatar with status indicator
- `avatar-editable` - Editable avatar with overlay

### Custom Styling

```css
/* Custom avatar styling */
.avatar-custom {
	position: relative;
	display: inline-block;
	border: 3px solid #fff;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
	transition: all 0.3s ease;
}

.avatar-custom:hover {
	transform: scale(1.05);
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.avatar-custom .avatar-image {
	width: 100%;
	height: 100%;
	object-fit: cover;
	border-radius: inherit;
}

.avatar-custom .avatar-text {
	font-weight: 600;
	font-size: 0.875em;
	text-transform: uppercase;
	letter-spacing: 0.5px;
}

/* Status indicators */
.avatar-with-status::after {
	content: "";
	position: absolute;
	bottom: 0;
	right: 0;
	width: 12px;
	height: 12px;
	border: 2px solid #fff;
	border-radius: 50%;
	background: #6c757d;
}

.avatar-status-online::after {
	background: #28a745;
}

.avatar-status-away::after {
	background: #ffc107;
}

.avatar-status-busy::after {
	background: #dc3545;
}

.avatar-status-offline::after {
	background: #6c757d;
}

/* Avatar group */
.avatar-group {
	display: flex;
	align-items: center;
}

.avatar-group .avatar {
	margin-right: -8px;
	border: 2px solid #fff;
	z-index: 1;
}

.avatar-group .avatar:hover {
	z-index: 2;
}

/* Editable avatar */
.avatar-editable {
	cursor: pointer;
}

.avatar-edit-overlay {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background: rgba(0, 0, 0, 0.5);
	display: flex;
	align-items: center;
	justify-content: center;
	opacity: 0;
	transition: opacity 0.3s ease;
	border-radius: inherit;
}

.avatar-editable:hover .avatar-edit-overlay {
	opacity: 1;
}

.avatar-edit-btn {
	background: none;
	border: none;
	color: white;
	font-size: 20px;
	cursor: pointer;
}
```

## JavaScript Integration

### Avatar Loading

```javascript
// Handle avatar image loading
$(".avatar-image").on("load", function () {
	$(this).closest(".avatar").removeClass("avatar-loading");
});

$(".avatar-image").on("error", function () {
	const avatar = $(this).closest(".avatar");
	const fallbackInitials = avatar.data("initials");
	const fallbackColor = avatar.data("color") || "#6c757d";

	// Replace with initials fallback
	if (fallbackInitials) {
		avatar.html(`<span class="avatar-text">${fallbackInitials}</span>`);
		avatar.css("background-color", fallbackColor);
		avatar.addClass("avatar-initials");
	} else {
		// Replace with icon fallback
		avatar.html('<span class="mif-user"></span>');
		avatar.addClass("avatar-icon");
	}
});
```

### Avatar Upload

```javascript
// Handle avatar upload
function handleAvatarUpload(input) {
	const file = input.files[0];
	if (!file) return;

	// Validate file type
	if (!file.type.startsWith("image/")) {
		alert("Please select an image file");
		return;
	}

	// Validate file size (2MB limit)
	if (file.size > 2 * 1024 * 1024) {
		alert("Image size must be less than 2MB");
		return;
	}

	// Show preview
	const reader = new FileReader();
	reader.onload = function (e) {
		updateAvatarPreview(e.target.result);
	};
	reader.readAsDataURL(file);

	// Upload file
	uploadAvatarFile(file);
}

function updateAvatarPreview(imageSrc) {
	$(".avatar-image").attr("src", imageSrc);
	$(".avatar")
		.removeClass("avatar-initials avatar-icon")
		.addClass("avatar-image");
}

function uploadAvatarFile(file) {
	const formData = new FormData();
	formData.append("avatar", file);

	$.ajax({
		url: "/api/upload-avatar/",
		method: "POST",
		data: formData,
		processData: false,
		contentType: false,
		success: function (response) {
			if (response.success) {
				updateAvatarPreview(response.avatar_url);
				showNotification("Avatar updated successfully", "success");
			} else {
				showNotification("Failed to update avatar", "error");
			}
		},
		error: function () {
			showNotification("Error uploading avatar", "error");
		},
	});
}
```

### Avatar Status Updates

```javascript
// Update avatar status
function updateAvatarStatus(userId, status) {
	const avatar = $(`.avatar[data-user-id="${userId}"]`);

	// Remove existing status classes
	avatar.removeClass(
		"avatar-status-online avatar-status-away avatar-status-busy avatar-status-offline"
	);

	// Add new status class
	if (status) {
		avatar.addClass("avatar-with-status").addClass(`avatar-status-${status}`);
	} else {
		avatar.removeClass("avatar-with-status");
	}
}

// Real-time status updates via WebSocket
function handleStatusUpdate(data) {
	updateAvatarStatus(data.user_id, data.status);
}
```

## Best Practices

### 1. Consistent Sizing

```python
# Use consistent avatar sizes across the application
AVATAR_SIZES = {
    'thumbnail': 'small',    # 32px - for lists, comments
    'profile': 'medium',     # 48px - for user profiles
    'header': 'large',       # 64px - for page headers
    'hero': 'xlarge'         # 96px - for hero sections
}

def create_consistent_avatar(user, context='profile'):
    size = AVATAR_SIZES.get(context, 'medium')
    return create_user_avatar(user, size=size)
```

### 2. Color Generation

```python
# Generate consistent colors for users
def generate_user_color(user_id):
    """Generate consistent color based on user ID."""
    colors = [
        '#007acc', '#28a745', '#dc3545', '#ffc107',
        '#17a2b8', '#6f42c1', '#fd7e14', '#20c997'
    ]
    return colors[user_id % len(colors)]
```

### 3. Accessibility

```python
# Ensure avatars are accessible
def create_accessible_avatar(user, **kwargs):
    return render_avatar(
        alt=f"Avatar for {user.get_full_name()}",
        **kwargs,
        **{
            "role": "img",
            "aria-label": f"Profile picture of {user.get_full_name()}"
        }
    )
```

### 4. Performance Optimization

```python
# Optimize avatar loading
def create_optimized_avatar(user, size="medium"):
    if user.profile_picture:
        # Use appropriate image size
        image_url = get_thumbnail_url(user.profile_picture, size)
        return render_avatar(
            src=image_url,
            alt=user.get_full_name(),
            size=size,
            loading="lazy"  # Lazy loading for performance
        )

    return render_avatar(
        initials=get_user_initials(user),
        background_color=generate_user_color(user.id),
        size=size
    )
```

## Related Components

- [Buttons](buttons.md) - For avatar edit buttons
- [Icons](icons.md) - For avatar icons and status indicators
- [Images](images.md) - For avatar image handling
- [Badges](badges.md) - For avatar status badges
