# Справочник API компонентов

Полный справочник по всем функциям рендеринга компонентов MetroUI5, доступным в модуле `metroui5.components`.

## Обзор

Модуль компонентов предоставляет высокоуровневые функции для рендеринга полных UI компонентов со стилизацией MetroUI5. Каждая функция возвращает HTML строки, которые можно использовать непосредственно в шаблонах Django или представлениях.

```python
from metroui5.components import (
    render_alert, render_button, render_card, render_tile,
    render_table, render_navigation, render_modal,
    render_progress, render_input, render_panel, render_accordion,
    render_list, render_badge, render_pagination, render_calendar,
    render_dialog, render_dropdown, render_menu, render_sidebar,
    render_tabs, render_toolbar, render_breadcrumb, render_avatar,
    render_rating
)
```

## Компоненты уведомлений

### `render_alert(content, alert_type="info", dismissible=False, **attrs)`

Рендерит компоненты уведомлений/алертов.

**Параметры:**

- `content` (str): Содержимое уведомления
- `alert_type` (str): Тип уведомления - "info", "success", "warning", "danger", "error"
- `dismissible` (bool): Можно ли закрыть уведомление
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

**Пример:**

```python
alert_html = render_alert(
    content="Операция успешно завершена",
    alert_type="success",
    dismissible=True,
    id="success-alert"
)
```

## Компоненты кнопок

### `render_button(content, button_type="default", size=None, outline=False, **attrs)`

Рендерит компоненты кнопок с различными стилями и размерами.

**Параметры:**

- `content` (str): Текстовое содержимое кнопки
- `button_type` (str): Стиль кнопки - "default", "primary", "secondary", "success", "danger", "warning", "info"
- `size` (str, optional): Размер кнопки - "sm", "lg"
- `outline` (bool): Использовать ли контурный стиль
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

**Пример:**

```python
button_html = render_button(
    content="Сохранить изменения",
    button_type="primary",
    size="lg",
    onclick="saveForm()"
)
```

## Компоненты карточек

### `render_card(header=None, content=None, footer=None, **attrs)`

Рендерит компоненты карточек для отображения содержимого.

**Параметры:**

- `header` (str, optional): Содержимое заголовка карточки
- `content` (str, optional): Содержимое тела карточки
- `footer` (str, optional): Содержимое подвала карточки
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

**Пример:**

```python
card_html = render_card(
    header="Карточка продукта",
    content="<p>Описание продукта здесь</p>",
    footer='<button class="button">Купить сейчас</button>'
)
```

## Компоненты плиток

### `render_tile(title, content=None, size="medium", color="blue", icon=None, **attrs)`

Рендерит компоненты плиток MetroUI.

**Параметры:**

- `title` (str): Заголовок плитки
- `content` (str, optional): Дополнительное содержимое
- `size` (str): Размер плитки - "small", "medium", "large", "wide", "tall"
- `color` (str): Цвет плитки
- `icon` (str, optional): Название иконки MetroUI
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты таблиц

### `render_table(headers, rows, **attrs)`

Рендерит таблицы данных со стилизацией MetroUI5.

**Параметры:**

- `headers` (list): Заголовки таблицы
- `rows` (list): Строки данных таблицы (каждая строка - список ячеек)
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

**Пример:**

```python
table_html = render_table(
    headers=["Имя", "Email", "Роль"],
    rows=[
        ["Иван Иванов", "ivan@example.com", "Администратор"],
        ["Мария Петрова", "maria@example.com", "Пользователь"]
    ]
)
```

## Компоненты навигации

### `render_navigation(items, **attrs)`

Рендерит меню навигации.

**Параметры:**

- `items` (list): Элементы навигации (строки или словари с 'text' и 'url')
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты модальных окон

### `render_modal(title, content, **attrs)`

Рендерит модальные диалоги.

**Параметры:**

- `title` (str): Заголовок модального окна
- `content` (str): HTML содержимое модального окна
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты прогресса

### `render_progress(value, max_value=100, color="blue", size="default", **attrs)`

Рендерит индикаторы прогресса и полосы.

**Параметры:**

- `value` (int/float): Текущее значение прогресса
- `max_value` (int/float): Максимальное значение
- `color` (str): Цвет полосы прогресса
- `size` (str): Размер - "mini", "small", "large" или "default"
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты полей ввода

### `render_input(input_type="text", placeholder="", **attrs)`

Рендерит различные типы полей ввода.

**Параметры:**

- `input_type` (str): Тип поля ввода - "text", "email", "password", "number" и т.д.
- `placeholder` (str): Текст-заполнитель
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты панелей

### `render_panel(title=None, content=None, **attrs)`

Рендерит сворачиваемые панели.

**Параметры:**

- `title` (str, optional): Заголовок панели
- `content` (str, optional): HTML содержимое панели
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты аккордеонов

### `render_accordion(items, **attrs)`

Рендерит компоненты аккордеонов с несколькими секциями.

**Параметры:**

- `items` (list): Список словарей с ключами 'title' и 'content'
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

**Пример:**

```python
accordion_html = render_accordion(
    items=[
        {"title": "Секция 1", "content": "Содержимое 1"},
        {"title": "Секция 2", "content": "Содержимое 2"}
    ]
)
```

## Компоненты списков

### `render_list(items, list_type="ul", **attrs)`

Рендерит различные типы списков.

**Параметры:**

- `items` (list): Элементы списка (строки или словари с 'text' и 'url')
- `list_type` (str): Тип списка - "ul" или "ol"
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты меню

### `render_menu(items, **attrs)`

Рендерит меню навигации.

**Параметры:**

- `items` (list): Элементы меню (строки или словари с 'text' и 'url')
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты боковых панелей

### `render_sidebar(items, **attrs)`

Рендерит боковые панели.

**Параметры:**

- `items` (list): Элементы боковой панели (строки или словари с 'text' и 'url')
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты вкладок

### `render_tabs(tabs, **attrs)`

Рендерит интерфейсы с вкладками.

**Параметры:**

- `tabs` (list): Список словарей с ключами 'title' и 'content'
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты панелей инструментов

### `render_toolbar(items, **attrs)`

Рендерит панели инструментов действий.

**Параметры:**

- `items` (list): Элементы панели инструментов
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты хлебных крошек

### `render_breadcrumb(items, **attrs)`

Рендерит навигационные хлебные крошки.

**Параметры:**

- `items` (list): Элементы хлебных крошек (строки или словари с 'text' и 'url')
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты бейджей

### `render_badge(content, badge_type="default", **attrs)`

Рендерит бейджи и метки.

**Параметры:**

- `content` (str): Содержимое бейджа
- `badge_type` (str): Тип бейджа - "default", "primary", "secondary", "success", "danger", "warning", "info"
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты пагинации

### `render_pagination(current_page, total_pages, **attrs)`

Рендерит элементы управления пагинацией.

**Параметры:**

- `current_page` (int): Номер текущей страницы
- `total_pages` (int): Общее количество страниц
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты календарей

### `render_calendar(**attrs)`

Рендерит виджеты календарей.

**Параметры:**

- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты диалогов

### `render_dialog(title, content, **attrs)`

Рендерит диалоговые окна.

**Параметры:**

- `title` (str): Заголовок диалога
- `content` (str): HTML содержимое диалога
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты выпадающих списков

### `render_dropdown(items, button_text="Dropdown", **attrs)`

Рендерит выпадающие списки выбора.

**Параметры:**

- `items` (list): Элементы выпадающего списка (строки или словари с 'text' и 'url')
- `button_text` (str): Текст кнопки для триггера выпадающего списка
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты аватаров

### `render_avatar(image_url, size="medium", **attrs)`

Рендерит аватары пользователей.

**Параметры:**

- `image_url` (str): URL изображения аватара
- `size` (str): Размер аватара - "mini", "small", "medium", "large"
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Компоненты рейтингов

### `render_rating(value, max_value=5, **attrs)`

Рендерит звездные рейтинги.

**Параметры:**

- `value` (int/float): Значение рейтинга
- `max_value` (int): Максимальное значение рейтинга
- `**attrs`: Дополнительные HTML атрибуты

**Возвращает:** HTML строку

## Функции форм (доступны в `metroui5.forms`)

Для функций, связанных с формами, импортируйте из модуля forms:

```python
from metroui5.forms import (
    render_form, render_field, render_formset,
    render_form_errors, render_formset_errors, render_label
)
```

### `render_form(form, **kwargs)`

Рендерит Django формы со стилизацией MetroUI5.

### `render_field(field, **kwargs)`

Рендерит отдельные поля форм.

### `render_formset(formset, **kwargs)`

Рендерит Django наборы форм.

## Общие параметры

Все функции компонентов принимают эти общие параметры:

### HTML атрибуты

- `id` (str): ID элемента
- `class` (str): CSS классы
- `style` (str): Встроенные стили
- `data-*` (str): Атрибуты данных

### Обработчики событий

- `onclick` (str): Обработчик клика
- `onchange` (str): Обработчик изменения
- `onsubmit` (str): Обработчик отправки

## Примеры использования

### Базовое использование компонентов

```python
from metroui5.components import render_button, render_alert

# Простая кнопка
button = render_button("Нажми меня", button_type="primary")

# Уведомление с пользовательской стилизацией
alert = render_alert(
    "Сообщение об успехе",
    alert_type="success",
    **{"class": "my-custom-alert", "data-timeout": "5000"}
)
```

### Сложная композиция компонентов

```python
from metroui5.components import render_card, render_button, render_badge

# Карточка с несколькими элементами
card_content = f"""
    <p>Описание продукта здесь</p>
    {render_badge("Новый", badge_type="success")}
    <div class="mt-3">
        {render_button("Добавить в корзину", button_type="primary")}
        {render_button("Просмотреть детали", button_type="secondary", outline=True)}
    </div>
"""

product_card = render_card(
    header="Название продукта",
    content=card_content
)
```

### Интеграция с формами

```python
from django import forms
from metroui5.forms import render_form
from metroui5.components import render_button

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

def contact_view(request):
    form = ContactForm()

    form_html = render_form(form)
    submit_button = render_button(
        "Отправить сообщение",
        button_type="primary",
        type="submit"
    )

    return render(request, 'contact.html', {
        'form_html': form_html,
        'submit_button': submit_button
    })
```

## Связанная документация

- [API форм](forms.md) - Функции рендеринга форм
- [Теги шаблонов](templatetags.md) - Эквиваленты Django тегов шаблонов
- [HTML утилиты](html.md) - Низкоуровневая генерация HTML
- [CSS утилиты](css.md) - Управление CSS классами
