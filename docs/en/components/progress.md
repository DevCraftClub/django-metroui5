# Progress Bars

MetroUI5 Django provides a flexible progress bar component system for displaying loading states, completion percentages, and progress indicators.

## Basic Usage

```python
from metroui5.components import render_progress

# Simple progress bar
progress_html = render_progress(value=75, max_value=100)
```

## Parameters

### `render_progress(value, max_value=100, color="blue", size="default", **attrs)`

- **value** (int): Current progress value
- **max_value** (int): Maximum progress value (default: 100)
- **color** (str): Progress bar color (blue, green, red, yellow, etc.)
- **size** (str): Progress bar size (small, default, large)
- **attrs** (dict): Additional HTML attributes

## Examples

### Basic Progress Bar

```python
from metroui5.components import render_progress

# 75% progress
progress = render_progress(value=75)
```

### Progress Bar with Custom Color

```python
# Green progress bar
progress = render_progress(value=60, color="green")

# Red progress bar
progress = render_progress(value=25, color="red")

# Yellow progress bar
progress = render_progress(value=45, color="yellow")
```

### Progress Bar with Custom Size

```python
# Small progress bar
progress = render_progress(value=50, size="small")

# Large progress bar
progress = render_progress(value=80, size="large")
```

### Progress Bar with Custom Attributes

```python
progress = render_progress(
    value=65,
    color="blue",
    size="default",
    id="upload-progress",
    class="progress-bar-custom"
)
```

## MetroUI Progress Classes

MetroUI5 provides several CSS classes for progress bar styling:

### Color Classes

- `bg-blue` - Blue progress bar
- `bg-green` - Green progress bar
- `bg-red` - Red progress bar
- `bg-yellow` - Yellow progress bar
- `bg-orange` - Orange progress bar
- `bg-purple` - Purple progress bar
- `bg-pink` - Pink progress bar
- `bg-cyan` - Cyan progress bar
- `bg-teal` - Teal progress bar
- `bg-indigo` - Indigo progress bar

### Size Classes

- `progress-small` - Small progress bar
- `progress-large` - Large progress bar
- `progress-thin` - Thin progress bar
- `progress-thick` - Thick progress bar

### Style Classes

- `progress-striped` - Striped progress bar
- `progress-animated` - Animated progress bar
- `progress-rounded` - Rounded progress bar

## Progress Bar Types

### Determinate Progress Bar

```python
# Shows exact progress percentage
progress = render_progress(
    value=75,
    max_value=100,
    color="blue"
)
```

### Indeterminate Progress Bar

```python
# Shows loading state without specific percentage
progress = render_progress(
    value=0,
    max_value=0,
    color="blue",
    class="progress-indeterminate"
)
```

### Custom Range Progress Bar

```python
# Progress bar with custom range (e.g., 0-50)
progress = render_progress(
    value=25,
    max_value=50,
    color="green"
)
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_progress value=75 color="blue" size="default" %}
```

## Advanced Examples

### File Upload Progress

```python
def create_upload_progress(current_bytes, total_bytes):
    percentage = int((current_bytes / total_bytes) * 100) if total_bytes > 0 else 0

    progress = render_progress(
        value=percentage,
        color="blue",
        id="upload-progress",
        class="progress-upload"
    )

    return f"""
    <div class="upload-status">
        <p>Uploading file... {percentage}%</p>
        {progress}
        <p>{current_bytes} / {total_bytes} bytes</p>
    </div>
    """

upload_status = create_upload_progress(1024 * 1024, 5 * 1024 * 1024)  # 1MB / 5MB
```

### Multi-Step Progress

```python
def create_multi_step_progress(current_step, total_steps):
    percentage = int((current_step / total_steps) * 100)

    steps = ["Setup", "Configuration", "Installation", "Testing", "Complete"]
    current_step_name = steps[current_step - 1] if current_step <= len(steps) else "Complete"

    progress = render_progress(
        value=percentage,
        color="green",
        class="progress-multi-step"
    )

    return f"""
    <div class="multi-step-progress">
        <h4>Step {current_step} of {total_steps}: {current_step_name}</h4>
        {progress}
        <div class="step-indicators">
            {''.join([f'<span class="step {"active" if i < current_step else ""}">{step}</span>' for i, step in enumerate(steps)])}
        </div>
    </div>
    """

multi_progress = create_multi_step_progress(3, 5)
```

### Animated Progress Bar

```python
def create_animated_progress(value, color="blue"):
    return render_progress(
        value=value,
        color=color,
        class="progress-animated progress-striped"
    )

animated_progress = create_animated_progress(60, "green")
```

### Progress Bar with Labels

```python
def create_labeled_progress(value, label, color="blue"):
    progress = render_progress(
        value=value,
        color=color,
        class="progress-labeled"
    )

    return f"""
    <div class="progress-container">
        <div class="progress-label">{label}</div>
        {progress}
        <div class="progress-value">{value}%</div>
    </div>
    """

labeled_progress = create_labeled_progress(85, "Task Completion", "green")
```

### Progress Bar with Status Text

```python
def create_status_progress(value, status_text, color="blue"):
    progress = render_progress(
        value=value,
        color=color,
        class="progress-status"
    )

    return f"""
    <div class="status-progress">
        <div class="status-header">
            <span class="status-text">{status_text}</span>
            <span class="status-percentage">{value}%</span>
        </div>
        {progress}
    </div>
    """

status_progress = create_status_progress(45, "Processing data...", "orange")
```

## JavaScript Integration

### Updating Progress Dynamically

```javascript
// Update progress value
function updateProgress(value) {
	const progressBar = document.querySelector("#my-progress");
	const progressFill = progressBar.querySelector(".progress-bar");
	const percentage = (value / 100) * 100;

	progressFill.style.width = percentage + "%";
	progressFill.setAttribute("aria-valuenow", value);
}

// Example usage
updateProgress(75);
```

### Animated Progress Updates

```javascript
// Animate progress from 0 to target value
function animateProgress(targetValue, duration = 1000) {
	const progressBar = document.querySelector("#my-progress");
	const progressFill = progressBar.querySelector(".progress-bar");
	let currentValue = 0;
	const increment = targetValue / (duration / 16); // 60fps

	const animate = () => {
		currentValue += increment;
		if (currentValue >= targetValue) {
			currentValue = targetValue;
		}

		const percentage = (currentValue / 100) * 100;
		progressFill.style.width = percentage + "%";

		if (currentValue < targetValue) {
			requestAnimationFrame(animate);
		}
	};

	animate();
}

// Example usage
animateProgress(80, 2000); // Animate to 80% over 2 seconds
```

## Best Practices

1. **Use appropriate colors**: Choose colors that match your application's theme
2. **Provide context**: Include labels or text to explain what the progress represents
3. **Handle edge cases**: Account for 0% and 100% states
4. **Make it accessible**: Include proper ARIA attributes for screen readers
5. **Use consistent sizing**: Apply consistent size classes across your application
6. **Consider mobile**: Ensure progress bars are visible on mobile devices
7. **Add animations**: Use animations for better user experience

## Related Components

- [Alerts](alerts.md) - For status messages
- [Buttons](buttons.md) - For action buttons
- [Cards](cards.md) - For containing progress bars
- [Forms](forms.md) - For form-related progress indicators
