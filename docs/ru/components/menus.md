# Меню

Компонент для создания навигационных меню, контекстных меню и систем выпадающих меню.

## Базовое использование

### Простое меню

```python
from metroui5.components import render_menu

# Базовое меню
menu_items = [
    {"text": "Главная", "url": "/"},
    {"text": "О нас", "url": "/about/"},
    {"text": "Контакты", "url": "/contact/"}
]

menu_html = render_menu(items=menu_items)
```

### Меню с иконками

```python
# Меню с иконками
menu_items = [
    {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Пользователи", "url": "/users/", "icon": "users"},
    {"text": "Настройки", "url": "/settings/", "icon": "cog"}
]

menu_html = render_menu(items=menu_items, show_icons=True)
```

### Вложенное меню

```python
# Меню с подменю
menu_items = [
    {"text": "Главная", "url": "/"},
    {
        "text": "Продукты",
        "children": [
            {"text": "Ноутбуки", "url": "/products/laptops/"},
            {"text": "Телефоны", "url": "/products/phones/"}
        ]
    },
    {"text": "Контакты", "url": "/contact/"}
]

menu_html = render_menu(items=menu_items)
```

## Результат рендеринга

### Базовое меню

```html
<!-- Ввод -->
render_menu(items=[{"text": "Главная", "url": "/"}, {"text": "О нас", "url":
"/about/"}])

<!-- Вывод -->
<ul class="menu" data-role="menu">
	<li class="menu-item">
		<a href="/" class="menu-link">Главная</a>
	</li>
	<li class="menu-item">
		<a href="/about/" class="menu-link">О нас</a>
	</li>
</ul>
```

### Меню с иконками

```html
<!-- Ввод -->
render_menu(items=[{"text": "Главная", "url": "/", "icon": "home"}],
show_icons=True)

<!-- Вывод -->
<ul class="menu menu-with-icons" data-role="menu">
	<li class="menu-item">
		<a href="/" class="menu-link">
			<span class="mif-home"></span>
			Главная
		</a>
	</li>
</ul>
```

### Вложенное меню

```html
<!-- Ввод -->
render_menu(items=[{"text": "Продукты", "children": [{"text": "Ноутбуки", "url":
"/laptops/"}]}])

<!-- Вывод -->
<ul class="menu" data-role="menu">
	<li class="menu-item has-children">
		<a href="#" class="menu-link">Продукты</a>
		<ul class="menu-submenu">
			<li class="menu-item">
				<a href="/laptops/" class="menu-link">Ноутбуки</a>
			</li>
		</ul>
	</li>
</ul>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовое меню -->
{% metroui5_menu items=menu_items %}

<!-- Меню с иконками -->
{% metroui5_menu items=menu_items show_icons=True %}

<!-- Пользовательское меню -->
{% metroui5_menu items=menu_items class="menu-vertical" %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_menu

def menu_view(request):
    # Создать навигационное меню
    nav_items = [
        {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard"},
        {"text": "Пользователи", "url": "/users/", "icon": "users"},
        {
            "text": "Отчеты",
            "icon": "chart",
            "children": [
                {"text": "Продажи", "url": "/reports/sales/"},
                {"text": "Аналитика", "url": "/reports/analytics/"}
            ]
        }
    ]

    menu_html = render_menu(
        items=nav_items,
        show_icons=True,
        class="menu-primary"
    )

    context = {
        'menu_html': menu_html,
        'nav_items': nav_items
    }
    return render(request, 'menu.html', context)
```

```html
<!-- menu.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ menu_html|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_menu items=nav_items show_icons=True %} {% endblock %}
```

## Параметры

### `items` (обязательно)

Список элементов меню с текстом, URL и опциональными свойствами.

**Формат**:

```python
items = [
    {
        "text": "Элемент меню",
        "url": "/путь/",
        "icon": "название-иконки",  # Опционально
        "active": True,              # Опционально
        "children": []               # Опционально для подменю
    }
]
```

### `show_icons` (опционально)

Отображать ли иконки в элементах меню.

**По умолчанию**: `False`

**Пример**:

```python
menu_html = render_menu(items=items, show_icons=True)
```

### `orientation` (опционально)

Ориентация меню: горизонтальная или вертикальная.

**По умолчанию**: `"horizontal"`

**Пример**:

```python
menu_html = render_menu(items=items, orientation="vertical")
```

### `id` (опционально)

Уникальный идентификатор для элемента меню.

**Пример**:

```python
menu_html = render_menu(items=items, id="main-menu")
```

### `class` (опционально)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
menu_html = render_menu(items=items, class="menu-primary")
```

## Продвинутые примеры

### Контекстное меню

```python
def create_context_menu(actions):
    """Создать контекстное меню по правому клику."""

    context_items = []
    for action in actions:
        context_items.append({
            "text": action["text"],
            "onclick": action["function"],
            "icon": action.get("icon"),
            "disabled": action.get("disabled", False)
        })

    return render_menu(
        items=context_items,
        class="menu-context",
        show_icons=True
    )
```

### Меню-хлебные крошки

```python
def create_breadcrumb_menu(path_items):
    """Создать навигационное меню-хлебные крошки."""

    breadcrumb_items = []
    for i, item in enumerate(path_items):
        breadcrumb_items.append({
            "text": item["text"],
            "url": item["url"] if i < len(path_items) - 1 else None,
            "active": i == len(path_items) - 1
        })

    return render_menu(
        items=breadcrumb_items,
        class="menu-breadcrumb",
        orientation="horizontal"
    )
```

### Пользовательское меню

```python
def create_user_menu(user):
    """Создать меню профиля пользователя."""

    user_items = [
        {"text": f"Добро пожаловать, {user.first_name}", "disabled": True},
        {"text": "Профиль", "url": "/profile/", "icon": "user"},
        {"text": "Настройки", "url": "/settings/", "icon": "cog"},
        {"text": "Выход", "url": "/logout/", "icon": "exit"}
    ]

    return render_menu(
        items=user_items,
        class="menu-user",
        show_icons=True
    )
```

### Боковое меню

```python
def create_sidebar_menu(sections):
    """Создать боковое навигационное меню."""

    sidebar_items = []
    for section in sections:
        if section.get("children"):
            sidebar_items.append({
                "text": section["title"],
                "icon": section.get("icon"),
                "children": section["children"]
            })
        else:
            sidebar_items.append({
                "text": section["title"],
                "url": section["url"],
                "icon": section.get("icon")
            })

    return render_menu(
        items=sidebar_items,
        orientation="vertical",
        class="menu-sidebar",
        show_icons=True
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `menu` - Базовый класс меню
- `menu-primary` - Основной стиль меню
- `menu-secondary` - Вторичный стиль меню

#### Классы ориентации

- `menu-horizontal` - Горизонтальная компоновка меню
- `menu-vertical` - Вертикальная компоновка меню

#### Классы функций

- `menu-with-icons` - Меню с поддержкой иконок
- `menu-collapsible` - Сворачиваемые секции меню

#### Классы типов

- `menu-context` - Стиль контекстного меню
- `menu-breadcrumb` - Стиль меню-хлебных крошек
- `menu-sidebar` - Стиль бокового меню

### Пользовательская стилизация

```css
/* Пользовательская стилизация меню */
.menu-custom {
	background: #f8f9fa;
	border: 1px solid #dee2e6;
	border-radius: 6px;
	padding: 10px 0;
}

.menu-custom .menu-item {
	margin: 0;
}

.menu-custom .menu-link {
	padding: 12px 20px;
	color: #495057;
	text-decoration: none;
	display: block;
	transition: all 0.3s ease;
}

.menu-custom .menu-link:hover {
	background: #007acc;
	color: white;
}

.menu-custom .menu-link.active {
	background: #0056b3;
	color: white;
	font-weight: bold;
}

/* Стилизация подменю */
.menu-custom .menu-submenu {
	background: #ffffff;
	border-left: 3px solid #007acc;
	margin-left: 20px;
}
```

## Интеграция с JavaScript

### События меню

```javascript
// Обработать клики по элементам меню
$(".menu").on("click", ".menu-link", function (e) {
	const menuItem = $(this);
	const hasChildren = menuItem.parent().hasClass("has-children");

	if (hasChildren) {
		e.preventDefault();
		toggleSubmenu(menuItem);
	} else {
		handleMenuClick(menuItem);
	}
});

function toggleSubmenu(menuLink) {
	const submenu = menuLink.siblings(".menu-submenu");
	submenu.slideToggle();
	menuLink.parent().toggleClass("expanded");
}

function handleMenuClick(menuLink) {
	// Убрать активный класс со всех элементов
	$(".menu-link").removeClass("active");

	// Добавить активный класс к нажатому элементу
	menuLink.addClass("active");

	// Отследить навигацию по меню
	const url = menuLink.attr("href");
	console.log("Переход к:", url);
}
```

### Контекстное меню

```javascript
// Показать контекстное меню по правому клику
$(document).on("contextmenu", ".context-target", function (e) {
	e.preventDefault();

	const contextMenu = $(".menu-context");
	contextMenu.css({
		display: "block",
		left: e.pageX,
		top: e.pageY,
	});

	// Скрыть контекстное меню при клике в другом месте
	$(document).one("click", function () {
		contextMenu.hide();
	});
});
```

### Динамическая загрузка меню

```javascript
// Загрузить элементы меню динамически
function loadMenuItems(menuId, url) {
	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			updateMenu(menuId, data.items);
		},
		error: function (xhr, status, error) {
			console.error("Ошибка загрузки меню:", error);
		},
	});
}

function updateMenu(menuId, items) {
	const menu = $(`#${menuId}`);
	menu.empty();

	items.forEach((item) => {
		const menuItem = createMenuItem(item);
		menu.append(menuItem);
	});
}

function createMenuItem(item) {
	const icon = item.icon ? `<span class="mif-${item.icon}"></span>` : "";
	const link = `<a href="${item.url}" class="menu-link">${icon}${item.text}</a>`;
	return `<li class="menu-item">${link}</li>`;
}
```

## Лучшие практики

### 1. Структура меню

```python
# Консистентная структура элементов меню
def create_menu_item(text, url=None, icon=None, children=None, **kwargs):
    """Создать стандартизированный элемент меню."""
    item = {"text": text}
    if url:
        item["url"] = url
    if icon:
        item["icon"] = icon
    if children:
        item["children"] = children
    item.update(kwargs)
    return item
```

### 2. Управление активным состоянием

```python
# Определить активные элементы меню
def set_active_menu_item(menu_items, current_path):
    """Установить активное состояние для текущей страницы."""
    for item in menu_items:
        if item.get("url") == current_path:
            item["active"] = True
        elif item.get("children"):
            set_active_menu_item(item["children"], current_path)
```

### 3. Меню на основе разрешений

```python
# Фильтровать элементы меню на основе разрешений
def filter_menu_by_permissions(menu_items, user):
    """Фильтровать элементы меню на основе разрешений пользователя."""
    filtered_items = []
    for item in menu_items:
        if has_permission(user, item.get("permission")):
            if item.get("children"):
                item["children"] = filter_menu_by_permissions(item["children"], user)
            filtered_items.append(item)
    return filtered_items
```

## Связанные компоненты

- [Навигация](navigation.md) - Для систем навигации
- [Кнопки](buttons.md) - Для триггеров меню
- [Иконки](icons.md) - Для иконок элементов меню
- [Выпадающие списки](dropdowns.md) - Для выпадающих меню
