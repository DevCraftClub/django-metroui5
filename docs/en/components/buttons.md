# Кнопки (Buttons)

Компонент для создания интерактивных кнопок различных типов и размеров.

## Основное использование

### Простая кнопка

```python
from metroui5.components import render_button

# Базовая кнопка
button = render_button("Нажми меня")
```

### Кнопка с типом

```python
# Различные типы кнопок
primary_button = render_button("Основная", button_type="primary")
secondary_button = render_button("Вторичная", button_type="secondary")
success_button = render_button("Успех", button_type="success")
alert_button = render_button("Ошибка", button_type="alert")
```

### Кнопка с размером

```python
# Различные размеры
small_button = render_button("Маленькая", size="small")
default_button = render_button("Обычная", size="default")
large_button = render_button("Большая", size="large")
```

## Параметры

### `content` (обязательный)

Текст или содержимое кнопки.

```python
button = render_button("Текст кнопки")
```

### `button_type` (опционально)

Тип кнопки, определяющий стиль и цвет. Доступные значения:

- `"default"` (по умолчанию) - стандартная
- `"primary"` - основная (синяя)
- `"secondary"` - вторичная (серая)
- `"success"` - успех (зеленая)
- `"alert"` - ошибка (красная)
- `"warning"` - предупреждение (желтая)

```python
button = render_button("Кнопка", button_type="primary")
```

### `size` (опционально)

Размер кнопки. Доступные значения:

- `"small"` - маленькая
- `"default"` (по умолчанию) - обычная
- `"large"` - большая

```python
button = render_button("Кнопка", size="large")
```

### `outline` (опционально)

Если `True`, создает контурную кнопку. По умолчанию `False`.

```python
button = render_button("Контурная", outline=True)
```

### `icon` (опционально)

Иконка для кнопки (имя иконки MetroUI).

```python
button = render_button("С иконкой", icon="plus")
```

### `**attrs` (опционально)

Дополнительные HTML атрибуты.

```python
button = render_button(
	"Кастомная",
	**{"class": "custom-btn", "id": "myButton", "onclick": "handleClick()"}
)
```

## Примеры использования

### В представлении

```python
from metroui5.components import render_button


def dashboard(request):
	context = {
		'action_buttons': [
			render_button("Создать", button_type="primary", icon="plus"),
			render_button("Редактировать", button_type="secondary", icon="edit"),
			render_button("Удалить", button_type="alert", icon="trash"),
		],
		'size_buttons': [
			render_button("Маленькая", size="small"),
			render_button("Обычная", size="default"),
			render_button("Большая", size="large"),
		],
		'outline_buttons': [
			render_button("Основная", button_type="primary", outline=True),
			render_button("Успех", button_type="success", outline=True),
		]
	}
	return render(request, 'dashboard.html', context)
```

### В шаблоне

```html
{% extends 'base.html' %} {% block content %}
<h3>Действия</h3>
<div class="button-group">
    {% for button in action_buttons %} {{ button|safe }} {% endfor %}
</div>

<h3>Размеры</h3>
<div class="button-group">
    {% for button in size_buttons %} {{ button|safe }} {% endfor %}
</div>

<h3>Контурные кнопки</h3>
<div class="button-group">
    {% for button in outline_buttons %} {{ button|safe }} {% endfor %}
</div>
{% endblock %}
```

### Кнопки для форм

```python
def form_view(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			# Обработка формы
			pass
	else:
		form = MyForm()

	submit_button = render_button(
		"Отправить",
		button_type="primary",
		**{"type": "submit"}
	)

	cancel_button = render_button(
		"Отмена",
		button_type="secondary",
		**{"type": "button", "onclick": "history.back()"}
	)

	context = {
		'form': form,
		'submit_button': submit_button,
		'cancel_button': cancel_button,
	}
	return render(request, 'form.html', context)
```

### Интерактивные кнопки

```python
def interactive_view(request):
	context = {
		'modal_button': render_button(
			"Открыть модальное окно",
			button_type="primary",
			**{
				"data-role": "button",
				"data-toggle": "modal",
				"data-target": "#exampleModal"
			}
		),
		'ajax_button': render_button(
			"Загрузить данные",
			button_type="success",
			**{
				"onclick": "loadData()",
				"data-loading": "Загрузка..."
			}
		),
		'toggle_button': render_button(
			"Показать/скрыть",
			button_type="secondary",
			**{
				"data-role": "button",
				"data-toggle": "collapse",
				"data-target": "#content"
			}
		)
	}
	return render(request, 'interactive.html', context)
```

## Кастомизация

### Дополнительные CSS классы

```python
button = render_button(
	"Кастомная кнопка",
	**{"class": "btn-custom my-button"}
)
```

### Атрибуты для JavaScript

```python
button = render_button(
	"Интерактивная",
	**{
		"data-action": "save",
		"data-id": "123",
		"onclick": "handleButtonClick(this)"
	}
)
```

### Стилизация через CSS

```css
/* Кастомные стили для кнопок */
.btn-custom {
    border-radius: 20px;
    text-transform: uppercase;
    font-weight: bold;
}

.my-button {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.my-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}
```

## Группировка кнопок

### Горизонтальная группа

```python
def button_group_view(request):
	context = {
		'button_group': [
			render_button("Левая", button_type="secondary"),
			render_button("Центр", button_type="primary"),
			render_button("Правая", button_type="secondary"),
		]
	}
	return render(request, 'button_group.html', context)
```

### Вертикальная группа

```html
{% extends 'base.html' %} {% block content %}
<div class="vertical-button-group">
    {% for button in button_group %}
    <div class="mb-2">{{ button|safe }}</div>
    {% endfor %}
</div>
{% endblock %}
```

## Лучшие практики

### 1. Используйте правильные типы

- `primary` - для основного действия
- `secondary` - для вторичных действий
- `success` - для позитивных действий
- `alert` - для деструктивных действий

### 2. Выбирайте подходящие размеры

- `small` - для компактных интерфейсов
- `default` - для большинства случаев
- `large` - для важных действий

### 3. Добавляйте иконки для ясности

```python
# Хорошо
button = render_button("Сохранить", icon="check", button_type="success")

# Плохо
button = render_button("Сохранить", button_type="success")
```

### 4. Используйте outline для вторичных действий

```python
# Основное действие
primary_button = render_button("Сохранить", button_type="primary")

# Вторичное действие
secondary_button = render_button("Отмена", button_type="secondary", outline=True)
```

### 5. Группируйте связанные кнопки

```python
def form_actions(request):
	context = {
		'form_buttons': [
			render_button("Сохранить", button_type="primary", icon="check"),
			render_button("Сохранить как черновик", button_type="secondary", icon="save"),
			render_button("Отмена", button_type="secondary", outline=True),
		]
	}
	return render(request, 'form_actions.html', context)
```

## Решение проблем

### Кнопка не отображается

1. Проверьте, что функция `render_button` импортирована
2. Убедитесь, что в шаблоне используется `|safe` фильтр
3. Проверьте консоль браузера на ошибки

### Стили не применяются

1. Убедитесь, что MetroUI5 CSS загружен
2. Проверьте, что нет конфликтующих CSS правил
3. Используйте инспектор браузера для проверки применяемых стилей

### JavaScript не работает

1. Проверьте, что MetroUI5 JavaScript загружен
2. Убедитесь, что нет конфликтов с другими скриптами
3. Проверьте консоль браузера на ошибки

### Кнопки не группируются

1. Убедитесь, что кнопки находятся в одном контейнере
2. Проверьте CSS классы для группировки
3. Используйте MetroUI5 классы для группировки кнопок

## Связанные компоненты

- [Алерты](alerts.md) - для отображения сообщений
- [Формы](forms.md) - для кнопок отправки
- [Модальные окна](modals.md) - для кнопок открытия/закрытия
- [Карточки](cards.md) - для размещения кнопок

## Следующие шаги

Теперь, когда вы освоили кнопки:

1. Изучите другие [компоненты](../) для создания полноценных интерфейсов
2. Ознакомьтесь с [примерами](../../getting-started/examples.md)
3. Изучите [API справочник](../../api-reference/) для детальной информации
4. Создайте интерактивные формы и интерфейсы!
