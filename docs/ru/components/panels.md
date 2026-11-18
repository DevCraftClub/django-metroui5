# Панели

MetroUI5 Django предоставляет гибкую систему компонентов панелей для создания сворачиваемых областей контента, боковых панелей и организованных разделов контента.

## Базовое использование

```python
from metroui5.components import render_panel

# Простая панель
panel_html = render_panel(
    title="Заголовок панели",
    content="Содержимое панели..."
)
```

## Параметры

### `render_panel(title=None, content=None, **attrs)`

- **title** (str, необязательный): Заголовок панели
- **content** (str): Содержимое панели (может быть HTML)
- **attrs** (dict): Дополнительные HTML атрибуты

## Примеры

### Базовая панель

```python
from metroui5.components import render_panel

panel = render_panel(
    title="Информация о пользователе",
    content="""
    <p><strong>Имя:</strong> Джон Доу</p>
    <p><strong>Email:</strong> john@example.com</p>
    <p><strong>Роль:</strong> Администратор</p>
    """
)
```

### Панель с пользовательскими классами

```python
panel = render_panel(
    title="Настройки",
    content="Содержимое панели...",
    class="panel panel-primary",
    id="settings-panel"
)
```

### Сворачиваемая панель

```python
panel = render_panel(
    title="Дополнительные опции",
    content="Содержимое дополнительных настроек...",
    class="panel panel-collapsible",
    data_role="panel"
)
```

## Классы панелей MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации панелей:

### Классы стилей

- `panel` - Базовый класс панели
- `panel-primary` - Основной стиль панели
- `panel-secondary` - Вторичный стиль панели
- `panel-success` - Стиль панели успеха
- `panel-warning` - Предупреждающий стиль панели
- `panel-danger` - Опасный стиль панели
- `panel-info` - Информационный стиль панели

### Классы размеров

- `panel-small` - Маленькая панель
- `panel-large` - Большая панель
- `panel-compact` - Компактная панель

### Классы макета

- `panel-collapsible` - Сворачиваемая панель
- `panel-expandable` - Расширяемая панель
- `panel-fixed` - Панель с фиксированной высотой
- `panel-scrollable` - Прокручиваемая панель

## Типы панелей

### Базовая информационная панель

```python
def create_info_panel(title, data):
    """Создание информационной панели со структурированными данными."""

    content = "<div class='info-list'>"
    for key, value in data.items():
        content += f"""
        <div class='info-item'>
            <span class='info-label'>{key}:</span>
            <span class='info-value'>{value}</span>
        </div>
        """
    content += "</div>"

    return render_panel(
        title=title,
        content=content,
        class="panel panel-info"
    )

# Использование
user_data = {
    "Имя": "Джон Доу",
    "Email": "john@example.com",
    "Телефон": "+1-555-0123",
    "Отдел": "Инженерия"
}

info_panel = create_info_panel("Детали пользователя", user_data)
```

### Сворачиваемая панель настроек

```python
def create_settings_panel():
    """Создание сворачиваемой панели настроек."""

    content = """
    <form class="settings-form">
        <div class="form-group">
            <label>Тема:</label>
            <select class="select">
                <option>Светлая</option>
                <option>Темная</option>
                <option>Авто</option>
            </select>
        </div>
        <div class="form-group">
            <label>Язык:</label>
            <select class="select">
                <option>Английский</option>
                <option>Испанский</option>
                <option>Французский</option>
            </select>
        </div>
        <div class="form-group">
            <label class="checkbox">
                <input type="checkbox" data-role="checkbox">
                <span class="check"></span>
                Включить уведомления
            </label>
        </div>
        <button class="button button-primary">Сохранить настройки</button>
    </form>
    """

    return render_panel(
        title="Настройки",
        content=content,
        class="panel panel-collapsible",
        data_role="panel"
    )

settings_panel = create_settings_panel()
```

### Панель статистики

```python
def create_stats_panel(title, stats):
    """Создание панели статистики с метриками."""

    content = "<div class='stats-grid'>"
    for stat in stats:
        content += f"""
        <div class='stat-item'>
            <div class='stat-value'>{stat['value']}</div>
            <div class='stat-label'>{stat['label']}</div>
            <div class='stat-change {stat.get('change_type', 'neutral')}'>
                {stat.get('change', '')}
            </div>
        </div>
        """
    content += "</div>"

    return render_panel(
        title=title,
        content=content,
        class="panel panel-primary"
    )

# Использование
dashboard_stats = [
    {"value": "1,234", "label": "Всего пользователей", "change": "+12%", "change_type": "positive"},
    {"value": "567", "label": "Активные сессии", "change": "+5%", "change_type": "positive"},
    {"value": "89", "label": "Ошибки", "change": "-3%", "change_type": "negative"},
    {"value": "98.5%", "label": "Время работы", "change": "+0.2%", "change_type": "positive"}
]

stats_panel = create_stats_panel("Обзор панели управления", dashboard_stats)
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_panel title="Заголовок панели"
content="Содержимое панели..." class="panel panel-primary" %}
```

## Расширенные примеры

### Панель с действиями

```python
def create_action_panel(title, content, actions=None):
    """Создание панели с кнопками действий."""

    if actions is None:
        actions = []

    action_buttons = ""
    for action in actions:
        action_buttons += f"""
        <button class="button button-{action.get('type', 'default')}"
                onclick="{action.get('onclick', '')}">
            {action.get('text', 'Действие')}
        </button>
        """

    panel_content = f"""
    <div class="panel-content">
        {content}
    </div>
    <div class="panel-actions">
        {action_buttons}
    </div>
    """

    return render_panel(
        title=title,
        content=panel_content,
        class="panel panel-with-actions"
    )

# Использование
actions = [
    {"text": "Редактировать", "type": "primary", "onclick": "editItem()"},
    {"text": "Удалить", "type": "danger", "onclick": "deleteItem()"},
    {"text": "Просмотр", "type": "secondary", "onclick": "viewItem()"}
]

action_panel = create_action_panel(
    "Профиль пользователя",
    "Содержимое профиля пользователя...",
    actions
)
```

### Панель с вкладками

```python
def create_tabbed_panel(title, tabs):
    """Создание панели с содержимым вкладок."""

    tab_nav = "<ul class='tabs-nav'>"
    tab_content = "<div class='tabs-content'>"

    for i, tab in enumerate(tabs):
        tab_id = f"tab-{i}"
        tab_nav += f"<li><a href='#{tab_id}'>{tab['title']}</a></li>"
        tab_content += f"<div id='{tab_id}'>{tab['content']}</div>"

    tab_nav += "</ul>"
    tab_content += "</div>"

    content = f"""
    <div class="tabs" data-role="tabs">
        {tab_nav}
        {tab_content}
    </div>
    """

    return render_panel(
        title=title,
        content=content,
        class="panel panel-tabbed"
    )

# Использование
tabs = [
    {
        "title": "Общие",
        "content": "Содержимое общих настроек..."
    },
    {
        "title": "Безопасность",
        "content": "Содержимое настроек безопасности..."
    },
    {
        "title": "Уведомления",
        "content": "Содержимое настроек уведомлений..."
    }
]

tabbed_panel = create_tabbed_panel("Настройки пользователя", tabs)
```

### Панель с индикаторами прогресса

```python
def create_progress_panel(title, tasks):
    """Создание панели, показывающей прогресс задач."""

    content = "<div class='task-list'>"
    for task in tasks:
        progress = task.get('progress', 0)
        status_class = "success" if progress == 100 else "warning" if progress > 0 else "default"

        content += f"""
        <div class='task-item'>
            <div class='task-header'>
                <span class='task-name'>{task['name']}</span>
                <span class='task-status badge badge-{status_class}'>{progress}%</span>
            </div>
            <div class='progress-bar'>
                <div class='progress-fill' style='width: {progress}%'></div>
            </div>
        </div>
        """
    content += "</div>"

    return render_panel(
        title=title,
        content=content,
        class="panel panel-progress"
    )

# Использование
tasks = [
    {"name": "Миграция базы данных", "progress": 100},
    {"name": "Загрузка файлов", "progress": 75},
    {"name": "Настройка email", "progress": 25},
    {"name": "Сканирование безопасности", "progress": 0}
]

progress_panel = create_progress_panel("Системные задачи", tasks)
```

### Панель с таблицей данных

```python
def create_table_panel(title, headers, rows):
    """Создание панели с таблицей данных."""

    from metroui5.components import render_table

    table = render_table(headers, rows, class="table table-border table-striped")

    return render_panel(
        title=title,
        content=table,
        class="panel panel-table"
    )

# Использование
headers = ["Имя", "Email", "Роль", "Статус"]
rows = [
    ["Джон Доу", "john@example.com", "Админ", "Активный"],
    ["Джейн Смит", "jane@example.com", "Пользователь", "Активный"],
    ["Боб Джонсон", "bob@example.com", "Редактор", "Неактивный"]
]

table_panel = create_table_panel("Пользователи", headers, rows)
```

### Адаптивная сетка панелей

```python
def create_panel_grid(panels, columns=3):
    """Создание адаптивной сетки панелей."""

    grid_class = f"grid grid-columns-{columns}"
    grid_content = f"<div class='{grid_class}'>"

    for panel in panels:
        grid_content += f"<div class='cell'>{panel}</div>"

    grid_content += "</div>"

    return grid_content

# Использование
panels = [
    create_info_panel("Панель 1", {"Ключ": "Значение"}),
    create_info_panel("Панель 2", {"Ключ": "Значение"}),
    create_info_panel("Панель 3", {"Ключ": "Значение"}),
    create_info_panel("Панель 4", {"Ключ": "Значение"})
]

panel_grid = create_panel_grid(panels, columns=2)
```

## Интеграция с JavaScript

### Сворачивание/разворачивание панели

```javascript
// Переключение сворачивания панели
function togglePanel(panelId) {
	const panel = document.querySelector(`#${panelId}`);
	if (panel) {
		panel.classList.toggle("panel-collapsed");

		const content = panel.querySelector(".panel-content");
		if (content) {
			content.style.display =
				content.style.display === "none" ? "block" : "none";
		}
	}
}

// Автоматическое сворачивание панелей
document.querySelectorAll(".panel-collapsible").forEach((panel) => {
	const header = panel.querySelector(".panel-header");
	if (header) {
		header.addEventListener("click", function () {
			togglePanel(panel.id);
		});
	}
});
```

### Состояния загрузки панели

```javascript
// Показать состояние загрузки в панели
function showPanelLoading(panelId) {
	const panel = document.querySelector(`#${panelId}`);
	if (panel) {
		const content = panel.querySelector(".panel-content");
		if (content) {
			content.innerHTML = '<div class="loading-spinner">Загрузка...</div>';
		}
	}
}

// Обновить содержимое панели
function updatePanelContent(panelId, newContent) {
	const panel = document.querySelector(`#${panelId}`);
	if (panel) {
		const content = panel.querySelector(".panel-content");
		if (content) {
			content.innerHTML = newContent;
		}
	}
}
```

### События панели

```javascript
// Обработка событий панели
document.querySelectorAll(".panel").forEach((panel) => {
	panel.addEventListener("panel-open", function () {
		console.log("Панель открыта:", this.id);
	});

	panel.addEventListener("panel-close", function () {
		console.log("Панель закрыта:", this.id);
	});

	panel.addEventListener("panel-toggle", function () {
		console.log("Панель переключена:", this.id);
	});
});
```

## Лучшие практики

1. **Используйте описательные заголовки**: Делайте заголовки панелей ясными и описательными
2. **Организуйте контент логически**: Группируйте связанную информацию вместе
3. **Используйте соответствующие размеры**: Выбирайте размеры панелей, которые подходят вашему контенту
4. **Предоставляйте четкие действия**: Делайте кнопки действий очевидными и доступными
5. **Обрабатывайте состояния загрузки**: Показывайте индикаторы загрузки для динамического контента
6. **Делайте адаптивным**: Убедитесь, что панели хорошо работают на всех размерах экрана
7. **Используйте последовательную стилизацию**: Применяйте последовательные классы во всем приложении

## Связанные компоненты

- [Карточки](cards.md) - Для макетов на основе карточек
- [Вкладки](tabs.md) - Для содержимого вкладок в панелях
- [Таблицы](tables.md) - Для отображения данных в панелях
- [Полосы прогресса](progress.md) - Для индикаторов прогресса в панелях


## metroui5_panel

```python
render_panel()
```

Пустое или неверное значение: `render_panel()` даёт `<div class="panel" data-role="panel"><div class="panel-content"></div></div>`.

```django
{% metroui5_panel %}
```
