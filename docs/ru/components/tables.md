# Таблицы

MetroUI5 Django предоставляет комплексную систему компонентов таблиц для отображения табличных данных с различными вариантами стилизации и интерактивными функциями.

## Базовое использование

```python
from metroui5.components import render_table

# Простая таблица
headers = ["Имя", "Email", "Роль"]
rows = [
    ["Джон Доу", "john@example.com", "Админ"],
    ["Джейн Смит", "jane@example.com", "Пользователь"],
    ["Боб Джонсон", "bob@example.com", "Редактор"]
]

table_html = render_table(headers, rows)
```

## Параметры

### `render_table(headers, rows, **attrs)`

- **headers** (list): Список заголовков столбцов
- **rows** (list): Список строк, где каждая строка представляет собой список значений ячеек
- **attrs** (dict): Дополнительные HTML атрибуты для таблицы

## Примеры

### Базовая таблица

```python
from metroui5.components import render_table

headers = ["ID", "Имя", "Статус", "Действия"]
rows = [
    ["1", "Проект Альфа", "Активный", "Редактировать | Удалить"],
    ["2", "Проект Бета", "Ожидающий", "Редактировать | Удалить"],
    ["3", "Проект Гамма", "Завершен", "Редактировать | Удалить"]
]

table = render_table(headers, rows)
```

### Таблица с пользовательскими классами

```python
table = render_table(
    headers=["Имя", "Email", "Роль"],
    rows=[
        ["Джон Доу", "john@example.com", "Админ"],
        ["Джейн Смит", "jane@example.com", "Пользователь"]
    ],
    class="table table-border table-striped table-hover"
)
```

### Таблица с дополнительными атрибутами

```python
table = render_table(
    headers=["Продукт", "Цена", "Запас"],
    rows=[
        ["Ноутбук", "$999", "15"],
        ["Мышь", "$25", "50"],
        ["Клавиатура", "$75", "30"]
    ],
    id="products-table",
    data_role="table",
    data_sort="true"
)
```

## Классы таблиц MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации таблиц:

### Базовые классы

- `table` - Базовый класс таблицы
- `table-border` - Добавляет границы к ячейкам таблицы
- `table-striped` - Чередующиеся цвета строк
- `table-hover` - Эффекты при наведении на строки
- `table-compact` - Компактная таблица с уменьшенными отступами

### Классы размеров

- `table-small` - Маленькая таблица
- `table-large` - Большая таблица

### Классы цветов

- `table-dark` - Таблица с темной темой
- `table-light` - Таблица со светлой темой

## Интерактивные функции

### Сортируемые таблицы

```python
table = render_table(
    headers=["Имя", "Возраст", "Город"],
    rows=[
        ["Алиса", "25", "Нью-Йорк"],
        ["Боб", "30", "Лос-Анджелес"],
        ["Чарли", "28", "Чикаго"]
    ],
    data_role="table",
    data_sort="true"
)
```

### Адаптивные таблицы

```python
table = render_table(
    headers=["Имя", "Email", "Телефон", "Адрес"],
    rows=[
        ["Джон Доу", "john@example.com", "+1-555-0123", "123 Main St"],
        ["Джейн Смит", "jane@example.com", "+1-555-0124", "456 Oak Ave"]
    ],
    class="table table-border table-responsive"
)
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_table headers=headers rows=rows class="table
table-border" %}
```

## Расширенные примеры

### Таблица с действиями

```python
def create_action_buttons(row_id):
    return f"""
    <button class="button button-small button-primary" onclick="editRow({row_id})">
        Редактировать
    </button>
    <button class="button button-small button-danger" onclick="deleteRow({row_id})">
        Удалить
    </button>
    """

headers = ["ID", "Имя", "Email", "Действия"]
rows = [
    ["1", "Джон Доу", "john@example.com", create_action_buttons(1)],
    ["2", "Джейн Смит", "jane@example.com", create_action_buttons(2)]
]

table = render_table(headers, rows, class="table table-border")
```

### Таблица с индикаторами статуса

```python
def get_status_badge(status):
    color_map = {
        "active": "success",
        "pending": "warning",
        "inactive": "danger"
    }
    color = color_map.get(status.lower(), "default")
    return f'<span class="badge badge-{color}">{status}</span>'

headers = ["Имя", "Статус", "Последний вход"]
rows = [
    ["Джон Доу", get_status_badge("Активный"), "2024-01-15"],
    ["Джейн Смит", get_status_badge("Ожидающий"), "2024-01-14"],
    ["Боб Джонсон", get_status_badge("Неактивный"), "2024-01-10"]
]

table = render_table(headers, rows, class="table table-border")
```

## Лучшие практики

1. **Используйте соответствующие заголовки**: Убедитесь, что заголовки столбцов описательные и ясные
2. **Сохраняйте таблицы адаптивными**: Используйте класс `table-responsive` для таблиц с множеством столбцов
3. **Добавляйте сортировку при необходимости**: Включайте сортировку для таблиц с сортируемыми данными
4. **Используйте последовательную стилизацию**: Применяйте последовательные классы во всем приложении
5. **Учитывайте доступность**: Обеспечивайте правильные ARIA метки и семантическую разметку

## Связанные компоненты

- [Карточки](cards.md) - Для макетов на основе карточек
- [Списки](lists.md) - Для отображения данных на основе списков
- [Пагинация](pagination.md) - Для табличных данных с пагинацией


## metroui5_table

```python
render_table(['Name'], [['One']])
```

Пустое или неверное значение: `render_table(['Name'], [['One']])` даёт `<table class="table" data-role="table"><tr><th>Name</th></tr><tr><td>One</td></tr></table>`. Пустой вызов даёт `<table class="table" data-role="table"><tr></tr></table>`.

```django
{% metroui5_table headers rows %}
```
