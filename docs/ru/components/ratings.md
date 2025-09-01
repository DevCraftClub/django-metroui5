# Рейтинги

Компонент для создания звездных рейтингов, систем отзывов и интерактивных элементов управления рейтингом.

## Базовое использование

### Простое отображение рейтинга

```python
from metroui5.components import render_rating

# Базовый звездный рейтинг
rating_html = render_rating(
    value=4.5,
    max_value=5
)
```

### Интерактивный рейтинг

```python
# Интерактивный рейтинг для пользовательского ввода
rating_html = render_rating(
    value=0,
    max_value=5,
    interactive=True,
    name="product_rating"
)
```

### Пользовательский рейтинг с отзывами

```python
# Рейтинг с количеством отзывов
rating_html = render_rating(
    value=4.2,
    max_value=5,
    show_value=True,
    review_count=156,
    show_reviews=True
)
```

## Вывод HTML

### Базовый рейтинг

```html
<!-- Ввод -->
render_rating(value=4.5, max_value=5)

<!-- Вывод -->
<div class="rating" data-role="rating" data-value="4.5" data-max="5">
	<span class="rating-star active">★</span>
	<span class="rating-star active">★</span>
	<span class="rating-star active">★</span>
	<span class="rating-star active">★</span>
	<span class="rating-star half">★</span>
</div>
```

### Интерактивный рейтинг

```html
<!-- Ввод -->
render_rating(value=0, max_value=5, interactive=True, name="rating")

<!-- Вывод -->
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

### Рейтинг с отзывами

```html
<!-- Ввод -->
render_rating(value=4.2, show_value=True, review_count=156, show_reviews=True)

<!-- Вывод -->
<div class="rating rating-with-details">
	<div class="rating-stars" data-role="rating" data-value="4.2" data-max="5">
		<span class="rating-star active">★</span>
		<span class="rating-star active">★</span>
		<span class="rating-star active">★</span>
		<span class="rating-star active">★</span>
		<span class="rating-star partial">★</span>
	</div>
	<span class="rating-value">4.2</span>
	<span class="rating-reviews">(156 отзывов)</span>
</div>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовый рейтинг -->
{% metroui5_rating value=4.5 max_value=5 %}

<!-- Интерактивный рейтинг -->
{% metroui5_rating value=0 interactive=True name="rating" %}

<!-- Рейтинг с деталями -->
{% metroui5_rating value=product.rating show_value=True
review_count=product.review_count %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_rating

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Отображение рейтинга
    rating_display = render_rating(
        value=product.average_rating,
        max_value=5,
        show_value=True,
        review_count=product.reviews.count(),
        show_reviews=True
    )

    # Интерактивный рейтинг для авторизованных пользователей
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

	<!-- Отображение среднего рейтинга -->
	{{ rating_display|safe }}

	<!-- Ввод пользовательского рейтинга -->
	{% if user.is_authenticated %}
	<div class="user-rating">
		<h3>Оцените этот продукт:</h3>
		{{ user_rating|safe }}
	</div>
	{% endif %}
</div>
{% endblock %}
```

## Параметры

### `value` (обязательный)

Текущее значение рейтинга.

**Пример**:

```python
rating_html = render_rating(value=4.5)
```

### `max_value` (необязательный)

Максимальное значение рейтинга (количество звезд).

**По умолчанию**: `5`

**Пример**:

```python
rating_html = render_rating(value=8, max_value=10)
```

### `interactive` (необязательный)

Может ли рейтинг быть изменен пользователем.

**По умолчанию**: `False`

**Пример**:

```python
rating_html = render_rating(value=0, interactive=True)
```

### `name` (необязательный)

Атрибут name для скрытого поля ввода (интерактивные рейтинги).

**Пример**:

```python
rating_html = render_rating(value=0, interactive=True, name="rating")
```

### `show_value` (необязательный)

Отображать ли числовое значение рейтинга.

**По умолчанию**: `False`

**Пример**:

```python
rating_html = render_rating(value=4.2, show_value=True)
```

### `review_count` (необязательный)

Количество отзывов для этого рейтинга.

**Пример**:

```python
rating_html = render_rating(value=4.2, review_count=156)
```

### `show_reviews` (необязательный)

Отображать ли количество отзывов.

**По умолчанию**: `False`

**Пример**:

```python
rating_html = render_rating(value=4.2, review_count=156, show_reviews=True)
```

### `size` (необязательный)

Размер звезд рейтинга: small, medium, large.

**По умолчанию**: `"medium"`

**Пример**:

```python
rating_html = render_rating(value=4.5, size="large")
```

### `color` (необязательный)

Цветовая схема для звезд: default, warning, info, success.

**По умолчанию**: `"default"`

**Пример**:

```python
rating_html = render_rating(value=4.5, color="warning")
```

### `readonly` (необязательный)

Только ли для чтения рейтинг (только для отображения).

**По умолчанию**: `True` (если не interactive=True)

**Пример**:

```python
rating_html = render_rating(value=4.5, readonly=True)
```

## Расширенные примеры

### Система рейтинга продуктов

```python
def create_product_rating(product, user=None):
    """Создание комплексного отображения рейтинга продукта."""

    # Основное отображение рейтинга
    main_rating = render_rating(
        value=product.average_rating,
        max_value=5,
        show_value=True,
        review_count=product.reviews.count(),
        show_reviews=True,
        size="large"
    )

    # Ввод рейтинга пользователя
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

### Сводка отзывов с рейтингами

```python
def create_review_summary(reviews):
    """Создание сводки отзывов с разбивкой рейтинга."""

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

### Многокритериальный рейтинг

```python
def create_multi_criteria_rating(criteria_ratings):
    """Создание рейтинга для нескольких критериев."""

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

### Рейтинг с предварительным просмотром при наведении

```python
def create_hover_rating(current_value=0, max_value=5):
    """Создание интерактивного рейтинга с предварительным просмотром при наведении."""

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

## Стилизация

### CSS классы

#### Базовые классы

- `rating` - Базовый контейнер рейтинга
- `rating-stars` - Контейнер звезд
- `rating-star` - Отдельная звезда
- `rating-interactive` - Интерактивный рейтинг

#### Классы состояний

- `rating-star active` - Заполненная звезда
- `rating-star half` - Полузаполненная звезда
- `rating-star partial` - Частично заполненная звезда
- `rating-star hover` - Звезда при наведении

#### Классы размеров

- `rating-small` - Маленькие звезды рейтинга
- `rating-medium` - Средние звезды рейтинга (по умолчанию)
- `rating-large` - Большие звезды рейтинга

#### Цветовые классы

- `rating-default` - Звезды по умолчанию (желтые)
- `rating-warning` - Звезды предупреждающего цвета
- `rating-info` - Звезды информационного цвета
- `rating-success` - Звезды цвета успеха

### Пользовательская стилизация

```css
/* Пользовательская стилизация рейтинга */
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

/* Интерактивный рейтинг */
.rating-interactive .rating-star {
	cursor: pointer;
}

.rating-interactive .rating-star:hover,
.rating-interactive .rating-star.hover {
	color: #ffb400;
}

/* Размеры рейтинга */
.rating-small .rating-star {
	font-size: 16px;
}

.rating-large .rating-star {
	font-size: 28px;
}

/* Рейтинг с деталями */
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

/* Разбивка рейтинга */
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

## Интеграция с JavaScript

### Интерактивный рейтинг

```javascript
// Обработка кликов по интерактивному рейтингу
$(".rating-interactive").on("click", ".rating-star", function () {
	const star = $(this);
	const rating = star.closest(".rating");
	const value = parseInt(star.data("value"));
	const hiddenInput = rating.find('input[type="hidden"]');

	// Обновить значение рейтинга
	updateRatingDisplay(rating, value);
	hiddenInput.val(value);

	// Запустить событие изменения
	rating.trigger("rating-changed", [value]);
});

// Обработка наведения на рейтинг
$(".rating-interactive").on("mouseenter", ".rating-star", function () {
	const star = $(this);
	const rating = star.closest(".rating");
	const value = parseInt(star.data("value"));

	// Показать предварительный просмотр
	updateRatingPreview(rating, value);
});

$(".rating-interactive").on("mouseleave", function () {
	const rating = $(this);
	const currentValue = parseInt(rating.find('input[type="hidden"]').val()) || 0;

	// Восстановить текущий рейтинг
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

### Отправка рейтинга через AJAX

```javascript
// Отправка рейтинга через AJAX
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
				showNotification("Рейтинг успешно отправлен", "success");
				updateAverageRating(response.new_average, response.review_count);
			} else {
				showNotification("Не удалось отправить рейтинг", "error");
			}
		},
		error: function () {
			showNotification("Ошибка отправки рейтинга", "error");
		},
	});
});

function updateAverageRating(average, count) {
	$(".rating-value").text(average.toFixed(1));
	$(".rating-reviews").text(`(${count} отзывов)`);
}
```

### Анимация рейтинга

```javascript
// Анимация отображения рейтинга
function animateRating(ratingElement, targetValue, duration = 1000) {
	const maxValue = parseInt(ratingElement.data("max")) || 5;
	const steps = targetValue * 10; // 10 шагов на звезду для плавной анимации
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

## Лучшие практики

### 1. Последовательная шкала рейтинга

```python
# Использовать последовательные шкалы рейтинга во всем приложении
RATING_SCALES = {
    'product': 5,      # 1-5 звезд для продуктов
    'service': 10,     # 1-10 для услуг
    'content': 5       # 1-5 для контента
}

def create_consistent_rating(value, rating_type='product'):
    max_value = RATING_SCALES.get(rating_type, 5)
    return render_rating(value=value, max_value=max_value)
```

### 2. Валидация рейтинга

```python
# Валидация значений рейтинга
def validate_rating(value, max_value=5):
    """Валидация значения рейтинга в допустимом диапазоне."""
    if not isinstance(value, (int, float)):
        raise ValueError("Рейтинг должен быть числом")

    if value < 0 or value > max_value:
        raise ValueError(f"Рейтинг должен быть между 0 и {max_value}")

    return round(value, 1)  # Округлить до 1 знака после запятой
```

### 3. Доступность

```python
# Создание доступных рейтингов
def create_accessible_rating(value, max_value=5, **kwargs):
    return render_rating(
        value=value,
        max_value=max_value,
        **kwargs,
        **{
            "aria-label": f"Рейтинг: {value} из {max_value} звезд",
            "role": "img"
        }
    )
```

### 4. Оптимизация производительности

```python
# Кэширование расчетов рейтинга
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
        cache.set(cache_key, rating_data, 3600)  # Кэш на 1 час

    return rating_data
```

## Связанные компоненты

- [Кнопки](buttons.md) - Для кнопок отправки рейтинга
- [Формы](forms.md) - Для интеграции с формами рейтинга
- [Иконки](icons.md) - Для пользовательских символов рейтинга
- [Полосы прогресса](progress.md) - Для отображения разбивки рейтинга
