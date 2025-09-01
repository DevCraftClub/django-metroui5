# Хлебные крошки

Компонент для создания навигационных хлебных крошек, которые показывают текущее расположение страницы в иерархии навигации.

## Базовое использование

### Простые хлебные крошки

```python
from metroui5.components import render_breadcrumb

# Базовые хлебные крошки
breadcrumb_items = [
    {"text": "Главная", "url": "/"},
    {"text": "Продукты", "url": "/products/"},
    {"text": "Ноутбуки", "url": "/products/laptops/"},
    {"text": "Игровые ноутбуки"}  # Текущая страница (без URL)
]

breadcrumb_html = render_breadcrumb(items=breadcrumb_items)
```

### Хлебные крошки с иконками

```python
# Хлебные крошки с иконками
breadcrumb_items = [
    {"text": "Главная", "url": "/", "icon": "home"},
    {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Пользователи", "url": "/users/", "icon": "users"},
    {"text": "Профиль", "icon": "user"}
]

breadcrumb_html = render_breadcrumb(items=breadcrumb_items, show_icons=True)
```

### Пользовательские хлебные крошки

```python
# Пользовательские хлебные крошки с разделителем
breadcrumb_html = render_breadcrumb(
    items=breadcrumb_items,
    separator="→",
    class="breadcrumb-custom",
    id="page-breadcrumb"
)
```

## Вывод HTML

### Базовые хлебные крошки

```html
<!-- Ввод -->
render_breadcrumb(items=[{"text": "Главная", "url": "/"}, {"text": "Продукты",
"url": "/products/"}, {"text": "Ноутбуки"}])

<!-- Вывод -->
<nav class="breadcrumb" aria-label="breadcrumb">
	<ol class="breadcrumb-list">
		<li class="breadcrumb-item">
			<a href="/" class="breadcrumb-link">Главная</a>
		</li>
		<li class="breadcrumb-separator">/</li>
		<li class="breadcrumb-item">
			<a href="/products/" class="breadcrumb-link">Продукты</a>
		</li>
		<li class="breadcrumb-separator">/</li>
		<li class="breadcrumb-item active" aria-current="page">
			<span class="breadcrumb-text">Ноутбуки</span>
		</li>
	</ol>
</nav>
```

### Хлебные крошки с иконками

```html
<!-- Ввод -->
render_breadcrumb(items=[{"text": "Главная", "url": "/", "icon": "home"},
{"text": "Профиль", "icon": "user"}], show_icons=True)

<!-- Вывод -->
<nav class="breadcrumb breadcrumb-with-icons" aria-label="breadcrumb">
	<ol class="breadcrumb-list">
		<li class="breadcrumb-item">
			<a href="/" class="breadcrumb-link">
				<span class="mif-home"></span>
				Главная
			</a>
		</li>
		<li class="breadcrumb-separator">/</li>
		<li class="breadcrumb-item active" aria-current="page">
			<span class="breadcrumb-text">
				<span class="mif-user"></span>
				Профиль
			</span>
		</li>
	</ol>
</nav>
```

### Хлебные крошки с пользовательским разделителем

```html
<!-- Ввод -->
render_breadcrumb(items=breadcrumb_items, separator="→")

<!-- Вывод -->
<nav class="breadcrumb" aria-label="breadcrumb">
	<ol class="breadcrumb-list">
		<li class="breadcrumb-item">
			<a href="/" class="breadcrumb-link">Главная</a>
		</li>
		<li class="breadcrumb-separator">→</li>
		<li class="breadcrumb-item active" aria-current="page">
			<span class="breadcrumb-text">Профиль</span>
		</li>
	</ol>
</nav>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовые хлебные крошки -->
{% metroui5_breadcrumb items=breadcrumb_items %}

<!-- Хлебные крошки с иконками -->
{% metroui5_breadcrumb items=breadcrumb_items show_icons=True %}

<!-- Пользовательские хлебные крошки -->
{% metroui5_breadcrumb items=breadcrumb_items separator="→"
class="breadcrumb-custom" %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_breadcrumb

def product_detail_view(request, category_slug, product_slug):
    # Построение пути хлебных крошек
    breadcrumb_items = [
        {"text": "Главная", "url": "/", "icon": "home"},
        {"text": "Продукты", "url": "/products/", "icon": "grid"},
        {"text": category.name, "url": f"/products/{category_slug}/", "icon": "folder"},
        {"text": product.name, "icon": "box"}  # Текущая страница
    ]

    breadcrumb_html = render_breadcrumb(
        items=breadcrumb_items,
        show_icons=True,
        class="breadcrumb-product"
    )

    context = {
        'breadcrumb_html': breadcrumb_html,
        'breadcrumb_items': breadcrumb_items,
        'product': product
    }
    return render(request, 'product_detail.html', context)
```

```html
<!-- product_detail.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ breadcrumb_html|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_breadcrumb items=breadcrumb_items show_icons=True %}

<div class="product-details">
	<h1>{{ product.name }}</h1>
	<!-- Содержимое продукта -->
</div>
{% endblock %}
```

## Параметры

### `items` (обязательный)

Список элементов хлебных крошек, представляющих путь навигации.

**Формат**:

```python
items = [
    {
        "text": "Название страницы",
        "url": "/путь/",        # Необязательно (пропустить для текущей страницы)
        "icon": "имя-иконки",   # Необязательно
        "title": "Подсказка"    # Необязательно
    }
]
```

### `show_icons` (необязательный)

Отображать ли иконки в элементах хлебных крошек.

**По умолчанию**: `False`

**Пример**:

```python
breadcrumb_html = render_breadcrumb(items=items, show_icons=True)
```

### `separator` (необязательный)

Символ или строка для использования в качестве разделителя между элементами.

**По умолчанию**: `"/"`

**Пример**:

```python
breadcrumb_html = render_breadcrumb(items=items, separator="→")
```

### `max_items` (необязательный)

Максимальное количество элементов для отображения (с многоточием для переполнения).

**Пример**:

```python
breadcrumb_html = render_breadcrumb(items=items, max_items=4)
```

### `id` (необязательный)

Уникальный идентификатор для элемента хлебных крошек.

**Пример**:

```python
breadcrumb_html = render_breadcrumb(items=items, id="page-breadcrumb")
```

### `class` (необязательный)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
breadcrumb_html = render_breadcrumb(items=items, class="breadcrumb-custom")
```

## Расширенные примеры

### Динамические хлебные крошки

```python
def create_dynamic_breadcrumb(request, current_object=None):
    """Создание хлебных крошек на основе текущего URL и объекта."""

    breadcrumb_items = [{"text": "Главная", "url": "/", "icon": "home"}]

    # Построение хлебных крошек из пути URL
    path_parts = request.path.strip('/').split('/')
    current_path = ""

    for part in path_parts[:-1]:  # Исключить текущую страницу
        current_path += f"/{part}"
        breadcrumb_items.append({
            "text": part.replace('-', ' ').title(),
            "url": current_path + "/"
        })

    # Добавить текущую страницу
    if current_object:
        breadcrumb_items.append({
            "text": str(current_object),
            "icon": get_object_icon(current_object)
        })

    return render_breadcrumb(
        items=breadcrumb_items,
        show_icons=True,
        class="breadcrumb-dynamic"
    )
```

### Иерархические хлебные крошки

```python
def create_hierarchical_breadcrumb(category):
    """Создание хлебных крошек для иерархических категорий."""

    breadcrumb_items = [{"text": "Главная", "url": "/", "icon": "home"}]

    # Построение иерархии из родительских категорий
    ancestors = []
    current = category
    while current.parent:
        ancestors.append(current.parent)
        current = current.parent

    # Обратить для получения порядка от корня к листу
    ancestors.reverse()

    for ancestor in ancestors:
        breadcrumb_items.append({
            "text": ancestor.name,
            "url": ancestor.get_absolute_url(),
            "icon": "folder"
        })

    # Добавить текущую категорию
    breadcrumb_items.append({
        "text": category.name,
        "icon": "folder-open"
    })

    return render_breadcrumb(
        items=breadcrumb_items,
        show_icons=True,
        separator="→"
    )
```

### Усеченные хлебные крошки

```python
def create_truncated_breadcrumb(items, max_display=4):
    """Создание хлебных крошек с многоточием для длинных путей."""

    if len(items) <= max_display:
        return render_breadcrumb(items=items)

    # Сохранить первый элемент, последние элементы и добавить многоточие
    truncated_items = [items[0]]

    if len(items) > max_display:
        truncated_items.append({
            "text": "...",
            "class": "breadcrumb-ellipsis",
            "title": f"Скрыто {len(items) - max_display + 1} уровней"
        })

    # Добавить последние несколько элементов
    truncated_items.extend(items[-(max_display-2):])

    return render_breadcrumb(
        items=truncated_items,
        class="breadcrumb-truncated"
    )
```

### Контекстные хлебные крошки

```python
def create_contextual_breadcrumb(request, context_type="default"):
    """Создание хлебных крошек на основе типа контекста."""

    breadcrumb_configs = {
        "admin": [
            {"text": "Админ", "url": "/admin/", "icon": "cog"},
            {"text": "Панель управления", "url": "/admin/dashboard/", "icon": "dashboard"}
        ],
        "user": [
            {"text": "Мой аккаунт", "url": "/account/", "icon": "user"},
            {"text": "Профиль", "url": "/account/profile/", "icon": "id-card"}
        ],
        "default": [
            {"text": "Главная", "url": "/", "icon": "home"}
        ]
    }

    base_items = breadcrumb_configs.get(context_type, breadcrumb_configs["default"])

    # Добавить информацию о текущей странице
    current_page = get_current_page_info(request)
    if current_page:
        base_items.append(current_page)

    return render_breadcrumb(
        items=base_items,
        show_icons=True,
        class=f"breadcrumb-{context_type}"
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `breadcrumb` - Базовый контейнер хлебных крошек
- `breadcrumb-primary` - Основной стиль хлебных крошек
- `breadcrumb-secondary` - Вторичный стиль хлебных крошек

#### Классы функций

- `breadcrumb-with-icons` - Хлебные крошки с поддержкой иконок
- `breadcrumb-truncated` - Усеченные хлебные крошки с многоточием
- `breadcrumb-compact` - Компактный стиль хлебных крошек

#### Контекстные классы

- `breadcrumb-admin` - Хлебные крошки контекста админа
- `breadcrumb-user` - Хлебные крошки пользовательского контекста
- `breadcrumb-product` - Хлебные крошки страницы продукта

### Пользовательская стилизация

```css
/* Пользовательская стилизация хлебных крошек */
.breadcrumb-custom {
	background: #f8f9fa;
	border: 1px solid #dee2e6;
	border-radius: 6px;
	padding: 12px 16px;
	margin-bottom: 20px;
}

.breadcrumb-custom .breadcrumb-list {
	display: flex;
	align-items: center;
	list-style: none;
	margin: 0;
	padding: 0;
	flex-wrap: wrap;
}

.breadcrumb-custom .breadcrumb-item {
	display: flex;
	align-items: center;
}

.breadcrumb-custom .breadcrumb-link {
	color: #007acc;
	text-decoration: none;
	padding: 4px 8px;
	border-radius: 4px;
	transition: all 0.3s ease;
	display: flex;
	align-items: center;
	gap: 6px;
}

.breadcrumb-custom .breadcrumb-link:hover {
	background: #e3f2fd;
	color: #0056b3;
}

.breadcrumb-custom .breadcrumb-item.active .breadcrumb-text {
	color: #495057;
	font-weight: 500;
	padding: 4px 8px;
	display: flex;
	align-items: center;
	gap: 6px;
}

.breadcrumb-custom .breadcrumb-separator {
	color: #6c757d;
	margin: 0 8px;
	font-size: 14px;
}

/* Адаптивные хлебные крошки */
@media (max-width: 768px) {
	.breadcrumb-custom .breadcrumb-list {
		flex-direction: column;
		align-items: flex-start;
	}

	.breadcrumb-custom .breadcrumb-separator {
		display: none;
	}

	.breadcrumb-custom .breadcrumb-item {
		margin-bottom: 4px;
	}
}

/* Усеченные хлебные крошки */
.breadcrumb-ellipsis {
	color: #6c757d;
	cursor: help;
	padding: 4px 8px;
}

.breadcrumb-ellipsis:hover {
	background: #f8f9fa;
	border-radius: 4px;
}
```

## Интеграция с JavaScript

### Навигация по хлебным крошкам

```javascript
// Обработка кликов по хлебным крошкам с аналитикой
$(".breadcrumb").on("click", ".breadcrumb-link", function (e) {
	const link = $(this);
	const breadcrumbText = link.text().trim();
	const url = link.attr("href");

	// Отслеживание навигации по хлебным крошкам
	trackBreadcrumbClick(breadcrumbText, url);

	// Разрешить обычную навигацию
	return true;
});

function trackBreadcrumbClick(text, url) {
	// Отслеживание аналитики
	if (typeof gtag !== "undefined") {
		gtag("event", "breadcrumb_click", {
			breadcrumb_text: text,
			destination_url: url,
		});
	}
}
```

### Динамические обновления хлебных крошек

```javascript
// Обновление хлебных крошек динамически
function updateBreadcrumbs(newItems) {
	const breadcrumb = $(".breadcrumb");
	const list = breadcrumb.find(".breadcrumb-list");

	list.empty();

	newItems.forEach((item, index) => {
		// Добавить элемент хлебных крошек
		const itemElement = createBreadcrumbItem(
			item,
			index === newItems.length - 1
		);
		list.append(itemElement);

		// Добавить разделитель (кроме последнего элемента)
		if (index < newItems.length - 1) {
			list.append('<li class="breadcrumb-separator">/</li>');
		}
	});
}

function createBreadcrumbItem(item, isLast) {
	const icon = item.icon ? `<span class="mif-${item.icon}"></span>` : "";

	if (isLast || !item.url) {
		return `
			<li class="breadcrumb-item active" aria-current="page">
				<span class="breadcrumb-text">${icon}${item.text}</span>
			</li>
		`;
	} else {
		return `
			<li class="breadcrumb-item">
				<a href="${item.url}" class="breadcrumb-link">${icon}${item.text}</a>
			</li>
		`;
	}
}
```

### Адаптивные хлебные крошки

```javascript
// Обработка адаптивного поведения хлебных крошек
function handleResponsiveBreadcrumbs() {
	const breadcrumb = $(".breadcrumb");
	const items = breadcrumb.find(".breadcrumb-item");
	const windowWidth = $(window).width();

	if (windowWidth < 768) {
		// Мобильные устройства: показать только последние несколько элементов
		showMobileBreadcrumbs(items);
	} else {
		// Десктоп: показать все элементы
		items.show();
		breadcrumb.find(".breadcrumb-mobile-toggle").remove();
	}
}

function showMobileBreadcrumbs(items) {
	const maxMobileItems = 2;

	if (items.length <= maxMobileItems) {
		return; // Показать все, если мало элементов
	}

	// Скрыть средние элементы
	items.slice(1, -1).hide();

	// Добавить кнопку переключения
	const toggleButton = `
		<li class="breadcrumb-mobile-toggle">
			<button class="breadcrumb-toggle-btn" onclick="toggleHiddenBreadcrumbs()">
				<span class="mif-more"></span>
			</button>
		</li>
	`;

	items.eq(0).after(toggleButton);
}

function toggleHiddenBreadcrumbs() {
	const hiddenItems = $(".breadcrumb-item:hidden");
	hiddenItems.toggle();
}

// Обработка изменения размера окна
$(window).on("resize", handleResponsiveBreadcrumbs);
$(document).ready(handleResponsiveBreadcrumbs);
```

## Лучшие практики

### 1. Последовательная структура

```python
# Использовать последовательную структуру хлебных крошек
def build_breadcrumb_path(request, current_object=None):
	"""Построение последовательной структуры хлебных крошек."""
	items = [{"text": "Главная", "url": "/", "icon": "home"}]

	# Добавить элементы на основе пути
	path_items = extract_path_items(request.path)
	items.extend(path_items)

	# Добавить текущий объект
	if current_object:
		items.append({
			"text": str(current_object),
			"icon": get_model_icon(current_object._meta.model)
		})

	return items
```

### 2. SEO оптимизация

```python
# Создание SEO-дружественных хлебных крошек
def create_seo_breadcrumb(items):
	"""Создание хлебных крошек со структурированными данными."""
	breadcrumb_html = render_breadcrumb(items=items)

	# Добавить JSON-LD структурированные данные
	structured_data = {
		"@context": "https://schema.org",
		"@type": "BreadcrumbList",
		"itemListElement": [
			{
				"@type": "ListItem",
				"position": i + 1,
				"name": item["text"],
				"item": request.build_absolute_uri(item.get("url", ""))
			}
			for i, item in enumerate(items) if item.get("url")
		]
	}

	return breadcrumb_html, structured_data
```

### 3. Доступность

```python
# Обеспечение доступности хлебных крошек
def create_accessible_breadcrumb(items):
	return render_breadcrumb(
		items=items,
		**{
			"aria-label": "навигация по хлебным крошкам",
			"role": "navigation"
		}
	)
```

## Связанные компоненты

- [Навигация](navigation.md) - Для основных систем навигации
- [Меню](menus.md) - Для выпадающих меню навигации
- [Иконки](icons.md) - Для иконок хлебных крошек
- [Ссылки](links.md) - Для стилизации ссылок хлебных крошек
