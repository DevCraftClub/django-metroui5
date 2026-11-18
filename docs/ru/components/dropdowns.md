# Выпадающие списки

Компонент для создания выпадающих меню и списков выбора с различными опциями и интерактивными функциями.

## Базовое использование

### Простой выпадающий список

```python
from metroui5.components import render_dropdown

# Базовый выпадающий список
dropdown_html = render_dropdown(
    options=["Опция 1", "Опция 2", "Опция 3"]
)
```

### Выпадающий список со значениями

```python
# Выпадающий список с определенными значениями
options = [
    {"text": "Главная", "value": "home"},
    {"text": "О нас", "value": "about"},
    {"text": "Контакты", "value": "contact"}
]

dropdown_html = render_dropdown(
    options=options,
    selected="home"
)
```

### Пользовательский выпадающий список

```python
# Пользовательский выпадающий список со стилизацией
dropdown_html = render_dropdown(
    options=options,
    id="main-dropdown",
    class="dropdown-primary",
    placeholder="Выберите опцию..."
)
```

## Результат рендеринга

### Базовый выпадающий список

```html
<!-- Ввод -->
render_dropdown(options=["Опция 1", "Опция 2", "Опция 3"])

<!-- Вывод -->
<select class="dropdown" data-role="dropdown">
	<option value="Опция 1">Опция 1</option>
	<option value="Опция 2">Опция 2</option>
	<option value="Опция 3">Опция 3</option>
</select>
```

### Выпадающий список со значениями

```html
<!-- Ввод -->
render_dropdown(options=[{"text": "Главная", "value": "home"}, {"text": "О нас",
"value": "about"}], selected="home")

<!-- Вывод -->
<select class="dropdown" data-role="dropdown">
	<option value="home" selected>Главная</option>
	<option value="about">О нас</option>
</select>
```

### Выпадающий список с заполнителем

```html
<!-- Ввод -->
render_dropdown(options=options, placeholder="Выберите опцию...")

<!-- Вывод -->
<select class="dropdown" data-role="dropdown">
	<option value="" disabled selected>Выберите опцию...</option>
	<option value="home">Главная</option>
	<option value="about">О нас</option>
</select>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовый выпадающий список -->
{% metroui5_dropdown options=dropdown_options %}

<!-- Выпадающий список с выбором -->
{% metroui5_dropdown options=dropdown_options selected="home" %}

<!-- Пользовательский выпадающий список -->
{% metroui5_dropdown options=dropdown_options placeholder="Выберите..."
class="dropdown-large" %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_dropdown

def dropdown_view(request):
    # Создать опции выпадающего списка
    category_options = [
        {"text": "Технологии", "value": "tech"},
        {"text": "Спорт", "value": "sports"},
        {"text": "Новости", "value": "news"}
    ]

    dropdown_html = render_dropdown(
        options=category_options,
        selected=request.GET.get('category', ''),
        placeholder="Выберите категорию...",
        id="category-dropdown"
    )

    context = {
        'dropdown_html': dropdown_html,
        'category_options': category_options
    }
    return render(request, 'dropdown.html', context)
```

```html
<!-- dropdown.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ dropdown_html|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_dropdown options=category_options selected=selected_category %} {%
endblock %}
```

## Параметры

### `options` (обязательно)

Список опций для выпадающего списка. Может быть строками или словарями.

**Формат**:

```python
# Простые строки
options = ["Опция 1", "Опция 2", "Опция 3"]

# Словари с текстом и значением
options = [
    {"text": "Отображаемый текст", "value": "фактическое_значение"},
    {"text": "Другая опция", "value": "другое_значение"}
]
```

### `selected` (опционально)

Значение изначально выбранной опции.

**Пример**:

```python
dropdown_html = render_dropdown(options=options, selected="home")
```

### `placeholder` (опционально)

Текст-заполнитель, когда опция не выбрана.

**Пример**:

```python
dropdown_html = render_dropdown(options=options, placeholder="Выберите...")
```

### `id` (опционально)

Уникальный идентификатор для элемента выпадающего списка.

**Пример**:

```python
dropdown_html = render_dropdown(options=options, id="my-dropdown")
```

### `class` (опционально)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
dropdown_html = render_dropdown(options=options, class="dropdown-large")
```

### `multiple` (опционально)

Разрешить множественный выбор.

**Пример**:

```python
dropdown_html = render_dropdown(options=options, multiple=True)
```

## Продвинутые примеры

### Группированный выпадающий список

```python
def create_grouped_dropdown(groups):
    """Создать выпадающий список с группами опций."""

    dropdown_html = '<select class="dropdown" data-role="dropdown">'

    for group in groups:
        dropdown_html += f'<optgroup label="{group["label"]}">'
        for option in group["options"]:
            dropdown_html += f'<option value="{option["value"]}">{option["text"]}</option>'
        dropdown_html += '</optgroup>'

    dropdown_html += '</select>'
    return dropdown_html
```

### Поисковый выпадающий список

```python
def create_searchable_dropdown(options, searchable=True):
    """Создать выпадающий список с функцией поиска."""

    return render_dropdown(
        options=options,
        class="dropdown-search" if searchable else "dropdown",
        **{"data-search": "true"} if searchable else {}
    )
```

### Динамический выпадающий список

```python
def create_dynamic_dropdown(options, ajax_url=None):
    """Создать выпадающий список, который загружает опции динамически."""

    return render_dropdown(
        options=options,
        class="dropdown-dynamic",
        **{"data-ajax-url": ajax_url} if ajax_url else {}
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `dropdown` - Базовый класс выпадающего списка
- `dropdown-primary` - Основной стиль выпадающего списка
- `dropdown-secondary` - Вторичный стиль выпадающего списка

#### Классы размеров

- `dropdown-small` - Маленький выпадающий список
- `dropdown-large` - Большой выпадающий список
- `dropdown-mini` - Мини выпадающий список

#### Классы функций

- `dropdown-search` - Поисковый выпадающий список
- `dropdown-multi` - Выпадающий список с множественным выбором

### Пользовательская стилизация

```css
/* Пользовательская стилизация выпадающего списка */
.dropdown-custom {
	border: 2px solid #007acc;
	border-radius: 6px;
	padding: 10px;
	font-size: 16px;
	background: white;
}

.dropdown-custom:focus {
	outline: none;
	border-color: #005a99;
	box-shadow: 0 0 5px rgba(0, 122, 204, 0.3);
}

/* Пользовательская стрелка выпадающего списка */
.dropdown-custom::after {
	content: "▼";
	position: absolute;
	right: 10px;
	pointer-events: none;
}
```

## Интеграция с JavaScript

### Базовые события

```javascript
// Обработать изменение выпадающего списка
$(".dropdown").on("change", function () {
	const selectedValue = $(this).val();
	console.log("Выбрано:", selectedValue);
	handleDropdownChange(selectedValue);
});

function handleDropdownChange(value) {
	// Обработать выбранное значение
	updateContent(value);
}
```

### Динамическая загрузка

```javascript
// Загрузить опции выпадающего списка через AJAX
function loadDropdownOptions(dropdownId, url) {
	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			updateDropdownOptions(dropdownId, data.options);
		},
		error: function (xhr, status, error) {
			console.error("Ошибка загрузки опций:", error);
		},
	});
}

function updateDropdownOptions(dropdownId, options) {
	const dropdown = $(`#${dropdownId}`);
	dropdown.empty();

	options.forEach((option) => {
		dropdown.append(`<option value="${option.value}">${option.text}</option>`);
	});
}
```

## Лучшие практики

### 1. Структура опций

```python
# Консистентный формат опций
def format_dropdown_options(items, text_field='name', value_field='id'):
    """Форматировать элементы для использования в выпадающем списке."""
    return [
        {"text": getattr(item, text_field), "value": getattr(item, value_field)}
        for item in items
    ]
```

### 2. Выбор по умолчанию

```python
# Обработать выбор по умолчанию
def create_dropdown_with_default(options, default_value=None):
    return render_dropdown(
        options=options,
        selected=default_value or options[0]['value'] if options else None
    )
```

## Связанные компоненты

- [Формы](forms.md) - Для интеграции с формами
- [Кнопки](buttons.md) - Для триггеров выпадающих списков
- [Навигация](navigation.md) - Для навигационных выпадающих списков


## metroui5_dropdown

```python
render_dropdown()
```

Пустое или неверное значение: `render_dropdown()` даёт `<div class="dropdown-toggle">Click me<div class="dropdown" data-role="dropdown"></div></div>`.

```django
{% metroui5_dropdown items %}
```
