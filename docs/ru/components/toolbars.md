# Панели инструментов

Компонент для создания панелей инструментов действий, групп кнопок и панелей навигации с различными инструментами и элементами управления.

## Базовое использование

### Простая панель инструментов

```python
from metroui5.components import render_toolbar

# Базовая панель инструментов
toolbar_items = [
    {"text": "Новый", "icon": "plus"},
    {"text": "Сохранить", "icon": "checkmark"},
    {"text": "Удалить", "icon": "delete"}
]

toolbar_html = render_toolbar(items=toolbar_items)
```

### Панель инструментов с группами

```python
# Панель инструментов с сгруппированными элементами
toolbar_groups = [
    {
        "items": [
            {"text": "Новый", "icon": "plus", "onclick": "createNew()"},
            {"text": "Открыть", "icon": "folder", "onclick": "openFile()"}
        ]
    },
    {
        "items": [
            {"text": "Сохранить", "icon": "checkmark", "onclick": "saveFile()"},
            {"text": "Сохранить как", "icon": "save", "onclick": "saveAsFile()"}
        ]
    }
]

toolbar_html = render_toolbar(groups=toolbar_groups)
```

### Пользовательская панель инструментов

```python
# Пользовательская панель инструментов с позиционированием
toolbar_html = render_toolbar(
    items=toolbar_items,
    position="top",
    class="toolbar-primary",
    id="main-toolbar"
)
```

## Вывод HTML

### Базовая панель инструментов

```html
<!-- Ввод -->
render_toolbar(items=[{"text": "Новый", "icon": "plus"}, {"text": "Сохранить",
"icon": "checkmark"}])

<!-- Вывод -->
<div class="toolbar" data-role="toolbar">
	<div class="toolbar-group">
		<button class="toolbar-button" type="button">
			<span class="mif-plus"></span>
			Новый
		</button>
		<button class="toolbar-button" type="button">
			<span class="mif-checkmark"></span>
			Сохранить
		</button>
	</div>
</div>
```

### Панель инструментов с группами

```html
<!-- Ввод -->
render_toolbar(groups=[{"items": [{"text": "Новый", "icon": "plus"}]}, {"items":
[{"text": "Сохранить", "icon": "save"}]}])

<!-- Вывод -->
<div class="toolbar" data-role="toolbar">
	<div class="toolbar-group">
		<button class="toolbar-button" type="button">
			<span class="mif-plus"></span>
			Новый
		</button>
	</div>
	<div class="toolbar-group">
		<button class="toolbar-button" type="button">
			<span class="mif-save"></span>
			Сохранить
		</button>
	</div>
</div>
```

### Панель инструментов с выпадающим списком

```html
<!-- Ввод -->
render_toolbar(items=[{"text": "Действия", "dropdown": [{"text":
"Редактировать"}, {"text": "Удалить"}]}])

<!-- Вывод -->
<div class="toolbar" data-role="toolbar">
	<div class="toolbar-group">
		<div class="toolbar-dropdown">
			<button class="toolbar-button dropdown-toggle" type="button">
				Действия
				<span class="mif-chevron-down"></span>
			</button>
			<ul class="dropdown-menu">
				<li><a href="#" class="dropdown-item">Редактировать</a></li>
				<li><a href="#" class="dropdown-item">Удалить</a></li>
			</ul>
		</div>
	</div>
</div>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовая панель инструментов -->
{% metroui5_toolbar items=toolbar_items %}

<!-- Панель инструментов с группами -->
{% metroui5_toolbar groups=toolbar_groups %}

<!-- Пользовательская панель инструментов -->
{% metroui5_toolbar items=toolbar_items position="bottom"
class="toolbar-secondary" %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_toolbar

def toolbar_view(request):
    # Создание панели инструментов действий
    action_items = [
        {"text": "Новая запись", "icon": "plus", "onclick": "createPost()", "class": "button-primary"},
        {"text": "Редактировать", "icon": "edit", "onclick": "editPost()", "disabled": True},
        {"text": "Удалить", "icon": "delete", "onclick": "deletePost()", "class": "button-danger"}
    ]

    toolbar_html = render_toolbar(
        items=action_items,
        position="top",
        class="toolbar-actions",
        id="post-toolbar"
    )

    context = {
        'toolbar_html': toolbar_html,
        'action_items': action_items
    }
    return render(request, 'toolbar.html', context)
```

```html
<!-- toolbar.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ toolbar_html|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_toolbar items=action_items position="top" %} {% endblock %}
```

## Параметры

### `items` (необязательный)

Список элементов панели инструментов (кнопки, выпадающие списки и т.д.).

**Формат**:

```python
items = [
    {
        "text": "Текст кнопки",
        "icon": "имя-иконки",      # Необязательно
        "onclick": "функция()",    # Необязательно
        "class": "класс-кнопки",   # Необязательно
        "disabled": False,         # Необязательно
        "dropdown": []             # Необязательно для элементов выпадающего списка
    }
]
```

### `groups` (необязательный)

Список групп панели инструментов, каждая содержит элементы.

**Формат**:

```python
groups = [
    {
        "items": [...],            # Список элементов
        "separator": True          # Необязательный разделитель после группы
    }
]
```

### `position` (необязательный)

Позиция панели инструментов: top, bottom, left, right.

**По умолчанию**: `"top"`

**Пример**:

```python
toolbar_html = render_toolbar(items=items, position="bottom")
```

### `orientation` (необязательный)

Ориентация панели инструментов: horizontal или vertical.

**По умолчанию**: `"horizontal"`

**Пример**:

```python
toolbar_html = render_toolbar(items=items, orientation="vertical")
```

### `id` (необязательный)

Уникальный идентификатор для элемента панели инструментов.

**Пример**:

```python
toolbar_html = render_toolbar(items=items, id="main-toolbar")
```

### `class` (необязательный)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
toolbar_html = render_toolbar(items=items, class="toolbar-custom")
```

## Расширенные примеры

### Панель инструментов редактора

```python
def create_editor_toolbar():
    """Создание панели инструментов для текстового редактора."""

    editor_groups = [
        {
            "items": [
                {"text": "Жирный", "icon": "bold", "onclick": "toggleBold()"},
                {"text": "Курсив", "icon": "italic", "onclick": "toggleItalic()"},
                {"text": "Подчеркнутый", "icon": "underline", "onclick": "toggleUnderline()"}
            ]
        },
        {
            "items": [
                {"text": "По левому краю", "icon": "align-left", "onclick": "alignLeft()"},
                {"text": "По центру", "icon": "align-center", "onclick": "alignCenter()"},
                {"text": "По правому краю", "icon": "align-right", "onclick": "alignRight()"}
            ]
        },
        {
            "items": [
                {"text": "Вставить ссылку", "icon": "link", "onclick": "insertLink()"},
                {"text": "Вставить изображение", "icon": "image", "onclick": "insertImage()"}
            ]
        }
    ]

    return render_toolbar(
        groups=editor_groups,
        class="toolbar-editor",
        id="editor-toolbar"
    )
```

### Панель инструментов таблицы данных

```python
def create_table_toolbar(selected_count=0):
    """Создание панели инструментов для операций с таблицей данных."""

    table_items = [
        {"text": "Добавить новый", "icon": "plus", "onclick": "addRecord()", "class": "button-primary"},
        {"text": "Обновить", "icon": "refresh", "onclick": "refreshTable()"},
        {
            "text": "Экспорт",
            "icon": "download",
            "dropdown": [
                {"text": "Экспорт CSV", "onclick": "exportCSV()"},
                {"text": "Экспорт Excel", "onclick": "exportExcel()"},
                {"text": "Экспорт PDF", "onclick": "exportPDF()"}
            ]
        }
    ]

    if selected_count > 0:
        table_items.extend([
            {"text": f"Редактировать ({selected_count})", "icon": "edit", "onclick": "editSelected()"},
            {"text": f"Удалить ({selected_count})", "icon": "delete", "onclick": "deleteSelected()", "class": "button-danger"}
        ])

    return render_toolbar(
        items=table_items,
        class="toolbar-table",
        id="table-toolbar"
    )
```

### Панель инструментов медиа

```python
def create_media_toolbar():
    """Создание панели инструментов для медиаплеера."""

    media_items = [
        {"text": "Воспроизвести", "icon": "play", "onclick": "playMedia()", "id": "play-btn"},
        {"text": "Пауза", "icon": "pause", "onclick": "pauseMedia()", "id": "pause-btn", "style": "display:none"},
        {"text": "Стоп", "icon": "stop", "onclick": "stopMedia()"},
        {"text": "Предыдущий", "icon": "previous", "onclick": "previousTrack()"},
        {"text": "Следующий", "icon": "next", "onclick": "nextTrack()"},
        {"text": "Громкость", "icon": "volume", "onclick": "toggleMute()"}
    ]

    return render_toolbar(
        items=media_items,
        class="toolbar-media",
        orientation="horizontal"
    )
```

### Панель инструментов фильтров

```python
def create_filter_toolbar(filters):
    """Создание панели инструментов с элементами управления фильтрами."""

    filter_items = [
        {"text": "Все", "onclick": "filterAll()", "class": "filter-btn active"},
        {"text": "Активные", "onclick": "filterActive()", "class": "filter-btn"},
        {"text": "Неактивные", "onclick": "filterInactive()", "class": "filter-btn"},
        {"text": "Очистить фильтры", "icon": "clear", "onclick": "clearFilters()"}
    ]

    return render_toolbar(
        items=filter_items,
        class="toolbar-filters",
        position="top"
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `toolbar` - Базовый класс панели инструментов
- `toolbar-primary` - Основной стиль панели инструментов
- `toolbar-secondary` - Вторичный стиль панели инструментов

#### Классы позиционирования

- `toolbar-top` - Панель инструментов сверху
- `toolbar-bottom` - Панель инструментов снизу
- `toolbar-left` - Панель инструментов слева
- `toolbar-right` - Панель инструментов справа

#### Классы ориентации

- `toolbar-horizontal` - Горизонтальная компоновка панели инструментов
- `toolbar-vertical` - Вертикальная компоновка панели инструментов

#### Типы классов

- `toolbar-editor` - Панель инструментов в стиле редактора
- `toolbar-table` - Панель инструментов для операций с таблицами
- `toolbar-media` - Панель инструментов для управления медиа

### Пользовательская стилизация

```css
/* Пользовательская стилизация панели инструментов */
.toolbar-custom {
	background: #f8f9fa;
	border: 1px solid #dee2e6;
	border-radius: 6px;
	padding: 10px;
	display: flex;
	align-items: center;
	gap: 10px;
}

.toolbar-custom .toolbar-group {
	display: flex;
	align-items: center;
	gap: 5px;
	padding: 0 10px;
	border-right: 1px solid #dee2e6;
}

.toolbar-custom .toolbar-group:last-child {
	border-right: none;
}

.toolbar-custom .toolbar-button {
	background: white;
	border: 1px solid #ced4da;
	border-radius: 4px;
	padding: 8px 12px;
	color: #495057;
	cursor: pointer;
	transition: all 0.3s ease;
	display: flex;
	align-items: center;
	gap: 5px;
}

.toolbar-custom .toolbar-button:hover {
	background: #e9ecef;
	border-color: #007acc;
	color: #007acc;
}

.toolbar-custom .toolbar-button:active,
.toolbar-custom .toolbar-button.active {
	background: #007acc;
	border-color: #0056b3;
	color: white;
}

.toolbar-custom .toolbar-button:disabled {
	background: #f8f9fa;
	border-color: #e9ecef;
	color: #6c757d;
	cursor: not-allowed;
	opacity: 0.6;
}

/* Вертикальная панель инструментов */
.toolbar-custom.toolbar-vertical {
	flex-direction: column;
	align-items: stretch;
}

.toolbar-custom.toolbar-vertical .toolbar-group {
	border-right: none;
	border-bottom: 1px solid #dee2e6;
	padding: 10px 0;
}
```

## Интеграция с JavaScript

### События панели инструментов

```javascript
// Обработка кликов по кнопкам панели инструментов
$(".toolbar").on("click", ".toolbar-button", function (e) {
	const button = $(this);
	const onclick = button.data("onclick");

	if (onclick && typeof window[onclick] === "function") {
		window[onclick]();
	}

	// Переключение активного состояния для кнопок-переключателей
	if (button.hasClass("toggle-btn")) {
		button.toggleClass("active");
	}
});

// Обработка переключений выпадающих списков
$(".toolbar").on("click", ".dropdown-toggle", function (e) {
	e.preventDefault();
	const dropdown = $(this).closest(".toolbar-dropdown");
	dropdown.find(".dropdown-menu").toggle();
});
```

### Динамические обновления панели инструментов

```javascript
// Обновление состояния панели инструментов
function updateToolbarState(toolbarId, updates) {
	const toolbar = $(`#${toolbarId}`);

	Object.keys(updates).forEach((buttonId) => {
		const button = toolbar.find(`#${buttonId}`);
		const update = updates[buttonId];

		if (update.disabled !== undefined) {
			button.prop("disabled", update.disabled);
		}

		if (update.active !== undefined) {
			button.toggleClass("active", update.active);
		}

		if (update.text !== undefined) {
			button.find(".button-text").text(update.text);
		}

		if (update.visible !== undefined) {
			button.toggle(update.visible);
		}
	});
}

// Пример использования
updateToolbarState("editor-toolbar", {
	"bold-btn": { active: true },
	"save-btn": { disabled: false },
	"delete-btn": { visible: false },
});
```

### Адаптивная панель инструментов

```javascript
// Обработка адаптивного поведения панели инструментов
function handleResponsiveToolbar() {
	const toolbar = $(".toolbar");
	const windowWidth = $(window).width();

	if (windowWidth < 768) {
		// Мобильные устройства: преобразование в вертикальную или свернутую
		toolbar.addClass("toolbar-mobile");
		collapseToolbarGroups();
	} else {
		// Десктоп: показ полной панели инструментов
		toolbar.removeClass("toolbar-mobile");
		expandToolbarGroups();
	}
}

function collapseToolbarGroups() {
	$(".toolbar-group").each(function () {
		const group = $(this);
		const buttons = group.find(".toolbar-button");

		if (buttons.length > 3) {
			// Скрытие лишних кнопок и показ выпадающего списка "еще"
			buttons.slice(3).hide();
			group.append('<button class="toolbar-button more-btn">Еще...</button>');
		}
	});
}

function expandToolbarGroups() {
	$(".toolbar-button").show();
	$(".more-btn").remove();
}

// Обработка изменения размера окна
$(window).on("resize", handleResponsiveToolbar);
$(document).ready(handleResponsiveToolbar);
```

### Контекстное меню панели инструментов

```javascript
// Добавление контекстного меню к панели инструментов
$(".toolbar").on("contextmenu", ".toolbar-button", function (e) {
	e.preventDefault();

	const button = $(this);
	const contextMenu = createToolbarContextMenu(button);

	showContextMenu(contextMenu, e.pageX, e.pageY);
});

function createToolbarContextMenu(button) {
	const isVisible = button.is(":visible");
	const isDisabled = button.is(":disabled");

	return [
		{
			text: isVisible ? "Скрыть кнопку" : "Показать кнопку",
			onclick: () => button.toggle(),
		},
		{
			text: isDisabled ? "Включить кнопку" : "Отключить кнопку",
			onclick: () => button.prop("disabled", !isDisabled),
		},
		{
			text: "Сбросить панель инструментов",
			onclick: () => resetToolbar(button.closest(".toolbar")),
		},
	];
}
```

## Лучшие практики

### 1. Группировка кнопок

```python
# Группировка связанных действий вместе
def create_grouped_toolbar(action_groups):
	groups = []
	for group_name, actions in action_groups.items():
		groups.append({
			"items": actions,
			"separator": True
		})

	return render_toolbar(groups=groups)
```

### 2. Управление состоянием

```python
# Последовательное отслеживание состояния панели инструментов
def create_stateful_toolbar(items, state=None):
	if state:
		for item in items:
			item_id = item.get('id')
			if item_id in state:
				item.update(state[item_id])

	return render_toolbar(items=items)
```

### 3. Адаптивный дизайн

```python
# Создание адаптивной панели инструментов
def create_responsive_toolbar(items, mobile_limit=3):
	return render_toolbar(
		items=items,
		class="toolbar-responsive",
		**{"data-mobile-limit": mobile_limit}
	)
```

### 4. Доступность

```python
# Обеспечение доступности панели инструментов
def create_accessible_toolbar(items):
	for item in items:
		if not item.get('aria-label'):
			item['aria-label'] = item.get('text', 'Кнопка панели инструментов')

	return render_toolbar(
		items=items,
		**{
			"role": "toolbar",
			"aria-label": "Основная панель инструментов"
		}
	)
```

## Связанные компоненты

- [Кнопки](buttons.md) - Для элементов кнопок панели инструментов
- [Выпадающие списки](dropdowns.md) - Для выпадающих меню панели инструментов
- [Иконки](icons.md) - Для иконок кнопок панели инструментов
- [Навигация](navigation.md) - Для панелей инструментов навигации
