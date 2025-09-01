# Навигация

MetroUI5 Django предоставляет гибкую систему компонентов навигации для создания различных типов навигационных меню и структур навигации.

## Базовое использование

```python
from metroui5.components import render_navigation

# Простое навигационное меню
items = [
    {"text": "Главная", "url": "/", "icon": "home"},
    {"text": "О нас", "url": "/about/", "icon": "info"},
    {"text": "Контакты", "url": "/contact/", "icon": "mail"}
]

nav_html = render_navigation(items)
```

## Параметры

### `render_navigation(items, **attrs)`

- **items** (list): Список элементов навигации, каждый содержащий:
  - `text` (str): Отображаемый текст для элемента навигации
  - `url` (str): URL для элемента навигации
  - `icon` (str, необязательный): Имя иконки MetroUI
  - `active` (bool, необязательный): Является ли этот элемент в данный момент активным
  - `disabled` (bool, необязательный): Отключен ли этот элемент
- **attrs** (dict): Дополнительные HTML атрибуты для контейнера навигации

## Примеры

### Базовая навигация

```python
from metroui5.components import render_navigation

items = [
    {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard"},
    {"text": "Пользователи", "url": "/users/", "icon": "users"},
    {"text": "Настройки", "url": "/settings/", "icon": "cog"},
    {"text": "Отчеты", "url": "/reports/", "icon": "chart"}
]

nav = render_navigation(items)
```

### Навигация с активным состоянием

```python
items = [
    {"text": "Главная", "url": "/", "icon": "home"},
    {"text": "Продукты", "url": "/products/", "icon": "box", "active": True},
    {"text": "О нас", "url": "/about/", "icon": "info"},
    {"text": "Контакты", "url": "/contact/", "icon": "mail"}
]

nav = render_navigation(items, class="nav nav-horizontal")
```

### Навигация с пользовательскими классами

```python
nav = render_navigation(
    items=[
        {"text": "Главная", "url": "/", "icon": "home"},
        {"text": "О нас", "url": "/about/", "icon": "info"},
        {"text": "Контакты", "url": "/contact/", "icon": "mail"}
    ],
    class="nav nav-horizontal nav-dark",
    id="main-navigation"
)
```

## Классы навигации MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации навигации:

### Классы макета

- `nav` - Базовый класс навигации
- `nav-horizontal` - Горизонтальная навигация
- `nav-vertical` - Вертикальная навигация
- `nav-expand` - Расширяемая навигация

### Классы стилей

- `nav-dark` - Навигация с темной темой
- `nav-light` - Навигация со светлой темой
- `nav-compact` - Компактная навигация
- `nav-large` - Большая навигация

### Классы позиционирования

- `nav-top` - Верхняя навигация
- `nav-bottom` - Нижняя навигация
- `nav-left` - Левая навигация
- `nav-right` - Правая навигация

## Типы навигации

### Горизонтальная навигация

```python
nav = render_navigation(
    items=[
        {"text": "Главная", "url": "/", "icon": "home"},
        {"text": "Продукты", "url": "/products/", "icon": "box"},
        {"text": "Услуги", "url": "/services/", "icon": "wrench"},
        {"text": "Контакты", "url": "/contact/", "icon": "mail"}
    ],
    class="nav nav-horizontal"
)
```

### Вертикальная навигация

```python
nav = render_navigation(
    items=[
        {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard"},
        {"text": "Пользователи", "url": "/users/", "icon": "users"},
        {"text": "Настройки", "url": "/settings/", "icon": "cog"},
        {"text": "Отчеты", "url": "/reports/", "icon": "chart"}
    ],
    class="nav nav-vertical"
)
```

### Навигация по хлебным крошкам

```python
breadcrumb_items = [
    {"text": "Главная", "url": "/"},
    {"text": "Продукты", "url": "/products/"},
    {"text": "Электроника", "url": "/products/electronics/"},
    {"text": "Смартфоны", "url": None, "active": True}
]

breadcrumb = render_navigation(
    breadcrumb_items,
    class="breadcrumb"
)
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_navigation items=navigation_items class="nav
nav-horizontal" %}
```

## Расширенные примеры

### Навигация с выпадающими меню

```python
def create_dropdown_nav():
    items = [
        {"text": "Главная", "url": "/", "icon": "home"},
        {
            "text": "Продукты",
            "url": "#",
            "icon": "box",
            "dropdown": [
                {"text": "Электроника", "url": "/products/electronics/"},
                {"text": "Одежда", "url": "/products/clothing/"},
                {"text": "Книги", "url": "/products/books/"}
            ]
        },
        {"text": "О нас", "url": "/about/", "icon": "info"}
    ]
    return render_navigation(items, class="nav nav-horizontal")

nav = create_dropdown_nav()
```

### Адаптивная навигация

```python
nav = render_navigation(
    items=[
        {"text": "Главная", "url": "/", "icon": "home"},
        {"text": "Продукты", "url": "/products/", "icon": "box"},
        {"text": "Услуги", "url": "/services/", "icon": "wrench"},
        {"text": "Контакты", "url": "/contact/", "icon": "mail"}
    ],
    class="nav nav-horizontal nav-responsive",
    data_role="navigation"
)
```

### Навигация с бейджами

```python
def create_nav_with_badges():
    items = [
        {"text": "Главная", "url": "/", "icon": "home"},
        {"text": "Сообщения", "url": "/messages/", "icon": "mail", "badge": "5"},
        {"text": "Уведомления", "url": "/notifications/", "icon": "bell", "badge": "12"},
        {"text": "Настройки", "url": "/settings/", "icon": "cog"}
    ]
    return render_navigation(items, class="nav nav-horizontal")

nav = create_nav_with_badges()
```

### Условная навигация

```python
def get_navigation_items(user):
    base_items = [
        {"text": "Главная", "url": "/", "icon": "home"},
        {"text": "О нас", "url": "/about/", "icon": "info"}
    ]

    if user.is_authenticated:
        base_items.extend([
            {"text": "Панель управления", "url": "/dashboard/", "icon": "dashboard"},
            {"text": "Профиль", "url": "/profile/", "icon": "user"},
            {"text": "Выход", "url": "/logout/", "icon": "exit"}
        ])
    else:
        base_items.extend([
            {"text": "Вход", "url": "/login/", "icon": "enter"},
            {"text": "Регистрация", "url": "/register/", "icon": "user-plus"}
        ])

    return render_navigation(base_items, class="nav nav-horizontal")

nav = get_navigation_items(request.user)
```

## Лучшие практики

1. **Используйте описательный текст**: Делайте метки навигации ясными и описательными
2. **Включайте иконки**: Используйте иконки MetroUI для улучшения визуального распознавания
3. **Выделяйте активное состояние**: Всегда указывайте текущую страницу
4. **Держите просто**: Не перегружайте навигацию слишком большим количеством элементов
5. **Делайте адаптивной**: Обеспечивайте работу навигации на всех размерах экрана
6. **Используйте последовательную стилизацию**: Применяйте последовательные классы во всем приложении

## Связанные компоненты

- [Меню](menus.md) - Для выпадающих и контекстных меню
- [Хлебные крошки](breadcrumbs.md) - Для навигации по хлебным крошкам
- [Боковые панели](sidebars.md) - Для боковой навигации
- [Вкладки](tabs.md) - Для навигации по вкладкам
