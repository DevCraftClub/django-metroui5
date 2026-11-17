# Вкладки

Компонент для создания интерфейсов с вкладками, содержащими несколько панелей контента и навигационные вкладки.

## Базовое использование

### Простые вкладки

```python
from metroui5.components import render_tabs

# Базовые вкладки
tab_items = [
    {"title": "Вкладка 1", "content": "Содержимое для вкладки 1"},
    {"title": "Вкладка 2", "content": "Содержимое для вкладки 2"},
    {"title": "Вкладка 3", "content": "Содержимое для вкладки 3"}
]

tabs_html = render_tabs(items=tab_items)
```

### Вкладки с иконками

```python
# Вкладки с иконками
tab_items = [
    {"title": "Главная", "content": "Содержимое главной", "icon": "home"},
    {"title": "Профиль", "content": "Содержимое профиля", "icon": "user"},
    {"title": "Настройки", "content": "Содержимое настроек", "icon": "cog"}
]

tabs_html = render_tabs(items=tab_items, show_icons=True)
```

### Пользовательские вкладки

```python
# Пользовательские вкладки с активной вкладкой
tabs_html = render_tabs(
    items=tab_items,
    active_tab=1,
    orientation="horizontal",
    id="main-tabs"
)
```

## Вывод HTML

### Базовые вкладки

```html
<!-- Ввод -->
render_tabs(items=[{"title": "Вкладка 1", "content": "Содержимое 1"}, {"title":
"Вкладка 2", "content": "Содержимое 2"}])

<!-- Вывод -->
<div class="tabs" data-role="tabs">
	<ul class="tabs-nav">
		<li class="tab-nav-item active">
			<a href="#tab-0" class="tab-nav-link">Вкладка 1</a>
		</li>
		<li class="tab-nav-item">
			<a href="#tab-1" class="tab-nav-link">Вкладка 2</a>
		</li>
	</ul>
	<div class="tabs-content">
		<div id="tab-0" class="tab-panel active">Содержимое 1</div>
		<div id="tab-1" class="tab-panel">Содержимое 2</div>
	</div>
</div>
```

### Вкладки с иконками

```html
<!-- Ввод -->
render_tabs(items=[{"title": "Главная", "content": "Содержимое главной", "icon":
"home"}], show_icons=True)

<!-- Вывод -->
<div class="tabs tabs-with-icons" data-role="tabs">
	<ul class="tabs-nav">
		<li class="tab-nav-item active">
			<a href="#tab-0" class="tab-nav-link">
				<span class="mif-home"></span>
				Главная
			</a>
		</li>
	</ul>
	<div class="tabs-content">
		<div id="tab-0" class="tab-panel active">Содержимое главной</div>
	</div>
</div>
```

### Вертикальные вкладки

```html
<!-- Ввод -->
render_tabs(items=tab_items, orientation="vertical")

<!-- Вывод -->
<div class="tabs tabs-vertical" data-role="tabs">
	<ul class="tabs-nav tabs-nav-vertical">
		<li class="tab-nav-item active">
			<a href="#tab-0" class="tab-nav-link">Вкладка 1</a>
		</li>
	</ul>
	<div class="tabs-content">
		<div id="tab-0" class="tab-panel active">Содержимое 1</div>
	</div>
</div>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовые вкладки -->
{% metroui5_tabs items=tab_items %}

<!-- Вкладки с иконками -->
{% metroui5_tabs items=tab_items show_icons=True %}

<!-- Пользовательские вкладки -->
{% metroui5_tabs items=tab_items active_tab=2 orientation="vertical" %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_tabs

def tabs_view(request):
    # Создание вкладок контента
    content_tabs = [
        {
            "title": "Обзор",
            "content": "<p>Обзор проекта и резюме</p>",
            "icon": "chart"
        },
        {
            "title": "Детали",
            "content": "<p>Подробная информация о проекте</p>",
            "icon": "info"
        },
        {
            "title": "Команда",
            "content": "<p>Члены команды и роли</p>",
            "icon": "users"
        }
    ]

    tabs_html = render_tabs(
        items=content_tabs,
        show_icons=True,
        active_tab=0,
        id="project-tabs"
    )

    context = {
        'tabs_html': tabs_html,
        'content_tabs': content_tabs
    }
    return render(request, 'tabs.html', context)
```

```html
<!-- tabs.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ tabs_html|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_tabs items=content_tabs show_icons=True %} {% endblock %}
```

## Параметры

### `items` (обязательный)

Список элементов вкладок с заголовком и содержимым.

**Формат**:

```python
items = [
    {
        "title": "Заголовок вкладки",
        "content": "HTML содержимое вкладки",
        "icon": "имя-иконки",    # Необязательно
        "disabled": False,      # Необязательно
        "closable": False       # Необязательно
    }
]
```

### `active_tab` (необязательный)

Индекс изначально активной вкладки.

**По умолчанию**: `0`

**Пример**:

```python
tabs_html = render_tabs(items=items, active_tab=2)
```

### `show_icons` (необязательный)

Отображать ли иконки в заголовках вкладок.

**По умолчанию**: `False`

**Пример**:

```python
tabs_html = render_tabs(items=items, show_icons=True)
```

### `orientation` (необязательный)

Ориентация вкладок: горизонтальная или вертикальная.

**По умолчанию**: `"horizontal"`

**Пример**:

```python
tabs_html = render_tabs(items=items, orientation="vertical")
```

### `closable` (необязательный)

Можно ли закрывать вкладки.

**По умолчанию**: `False`

**Пример**:

```python
tabs_html = render_tabs(items=items, closable=True)
```

### `id` (необязательный)

Уникальный идентификатор для контейнера вкладок.

**Пример**:

```python
tabs_html = render_tabs(items=items, id="main-tabs")
```

### `class` (необязательный)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
tabs_html = render_tabs(items=items, class="tabs-custom")
```

## Расширенные примеры

### Динамические вкладки

```python
def create_dynamic_tabs(base_tabs, user_tabs=None):
    """Создание вкладок с динамическим пользовательским контентом."""

    all_tabs = base_tabs.copy()

    if user_tabs:
        all_tabs.extend(user_tabs)

    return render_tabs(
        items=all_tabs,
        closable=True,
        class="tabs-dynamic"
    )
```

### Вкладки форм

```python
def create_form_tabs(form_sections):
    """Создание вкладок для многошаговой формы."""

    form_tabs = []
    for i, section in enumerate(form_sections):
        form_tabs.append({
            "title": section["title"],
            "content": section["form_html"],
            "icon": section.get("icon"),
            "data-step": i + 1
        })

    return render_tabs(
        items=form_tabs,
        show_icons=True,
        class="tabs-form"
    )
```

### Вкладки управления контентом

```python
def create_content_tabs(content_types):
    """Создание вкладок для различных типов контента."""

    content_tabs = []
    for content_type in content_types:
        content_tabs.append({
            "title": content_type["name"],
            "content": f"""
            <div class="content-section">
                <h3>{content_type["name"]}</h3>
                <div class="content-list">
                    {render_content_list(content_type["items"])}
                </div>
            </div>
            """,
            "icon": content_type.get("icon"),
            "count": len(content_type["items"])
        })

    return render_tabs(
        items=content_tabs,
        show_icons=True,
        class="tabs-content-management"
    )
```

### Вкладки панели управления

```python
def create_dashboard_tabs(dashboard_sections):
    """Создание панели управления с вкладками."""

    dashboard_tabs = []
    for section in dashboard_sections:
        dashboard_tabs.append({
            "title": section["title"],
            "content": f"""
            <div class="dashboard-section">
                {render_dashboard_widgets(section["widgets"])}
            </div>
            """,
            "icon": section.get("icon")
        })

    return render_tabs(
        items=dashboard_tabs,
        show_icons=True,
        class="tabs-dashboard"
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `tabs` - Базовый контейнер вкладок
- `tabs-primary` - Основной стиль вкладок
- `tabs-secondary` - Вторичный стиль вкладок

#### Классы ориентации

- `tabs-horizontal` - Горизонтальная компоновка вкладок
- `tabs-vertical` - Вертикальная компоновка вкладок

#### Классы функций

- `tabs-with-icons` - Вкладки с поддержкой иконок
- `tabs-closable` - Закрываемые вкладки
- `tabs-scrollable` - Прокручиваемая навигация вкладок

#### Типы классов

- `tabs-form` - Вкладки в стиле форм
- `tabs-dashboard` - Вкладки в стиле панели управления
- `tabs-content` - Вкладки управления контентом

### Пользовательская стилизация

```css
/* Пользовательская стилизация вкладок */
.tabs-custom {
	border: 1px solid #dee2e6;
	border-radius: 6px;
	overflow: hidden;
}

.tabs-custom .tabs-nav {
	background: #f8f9fa;
	border-bottom: 1px solid #dee2e6;
	margin: 0;
	padding: 0;
	list-style: none;
	display: flex;
}

.tabs-custom .tab-nav-item {
	margin: 0;
}

.tabs-custom .tab-nav-link {
	display: block;
	padding: 15px 20px;
	color: #495057;
	text-decoration: none;
	border-right: 1px solid #dee2e6;
	transition: all 0.3s ease;
}

.tabs-custom .tab-nav-link:hover {
	background: #e9ecef;
	color: #007acc;
}

.tabs-custom .tab-nav-item.active .tab-nav-link {
	background: #007acc;
	color: white;
	border-bottom: 2px solid #0056b3;
}

.tabs-custom .tabs-content {
	padding: 20px;
}

.tabs-custom .tab-panel {
	display: none;
}

.tabs-custom .tab-panel.active {
	display: block;
}

/* Вертикальные вкладки */
.tabs-custom.tabs-vertical {
	display: flex;
}

.tabs-custom.tabs-vertical .tabs-nav {
	flex-direction: column;
	width: 200px;
	border-right: 1px solid #dee2e6;
	border-bottom: none;
}

.tabs-custom.tabs-vertical .tab-nav-link {
	border-right: none;
	border-bottom: 1px solid #dee2e6;
}

.tabs-custom.tabs-vertical .tabs-content {
	flex: 1;
}
```

## Интеграция с JavaScript

### Навигация по вкладкам

```javascript
// Обработка кликов по вкладкам
$(".tabs").on("click", ".tab-nav-link", function (e) {
	e.preventDefault();

	const tabLink = $(this);
	const tabsContainer = tabLink.closest(".tabs");
	const targetId = tabLink.attr("href");

	// Обновление активной навигации вкладок
	tabsContainer.find(".tab-nav-item").removeClass("active");
	tabLink.parent().addClass("active");

	// Обновление активного содержимого вкладки
	tabsContainer.find(".tab-panel").removeClass("active");
	tabsContainer.find(targetId).addClass("active");

	// Запуск события изменения вкладки
	tabsContainer.trigger("tab-changed", [targetId]);
});
```

### Динамическое управление вкладками

```javascript
// Добавление новой вкладки
function addTab(tabsId, title, content, icon = null) {
	const tabs = $(`#${tabsId}`);
	const tabsNav = tabs.find(".tabs-nav");
	const tabsContent = tabs.find(".tabs-content");
	const tabIndex = tabs.find(".tab-nav-item").length;
	const tabId = `tab-${tabIndex}`;

	// Добавление элемента навигации
	const iconHtml = icon ? `<span class="mif-${icon}"></span>` : "";
	const navItem = `
        <li class="tab-nav-item">
            <a href="#${tabId}" class="tab-nav-link">
                ${iconHtml}${title}
                <button class="tab-close" onclick="closeTab('${tabId}')">&times;</button>
            </a>
        </li>
    `;
	tabsNav.append(navItem);

	// Добавление панели содержимого
	const contentPanel = `
        <div id="${tabId}" class="tab-panel">
            ${content}
        </div>
    `;
	tabsContent.append(contentPanel);

	// Активация новой вкладки
	switchTab(tabsId, tabId);
}

// Закрытие вкладки
function closeTab(tabId) {
	const tabPanel = $(`#${tabId}`);
	const tabsContainer = tabPanel.closest(".tabs");
	const tabNavItem = tabsContainer.find(`a[href="#${tabId}"]`).parent();

	// Удаление навигации и содержимого вкладки
	tabNavItem.remove();
	tabPanel.remove();

	// Активация первой оставшейся вкладки, если закрытая вкладка была активной
	if (tabPanel.hasClass("active")) {
		const firstTab = tabsContainer.find(".tab-nav-link").first();
		if (firstTab.length) {
			firstTab.click();
		}
	}
}

// Переключение на конкретную вкладку
function switchTab(tabsId, tabId) {
	const tabs = $(`#${tabsId}`);
	const targetLink = tabs.find(`a[href="#${tabId}"]`);
	targetLink.click();
}
```

### Загрузка содержимого вкладок

```javascript
// Загрузка содержимого вкладки через AJAX
function loadTabContent(tabId, url) {
	const tabPanel = $(`#${tabId}`);

	// Показ состояния загрузки
	tabPanel.html('<div class="loading">Загрузка...</div>');

	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			tabPanel.html(data);
		},
		error: function (xhr, status, error) {
			tabPanel.html('<div class="error">Ошибка загрузки содержимого</div>');
			console.error("Ошибка загрузки содержимого вкладки:", error);
		},
	});
}

// Ленивая загрузка содержимого вкладок
$(".tabs").on("tab-changed", function (e, tabId) {
	const tabPanel = $(tabId);
	const loadUrl = tabPanel.data("load-url");

	if (loadUrl && !tabPanel.data("loaded")) {
		loadTabContent(tabId.substring(1), loadUrl);
		tabPanel.data("loaded", true);
	}
});
```

## Лучшие практики

### 1. Структура содержимого вкладок

```python
# Последовательная структура вкладок
def create_tab_item(title, content, icon=None, **kwargs):
    """Создание стандартизированного элемента вкладки."""
    tab = {"title": title, "content": content}
    if icon:
        tab["icon"] = icon
    tab.update(kwargs)
    return tab
```

### 2. Адаптивные вкладки

```python
# Создание адаптивных вкладок, работающих на мобильных устройствах
def create_responsive_tabs(items, mobile_accordion=True):
    return render_tabs(
        items=items,
        class="tabs-responsive" + (" tabs-mobile-accordion" if mobile_accordion else "")
    )
```

### 3. Сохранение состояния

```python
# Запоминание активной вкладки между загрузками страниц
def create_stateful_tabs(items, request):
    active_tab = int(request.GET.get('tab', 0))
    return render_tabs(
        items=items,
        active_tab=active_tab,
        class="tabs-stateful"
    )
```

## Связанные компоненты

- [Навигация](navigation.md) - Для навигации по вкладкам
- [Панели](panels.md) - Для панелей содержимого вкладок
- [Иконки](icons.md) - Для иконок вкладок
- [Формы](forms.md) - Для форм с вкладками


## metroui5_tabs

```python
render_tabs([{'title': 'One', 'content': 'Text'}])
```

Пустое или неверное значение: `render_tabs([{'title': 'One', 'content': 'Text'}])` даёт `<ul data-role="tabs"><li><a href="#tab-0">One</a></li></ul><div class="tabs-targets"><div id="tab-0">Text</div></div>`. Пустой вызов даёт `<ul data-role="tabs"></ul><div class="tabs-targets"></div>`.

```django
{% metroui5_tabs tabs %}
```
