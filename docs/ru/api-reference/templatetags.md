# Теги шаблонов

Справочник API для тегов шаблонов MetroUI5 Django.

## Обзор

Модуль `templatetags` содержит теги шаблонов Django для подключения ресурсов и компонентов MetroUI5 в шаблонах.

## Загрузка тегов

В начале каждого шаблона загрузите теги MetroUI5:

```html
{% load metroui5 %}
```

## Доступные теги

### `{% metroui5_css %}`

Подключает CSS файлы MetroUI5.

#### Использование

```html
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>{% block title %}Заголовок{% endblock %}</title>

	{% metroui5_css %}
</head>
```

#### Результат

```html
<link
	href="/static/metroui5/css/metro.all.css"
	rel="stylesheet"
	type="text/css"
/>
```

#### Параметры

Этот тег не принимает параметры.

### `{% metroui5_javascript %}`

Подключает JavaScript файлы MetroUI5.

#### Использование

```html
<body>
	<div class="container">{% block content %} {% endblock %}</div>

	{% metroui5_javascript %}
</body>
```

#### Результат

```html
<script src="/static/metroui5/js/metro.all.js"></script>
```

#### Параметры

Этот тег не принимает параметры.

### `{% metroui5_icons %}`

Подключает CSS файл иконок MetroUI5.

#### Использование

```html
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>{% block title %}Заголовок{% endblock %}</title>

	{% metroui5_css %} {% metroui5_icons %}
</head>
```

#### Результат

```html
<link
	href="/static/metroui5/icons/icons.css"
	rel="stylesheet"
	type="text/css"
/>
```

#### Параметры

Этот тег не принимает параметры.

### `{% metroui5_theme %}`

Подключает тему MetroUI5 (если настроена).

#### Использование

```html
<head>
	{% metroui5_css %} {% metroui5_theme %}
</head>
```

#### Результат

```html
<link
	href="/static/metroui5/themes/dark.css"
	rel="stylesheet"
	type="text/css"
/>
```

#### Параметры

Этот тег не принимает параметры.

## Полный базовый шаблон

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{% block title %}Заголовок{% endblock %}</title>

		{% metroui5_css %} {% metroui5_icons %} {% metroui5_theme %} {% block
		extra_css %}{% endblock %}
	</head>
	<body>
		<div class="container">{% block content %} {% endblock %}</div>

		{% metroui5_javascript %} {% block extra_js %}{% endblock %}
	</body>
</html>
```

## Расширенные возможности

### Подключение пользовательских CSS файлов

```html
{% load metroui5 %}

<head>
	{% metroui5_css %}

	<!-- Пользовательские CSS файлы -->
	<link href="{% static 'css/custom.css' %}" rel="stylesheet" type="text/css" />
	<link href="{% static 'css/theme.css' %}" rel="stylesheet" type="text/css" />
</head>
```

### Подключение пользовательских JavaScript файлов

```html
{% load metroui5 %}

<body>
	<!-- Основной контент -->
	{% block content %}{% endblock %} {% metroui5_javascript %}

	<!-- Пользовательские JavaScript файлы -->
	<script src="{% static 'js/custom.js' %}"></script>
	<script src="{% static 'js/plugins.js' %}"></script>
</body>
```

### Условное подключение ресурсов

```html
{% load metroui5 %}

<head>
	{% metroui5_css %} {% if debug %}
	<!-- Дополнительные стили для разработки -->
	<link href="{% static 'css/debug.css' %}" rel="stylesheet" type="text/css" />
	{% endif %} {% if user.is_authenticated %}
	<!-- Стили для аутентифицированных пользователей -->
	<link href="{% static 'css/user.css' %}" rel="stylesheet" type="text/css" />
	{% endif %}
</head>
```

## Настройка через settings.py

### Базовые настройки

```python
# settings.py

METROUI5 = {
	'CDN_MODE': False,  # Использовать локальные файлы
	'THEME': 'default',  # Тема по умолчанию
	'VERSION': '5.0.0',  # Версия MetroUI
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

### Пользовательские файлы

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

## Лучшие практики

### 1. Размещайте CSS в `<head>`

```html
<!-- Хорошо -->
<head>
	{% metroui5_css %} {% metroui5_icons %}
</head>

<!-- Плохо -->
<body>
	{% metroui5_css %} {% metroui5_icons %}
</body>
```

### 2. Размещайте JavaScript перед закрывающим `</body>`

```html
<!-- Хорошо -->
<body>
	<!-- Контент -->
	{% metroui5_javascript %}
</body>

<!-- Плохо -->
<head>
	{% metroui5_javascript %}
</head>
```

### 3. Используйте блоки для дополнительных ресурсов

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{% block title %}Заголовок{% endblock %}</title>

		{% metroui5_css %} {% metroui5_icons %} {% block extra_css %}{% endblock %}
	</head>
	<body>
		{% block content %}{% endblock %} {% metroui5_javascript %} {% block
		extra_js %}{% endblock %}
	</body>
</html>
```

### 4. Переопределяйте блоки в дочерних шаблонах

```html
<!-- base.html -->
{% block extra_css %}{% endblock %}

<!-- child.html -->
{% extends 'base.html' %} {% block extra_css %}
<link
	href="{% static 'css/page-specific.css' %}"
	rel="stylesheet"
	type="text/css"
/>
{% endblock %}
```

## Устранение неполадок

### Теги не загружаются

1. Убедитесь, что `metroui5` добавлен в `INSTALLED_APPS`
2. Проверьте, что `{% load metroui5 %}` указан в начале шаблона
3. Перезапустите сервер Django

### Ресурсы не загружаются

1. Проверьте настройки `METROUI5` в `settings.py`
2. Убедитесь, что статические файлы настроены правильно
3. Запустите `python manage.py collectstatic`

### Ошибки в консоли браузера

1. Проверьте, что все теги загружены в правильном порядке
2. Убедитесь, что нет конфликтов с другими CSS/JS файлами
3. Проверьте вкладку Network в DevTools

## Тестирование

### Модульные тесты

```python
from django.test import TestCase
from django.template import Template, Context


class TemplateTagsTestCase(TestCase):

	def test_metroui5_css_tag(self):
		"""Тест тега metroui5_css"""
		template = Template('{% load metroui5 %}{% metroui5_css %}')
		context = Context({})
		result = template.render(context)

		self.assertIn('metro.all.css', result)
		self.assertIn('rel="stylesheet"', result)

	def test_metroui5_javascript_tag(self):
		"""Тест тега metroui5_javascript"""
		template = Template('{% load metroui5 %}{% metroui5_javascript %}')
		context = Context({})
		result = template.render(context)

		self.assertIn('metro.all.js', result)
		self.assertIn('<script', result)

	def test_metroui5_icons_tag(self):
		"""Тест тега metroui5_icons"""
		template = Template('{% load metroui5 %}{% metroui5_icons %}')
		context = Context({})
		result = template.render(context)

		self.assertIn('icons.css', result)
		self.assertIn('rel="stylesheet"', result)
```

### Интеграционные тесты

```python
from django.test import TestCase, Client
from django.urls import reverse


class TemplateTagsIntegrationTestCase(TestCase):

	def setUp(self):
		self.client = Client()

	def test_base_template_renders(self):
		"""Тест рендеринга базового шаблона"""
		response = self.client.get(reverse('home'))

		# Проверка подключения CSS
		self.assertContains(response, 'metro.all.css')

		# Проверка подключения JavaScript
		self.assertContains(response, 'metro.all.js')

		# Проверка подключения иконок
		self.assertContains(response, 'icons.css')
```

## Связанные модули

- [Основные функции](core.md) - для получения настроек
- [HTML утилиты](html.md) - для генерации HTML
- [Компоненты](components.md) - для рендеринга UI

## Следующие шаги

Теперь, когда вы освоили теги шаблонов:

1. Изучите [основные функции](core.md) для понимания настроек
2. Ознакомьтесь с [HTML утилитами](html.md) для генерации HTML
3. Изучите [компоненты](components.md) для создания UI
4. Создайте свои собственные теги шаблонов для конкретных задач!
