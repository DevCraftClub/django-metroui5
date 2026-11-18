# Боковые панели

Компонент для создания навигационных боковых панелей, боковых панелей и сворачиваемых боковых областей контента.

## Базовое использование

### Простая боковая панель

```python
from metroui5.components import render_sidebar

# Базовая боковая панель
sidebar_html = render_sidebar(
    content="<p>Содержимое боковой панели здесь</p>"
)
```

### Боковая панель с меню

```python
# Боковая панель с навигационным меню
menu_items = [
    {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Пользователи", "url": "/users/", "icon": "users"},
    {"text": "Настройки", "url": "/settings/", "icon": "cog"}
]

sidebar_html = render_sidebar(
    menu_items=menu_items,
    title="Навигация"
)
```

### Сворачиваемая боковая панель

```python
# Сворачиваемая боковая панель
sidebar_html = render_sidebar(
    content="<p>Сворачиваемый контент</p>",
    collapsible=True,
    collapsed=False,
    position="left"
)
```

## Результат рендеринга

### Базовая боковая панель

```html
<!-- Ввод -->
render_sidebar(content="
<p>Содержимое боковой панели</p>
")

<!-- Вывод -->
<div class="sidebar" data-role="sidebar">
	<div class="sidebar-content">
		<p>Содержимое боковой панели</p>
	</div>
</div>
```

### Боковая панель с меню

```html
<!-- Ввод -->
render_sidebar(menu_items=[{"text": "Главная", "url": "/", "icon": "home"}],
title="Навигация")

<!-- Вывод -->
<div class="sidebar sidebar-with-menu" data-role="sidebar">
	<div class="sidebar-header">
		<h3>Навигация</h3>
	</div>
	<div class="sidebar-content">
		<ul class="sidebar-menu">
			<li class="sidebar-menu-item">
				<a href="/" class="sidebar-menu-link">
					<span class="mif-home"></span>
					Главная
				</a>
			</li>
		</ul>
	</div>
</div>
```

### Сворачиваемая боковая панель

```html
<!-- Ввод -->
render_sidebar(content="Контент", collapsible=True, position="left")

<!-- Вывод -->
<div
	class="sidebar sidebar-collapsible sidebar-left"
	data-role="sidebar"
	data-collapsible="true"
>
	<button class="sidebar-toggle" data-role="sidebar-toggle">☰</button>
	<div class="sidebar-content">Контент</div>
</div>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовая боковая панель -->
{% metroui5_sidebar content="
<p>Контент</p>
" %}

<!-- Боковая панель с меню -->
{% metroui5_sidebar menu_items=sidebar_menu title="Навигация" %}

<!-- Сворачиваемая боковая панель -->
{% metroui5_sidebar content="Контент" collapsible=True position="right" %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_sidebar

def sidebar_view(request):
    # Создать навигационную боковую панель
    nav_items = [
        {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard", "active": True},
        {"text": "Пользователи", "url": "/users/", "icon": "users"},
        {"text": "Отчеты", "url": "/reports/", "icon": "chart"},
        {"text": "Настройки", "url": "/settings/", "icon": "cog"}
    ]

    sidebar_html = render_sidebar(
        menu_items=nav_items,
        title="Главное меню",
        position="left",
        collapsible=True
    )

    context = {
        'sidebar_html': sidebar_html,
        'nav_items': nav_items
    }
    return render(request, 'sidebar.html', context)
```

```html
<!-- sidebar.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ sidebar_html|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_sidebar menu_items=nav_items title="Навигация" position="left" %} {%
endblock %}
```

## Параметры

### `content` (опционально)

HTML контент для отображения в боковой панели.

**Пример**:

```python
sidebar_html = render_sidebar(content="<p>Пользовательский контент</p>")
```

### `menu_items` (опционально)

Список элементов меню для навигационной боковой панели.

**Формат**:

```python
menu_items = [
    {
        "text": "Элемент меню",
        "url": "/путь/",
        "icon": "название-иконки",  # Опционально
        "active": True,              # Опционально
        "children": []               # Опционально для подменю
    }
]
```

### `title` (опционально)

Заголовок, отображаемый в заголовке боковой панели.

**Пример**:

```python
sidebar_html = render_sidebar(title="Навигационное меню")
```

### `position` (опционально)

Позиция боковой панели: left или right.

**По умолчанию**: `"left"`

**Пример**:

```python
sidebar_html = render_sidebar(content="Контент", position="right")
```

### `collapsible` (опционально)

Может ли боковая панель быть свернута.

**По умолчанию**: `False`

**Пример**:

```python
sidebar_html = render_sidebar(content="Контент", collapsible=True)
```

### `collapsed` (опционально)

Начальное свернутое состояние (если сворачиваемая).

**По умолчанию**: `False`

**Пример**:

```python
sidebar_html = render_sidebar(content="Контент", collapsible=True, collapsed=True)
```

### `width` (опционально)

Ширина боковой панели.

**Пример**:

```python
sidebar_html = render_sidebar(content="Контент", width="300px")
```

### `id` (опционально)

Уникальный идентификатор для элемента боковой панели.

**Пример**:

```python
sidebar_html = render_sidebar(content="Контент", id="main-sidebar")
```

### `class` (опционально)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
sidebar_html = render_sidebar(content="Контент", class="sidebar-custom")
```

## Продвинутые примеры

### Многоуровневая навигационная боковая панель

```python
def create_nav_sidebar(nav_sections):
    """Создать боковую панель с группированной навигацией."""

    menu_items = []
    for section in nav_sections:
        if section.get("children"):
            menu_items.append({
                "text": section["title"],
                "icon": section.get("icon"),
                "children": section["children"]
            })
        else:
            menu_items.append({
                "text": section["title"],
                "url": section["url"],
                "icon": section.get("icon")
            })

    return render_sidebar(
        menu_items=menu_items,
        title="Навигация",
        position="left",
        collapsible=True,
        class="sidebar-navigation"
    )
```

### Боковая панель фильтров

```python
def create_filter_sidebar(filters):
    """Создать боковую панель с опциями фильтров."""

    filter_content = "<div class='sidebar-filters'>"

    for filter_group in filters:
        filter_content += f"<h4>{filter_group['title']}</h4>"
        filter_content += "<div class='filter-group'>"

        for option in filter_group['options']:
            checked = "checked" if option.get('selected') else ""
            filter_content += f"""
            <label class="filter-option">
                <input type="checkbox" name="{filter_group['name']}"
                       value="{option['value']}" {checked}>
                {option['text']}
            </label>
            """

        filter_content += "</div>"

    filter_content += "</div>"

    return render_sidebar(
        content=filter_content,
        title="Фильтры",
        position="left",
        class="sidebar-filters"
    )
```

### Боковая панель профиля пользователя

```python
def create_profile_sidebar(user):
    """Создать боковую панель профиля пользователя."""

    profile_content = f"""
    <div class="user-profile">
        <div class="user-avatar">
            <img src="{user.avatar_url}" alt="{user.name}">
        </div>
        <div class="user-info">
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            <p class="user-role">{user.role}</p>
        </div>
        <div class="user-stats">
            <div class="stat">
                <span class="stat-value">{user.posts_count}</span>
                <span class="stat-label">Посты</span>
            </div>
            <div class="stat">
                <span class="stat-value">{user.followers_count}</span>
                <span class="stat-label">Подписчики</span>
            </div>
        </div>
    </div>
    """

    return render_sidebar(
        content=profile_content,
        title="Профиль",
        position="right",
        class="sidebar-profile"
    )
```

### Боковая панель виджетов

```python
def create_widget_sidebar(widgets):
    """Создать боковую панель с несколькими виджетами."""

    widget_content = ""

    for widget in widgets:
        widget_content += f"""
        <div class="sidebar-widget">
            <h4 class="widget-title">{widget['title']}</h4>
            <div class="widget-content">
                {widget['content']}
            </div>
        </div>
        """

    return render_sidebar(
        content=widget_content,
        title="Виджеты",
        position="right",
        class="sidebar-widgets"
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `sidebar` - Базовый класс боковой панели
- `sidebar-primary` - Основной стиль боковой панели
- `sidebar-secondary` - Вторичный стиль боковой панели

#### Классы позиции

- `sidebar-left` - Левосторонняя боковая панель
- `sidebar-right` - Правосторонняя боковая панель

#### Классы функций

- `sidebar-collapsible` - Сворачиваемая боковая панель
- `sidebar-collapsed` - Свернутое состояние
- `sidebar-with-menu` - Боковая панель с элементами меню

#### Классы типов

- `sidebar-navigation` - Навигационная боковая панель
- `sidebar-filters` - Боковая панель фильтров
- `sidebar-widgets` - Боковая панель виджетов

### Пользовательская стилизация

```css
/* Пользовательская стилизация боковой панели */
.sidebar-custom {
	background: #f8f9fa;
	border-right: 1px solid #dee2e6;
	box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
	width: 280px;
	height: 100vh;
	position: fixed;
	left: 0;
	top: 0;
	z-index: 1000;
}

.sidebar-custom .sidebar-header {
	background: #007acc;
	color: white;
	padding: 20px;
	border-bottom: 1px solid #005a99;
}

.sidebar-custom .sidebar-content {
	padding: 20px;
	height: calc(100vh - 80px);
	overflow-y: auto;
}

.sidebar-custom .sidebar-menu-item {
	margin-bottom: 5px;
}

.sidebar-custom .sidebar-menu-link {
	display: block;
	padding: 12px 15px;
	color: #495057;
	text-decoration: none;
	border-radius: 6px;
	transition: all 0.3s ease;
}

.sidebar-custom .sidebar-menu-link:hover {
	background: #007acc;
	color: white;
}

.sidebar-custom .sidebar-menu-link.active {
	background: #0056b3;
	color: white;
}

/* Свернутая боковая панель */
.sidebar-custom.sidebar-collapsed {
	width: 60px;
}

.sidebar-custom.sidebar-collapsed .sidebar-content {
	padding: 10px;
}

.sidebar-custom.sidebar-collapsed .sidebar-menu-link {
	text-align: center;
	padding: 15px 5px;
}

.sidebar-custom.sidebar-collapsed .sidebar-menu-link span:not(.mif) {
	display: none;
}
```

## Интеграция с JavaScript

### Переключение боковой панели

```javascript
// Переключить сворачивание боковой панели
function toggleSidebar(sidebarId) {
	const sidebar = $(`#${sidebarId}`);
	sidebar.toggleClass("sidebar-collapsed");

	// Сохранить состояние в localStorage
	const isCollapsed = sidebar.hasClass("sidebar-collapsed");
	localStorage.setItem("sidebar-collapsed", isCollapsed);
}

// Инициализировать состояние боковой панели из localStorage
$(document).ready(function () {
	const isCollapsed = localStorage.getItem("sidebar-collapsed") === "true";
	if (isCollapsed) {
		$(".sidebar").addClass("sidebar-collapsed");
	}

	// Обработать клики по кнопке переключения
	$(".sidebar-toggle").on("click", function () {
		const sidebar = $(this).closest(".sidebar");
		toggleSidebar(sidebar.attr("id"));
	});
});
```

### Адаптивная боковая панель

```javascript
// Обработать поведение адаптивной боковой панели
function handleResponsiveSidebar() {
	const sidebar = $(".sidebar");
	const windowWidth = $(window).width();

	if (windowWidth < 768) {
		// Мобильные: Скрыть боковую панель по умолчанию
		sidebar.addClass("sidebar-mobile");
		sidebar.addClass("sidebar-collapsed");
	} else {
		// Десктоп: Показать боковую панель
		sidebar.removeClass("sidebar-mobile");
		const savedState = localStorage.getItem("sidebar-collapsed") === "true";
		sidebar.toggleClass("sidebar-collapsed", savedState);
	}
}

// Обработать изменение размера окна
$(window).on("resize", handleResponsiveSidebar);

// Инициализировать при загрузке страницы
$(document).ready(handleResponsiveSidebar);
```

### Навигация по меню боковой панели

```javascript
// Обработать клики по меню боковой панели
$(".sidebar-menu").on("click", ".sidebar-menu-link", function (e) {
	const menuLink = $(this);
	const hasChildren = menuLink.parent().hasClass("has-children");

	if (hasChildren) {
		e.preventDefault();
		toggleSubmenu(menuLink);
	} else {
		setActiveMenuItem(menuLink);
	}
});

function toggleSubmenu(menuLink) {
	const submenu = menuLink.siblings(".sidebar-submenu");
	const parent = menuLink.parent();

	submenu.slideToggle();
	parent.toggleClass("expanded");
}

function setActiveMenuItem(menuLink) {
	// Убрать активный класс со всех элементов
	$(".sidebar-menu-link").removeClass("active");

	// Добавить активный класс к нажатому элементу
	menuLink.addClass("active");

	// Обновить хлебные крошки или заголовок страницы
	const itemText = menuLink.text().trim();
	updatePageTitle(itemText);
}
```

## Лучшие практики

### 1. Адаптивный дизайн

```python
# Создать адаптивную боковую панель
def create_responsive_sidebar(menu_items, mobile_collapsed=True):
    return render_sidebar(
        menu_items=menu_items,
        collapsible=True,
        collapsed=mobile_collapsed,
        class="sidebar-responsive"
    )
```

### 2. Управление состоянием

```python
# Сохранить состояние боковой панели
def get_sidebar_state(request):
    return {
        'collapsed': request.session.get('sidebar_collapsed', False),
        'active_item': request.path
    }
```

### 3. Меню на основе разрешений

```python
# Фильтровать элементы меню по разрешениям пользователя
def create_authorized_sidebar(user, all_menu_items):
    authorized_items = []
    for item in all_menu_items:
        if user.has_perm(item.get('permission', 'view')):
            authorized_items.append(item)

    return render_sidebar(
        menu_items=authorized_items,
        title="Навигация",
        collapsible=True
    )
```

## Связанные компоненты

- [Меню](menus.md) - Для элементов меню боковой панели
- [Навигация](navigation.md) - Для систем навигации
- [Иконки](icons.md) - Для иконок меню боковой панели
- [Панели](panels.md) - Для панелей содержимого боковой панели


## metroui5_sidebar

```python
render_sidebar([{'text': 'One', 'href': '/one'}])
```

Пустое или неверное значение: `render_sidebar([{'text': 'One', 'href': '/one'}])` даёт `<ul class="sidebar" data-role="sidebar"><li><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="sidebar" data-role="sidebar"></ul>`.

```django
{% metroui5_sidebar items %}
```
