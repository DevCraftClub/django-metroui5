# Поля ввода

MetroUI5 Django предоставляет комплексную систему компонентов полей ввода для создания различных типов полей формы с MetroUI стилизацией и функциональностью.

## Базовое использование

```python
from metroui5.components import render_input

# Простое текстовое поле
input_html = render_input(input_type="text", placeholder="Введите текст...")
```

## Параметры

### `render_input(input_type="text", placeholder="", **attrs)`

- **input_type** (str): Тип поля ввода (text, email, password, number, etc.)
- **placeholder** (str): Текст-заполнитель
- **attrs** (dict): Дополнительные HTML атрибуты

## Примеры

### Базовые поля ввода

```python
from metroui5.components import render_input

# Текстовое поле
text_input = render_input(
    input_type="text",
    placeholder="Введите ваше имя",
    class="input"
)

# Поле email
email_input = render_input(
    input_type="email",
    placeholder="Введите ваш email",
    class="input"
)

# Поле пароля
password_input = render_input(
    input_type="password",
    placeholder="Введите ваш пароль",
    class="input"
)
```

### Поле с пользовательскими атрибутами

```python
input_field = render_input(
    input_type="text",
    placeholder="Поиск...",
    id="search-input",
    class="input input-large",
    data_role="input",
    autocomplete="off"
)
```

### Поле с валидацией

```python
input_field = render_input(
    input_type="text",
    placeholder="Введите имя пользователя",
    class="input",
    required=True,
    minlength="3",
    maxlength="20",
    pattern="[a-zA-Z0-9_]+"
)
```

## Классы полей ввода MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации полей ввода:

### Классы размеров

- `input-small` - Маленькое поле
- `input-large` - Большое поле
- `input-mini` - Мини поле

### Классы стилей

- `input-rounded` - Скругленное поле
- `input-outlined` - Поле с контуром
- `input-filled` - Заполненное поле
- `input-clear` - Прозрачное поле

### Классы состояний

- `input-success` - Состояние успеха
- `input-error` - Состояние ошибки
- `input-warning` - Предупреждающее состояние
- `input-disabled` - Отключенное состояние

## Типы полей ввода

### Текстовые поля

```python
# Базовое текстовое поле
text_input = render_input(
    input_type="text",
    placeholder="Введите текст",
    class="input"
)

# Поле поиска
search_input = render_input(
    input_type="search",
    placeholder="Поиск...",
    class="input input-search"
)

# Поле URL
url_input = render_input(
    input_type="url",
    placeholder="Введите URL",
    class="input"
)
```

### Числовые поля

```python
# Числовое поле
number_input = render_input(
    input_type="number",
    placeholder="Введите число",
    class="input",
    min="0",
    max="100"
)

# Поле диапазона
range_input = render_input(
    input_type="range",
    class="input input-range",
    min="0",
    max="100",
    value="50"
)
```

### Поля даты и времени

```python
# Поле даты
date_input = render_input(
    input_type="date",
    class="input",
    data_role="datepicker"
)

# Поле времени
time_input = render_input(
    input_type="time",
    class="input",
    data_role="timepicker"
)

# Поле даты и времени
datetime_input = render_input(
    input_type="datetime-local",
    class="input",
    data_role="datetimepicker"
)
```

### Поля файлов

```python
# Поле файла
file_input = render_input(
    input_type="file",
    class="input input-file",
    accept="image/*,.pdf,.doc,.docx"
)

# Поле множественных файлов
multiple_file_input = render_input(
    input_type="file",
    class="input input-file",
    multiple=True,
    accept="image/*"
)
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_input type="text" placeholder="Введите текст..."
class="input" %}
```

## Расширенные примеры

### Поле с иконкой

```python
def create_input_with_icon(input_type="text", placeholder="", icon="search"):
    """Создание поля ввода с иконкой."""

    return f"""
    <div class="input-group">
        <span class="input-group-addon">
            <span class="mif-{icon}"></span>
        </span>
        {render_input(
            input_type=input_type,
            placeholder=placeholder,
            class="input"
        )}
    </div>
    """

# Использование
search_input = create_input_with_icon("text", "Поиск...", "search")
email_input = create_input_with_icon("email", "Введите email", "mail")
```

### Поле с состояниями валидации

```python
def create_validated_input(field_name, value="", is_valid=None, error_message=""):
    """Создание поля с состоянием валидации."""

    input_class = "input"

    if is_valid is True:
        input_class += " input-success"
    elif is_valid is False:
        input_class += " input-error"

    input_html = render_input(
        input_type="text",
        name=field_name,
        value=value,
        class=input_class
    )

    if is_valid is False and error_message:
        error_html = f'<div class="error-message">{error_message}</div>'
        return input_html + error_html

    return input_html

# Использование
valid_input = create_validated_input("username", "john_doe", True)
invalid_input = create_validated_input("email", "invalid-email", False, "Пожалуйста, введите корректный email")
```

### Адаптивное поле ввода

```python
def create_responsive_input(input_type="text", placeholder="", breakpoints=None):
    """Создание адаптивного поля ввода."""

    if breakpoints is None:
        breakpoints = {
            'mobile': {'size': 'small'},
            'tablet': {'size': 'default'},
            'desktop': {'size': 'large'}
        }

    input_class = "input"

    # Добавление адаптивных классов
    for breakpoint, config in breakpoints.items():
        if config['size'] != 'default':
            input_class += f" input-{breakpoint}-{config['size']}"

    return render_input(
        input_type=input_type,
        placeholder=placeholder,
        class=input_class
    )

# Использование
responsive_input = create_responsive_input("text", "Введите текст...")
```

### Поле с автодополнением

```python
def create_autocomplete_input(field_name, placeholder="", options=None):
    """Создание поля с функцией автодополнения."""

    if options is None:
        options = []

    input_html = render_input(
        input_type="text",
        name=field_name,
        placeholder=placeholder,
        class="input",
        data_role="autocomplete",
        data_source=options
    )

    return input_html

# Использование
countries = ["США", "Канада", "Великобритания", "Германия", "Франция", "Япония"]
country_input = create_autocomplete_input("country", "Выберите страну", countries)
```

### Поле с маской

```python
def create_masked_input(input_type="text", placeholder="", mask="", pattern=""):
    """Создание поля с маской ввода."""

    return render_input(
        input_type=input_type,
        placeholder=placeholder,
        class="input",
        data_role="input",
        data_mask=mask,
        data_pattern=pattern
    )

# Использование
phone_input = create_masked_input("tel", "(___) ___-____", "(999) 999-9999")
date_input = create_masked_input("text", "__/__/____", "99/99/9999")
```

### Поле со счетчиком символов

```python
def create_counter_input(input_type="text", placeholder="", max_length=100):
    """Создание поля со счетчиком символов."""

    input_html = render_input(
        input_type=input_type,
        placeholder=placeholder,
        class="input",
        maxlength=max_length,
        data_role="input"
    )

    counter_html = f"""
    <div class="input-counter">
        <span class="counter-current">0</span>
        <span class="counter-separator">/</span>
        <span class="counter-max">{max_length}</span>
    </div>
    """

    return f"""
    <div class="input-with-counter">
        {input_html}
        {counter_html}
    </div>
    """

# Использование
counter_input = create_counter_input("text", "Введите описание...", 200)
```

## Интеграция с JavaScript

### Валидация поля ввода

```javascript
// Валидация поля при потере фокуса
document.querySelectorAll(".input").forEach((input) => {
	input.addEventListener("blur", function () {
		validateInput(this);
	});
});

function validateInput(input) {
	const value = input.value.trim();
	const type = input.type;

	// Удаление существующих классов валидации
	input.classList.remove("input-success", "input-error");

	if (value === "") {
		if (input.hasAttribute("required")) {
			input.classList.add("input-error");
		}
		return;
	}

	// Валидация по типу
	if (type === "email" && !isValidEmail(value)) {
		input.classList.add("input-error");
		return;
	}

	if (type === "url" && !isValidUrl(value)) {
		input.classList.add("input-error");
		return;
	}

	input.classList.add("input-success");
}

function isValidEmail(email) {
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	return emailRegex.test(email);
}

function isValidUrl(url) {
	try {
		new URL(url);
		return true;
	} catch {
		return false;
	}
}
```

### События поля ввода

```javascript
// Обработка событий поля ввода
document.querySelectorAll(".input").forEach((input) => {
	input.addEventListener("input", function () {
		// Обновление счетчика символов
		updateCounter(this);

		// Запуск пользовательских событий
		this.dispatchEvent(
			new CustomEvent("metroui-input-change", {
				detail: { value: this.value },
			})
		);
	});
});

function updateCounter(input) {
	const counter = input.parentNode.querySelector(".input-counter");
	if (counter) {
		const current = input.value.length;
		const max = input.maxLength;
		counter.querySelector(".counter-current").textContent = current;
	}
}
```

## Лучшие практики

1. **Используйте соответствующие типы полей**: Выбирайте правильный HTML5 тип поля ввода
2. **Предоставляйте полезные заполнители**: Используйте описательный текст-заполнитель
3. **Включайте правильную валидацию**: Добавляйте клиентскую и серверную валидацию
4. **Делайте поля доступными**: Включайте правильные метки и ARIA атрибуты
5. **Используйте последовательную стилизацию**: Применяйте последовательные классы во всем приложении
6. **Обрабатывайте крайние случаи**: Учитывайте пустые значения и неверный ввод
7. **Тестируйте тщательно**: Тестируйте поля с различными типами данных и крайними случаями

## Связанные компоненты

- [Формы](forms.md) - Для полной обработки форм
- [Кнопки](buttons.md) - Для кнопок, связанных с полями ввода
- [Уведомления](alerts.md) - Для сообщений валидации
- [Карточки](cards.md) - Для содержания полей ввода
