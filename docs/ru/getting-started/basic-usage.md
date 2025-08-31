# Базовое использование

Основы использования MetroUI5 Django в ваших проектах.

## Загрузка шаблонных тегов

В начале каждого шаблона загружайте теги MetroUI5:

```html
{% load metroui5 %}
```

## Подключение ресурсов

### CSS файлы

```html
{% metroui5_css %}
```

### JavaScript файлы

```html
{% metroui5_javascript %}
```

### Иконки

```html
{% metroui5_icons %}
```

### Полный базовый шаблон

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{% block title %}Заголовок{% endblock %}</title>

    {% metroui5_css %} {% metroui5_icons %}
</head>
<body>
<div class="container">{% block content %} {% endblock %}</div>

{% metroui5_javascript %}
</body>
</html>
```

## Использование компонентов

### В представлениях (Views)

```python
from metroui5.components import render_button, render_card, render_alert


def dashboard(request):
	context = {
		'welcome_alert': render_alert(
			"Добро пожаловать в панель управления!",
			alert_type="success"
		),
		'action_button': render_button(
			"Создать новый проект",
			button_type="primary",
			size="large"
		),
		'info_card': render_card(
			header="Информация",
			content="Это карточка с информацией",
			footer="Дополнительные действия"
		)
	}
	return render(request, 'dashboard.html', context)
```

### В шаблонах

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }}

<div class="row">
    <div class="cell-md-6">{{ action_button|safe }}</div>
    <div class="cell-md-6">{{ info_card|safe }}</div>
</div>
{% endblock %}
```

## Работа с формами

### Рендеринг формы

```python
from metroui5.forms import render_form


def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Обработка формы
			pass
	else:
		form = ContactForm()

	form_html = render_form(form, layout='horizontal')
	return render(request, 'contact.html', {'form': form_html})
```

### Рендеринг отдельного поля

```python
from metroui5.forms import render_field


def custom_form(request):
	form = CustomForm()

	# Рендерим только определенные поля
	name_field = render_field(form['name'], placeholder="Введите имя")
	email_field = render_field(form['email'], placeholder="Введите email")

	context = {
		'name_field': name_field,
		'email_field': email_field,
	}
	return render(request, 'custom_form.html', context)
```

## Использование утилит

### HTML утилиты

```python
from metroui5.html import render_tag, render_link_tag

# Создание HTML тега
div_tag = render_tag("div", {"class": "container"}, "Содержимое")

# Создание ссылки
link = render_link_tag("https://example.com", text="Пример", target="_blank")
```

### CSS утилиты

```python
from metroui5.css import merge_css_classes, add_css_class

# Объединение CSS классов
classes = merge_css_classes("btn", "btn-primary", "btn-large")

# Добавление класса
new_classes = add_css_class(classes, "btn-block")
```

## Настройка через settings.py

### Базовые настройки

```python
METROUI5 = {
	'CDN_MODE': False,
	'THEME': 'default',
	'VERSION': '5.0.0',
}
```

### Кастомные файлы

```python
METROUI5 = {
	'CUSTOM_CSS_FILES': [
		'css/custom.css',
		'css/theme.css',
	],
	'CUSTOM_JS_FILES': [
		'js/custom.js',
		'js/plugins.js',
	],
}
```

### Настройки CDN

```python
METROUI5 = {
	'CDN_MODE': True,
	'CDN_URL': 'https://cdn.metroui.org.ua/current',
	'THEME': 'default',
}
```

## Работа с рендерерами

### Кастомный рендерер формы

```python
from metroui5.renderers import get_form_renderer


def custom_form_view(request):
	form = MyForm()

	# Получаем кастомный рендерер
	renderer = get_form_renderer(
		form,
		layout='horizontal',
		label_class='custom-label',
		field_class='custom-field'
	)

	form_html = renderer.render()
	return render(request, 'form.html', {'form': form_html})
```

### Рендерер поля

```python
from metroui5.renderers import get_field_renderer


def field_view(request):
	form = MyForm()
	field = form['username']

	# Рендерим поле с кастомными настройками
	renderer = get_field_renderer(
		field,
		widget_class='custom-input',
		help_text_class='custom-help'
	)

	field_html = renderer.render()
	return render(request, 'field.html', {'field': field_html})
```

## Лучшие практики

### 1. Используйте базовый шаблон

Всегда создавайте базовый шаблон с подключенными ресурсами MetroUI5.

### 2. Группируйте компоненты

```python
# Хорошо
context = {
	'header_components': {
		'alert': render_alert("Сообщение", "info"),
		'breadcrumb': render_breadcrumb(breadcrumb_items),
	},
	'main_components': {
		'card': render_card(...),
		'table': render_table(...),
	}
}
```

### 3. Используйте константы для повторяющихся значений

```python
# settings.py
METROUI5_DEFAULT_BUTTON_CLASS = "btn btn-primary"

# views.py
from django.conf import settings

button = render_button(
	"Текст",
	**{"class": settings.METROUI5_DEFAULT_BUTTON_CLASS}
)
```

### 4. Обрабатывайте ошибки

```python
try:
	component_html = render_component(...)
except Exception as e:
	# Логирование ошибки
	logger.error(f"Ошибка рендеринга компонента: {e}")
	component_html = "<div>Ошибка загрузки компонента</div>"
```

## Отладка

### Проверка загруженных ресурсов

В браузере проверьте:

1. **Network** вкладка - CSS и JS файлы загружены
2. **Console** - нет ошибок JavaScript
3. **Elements** - CSS классы применяются

### Логирование

```python
import logging

logger = logging.getLogger(__name__)


def debug_view(request):
	logger.debug("Рендеринг компонента")
	component = render_component(...)
	logger.debug(f"Компонент создан: {component}")
	return render(request, 'debug.html', {'component': component})
```

## Следующие шаги

Теперь, когда вы освоили базовое использование:

1. Изучите [примеры](examples.md) для более сложных сценариев
2. Ознакомьтесь с доступными [компонентами](../components/)
3. Изучите [API справочник](../api-reference/) для детальной информации
4. Создайте свой первый проект с MetroUI5!
