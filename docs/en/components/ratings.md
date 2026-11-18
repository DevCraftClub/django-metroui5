# Ratings

Component for creating star ratings, review systems, and interactive rating controls.

## Basic Usage

### Simple Rating Display

```python
from metroui5.components import render_rating

# Basic star rating
rating_html = render_rating(
    value=4.5,
    max_value=5
)
```

### Interactive Rating

```python
# Interactive rating for user input
rating_html = render_rating(
    value=0,
    max_value=5,
    interactive=True,
    name="product_rating"
)
```

### Custom Rating with Reviews

```python
# Rating with review count
rating_html = render_rating(
    value=4.2,
    max_value=5,
    show_value=True,
    review_count=156,
    show_reviews=True
)
```

## Rendered Output

### Basic Rating

```html
<!-- Input -->
render_rating(value=4.5, max_value=5)

<!-- Output -->
<div class="rating" data-role="rating" data-value="4.5" data-max="5">
	<span class="rating-star active">★</span>
	<span class="rating-star active">★</span>
	<span class="rating-star active">★</span>
	<span class="rating-star active">★</span>
	<span class="rating-star half">★</span>
</div>
```

### Interactive Rating

```html
<!-- Input -->
render_rating(value=0, max_value=5, interactive=True, name="rating")

<!-- Output -->
<div
	class="rating rating-interactive"
	data-role="rating"
	data-value="0"
	data-max="5"
>
	<input type="hidden" name="rating" value="0" />
	<span class="rating-star" data-value="1">★</span>
	<span class="rating-star" data-value="2">★</span>
	<span class="rating-star" data-value="3">★</span>
	<span class="rating-star" data-value="4">★</span>
	<span class="rating-star" data-value="5">★</span>
</div>
```

### Rating with Reviews

```html
<!-- Input -->
render_rating(value=4.2, show_value=True, review_count=156, show_reviews=True)

<!-- Output -->
<div class="rating rating-with-details">
	<div class="rating-stars" data-role="rating" data-value="4.2" data-max="5">
		<span class="rating-star active">★</span>
		<span class="rating-star active">★</span>
		<span class="rating-star active">★</span>
		<span class="rating-star active">★</span>
		<span class="rating-star partial">★</span>
	</div>
	<span class="rating-value">4.2</span>
	<span class="rating-reviews">(156 reviews)</span>
</div>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic rating -->
{% metroui5_rating value=4.5 max_value=5 %}

<!-- Interactive rating -->
{% metroui5_rating value=0 interactive=True name="rating" %}

<!-- Rating with details -->
{% metroui5_rating value=product.rating show_value=True
review_count=product.review_count %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_rating

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Display rating
    rating_display = render_rating(
        value=product.average_rating,
        max_value=5,
        show_value=True,
        review_count=product.reviews.count(),
        show_reviews=True
    )

    # Interactive rating for logged-in users
    user_rating = None
    if request.user.is_authenticated:
        user_review = product.reviews.filter(user=request.user).first()
        current_rating = user_review.rating if user_review else 0

        user_rating = render_rating(
            value=current_rating,
            max_value=5,
            interactive=True,
            name="user_rating",
            id="user-rating-input"
        )

    context = {
        'product': product,
        'rating_display': rating_display,
        'user_rating': user_rating
    }
    return render(request, 'product_detail.html', context)
```

```html
<!-- product_detail.html -->
{% load metroui5 %} {% block content %}
<div class="product-header">
	<h1>{{ product.name }}</h1>

	<!-- Display average rating -->
	{{ rating_display|safe }}

	<!-- User rating input -->
	{% if user.is_authenticated %}
	<div class="user-rating">
		<h3>Rate this product:</h3>
		{{ user_rating|safe }}
	</div>
	{% endif %}
</div>
{% endblock %}
```

## Parameters

### `value` (required)

Current rating value.

**Example**:

```python
rating_html = render_rating(value=4.5)
```

### `max_value` (optional)

Maximum rating value (number of stars).

**Default**: `5`

**Example**:

```python
rating_html = render_rating(value=8, max_value=10)
```

### `interactive` (optional)

Whether the rating can be changed by user interaction.

**Default**: `False`

**Example**:

```python
rating_html = render_rating(value=0, interactive=True)
```

### `name` (optional)

Name attribute for the hidden input field (interactive ratings).

**Example**:

```python
rating_html = render_rating(value=0, interactive=True, name="rating")
```

### `show_value` (optional)

Whether to display the numeric rating value.

**Default**: `False`

**Example**:

```python
rating_html = render_rating(value=4.2, show_value=True)
```

### `review_count` (optional)

Number of reviews for this rating.

**Example**:

```python
rating_html = render_rating(value=4.2, review_count=156)
```

### `show_reviews` (optional)

Whether to display the review count.

**Default**: `False`

**Example**:

```python
rating_html = render_rating(value=4.2, review_count=156, show_reviews=True)
```

### `size` (optional)

Size of the rating stars: small, medium, large.

**Default**: `"medium"`

**Example**:

```python
rating_html = render_rating(value=4.5, size="large")
```

### `color` (optional)

Color scheme for the stars: default, warning, info, success.

**Default**: `"default"`

**Example**:

```python
rating_html = render_rating(value=4.5, color="warning")
```

### `readonly` (optional)

Whether the rating is read-only (for display only).

**Default**: `True` (unless interactive=True)

**Example**:

```python
rating_html = render_rating(value=4.5, readonly=True)
```

## Advanced Examples

### Product Rating System

```python
def create_product_rating(product, user=None):
    """Create comprehensive product rating display."""

    # Main rating display
    main_rating = render_rating(
        value=product.average_rating,
        max_value=5,
        show_value=True,
        review_count=product.reviews.count(),
        show_reviews=True,
        size="large"
    )

    # User's rating input
    user_rating = None
    if user and user.is_authenticated:
        current_rating = get_user_rating(product, user)
        user_rating = render_rating(
            value=current_rating,
            max_value=5,
            interactive=True,
            name="user_rating",
            id=f"rating-{product.id}"
        )

    return {
        'main_rating': main_rating,
        'user_rating': user_rating,
        'rating_breakdown': get_rating_breakdown(product)
    }
```

### Review Summary with Ratings

```python
def create_review_summary(reviews):
    """Create review summary with rating breakdown."""

    rating_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    total_reviews = len(reviews)

    for review in reviews:
        rating_counts[review.rating] += 1

    breakdown = []
    for rating in range(5, 0, -1):
        count = rating_counts[rating]
        percentage = (count / total_reviews * 100) if total_reviews > 0 else 0

        breakdown.append({
            'rating': rating,
            'count': count,
            'percentage': percentage,
            'stars': render_rating(value=rating, max_value=5, size="small")
        })

    return breakdown
```

### Multi-Criteria Rating

```python
def create_multi_criteria_rating(criteria_ratings):
    """Create rating for multiple criteria."""

    criteria_displays = []
    total_rating = 0

    for criterion, rating in criteria_ratings.items():
        criteria_displays.append({
            'name': criterion,
            'rating': render_rating(
                value=rating,
                max_value=5,
                show_value=True,
                size="small"
            )
        })
        total_rating += rating

    average_rating = total_rating / len(criteria_ratings)
    overall_rating = render_rating(
        value=average_rating,
        max_value=5,
        show_value=True,
        size="large"
    )

    return {
        'criteria': criteria_displays,
        'overall': overall_rating
    }
```

### Rating with Hover Preview

```python
def create_hover_rating(current_value=0, max_value=5):
    """Create interactive rating with hover preview."""

    return render_rating(
        value=current_value,
        max_value=max_value,
        interactive=True,
        class="rating-hover-preview",
        **{
            "data-hover": "true",
            "data-preview": "true"
        }
    )
```

## Styling

### CSS Classes

#### Base Classes

- `rating` - Base rating container
- `rating-stars` - Star container
- `rating-star` - Individual star
- `rating-interactive` - Interactive rating

#### State Classes

- `rating-star active` - Filled star
- `rating-star half` - Half-filled star
- `rating-star partial` - Partially filled star
- `rating-star hover` - Hovered star

#### Size Classes

- `rating-small` - Small rating stars
- `rating-medium` - Medium rating stars (default)
- `rating-large` - Large rating stars

#### Color Classes

- `rating-default` - Default yellow stars
- `rating-warning` - Warning color stars
- `rating-info` - Info color stars
- `rating-success` - Success color stars

### Custom Styling

```css
/* Custom rating styling */
.rating-custom {
	display: inline-flex;
	align-items: center;
	gap: 2px;
}

.rating-custom .rating-star {
	font-size: 20px;
	color: #dee2e6;
	cursor: pointer;
	transition: all 0.2s ease;
	user-select: none;
}

.rating-custom .rating-star.active {
	color: #ffc107;
}

.rating-custom .rating-star.half {
	background: linear-gradient(90deg, #ffc107 50%, #dee2e6 50%);
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
	background-clip: text;
}

.rating-custom .rating-star:hover {
	transform: scale(1.1);
}

/* Interactive rating */
.rating-interactive .rating-star {
	cursor: pointer;
}

.rating-interactive .rating-star:hover,
.rating-interactive .rating-star.hover {
	color: #ffb400;
}

/* Rating sizes */
.rating-small .rating-star {
	font-size: 16px;
}

.rating-large .rating-star {
	font-size: 28px;
}

/* Rating with details */
.rating-with-details {
	display: flex;
	align-items: center;
	gap: 8px;
}

.rating-value {
	font-weight: 600;
	color: #495057;
}

.rating-reviews {
	color: #6c757d;
	font-size: 0.875em;
}

/* Rating breakdown */
.rating-breakdown {
	margin-top: 20px;
}

.rating-breakdown-item {
	display: flex;
	align-items: center;
	gap: 10px;
	margin-bottom: 8px;
}

.rating-breakdown-bar {
	flex: 1;
	height: 8px;
	background: #e9ecef;
	border-radius: 4px;
	overflow: hidden;
}

.rating-breakdown-fill {
	height: 100%;
	background: #ffc107;
	transition: width 0.3s ease;
}
```

## JavaScript Integration

### Interactive Rating

```javascript
// Handle interactive rating clicks
$(".rating-interactive").on("click", ".rating-star", function () {
	const star = $(this);
	const rating = star.closest(".rating");
	const value = parseInt(star.data("value"));
	const hiddenInput = rating.find('input[type="hidden"]');

	// Update rating value
	updateRatingDisplay(rating, value);
	hiddenInput.val(value);

	// Trigger change event
	rating.trigger("rating-changed", [value]);
});

// Handle rating hover
$(".rating-interactive").on("mouseenter", ".rating-star", function () {
	const star = $(this);
	const rating = star.closest(".rating");
	const value = parseInt(star.data("value"));

	// Show preview
	updateRatingPreview(rating, value);
});

$(".rating-interactive").on("mouseleave", function () {
	const rating = $(this);
	const currentValue = parseInt(rating.find('input[type="hidden"]').val()) || 0;

	// Restore current rating
	updateRatingDisplay(rating, currentValue);
});

function updateRatingDisplay(rating, value) {
	rating.find(".rating-star").each(function (index) {
		const star = $(this);
		if (index < value) {
			star.addClass("active").removeClass("hover");
		} else {
			star.removeClass("active hover");
		}
	});
}

function updateRatingPreview(rating, value) {
	rating.find(".rating-star").each(function (index) {
		const star = $(this);
		if (index < value) {
			star.addClass("hover");
		} else {
			star.removeClass("hover");
		}
	});
}
```

### AJAX Rating Submission

```javascript
// Submit rating via AJAX
$(".rating-interactive").on("rating-changed", function (e, value) {
	const rating = $(this);
	const productId = rating.data("product-id");

	$.ajax({
		url: "/api/rate-product/",
		method: "POST",
		data: {
			product_id: productId,
			rating: value,
			csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
		},
		success: function (response) {
			if (response.success) {
				showNotification("Rating submitted successfully", "success");
				updateAverageRating(response.new_average, response.review_count);
			} else {
				showNotification("Failed to submit rating", "error");
			}
		},
		error: function () {
			showNotification("Error submitting rating", "error");
		},
	});
});

function updateAverageRating(average, count) {
	$(".rating-value").text(average.toFixed(1));
	$(".rating-reviews").text(`(${count} reviews)`);
}
```

### Rating Animation

```javascript
// Animate rating display
function animateRating(ratingElement, targetValue, duration = 1000) {
	const maxValue = parseInt(ratingElement.data("max")) || 5;
	const steps = targetValue * 10; // 10 steps per star for smooth animation
	let currentStep = 0;

	const interval = setInterval(() => {
		currentStep++;
		const currentValue = currentStep / 10;

		updateRatingStars(ratingElement, currentValue, maxValue);

		if (currentStep >= steps) {
			clearInterval(interval);
		}
	}, duration / steps);
}

function updateRatingStars(rating, value, maxValue) {
	rating.find(".rating-star").each(function (index) {
		const star = $(this);
		const starValue = index + 1;

		if (value >= starValue) {
			star.addClass("active").removeClass("half partial");
		} else if (value >= starValue - 0.5) {
			star.addClass("half").removeClass("active partial");
		} else if (value > starValue - 1) {
			const percentage = (value - (starValue - 1)) * 100;
			star.addClass("partial").removeClass("active half");
			star.css(
				"background",
				`linear-gradient(90deg, #ffc107 ${percentage}%, #dee2e6 ${percentage}%)`
			);
		} else {
			star.removeClass("active half partial");
		}
	});
}
```

## Best Practices

### 1. Consistent Rating Scale

```python
# Use consistent rating scales across the application
RATING_SCALES = {
    'product': 5,      # 1-5 stars for products
    'service': 10,     # 1-10 for services
    'content': 5       # 1-5 for content
}

def create_consistent_rating(value, rating_type='product'):
    max_value = RATING_SCALES.get(rating_type, 5)
    return render_rating(value=value, max_value=max_value)
```

### 2. Rating Validation

```python
# Validate rating values
def validate_rating(value, max_value=5):
    """Validate rating value is within acceptable range."""
    if not isinstance(value, (int, float)):
        raise ValueError("Rating must be a number")

    if value < 0 or value > max_value:
        raise ValueError(f"Rating must be between 0 and {max_value}")

    return round(value, 1)  # Round to 1 decimal place
```

### 3. Accessibility

```python
# Create accessible ratings
def create_accessible_rating(value, max_value=5, **kwargs):
    return render_rating(
        value=value,
        max_value=max_value,
        **kwargs,
        **{
            "aria-label": f"Rating: {value} out of {max_value} stars",
            "role": "img"
        }
    )
```

### 4. Performance Optimization

```python
# Cache rating calculations
from django.core.cache import cache

def get_cached_rating(product_id):
    cache_key = f"product_rating_{product_id}"
    rating_data = cache.get(cache_key)

    if not rating_data:
        product = Product.objects.get(id=product_id)
        rating_data = {
            'average': product.calculate_average_rating(),
            'count': product.reviews.count()
        }
        cache.set(cache_key, rating_data, 3600)  # Cache for 1 hour

    return rating_data
```

## Related Components

- [Buttons](buttons.md) - For rating submission buttons
- [Forms](forms.md) - For rating form integration
- [Icons](icons.md) - For custom rating symbols
- [Progress Bars](progress.md) - For rating breakdown displays


## metroui5_rating

```python
render_rating(0)
```

Empty or invalid: `render_rating(0)` returns `<input class="rating" data-role="rating" data-value="0" data-stars="5">`. An empty call returns `<input class="rating" data-role="rating" data-value="0" data-stars="0">`.

```django
{% metroui5_rating value="Text" %}
```
