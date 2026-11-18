# Списки

MetroUI5 Django предоставляет комплексную систему компонентов списков для отображения структурированных данных, элементов навигации и организованного контента в различных форматах списков.

## Базовое использование

```python
from metroui5.components import render_list

# Простой список
items = ["Элемент 1", "Элемент 2", "Элемент 3"]
list_html = render_list(items)
```

## Параметры

### `render_list(items, list_type="ul", **attrs)`

- **items** (list): Список элементов для отображения
- **list_type** (str): Тип списка ("ul" для неупорядоченного, "ol" для упорядоченного)
- **attrs** (dict): Дополнительные HTML атрибуты

## Примеры

### Базовый список

```python
from metroui5.components import render_list

# Неупорядоченный список
items = ["Яблоко", "Банан", "Апельсин", "Виноград"]
list_html = render_list(items)

# Упорядоченный список
ordered_list = render_list(items, list_type="ol")
```

### Список с пользовательскими классами

```python
list_html = render_list(
    items=["Главная", "О нас", "Контакты", "Услуги"],
    list_type="ul",
    class="list list-horizontal",
    id="main-navigation"
)
```

### Список со сложными элементами

```python
complex_items = [
    {"text": "Панель управления", "icon": "dashboard", "url": "/dashboard/"},
    {"text": "Пользователи", "icon": "users", "url": "/users/"},
    {"text": "Настройки", "icon": "cog", "url": "/settings/"},
    {"text": "Отчеты", "icon": "chart", "url": "/reports/"}
]

list_html = render_list(complex_items, class="list list-navigation")
```

## Классы списков MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации списков:

### Классы стилей

- `list` - Базовый класс списка
- `list-primary` - Основной стиль списка
- `list-secondary` - Вторичный стиль списка
- `list-success` - Стиль списка успеха
- `list-warning` - Предупреждающий стиль списка
- `list-danger` - Опасный стиль списка
- `list-info` - Информационный стиль списка

### Классы макета

- `list-horizontal` - Горизонтальный список
- `list-vertical` - Вертикальный список (по умолчанию)
- `list-inline` - Встроенный список
- `list-grid` - Список на основе сетки

### Классы размеров

- `list-small` - Маленький список
- `list-large` - Большой список
- `list-compact` - Компактный список

### Интерактивные классы

- `list-hover` - Эффекты при наведении
- `list-selectable` - Выбираемые элементы
- `list-sortable` - Сортируемые элементы
- `list-draggable` - Перетаскиваемые элементы

## Типы списков

### Навигационный список

```python
def create_navigation_list(menu_items):
    """Создание навигационного списка с иконками и ссылками."""

    items = []
    for item in menu_items:
        item_html = f"""
        <a href="{item['url']}" class="list-item">
            <span class="mif-{item['icon']}"></span>
            <span class="list-item-text">{item['text']}</span>
        </a>
        """
        items.append(item_html)

    return render_list(items, class="list list-navigation")

# Использование
menu_items = [
    {"text": "Панель управления", "icon": "dashboard", "url": "/dashboard/"},
    {"text": "Пользователи", "icon": "users", "url": "/users/"},
    {"text": "Продукты", "icon": "box", "url": "/products/"},
    {"text": "Заказы", "icon": "cart", "url": "/orders/"},
    {"text": "Настройки", "icon": "cog", "url": "/settings/"}
]

nav_list = create_navigation_list(menu_items)
```

### Список пользователей

```python
def create_user_list(users):
    """Создание списка пользователей с аватарами и информацией."""

    items = []
    for user in users:
        status_class = "success" if user['active'] else "default"
        item_html = f"""
        <div class="list-item user-item">
            <div class="user-avatar">
                <img src="{user.get('avatar', '/static/default-avatar.png')}" alt="Avatar">
            </div>
            <div class="user-info">
                <div class="user-name">{user['name']}</div>
                <div class="user-email">{user['email']}</div>
            </div>
            <div class="user-status">
                <span class="badge badge-{status_class}">
                    {'Активный' if user['active'] else 'Неактивный'}
                </span>
            </div>
        </div>
        """
        items.append(item_html)

    return render_list(items, class="list list-users")

# Использование
users = [
    {"name": "Джон Доу", "email": "john@example.com", "active": True, "avatar": "/static/avatars/john.jpg"},
    {"name": "Джейн Смит", "email": "jane@example.com", "active": True, "avatar": "/static/avatars/jane.jpg"},
    {"name": "Боб Джонсон", "email": "bob@example.com", "active": False, "avatar": "/static/avatars/bob.jpg"}
]

user_list = create_user_list(users)
```

### Список задач

```python
def create_task_list(tasks):
    """Создание списка задач с флажками и приоритетами."""

    items = []
    for task in tasks:
        priority_class = task.get('priority', 'normal')
        completed_class = "completed" if task.get('completed', False) else ""

        item_html = f"""
        <div class="list-item task-item {completed_class}">
            <div class="task-checkbox">
                <label class="checkbox">
                    <input type="checkbox" {'checked' if task.get('completed', False) else ''} data-role="checkbox">
                    <span class="check"></span>
                </label>
            </div>
            <div class="task-content">
                <div class="task-title">{task['title']}</div>
                <div class="task-description">{task.get('description', '')}</div>
            </div>
            <div class="task-meta">
                <span class="task-priority badge badge-{priority_class}">{priority_class.title()}</span>
                <span class="task-date">{task.get('due_date', '')}</span>
            </div>
        </div>
        """
        items.append(item_html)

    return render_list(items, class="list list-tasks")

# Использование
tasks = [
    {
        "title": "Завершить предложение проекта",
        "description": "Написать и отправить документ предложения проекта",
        "priority": "high",
        "completed": False,
        "due_date": "2024-01-20"
    },
    {
        "title": "Просмотреть изменения кода",
        "description": "Просмотреть и одобрить ожидающие изменения кода",
        "priority": "medium",
        "completed": True,
        "due_date": "2024-01-18"
    },
    {
        "title": "Обновить документацию",
        "description": "Обновить API документацию с новыми конечными точками",
        "priority": "low",
        "completed": False,
        "due_date": "2024-01-25"
    }
]

task_list = create_task_list(tasks)
```

### Список файлов

```python
def create_file_list(files):
    """Создание списка файлов с иконками и метаданными."""

    items = []
    for file in files:
        file_type = file.get('type', 'file')
        size_mb = file.get('size', 0) / (1024 * 1024)

        item_html = f"""
        <div class="list-item file-item">
            <div class="file-icon">
                <span class="mif-{file_type}"></span>
            </div>
            <div class="file-info">
                <div class="file-name">{file['name']}</div>
                <div class="file-meta">
                    {size_mb:.1f} МБ • Изменен {file.get('modified', 'Неизвестно')}
                </div>
            </div>
            <div class="file-actions">
                <button class="button button-mini" onclick="downloadFile('{file['id']}')">
                    <span class="mif-download"></span>
                </button>
                <button class="button button-mini" onclick="deleteFile('{file['id']}')">
                    <span class="mif-delete"></span>
                </button>
            </div>
        </div>
        """
        items.append(item_html)

    return render_list(items, class="list list-files")

# Использование
files = [
    {"id": 1, "name": "project-proposal.pdf", "type": "file-pdf", "size": 2048000, "modified": "2 дня назад"},
    {"id": 2, "name": "presentation.pptx", "type": "file-powerpoint", "size": 5120000, "modified": "1 неделю назад"},
    {"id": 3, "name": "data-analysis.xlsx", "type": "file-excel", "size": 1024000, "modified": "3 дня назад"},
    {"id": 4, "name": "team-photo.jpg", "type": "image", "size": 3072000, "modified": "1 день назад"}
]

file_list = create_file_list(files)
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_list items=list_items class="list list-primary"
%}
```

## Расширенные примеры

### Сортируемый список

```python
def create_sortable_list(items, sortable=True):
    """Создание сортируемого списка с функцией перетаскивания и отпускания."""

    list_class = "list list-sortable" if sortable else "list"

    items_html = []
    for item in items:
        item_html = f"""
        <div class="list-item sortable-item" data-id="{item['id']}">
            <div class="sort-handle">
                <span class="mif-menu"></span>
            </div>
            <div class="item-content">
                {item['content']}
            </div>
        </div>
        """
        items_html.append(item_html)

    return render_list(items_html, class=list_class)

# Использование
sortable_items = [
    {"id": 1, "content": "Первый элемент"},
    {"id": 2, "content": "Второй элемент"},
    {"id": 3, "content": "Третий элемент"},
    {"id": 4, "content": "Четвертый элемент"}
]

sortable_list = create_sortable_list(sortable_items)
```

### Фильтруемый список

```python
def create_filterable_list(items, filter_options=None):
    """Создание списка с возможностями фильтрации."""

    if filter_options is None:
        filter_options = ["Все", "Активные", "Неактивные", "Ожидающие"]

    filter_html = """
    <div class="list-filters">
        <div class="filter-group">
            <label>Фильтр по статусу:</label>
            <select class="select" data-role="select" onchange="filterList(this.value)">
    """

    for option in filter_options:
        filter_html += f'<option value="{option.lower()}">{option}</option>'

    filter_html += """
            </select>
        </div>
        <div class="search-group">
            <input type="text" class="input" placeholder="Поиск элементов..." onkeyup="searchList(this.value)">
        </div>
    </div>
    """

    items_html = []
    for item in items:
        item_html = f"""
        <div class="list-item filterable-item" data-status="{item.get('status', 'all')}" data-search="{item['name'].lower()}">
            <div class="item-content">
                <div class="item-name">{item['name']}</div>
                <div class="item-description">{item.get('description', '')}</div>
            </div>
            <div class="item-status">
                <span class="badge badge-{item.get('status', 'default')}">{item.get('status', 'Неизвестно').title()}</span>
            </div>
        </div>
        """
        items_html.append(item_html)

    list_html = render_list(items_html, class="list list-filterable")

    return filter_html + list_html

# Использование
filterable_items = [
    {"name": "Проект Альфа", "description": "Основной проект", "status": "active"},
    {"name": "Проект Бета", "description": "Вторичный проект", "status": "pending"},
    {"name": "Проект Гамма", "description": "Исследовательский проект", "status": "inactive"},
    {"name": "Проект Дельта", "description": "Новый проект", "status": "active"}
]

filterable_list = create_filterable_list(filterable_items)
```

### Список с пагинацией

```python
def create_paginated_list(items, page_size=10, current_page=1):
    """Создание списка с пагинацией."""

    start_index = (current_page - 1) * page_size
    end_index = start_index + page_size
    page_items = items[start_index:end_index]

    # Создание элементов списка
    items_html = []
    for item in page_items:
        item_html = f"""
        <div class="list-item">
            <div class="item-content">
                <div class="item-title">{item['title']}</div>
                <div class="item-description">{item.get('description', '')}</div>
            </div>
        </div>
        """
        items_html.append(item_html)

    list_html = render_list(items_html, class="list list-paginated")

    # Создание пагинации
    total_pages = (len(items) + page_size - 1) // page_size
    pagination_html = f"""
    <div class="pagination">
        <button class="button" {'disabled' if current_page == 1 else ''} onclick="goToPage({current_page - 1})">
            Предыдущая
        </button>
        <span class="page-info">Страница {current_page} из {total_pages}</span>
        <button class="button" {'disabled' if current_page == total_pages else ''} onclick="goToPage({current_page + 1})">
            Следующая
        </button>
    </div>
    """

    return list_html + pagination_html

# Использование
paginated_items = [
    {"title": f"Элемент {i}", "description": f"Описание для элемента {i}"}
    for i in range(1, 51)  # 50 элементов
]

paginated_list = create_paginated_list(paginated_items, page_size=10, current_page=1)
```

### Список с действиями

```python
def create_action_list(items, actions=None):
    """Создание списка с кнопками действий для каждого элемента."""

    if actions is None:
        actions = [
            {"text": "Редактировать", "class": "button-primary", "onclick": "editItem"},
            {"text": "Удалить", "class": "button-danger", "onclick": "deleteItem"}
        ]

    items_html = []
    for item in items:
        action_buttons = ""
        for action in actions:
            action_buttons += f"""
            <button class="button button-mini {action['class']}"
                    onclick="{action['onclick']}({item['id']})">
                {action['text']}
            </button>
            """

        item_html = f"""
        <div class="list-item action-item">
            <div class="item-content">
                <div class="item-title">{item['title']}</div>
                <div class="item-description">{item.get('description', '')}</div>
            </div>
            <div class="item-actions">
                {action_buttons}
            </div>
        </div>
        """
        items_html.append(item_html)

    return render_list(items_html, class="list list-actions")

# Использование
action_items = [
    {"id": 1, "title": "Профиль пользователя", "description": "Управление настройками профиля пользователя"},
    {"id": 2, "title": "Настройки аккаунта", "description": "Настройка предпочтений аккаунта"},
    {"id": 3, "title": "Настройки конфиденциальности", "description": "Контроль конфиденциальности и безопасности"}
]

action_list = create_action_list(action_items)
```

## Интеграция с JavaScript

### Фильтрация списка

```javascript
// Фильтрация элементов списка
function filterList(filterValue) {
	const items = document.querySelectorAll(".filterable-item");

	items.forEach((item) => {
		const status = item.getAttribute("data-status");
		if (filterValue === "all" || status === filterValue) {
			item.style.display = "block";
		} else {
			item.style.display = "none";
		}
	});
}

// Поиск элементов списка
function searchList(searchTerm) {
	const items = document.querySelectorAll(".filterable-item");

	items.forEach((item) => {
		const searchText = item.getAttribute("data-search");
		if (searchText.includes(searchTerm.toLowerCase())) {
			item.style.display = "block";
		} else {
			item.style.display = "none";
		}
	});
}
```

### Сортировка списка

```javascript
// Сортировка элементов списка
function sortList(sortBy, direction = "asc") {
	const list = document.querySelector(".list-sortable");
	const items = Array.from(list.querySelectorAll(".sortable-item"));

	items.sort((a, b) => {
		const aValue = a.querySelector(`[data-sort="${sortBy}"]`).textContent;
		const bValue = b.querySelector(`[data-sort="${sortBy}"]`).textContent;

		if (direction === "asc") {
			return aValue.localeCompare(bValue);
		} else {
			return bValue.localeCompare(aValue);
		}
	});

	// Повторное добавление отсортированных элементов
	items.forEach((item) => list.appendChild(item));
}
```

### Выбор элементов списка

```javascript
// Обработка выбора элементов списка
document.querySelectorAll(".list-selectable .list-item").forEach((item) => {
	item.addEventListener("click", function () {
		// Переключение выбора
		this.classList.toggle("selected");

		// Обновление счетчика выбора
		const selectedItems = document.querySelectorAll(".list-item.selected");
		updateSelectionCount(selectedItems.length);
	});
});

function updateSelectionCount(count) {
	const counter = document.querySelector(".selection-counter");
	if (counter) {
		counter.textContent = `${count} элемент(ов) выбрано`;
	}
}
```

### Перетаскивание и отпускание

```javascript
// Инициализация перетаскивания и отпускания для сортируемых списков
function initializeSortableList() {
	const sortableList = document.querySelector(".list-sortable");

	if (sortableList) {
		sortableList.addEventListener("dragstart", function (e) {
			e.target.classList.add("dragging");
		});

		sortableList.addEventListener("dragend", function (e) {
			e.target.classList.remove("dragging");
		});

		sortableList.addEventListener("dragover", function (e) {
			e.preventDefault();
			const dragging = document.querySelector(".dragging");
			const afterElement = getDragAfterElement(sortableList, e.clientY);

			if (afterElement == null) {
				sortableList.appendChild(dragging);
			} else {
				sortableList.insertBefore(dragging, afterElement);
			}
		});
	}
}

function getDragAfterElement(container, y) {
	const draggableElements = [
		...container.querySelectorAll(".sortable-item:not(.dragging)"),
	];

	return draggableElements.reduce(
		(closest, child) => {
			const box = child.getBoundingClientRect();
			const offset = y - box.top - box.height / 2;

			if (offset < 0 && offset > closest.offset) {
				return { offset: offset, element: child };
			} else {
				return closest;
			}
		},
		{ offset: Number.NEGATIVE_INFINITY }
	).element;
}
```

## Лучшие практики

1. **Используйте соответствующие типы списков**: Выбирайте ul/ol на основе структуры контента
2. **Сохраняйте элементы последовательными**: Используйте последовательную стилизацию и макет для элементов списка
3. **Предоставляйте четкие действия**: Делайте кнопки действий очевидными и доступными
4. **Обрабатывайте пустые состояния**: Показывайте соответствующие сообщения, когда списки пусты
5. **Оптимизируйте для производительности**: Используйте пагинацию или виртуализацию для больших списков
6. **Делайте доступным**: Обеспечивайте навигацию с клавиатуры и поддержку экранных читателей
7. **Используйте последовательные интервалы**: Применяйте последовательные отступы и поля

## Связанные компоненты

- [Навигация](navigation.md) - Для навигационных списков
- [Таблицы](tables.md) - Для отображения табличных данных
- [Карточки](cards.md) - Для организации контента на основе карточек
- [Пагинация](pagination.md) - Для контента списка с пагинацией


## metroui5_list

```python
render_list([{'text': 'One', 'href': '/one'}])
```

Пустое или неверное значение: `render_list([{'text': 'One', 'href': '/one'}])` даёт `<ul class="list" data-role="list"><li><a href="/one">One</a></li></ul>`. Пустой вызов даёт `<ul class="list" data-role="list"></ul>`.

```django
{% metroui5_list items %}
```
