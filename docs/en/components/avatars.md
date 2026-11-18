# Avatars

MetroUI provides several types of avatar components for displaying user profile images, icons, or initials.

## Initials Avatars

The initials avatar component generates actual image files from names using PIL (Pillow), with support for multiple formats and responsive design. By default, images are automatically generated for all sizes and saved to `/media/avatars/initials/{initial}/{size}.{format}`, with responsive HTML output using `<figure>` and `<picture>` elements.

> **⚠️ Custom Development Notice**: This `initials_avatar` functionality is **custom development** and not part of MetroUI core. It provides advanced image generation capabilities beyond the standard MetroUI avatar system.

### Basic Usage

```python
from metroui5.components import render_initials_avatar

# Basic initials avatar
avatar_html = avatar_initials("John Doe")

# Note: initials_avatar is custom development, not part of MetroUI core
```

### Django Template Usage

**Note**: The `initials_avatar` functionality is custom development and not part of MetroUI core. You can use it directly in Python code or create your own templatetag.

#### **Creating Your Own Templatetag**

To use this in Django templates, you'll need to create your own templatetag. Here's how:

1. **Create a templatetags directory** in your app:

```bash
mkdir myapp/templatetags
touch myapp/templatetags/__init__.py
touch myapp/templatetags/avatar_tags.py
```

2. **Define the templatetag** in `avatar_tags.py`:

```python
from django import template
from django.utils.safestring import mark_safe
from metroui5.components import render_initials_avatar

register = template.Library()

@register.simple_tag
def avatar_initials(name, **kwargs):
    """Renders initials avatar."""
    return mark_safe(render_initials_avatar(name, **kwargs))
```

3. **Load and use in templates**:

```django
{% load avatar_tags %}

{% avatar_initials "John Doe" %}
{% avatar_initials "Jane Smith" size="large" bg_color="#e74c3c" %}
```

```django
<!-- Custom templatetag (if you create one) -->
{% load your_custom_tags %}

<!-- Basic initials avatar -->
{% avatar_initials "John Doe" %}

<!-- With custom size -->
{% avatar_initials "Jane Smith" size="large" %}

<!-- With custom colors -->
{% avatar_initials "Bob Wilson" bg_color="#e74c3c" text_color="white" %}
```

### Parameters

| Parameter       | Type   | Default         | Description                                       |
| --------------- | ------ | --------------- | ------------------------------------------------- |
| `name`          | string | required        | Full name to generate initials from               |
| `size`          | string | "medium"        | Avatar size: "small", "medium", "large", "xlarge" |
| `bg_color`      | string | auto-generated  | Background color (hex code or color name)         |
| `text_color`    | string | "white"         | Text color (hex code or color name)               |
| `font_size`     | int    | auto-calculated | Font size in pixels                               |
| `font_weight`   | string | "bold"          | Font weight                                       |
| `shape`         | string | "circle"        | Avatar shape: "circle", "square", "rounded"       |
| `max_initials`  | int    | 2               | Maximum number of initials to show                |
| `output_format` | string | "png"           | Image format: "png", "jpg", "webp"                |
| `save_path`     | string | None            | File path to save the generated image             |

### Examples

#### Different Sizes

```django
{% avatar_initials "John Doe" size="small" %}
{% avatar_initials "John Doe" size="medium" %}
{% avatar_initials "John Doe" size="large" %}
{% avatar_initials "John Doe" size="xlarge" %}
```

#### Different Shapes

```django
{% avatar_initials "John Doe" shape="circle" %}
{% avatar_initials "John Doe" shape="square" %}
{% avatar_initials "John Doe" shape="rounded" %}
```

#### Custom Colors

```django
{% avatar_initials "John Doe" bg_color="#e74c3c" %}
{% avatar_initials "John Doe" bg_color="#3498db" text_color="white" %}
{% avatar_initials "John Doe" bg_color="#2ecc71" text_color="white" %}
```

#### Multiple Initials

```django
{% avatar_initials "John Michael Smith" max_initials=3 %}
{% avatar_initials "Maria Isabella Rodriguez" max_initials=3 %}
```

#### Different Image Formats

```django
{% avatar_initials "John Doe" output_format="png" %}
{% avatar_initials "Jane Smith" output_format="jpg" %}
{% avatar_initials "Bob Wilson" output_format="webp" %}
```

#### Default File Saving

By default, avatars are automatically generated for all sizes and saved to `/media/avatars/initials/{initial}/{size}.{format}`:

```django
{% avatar_initials "John Doe" %}
<!-- Generates and saves: -->
<!--   /media/avatars/initials/JD/small.png (48x48) -->
<!--   /media/avatars/initials/JD/medium.png (64x64) -->
<!--   /media/avatars/initials/JD/large.png (96x96) -->
<!--   /media/avatars/initials/JD/xlarge.png (128x128) -->
<!-- Returns responsive <figure> with <picture> elements -->
```

#### Responsive HTML Output

The component automatically generates responsive HTML using `<figure>` and `<picture>` elements:

```html
<figure class="avatar-figure">
	<picture>
		<source
			media="(max-width: 480px)"
			srcset="/media/avatars/initials/JD/small.png"
		/>
		<source
			media="(max-width: 768px)"
			srcset="/media/avatars/initials/JD/medium.png"
		/>
		<source
			media="(max-width: 1024px)"
			srcset="/media/avatars/initials/JD/large.png"
		/>
		<source
			media="(min-width: 1025px)"
			srcset="/media/avatars/initials/JD/xlarge.png"
		/>
		<img
			src="/media/avatars/initials/JD/medium.png"
			alt="Avatar for John Doe"
			class="avatar-img"
		/>
	</picture>
</figure>
```

#### Custom File Paths

To save to a custom location (disables responsive generation):

```django
{% avatar_initials "John Doe" save_path="/path/to/avatar.png" %}
{% avatar_initials "Jane Smith" save_path="/path/to/avatar.jpg" output_format="jpg" %}
```

## 📋 **Detailed Attribute Reference**

### **Core Attributes**

#### **`name` (required)**

The full name to generate initials from. Supports multiple formats:

```django
{% avatar_initials "John Doe" %}
{% avatar_initials "Jane Smith-Jones" %}
{% avatar_initials "Dr. Robert James Wilson Jr." %}
```

#### **`size`**

Controls the avatar size. When not specified, all sizes are generated automatically for responsive design.

```django
{% avatar_initials "John Doe" size="small" %}      <!-- 48x48px -->
{% avatar_initials "John Doe" size="medium" %}     <!-- 64x64px -->
{% avatar_initials "John Doe" size="large" %}      <!-- 96x96px -->
{% avatar_initials "John Doe" size="xlarge" %}     <!-- 128x128px -->
```

**Available sizes:**

- **`small`**: 48×48 pixels (mobile devices)
- **`medium`**: 64×64 pixels (tablets)
- **`large`**: 96×96 pixels (desktops)
- **`xlarge`**: 128×128 pixels (large screens)

### **Appearance Attributes**

#### **`bg_color`**

Background color for the avatar. Can be hex codes or color names.

```django
{% avatar_initials "John Doe" bg_color="#e74c3c" %}
{% avatar_initials "John Doe" bg_color="red" %}
{% avatar_initials "John Doe" bg_color="#3498db" %}
```

**Supported color formats:**

- **Hex codes**: `#ff0000`, `#e74c3c`, `#3498db`
- **Color names**: `red`, `blue`, `green`, `white`, `black`, `orange`, `purple`, `pink`, `yellow`, `gray`, `brown`, `gold`

#### **`text_color`**

Color of the initials text. Defaults to white for good contrast.

```django
{% avatar_initials "John Doe" text_color="black" %}
{% avatar_initials "John Doe" text_color="#ffffff" %}
{% avatar_initials "John Doe" text_color="gold" %}
```

#### **`shape`**

Avatar shape. All shapes maintain the same dimensions.

```django
{% avatar_initials "John Doe" shape="circle" %}    <!-- Circular -->
{% avatar_initials "John Doe" shape="square" %}    <!-- Square -->
{% avatar_initials "John Doe" shape="rounded" %}   <!-- Rounded corners -->
```

**Available shapes:**

- **`circle`**: Perfect circle (default)
- **`square`**: Sharp square corners
- **`rounded`**: Square with rounded corners

### **Typography Attributes**

#### **`font_size`**

Custom font size in pixels. Overrides automatic calculation.

```django
{% avatar_initials "John Doe" font_size="24" %}
{% avatar_initials "John Doe" font_size="32" %}
```

**Note**: When not specified, font size is automatically calculated based on avatar size and text length.

#### **`font_weight`**

Font weight for the initials. Currently supports "bold" (default).

```django
{% avatar_initials "John Doe" font_weight="bold" %}
```

#### **`max_initials`**

Maximum number of initials to display from the name.

```django
{% avatar_initials "John Doe" max_initials="1" %}      <!-- Shows: J -->
{% avatar_initials "John Doe" max_initials="2" %}      <!-- Shows: JD -->
{% avatar_initials "John Michael Smith" max_initials="3" %} <!-- Shows: JMS -->
```

**Default**: 2 initials
**Range**: 1-4 initials recommended for readability

### **Output Attributes**

#### **`output_format`**

Image format for generated avatars.

```django
{% avatar_initials "John Doe" output_format="png" %}   <!-- PNG (default) -->
{% avatar_initials "John Doe" output_format="jpg" %}   <!-- JPEG -->
{% avatar_initials "John Doe" output_format="webp" %}  <!-- WebP -->
```

**Supported formats:**

- **`png`**: Lossless, supports transparency (default)
- **`jpg`**: Compressed, smaller file size
- **`webp`**: Modern format, excellent compression

#### **`save_path`**

Custom file path for saving. When specified, disables responsive generation.

```django
{% avatar_initials "John Doe" save_path="/custom/path/avatar.png" %}
{% avatar_initials "John Doe" save_path="/avatars/john.jpg" output_format="jpg" %}
```

**Note**: Using `save_path` will:

- Generate only one image at the specified size
- Save to the exact path provided
- Return a simple `<img>` tag instead of responsive HTML

### **HTML Attributes**

All standard HTML attributes are supported and will be applied to the generated elements:

```django
{% avatar_initials "John Doe" class="my-avatar" %}
{% avatar_initials "John Doe" id="user-avatar" %}
{% avatar_initials "John Doe" data-user-id="123" %}
{% avatar_initials "John Doe" style="border: 2px solid #ccc;" %}
```

**Common HTML attributes:**

- **`class`**: CSS classes for styling
- **`id`**: Unique identifier
- **`style`**: Inline CSS styles
- **`data-*`**: Custom data attributes
- **`title`**: Tooltip text
- **`onclick`**: JavaScript event handlers

## 🎯 **Practical Examples & Use Cases**

## 🔧 **Attribute Combinations & Best Practices**

### **Recommended Attribute Combinations**

#### **Mobile-First Design**

```django
{% avatar_initials user.name
   shape="circle"
   class="mobile-avatar"
   style="max-width: 100%; height: auto;" %}
```

#### **Professional Business Cards**

```django
{% avatar_initials contact.name
   bg_color="#2c3e50"
   text_color="white"
   shape="rounded"
   class="business-card-avatar" %}
```

#### **Social Media Profiles**

```django
{% avatar_initials profile.name
   bg_color="#e74c3c"
   shape="circle"
   class="social-avatar"
   data-platform="twitter" %}
```

### **Performance Optimization Tips**

#### **Use Appropriate Formats**

- **`png`**: For avatars with transparency or when quality is priority
- **`jpg`**: For smaller file sizes (no transparency needed)
- **`webp`**: For modern browsers with excellent compression

#### **Size Selection Strategy**

- **Always generate all sizes**: Enables responsive design
- **Use `save_path` sparingly**: Only when you need a specific file location
- **Leverage browser caching**: Different sizes can have different cache strategies

### **Accessibility Best Practices**

#### **Always Include Alt Text**

```django
{% avatar_initials user.name
   alt="Avatar for {{ user.name }}"
   title="{{ user.name }}'s profile picture" %}
```

#### **Color Contrast**

- Ensure sufficient contrast between background and text colors
- Test with color blindness simulators
- Provide alternative styling for high contrast mode

### **Responsive Design Guidelines**

#### **Breakpoint Strategy**

The component automatically handles these breakpoints:

- **Mobile**: ≤480px → Small avatar (48×48)
- **Tablet**: ≤768px → Medium avatar (64×64)
- **Desktop**: ≤1024px → Large avatar (96×96)
- **Large Screen**: >1024px → XLarge avatar (128×128)

#### **CSS Media Queries**

```css
/* Custom breakpoints if needed */
@media (max-width: 320px) {
	.avatar-figure img {
		max-width: 40px;
	}
}

@media (min-width: 1440px) {
	.avatar-figure img {
		max-width: 160px;
	}
}
```

## 🎯 **Practical Examples & Use Cases**

### **Basic Usage Examples**

#### **Simple Avatar**

```django
{% avatar_initials "John Doe" %}
<!-- Generates responsive avatar with all sizes -->
```

#### **Custom Styling**

```django
{% avatar_initials "Jane Smith"
   bg_color="#e74c3c"
   text_color="white"
   shape="rounded"
   class="user-avatar" %}
```

#### **Professional Look**

```django
{% avatar_initials "Dr. Robert Wilson"
   bg_color="#2c3e50"
   text_color="gold"
   shape="circle"
   max_initials="3" %}
```

### **Advanced Use Cases**

#### **User Profile Avatars**

```django
{% avatar_initials user.full_name
   size="large"
   class="profile-avatar"
   id="user-{{ user.id }}-avatar"
   data-user-id="{{ user.id }}" %}
```

#### **Team Member Avatars**

```django
{% avatar_initials team_member.name
   bg_color="#3498db"
   shape="square"
   class="team-avatar"
   title="{{ team_member.role }}" %}
```

#### **Status-Based Avatars**

```django
{% avatar_initials user.name
   bg_color=user.status_color
   class="status-avatar status-{{ user.status }}"
   data-status="{{ user.status }}" %}
```

#### **Custom File Paths**

```django
{% avatar_initials "John Doe"
   save_path="/media/users/john/avatar.png"
   output_format="jpg" %}
```

### **CSS Integration Examples**

#### **Responsive Grid Layout**

```css
.avatar-figure {
	display: inline-block;
	margin: 8px;
}

.avatar-figure img {
	border-radius: 50%;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
	transition: transform 0.2s ease;
}

.avatar-figure img:hover {
	transform: scale(1.1);
}
```

#### **Size-Based Styling**

```css
.avatar-figure img[src*="small"] {
	border: 2px solid #e0e0e0;
}

.avatar-figure img[src*="large"] {
	border: 3px solid #2196f3;
}
```

### **JavaScript Integration**

#### **Dynamic Avatar Updates**

```javascript
// Update avatar background color based on user status
function updateAvatarStatus(userId, status) {
	const avatar = document.querySelector(`[data-user-id="${userId}"]`);
	if (avatar) {
		avatar.style.backgroundColor = getStatusColor(status);
	}
}
```

#### **Avatar Click Events**

```django
{% avatar_initials user.name
   onclick="showUserProfile('{{ user.id }}')"
   class="clickable-avatar" %}
```

## 🔧 **Core Avatar Functions**

### **`render_initials_avatar` Function**

The `render_initials_avatar` function is the main entry point for generating initials avatars. It automatically handles all the complexity of image generation, responsive sizing, and HTML output.

#### **Function Signature**

```python
def render_initials_avatar(name, **attr):
    """
    Renders custom initials avatar component.

    Args:
        name: Full name to generate initials from
        **attr: Additional attributes for customization

    Returns:
        HTML string with responsive avatar figure or img element
    """
```

#### **Core Functionality**

- **Automatic Initials Extraction**: Intelligently extracts initials from full names
- **Smart Color Generation**: Creates consistent background colors using name hashing
- **Multi-Size Generation**: Automatically generates all responsive sizes
- **Font Management**: Uses Geologica font with system font fallbacks
- **Responsive Output**: Returns HTML5 `<figure>` and `<picture>` elements

#### **Internal Helper Functions**

##### **`generate_initials(full_name, max_count=2)`**

Extracts initials from names with smart handling:

```python
generate_initials("John Doe")           # Returns: "JD"
generate_initials("Dr. Jane Smith")     # Returns: "JS"
generate_initials("Mary-Jane Wilson")   # Returns: "MW"
generate_initials("O'Connor")           # Returns: "OC"
```

##### **`generate_bg_color(full_name)`**

Creates consistent colors using MD5 hashing:

- **Deterministic**: Same name always produces same color
- **Color Palette**: 20 predefined professional colors
- **Contrast Optimized**: Ensures good readability

##### **`color_to_rgb(color)`**

Converts colors to RGB tuples:

- **Hex Support**: `#ff0000` → `(255, 0, 0)`
- **Color Names**: `"red"` → `(255, 0, 0)`
- **Fallback**: Invalid colors default to white

##### **`get_size_dimensions(size)`**

Maps size names to pixel dimensions:

```python
get_size_dimensions("small")   # Returns: 48
get_size_dimensions("medium")  # Returns: 64
get_size_dimensions("large")   # Returns: 96
get_size_dimensions("xlarge")  # Returns: 128
```

##### **`get_font_size(avatar_size, text_length)`**

Calculates optimal font sizes:

- **Base Calculation**: `avatar_size * 0.4`
- **Text Length Adjustment**: Longer text gets smaller fonts
- **Override Support**: Custom `font_size` attribute takes precedence

##### **`generate_avatar_image(initials, dimensions, bg_color, text_color, font_size, shape)`**

Core image generation using PIL:

- **Background Shapes**: Circle, square, rounded rectangle
- **Font Loading**: Geologica → System fonts → Default fallback
- **Text Centering**: Precise positioning with font baseline adjustment
- **Anti-aliasing**: High-quality rendering for all sizes

### **`render_responsive_avatar` Function**

Creates responsive HTML structure with `<picture>` elements:

#### **HTML Output Structure**

```html
<figure class="avatar-figure">
	<picture>
		<source
			media="(max-width: 480px)"
			srcset="/media/avatars/initials/JD/small.png"
		/>
		<source
			media="(max-width: 768px)"
			srcset="/media/avatars/initials/JD/medium.png"
		/>
		<source
			media="(max-width: 1024px)"
			srcset="/media/avatars/initials/JD/large.png"
		/>
		<source
			media="(min-width: 1025px)"
			srcset="/media/avatars/initials/JD/xlarge.png"
		/>
		<img
			src="/media/avatars/initials/JD/medium.png"
			alt="Avatar for John Doe"
			class="avatar-img"
		/>
	</picture>
</figure>
```

#### **Media Query Breakpoints**

- **Mobile**: `≤480px` → Small avatar (48×48)
- **Tablet**: `≤768px` → Medium avatar (64×64)
- **Desktop**: `≤1024px` → Large avatar (96×96)
- **Large Screen**: `>1024px` → XLarge avatar (128×128)

### **`render_image_avatar` Function**

Simple image tag renderer for custom paths:

```python
def render_image_avatar(image_url, **attrs):
    """Renders a simple img tag with the given URL and attributes"""
    img_attrs = {"src": image_url, **attrs}
    return render_tag("img", attrs=img_attrs, close=False)
```

## 🏗️ **Technical Implementation Details**

### **Image Generation Pipeline**

#### **1. Name Processing**

```python
# Input: "Dr. John Michael Smith-Jones"
name_parts = re.split(r'[\s\-_]+', full_name.strip())
# Result: ["Dr.", "John", "Michael", "Smith", "Jones"]

# Extract initials (max 2 by default)
initials = [part[0].upper() for part in name_parts[:max_count]]
# Result: ["J", "M"] → "JM"
```

#### **2. Color Generation Algorithm**

```python
# Create MD5 hash from lowercase name
name_hash = hashlib.md5(full_name.lower().encode()).hexdigest()

# Use first 8 characters of hash for color selection
color_index = int(name_hash[:8], 16) % len(colors)
selected_color = colors[color_index]
```

#### **3. Font Loading Strategy**

```python
# Priority order for font loading
geologica_paths = [
    "/System/Library/Fonts/Geologica.ttf",           # macOS
    "/usr/share/fonts/truetype/google/Geologica.ttf", # Linux
    "~/.fonts/Geologica.ttf",                        # User fonts
    "metroui5/static/fonts/Geologica.ttf",           # Package fonts
]

# Fallback chain: Geologica → Arial Bold → Helvetica → DejaVu → Default
```

#### **4. Text Positioning Algorithm**

```python
# Calculate text dimensions
bbox = draw.textbbox((0, 0), initials, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Center horizontally and vertically
x = (dimensions - text_width) // 2
y = (dimensions - text_height) // 2

# Adjust for font baseline
font_ascent = font.getmetrics()[0]
y = y - font_ascent // 4
```

### **File Organization Strategy**

#### **Directory Structure**

```
/media/avatars/initials/
├── JD/                    # John Doe
│   ├── small.png         # 48×48px (mobile)
│   ├── medium.png        # 64×64px (tablet)
│   ├── large.png         # 96×96px (desktop)
│   └── xlarge.png        # 128×128px (large screens)
├── JS/                    # Jane Smith
│   ├── small.png
│   ├── medium.png
│   ├── large.png
│   └── xlarge.png
└── ...
```

#### **File Naming Convention**

- **Format**: `{size}.{format}`
- **Examples**: `small.png`, `medium.jpg`, `large.webp`
- **Consistency**: All sizes use same naming pattern

### **Performance Optimizations**

#### **1. Lazy Generation**

- Images are only generated when first requested
- Subsequent requests use cached files
- Automatic directory creation on first use

#### **2. Font Caching**

- Font objects are loaded once per process
- Fallback fonts are tried in order of preference
- System font detection avoids repeated file system calls

#### **3. Memory Management**

- PIL images are properly disposed after saving
- Temporary buffers are cleaned up automatically
- File handles are closed immediately after use

#### **4. Responsive Loading**

- Browser automatically selects appropriate size
- No JavaScript required for size switching
- CSS media queries handle all responsive behavior

### **Error Handling & Fallbacks**

#### **1. Font Loading Failures**

```python
try:
    font = ImageFont.truetype(geologica_path, font_size)
except:
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()  # Final fallback
```

#### **2. Django Settings Unavailable**

```python
try:
    # Try to use Django settings for file saving
    from django.conf import settings
    # ... file saving logic
except Exception:
    # Fallback to base64 data URLs
    buffer = io.BytesIO()
    img.save(buffer, format=format)
    data_url = f"data:image/{format};base64,{base64_data}"
```

#### **3. File System Errors**

- Directory creation with `exist_ok=True`
- Graceful handling of permission issues
- Fallback to base64 when file saving fails

### **Advanced Usage Patterns**

#### **1. Custom Color Palettes**

```python
# Override default color palette
custom_colors = ["#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4"]
# Use in custom implementation
```

#### **2. Dynamic Font Sizing**

```python
# Custom font size calculation
def custom_font_size(avatar_size, text_length):
    base_size = avatar_size * 0.35  # Smaller than default
    if text_length > 2:
        base_size *= 0.7  # More aggressive scaling
    return int(base_size)
```

#### **3. Batch Generation**

```python
# Generate avatars for multiple users
users = ["John Doe", "Jane Smith", "Bob Johnson"]
for user in users:
    avatar_html = avatar_initials(user)
    # Store or display avatar_html
```

#### **4. Custom Shape Rendering**

```python
# Extend shape support
def custom_shape_draw(draw, dimensions, bg_color):
    # Custom shape logic
    draw.polygon([(0, 0), (dimensions, 0), (dimensions//2, dimensions)], fill=bg_color)
```

## 🔧 **Custom Development Integration**

### **About This Functionality**

The `initials_avatar` system is **custom development** and not part of MetroUI core. It provides:

- **Image Generation**: Creates actual PNG/JPG/WebP files using PIL
- **Responsive Output**: Generates HTML5 `<figure>` and `<picture>` elements
- **Automatic Sizing**: Creates all responsive sizes automatically
- **File Management**: Saves to organized directory structure
- **Font Integration**: Uses Geologica font with system fallbacks

### **Integration Options**

1. **Direct Python Usage**: Import and call functions directly
2. **Custom Templatetag**: Create your own Django templatetag
3. **API Integration**: Use as part of a REST API or service
4. **Background Processing**: Generate avatars asynchronously

### **File Structure Created**

```
/media/avatars/initials/
├── JD/                    # John Doe
│   ├── small.png         # 48×48px
│   ├── medium.png        # 64×64px
│   ├── large.png         # 96×96px
│   └── xlarge.png        # 128×128px
└── JS/                    # Jane Smith
    ├── small.png
    ├── medium.png
    ├── large.png
    └── xlarge.png
```

## 🔗 **MetroUI Core vs Custom Development**

### **MetroUI Core Functions**

These are the standard MetroUI avatar functions that come with the framework:

- **`render_avatar`**: Basic image avatar display (for existing image files)
- **`render_icon_avatar`**: Icon-based avatars using MetroUI icon font

### **Custom Development Functions**

These are additional functions you've developed:

- **`render_initials_avatar`**: Advanced initials avatar with image generation
- **`render_image_avatar`**: Simple image tag renderer
- **`render_responsive_avatar`**: Responsive HTML structure generator

### **Integration Strategy**

- Use MetroUI core functions for standard UI elements
- Use custom functions for advanced avatar generation needs
- Combine both for comprehensive avatar systems

## 🎨 **Additional Avatar Functions**

### **`render_icon_avatar` Function**

Renders MetroUI icon-based avatars using the MetroUI icon font:

#### **Function Signature**

```python
def render_icon_avatar(icon_name, **icon_attrs):
    """
    Renders MetroUI icon avatar component.

    Args:
        icon_name: MetroUI icon name (without 'mif-' prefix)
        **icon_attrs: Additional icon attributes

    Returns:
        HTML string with icon avatar span element
    """
```

#### **Usage Examples**

```django
{% render_icon_avatar "user" %}
{% render_icon_avatar "home" size="3" %}
{% render_icon_avatar "star" text_color="yellow" bg_color="blue" %}
```

#### **Supported Attributes**

- **`icon_name`**: MetroUI icon identifier (required)
- **`size`**: Icon size multiplier (1-10, adds `mif-{size}x` class)
- **`text_color`**: Text color (adds `fg-{color}` class)
- **`bg_color`**: Background color (adds `bg-{color}` class)

#### **Generated HTML**

```html
<!-- Basic usage -->
<span class="mif-user"></span>

<!-- With size and colors -->
<span class="mif-star mif-3x fg-yellow bg-blue"></span>
```

### **Icon Avatar vs Initials Avatar**

#### **When to Use Icon Avatars**

- **System/UI elements**: Navigation, buttons, toolbars
- **Generic representations**: Default user, placeholders
- **Consistent branding**: MetroUI design system compliance
- **Simple interactions**: Clickable elements, status indicators

#### **When to Use Initials Avatars**

- **User profiles**: Personal identification, user lists
- **Team management**: Member identification, contact lists
- **Personalized content**: User-specific data, custom branding
- **Professional appearance**: Business applications, corporate use

#### **Combination Usage**

```django
<!-- User list with fallback -->
{% if user.avatar_image %}
    <img src="{{ user.avatar_image.url }}" alt="{{ user.name }}">
{% elif user.initials %}
    {% avatar_initials user.name %}
{% else %}
    {% metroui5_icon_avatar "user" %}
{% endif %}
```

## 🚨 **Troubleshooting & Common Issues**

### **Common Problems & Solutions**

#### **Avatar Not Displaying**

```django
<!-- ❌ Incorrect: Missing quotes around name -->
{% avatar_initials John Doe %}

<!-- ✅ Correct: Name in quotes -->
{% avatar_initials "John Doe" %}
```

#### **Colors Not Working**

```django
<!-- ❌ Incorrect: Invalid color format -->
{% avatar_initials "John Doe" bg_color="invalid-color" %}

<!-- ✅ Correct: Use hex codes or valid color names -->
{% avatar_initials "John Doe" bg_color="#e74c3c" %}
{% avatar_initials "John Doe" bg_color="red" %}
```

#### **File Permission Issues**

If avatars aren't being saved, check:

- Django `MEDIA_ROOT` directory permissions
- Write access to `/media/avatars/initials/` folder
- Django `MEDIA_URL` configuration in settings

#### **Font Loading Problems**

The component automatically falls back to system fonts if Geologica isn't available:

- Check if Geologica font is in the correct location
- Verify font file integrity
- System fonts will be used as fallback

### **Debug Mode**

Enable Django debug mode to see detailed error messages:

```python
# settings.py
DEBUG = True
```

### **Testing Individual Components**

Test specific attributes in isolation:

```django
<!-- Test basic functionality -->
{% avatar_initials "Test User" %}

<!-- Test custom colors -->
{% avatar_initials "Test User" bg_color="#ff0000" %}

<!-- Test custom size -->
{% avatar_initials "Test User" size="large" %}
```

### **Performance Monitoring**

Monitor avatar generation performance:

- Check file sizes in `/media/avatars/initials/`
- Verify responsive images are being generated
- Monitor browser network tab for image loading

## 📋 **Complete Function Reference**

### **Core Avatar Functions Summary**

| Function                   | Purpose                   | Output                   | Use Case                       |
| -------------------------- | ------------------------- | ------------------------ | ------------------------------ |
| `render_initials_avatar`   | Advanced initials avatar  | Responsive HTML          | User profiles, team management |
| `render_icon_avatar`       | Icon-based avatars        | Icon spans               | System UI, navigation          |
| `render_image_avatar`      | Simple image tags         | `<img>` elements         | Custom file paths              |
| `render_responsive_avatar` | Responsive HTML structure | `<figure>` + `<picture>` | Responsive design              |

### **Attribute Compatibility Matrix**

| Attribute       | `render_initials_avatar` | `render_icon_avatar` | `render_image_avatar` |
| --------------- | ------------------------ | -------------------- | --------------------- |
| `name`          | ✅ Required              | ❌                   | ❌                    |
| `icon_name`     | ❌                       | ✅ Required          | ❌                    |
| `image_url`     | ❌                       | ❌                   | ✅ Required           |
| `size`          | ✅                       | ❌                   | ❌                    |
| `size`          | ✅                       | ✅                   | ❌                    |
| `bg_color`      | ✅                       | ✅                   | ❌                    |
| `text_color`    | ✅                       | ✅                   | ❌                    |
| `shape`         | ✅                       | ❌                   | ❌                    |
| `font_size`     | ✅                       | ❌                   | ❌                    |
| `max_initials`  | ✅                       | ❌                   | ❌                    |
| `output_format` | ✅                       | ❌                   | ❌                    |
| `save_path`     | ✅                       | ❌                   | ❌                    |
| HTML attributes | ✅ All                   | ✅ All               | ✅ All                |

### **Performance Characteristics**

| Function                   | Image Generation | File I/O         | Memory Usage | Responsiveness      |
| -------------------------- | ---------------- | ---------------- | ------------ | ------------------- |
| `render_initials_avatar`   | ⚡ Fast (PIL)    | 📁 Creates files | 💾 Low       | 📱 Fully responsive |
| `render_icon_avatar`       | ❌ None          | ❌ None          | 💾 Minimal   | 📱 CSS responsive   |
| `render_image_avatar`      | ❌ None          | ❌ None          | 💾 Minimal   | 📱 Basic            |
| `render_responsive_avatar` | ❌ None          | ❌ None          | 💾 Minimal   | 📱 Fully responsive |

### **Best Practices Summary**

#### **1. Choose the Right Function**

- **User avatars**: Use `render_initials_avatar` for personalized content
- **System icons**: Use `render_icon_avatar` for UI elements
- **Custom images**: Use `render_image_avatar` with `save_path`

#### **2. Optimize for Performance**

- **Leverage caching**: Generated images are cached automatically
- **Use appropriate formats**: PNG for quality, JPG for size, WebP for modern browsers
- **Responsive design**: Let the browser choose optimal image sizes
- **Font optimization**: Geologica provides excellent quality with fallbacks

#### **3. Ensure Accessibility**

- **Always include alt text**: Automatic generation with `render_initials_avatar`
- **Color contrast**: Test background/text color combinations
- **Semantic HTML**: Uses proper `<figure>` and `<picture>` elements
- **Screen reader support**: Proper alt attributes and ARIA labels

#### **4. Maintain Consistency**

- **Color schemes**: Use consistent color palettes across your application
- **Size standards**: Stick to the predefined size options
- **Shape consistency**: Choose one shape style for your brand
- **Font usage**: Geologica provides professional typography

### **Migration Guide**

#### **From Simple Images**

```django
<!-- Before: Static image -->
<img src="/static/default-avatar.png" alt="User Avatar">

<!-- After: Dynamic initials avatar -->
{% avatar_initials user.name alt="Avatar for {{ user.name }}" %}
```

#### **From Icon-Only Avatars**

```django
<!-- Before: Generic icon -->
<span class="mif-user mif-2x"></span>

<!-- After: Personalized initials avatar -->
{% avatar_initials user.name size="medium" %}
```

#### **From Custom Avatar Systems**

```django
<!-- Before: Custom avatar logic -->
{% if user.avatar %}
    <img src="{{ user.avatar.url }}" alt="{{ user.name }}">
{% else %}
    <div class="default-avatar">{{ user.initials }}</div>
{% endif %}

<!-- After: Unified avatar system -->
{% avatar_initials user.name %}
```

### Features

- **Image Generation**: Creates actual image files using PIL (Pillow)
- **Multiple Formats**: Supports PNG, JPG, and WebP formats
- **Responsive Design**: Automatically generates all sizes and outputs responsive HTML with `<figure>` and `<picture>` elements
- **Automatic Size Generation**: Creates small, medium, large, and xlarge variants automatically
- **Default File Saving**: Automatically saves to `/media/avatars/initials/{initial}/{size}.{format}`
- **Custom Paths**: Can save to custom file paths when specified
- **Consistent Colors**: Automatically generates consistent background colors from names
- **Flexible Sizing**: Supports small, medium, large, and xlarge sizes
- **Multiple Shapes**: Circle, square, and rounded rectangle options
- **Smart Initials**: Automatically extracts initials from full names
- **Font Fallbacks**: Automatically finds system fonts or falls back to default
- **High Quality**: Generates crisp, scalable images

### Generated HTML

The function generates responsive HTML with `<figure>` and `<picture>` elements like this:

```html
<figure class="avatar-figure">
	<picture>
		<source
			media="(max-width: 480px)"
			srcset="/media/avatars/initials/JD/small.png"
		/>
		<source
			media="(max-width: 768px)"
			srcset="/media/avatars/initials/JD/medium.png"
		/>
		<source
			media="(max-width: 1024px)"
			srcset="/media/avatars/initials/JD/large.png"
		/>
		<source
			media="(min-width: 1025px)"
			srcset="/media/avatars/initials/JD/xlarge.png"
		/>
		<img
			src="/media/avatars/initials/JD/medium.png"
			alt="Avatar for John Doe"
			class="avatar-img"
		/>
	</picture>
</figure>
```

### Color Generation

The component automatically generates consistent background colors from names using a hash-based algorithm. The same name will always generate the same color, making it easy to identify users consistently.

### Accessibility

The component includes proper accessibility features:

- `aria-label` attribute with descriptive text
- `title` attribute showing the full name on hover
- Semantic HTML structure
- High contrast color combinations

## Image Avatars

For displaying actual profile images:

```python
from metroui5.components import render_avatar

# Image avatar
avatar_html = render_avatar("/static/images/profile.jpg")
```

## Icon Avatars

For displaying icon-based avatars:

```python
from metroui5.components import render_icon_avatar

# Icon avatar
avatar_html = render_icon_avatar("user")
```

## 📋 **Summary & Best Practices**

### **What You've Built**

You've created a comprehensive initials avatar system that extends MetroUI with:

- **Advanced Image Generation**: PIL-based avatar creation with multiple formats
- **Responsive Design**: Automatic generation of all sizes with HTML5 responsive elements
- **Smart File Management**: Organized directory structure with automatic cleanup
- **Professional Typography**: Geologica font integration with fallback support
- **Performance Optimization**: Lazy generation, caching, and memory management

### **Key Benefits**

1. **User Experience**: Personalized avatars that are consistent and professional
2. **Performance**: Responsive images that load optimally for each device
3. **Maintainability**: Clean, organized code with comprehensive error handling
4. **Scalability**: Efficient file management and caching strategies
5. **Accessibility**: Proper alt text, ARIA labels, and semantic HTML

### **Integration Recommendations**

- **Use MetroUI core** for standard avatar needs (images, icons)
- **Use your custom system** for advanced initials avatar requirements
- **Create templatetags** for easy Django template integration
- **Implement caching** for production performance
- **Monitor file storage** to manage disk space usage

### **Next Steps**

1. **Create your templatetag** for Django template usage
2. **Add to your Django app** as a custom component
3. **Configure file permissions** for the media directory
4. **Test across devices** to verify responsive behavior
5. **Monitor performance** and optimize as needed

This system provides a solid foundation for professional avatar management while maintaining the flexibility to integrate with MetroUI's existing components.
