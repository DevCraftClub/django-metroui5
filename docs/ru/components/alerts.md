# Алерты (Alerts)

Компонент для отображения информационных сообщений, предупреждений и ошибок.

## Основное использование

### Простой алерт

```python
from metroui5.components import render_alert

# Базовый алерт
alert = render_alert("Это информационное сообщение")
```

### Алерт с типом

```python
# Различные типы алертов
info_alert = render_alert("Информация", alert_type="info")
success_alert = render_alert("Успешно!", alert_type="success")
warning_alert = render_alert("Внимание!", alert_type="warning")
error_alert = render_alert("Ошибка!", alert_type="error")
```

### Закрываемый алерт

```python
# Алерт с возможностью закрытия
dismissible_alert = render_alert(
	"Это сообщение можно закрыть",
	alert_type="info",
	dismissible=True
)
```

## Параметры

### `content` (обязательный)

Текст сообщения для отображения.

```python
alert = render_alert("Ваше сообщение здесь")
```

### `alert_type` (опционально)

Тип алерта, определяющий стиль и цвет. Доступные значения:

- `"info"` (по умолчанию) - синий
- `"success"` - зеленый
- `"warning"` - желтый/оранжевый
- `"error"` - красный

```python
alert = render_alert("Сообщение", alert_type="success")
```

### `dismissible` (опционально)

Если `True`, добавляет кнопку закрытия. По умолчанию `False`.

```python
alert = render_alert("Закрываемое сообщение", dismissible=True)
```

### `**attrs` (опционально)

Дополнительные HTML атрибуты.

```python
alert = render_alert(
	"Кастомный алерт",
	**{"class": "custom-alert", "id": "myAlert"}
)
```

## Примеры использования

### В представлении

```python
from metroui5.components import render_alert


def dashboard(request):
	context = {
		'welcome_alert': render_alert(
			"Добро пожаловать в панель управления!",
			alert_type="success"
		),
		'info_alert': render_alert(
			"Система обновлена до версии 2.0",
			alert_type="info",
			dismissible=True
		),
		'warning_alert': render_alert(
			"Не забудьте сохранить изменения перед выходом",
			alert_type="warning"
		)
	}
	return render(request, 'dashboard.html', context)
```

### В шаблоне

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }} {{
info_alert|safe }} {{ warning_alert|safe }}

<h2>Основное содержимое</h2>
<p>Содержимое страницы...</p>
{% endblock %}
```

### Динамические алерты

```python
def form_processing(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			# Обработка успешна
			alert = render_alert(
				"Форма успешно отправлена!",
				alert_type="success"
			)
		else:
			# Есть ошибки
			alert = render_alert(
				"Пожалуйста, исправьте ошибки в форме.",
				alert_type="error"
			)
	else:
		form = MyForm()
		alert = None

	return render(request, 'form.html', {
		'form': form,
		'alert': alert
	})
```

### Условное отображение

```html
{% if alert %} {{ alert|safe }} {% endif %} {% if messages %} {% for message in
messages %} {% if message.tags == 'success' %} {{ render_alert(message,
alert_type="success")|safe }} {% elif message.tags == 'error' %} {{
render_alert(message, alert_type="error")|safe }} {% elif message.tags ==
'warning' %} {{ render_alert(message, alert_type="warning")|safe }} {% else %}
{{ render_alert(message, alert_type="info")|safe }} {% endif %} {% endfor %} {%
endif %}
```

## Кастомизация

### Дополнительные CSS классы

```python
alert = render_alert(
	"Кастомный стиль",
	**{"class": "alert-custom my-alert"}
)
```

### Атрибуты для JavaScript

```python
alert = render_alert(
	"Интерактивный алерт",
	**{
		"data-auto-hide": "5000",
		"data-animation": "fade",
		"onclick": "handleAlertClick()"
	}
)
```

### Стилизация через CSS

```css
/* Кастомные стили для алертов */
.alert-custom {
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.my-alert {
    font-weight: bold;
    text-transform: uppercase;
}
```

## Лучшие практики

### 1. Используйте правильные типы

- `info` - для общей информации
- `success` - для успешных операций
- `warning` - для предупреждений
- `error` - для ошибок

### 2. Делайте сообщения краткими

```python
# Хорошо
alert = render_alert("Файл успешно загружен", alert_type="success")

# Плохо
alert = render_alert("Файл был успешно загружен в систему и сохранен в базе данных", alert_type="success")
```

### 3. Используйте dismissible для важных сообщений

```python
# Важное сообщение, которое пользователь может закрыть
alert = render_alert(
	"Не забудьте сохранить изменения!",
	alert_type="warning",
	dismissible=True
)
```

### 4. Группируйте связанные алерты

```python
def process_form(request):
	alerts = []

	if form.is_valid():
		alerts.append(render_alert("Форма валидна", "success"))

		if user.is_new:
			alerts.append(render_alert("Добро пожаловать!", "info"))

	context = {'alerts': alerts}
	return render(request, 'form.html', context)
```

## Решение проблем

### Алерт не отображается

1. Проверьте, что функция `render_alert` импортирована
2. Убедитесь, что в шаблоне используется `|safe` фильтр
3. Проверьте консоль браузера на ошибки JavaScript

### Стили не применяются

1. Убедитесь, что MetroUI5 CSS загружен
2. Проверьте, что нет конфликтующих CSS правил
3. Используйте инспектор браузера для проверки применяемых стилей

### JavaScript не работает

1. Проверьте, что MetroUI5 JavaScript загружен
2. Убедитесь, что нет конфликтов с другими скриптами
3. Проверьте консоль браузера на ошибки

## Связанные компоненты

- [Кнопки](buttons.md) - для действий в алертах
- [Карточки](cards.md) - для группировки информации
- [Формы](forms.md) - для отображения ошибок валидации

## Следующие шаги

Теперь, когда вы освоили алерты:

1. Изучите другие [компоненты](../) для создания полноценных интерфейсов
2. Ознакомьтесь с [примерами](../../getting-started/examples.md)
3. Изучите [API справочник](../../api-reference/) для детальной информации
