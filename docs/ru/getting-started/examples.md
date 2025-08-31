# Примеры

Практические примеры использования MetroUI5 Django в различных сценариях.

## Простая страница

### Представление

```python
from django.shortcuts import render
from metroui5.components import render_alert, render_button, render_card


def simple_page(request):
	context = {
		'welcome_alert': render_alert(
			"Добро пожаловать на нашу страницу!",
			alert_type="info"
		),
		'action_buttons': [
			render_button("Основная кнопка", button_type="primary"),
			render_button("Вторичная кнопка", button_type="secondary"),
			render_button("Успех", button_type="success"),
		],
		'info_card': render_card(
			header="Информация",
			content="Это простая карточка с информацией о проекте.",
			footer="Создано с MetroUI5 Django"
		)
	}
	return render(request, 'simple_page.html', context)
```

### Шаблон

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }}

<div class="row">
    <div class="cell-md-8">{{ info_card|safe }}</div>
    <div class="cell-md-4">
        <h3>Действия</h3>
        {% for button in action_buttons %}
        <div class="mb-2">{{ button|safe }}</div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

## Панель управления

### Представление

```python
from metroui5.components import (
	render_card, render_table, render_progress,
	render_badge, render_tile
)


def dashboard(request):
	# Статистика
	stats = [
		{'label': 'Пользователи', 'value': '1,234', 'color': 'blue'},
		{'label': 'Заказы', 'value': '567', 'color': 'green'},
		{'label': 'Доход', 'value': '$12,345', 'color': 'orange'},
		{'label': 'Товары', 'value': '89', 'color': 'red'},
	]

	# Последние заказы
	recent_orders = [
		['#1234', 'Иван Иванов', 'Продукт A', '$100', 'Обработан'],
		['#1235', 'Петр Петров', 'Продукт B', '$200', 'В пути'],
		['#1236', 'Сидор Сидоров', 'Продукт C', '$150', 'Доставлен'],
	]

	# Прогресс задач
	tasks = [
		{'name': 'Разработка', 'progress': 75, 'color': 'blue'},
		{'name': 'Тестирование', 'progress': 45, 'color': 'green'},
		{'name': 'Документация', 'progress': 90, 'color': 'orange'},
	]

	context = {
		'stats_tiles': [
			render_tile(
				title=stat['label'],
				content=stat['value'],
				color=stat['color'],
				size="small"
			) for stat in stats
		],
		'stats_card': render_card(
			header="Статистика",
			content="<div class='row'>" +
					"".join([f"<div class='cell-md-3'>{tile}</div>" for tile in context['stats_tiles']]) +
					"</div>"
		),
		'orders_table': render_table(
			headers=['Номер', 'Клиент', 'Товар', 'Сумма', 'Статус'],
			rows=recent_orders
		),
		'tasks_progress': [
			render_progress(
				value=task['progress'],
				color=task['color'],
				**{"data-label": task['name']}
			) for task in tasks
		]
	}

	return render(request, 'dashboard.html', context)
```

### Шаблон

```html
{% extends 'base.html' %} {% block content %}
<h1>Панель управления</h1>

{{ stats_card|safe }}

<div class="row">
    <div class="cell-md-8">
        <h3>Последние заказы</h3>
        {{ orders_table|safe }}
    </div>
    <div class="cell-md-4">
        <h3>Прогресс задач</h3>
        {% for progress in tasks_progress %} {{ progress|safe }}
        <br/>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

## Форма с валидацией

### Форма

```python
from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'})
	)
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'placeholder': 'Введите email'})
	)
	subject = forms.CharField(
		max_length=200,
		widget=forms.TextInput(attrs={'placeholder': 'Тема сообщения'})
	)
	message = forms.CharField(
		widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'rows': 5})
	)
```

### Представление

```python
from metroui5.forms import render_form, render_form_errors
from metroui5.components import render_alert, render_button


def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Обработка формы
			success_alert = render_alert(
				"Сообщение успешно отправлено!",
				alert_type="success"
			)
			return render(request, 'contact_success.html', {
				'alert': success_alert
			})
	else:
		form = ContactForm()

	# Рендерим форму с MetroUI5 стилями
	form_html = render_form(
		form,
		layout='horizontal',
		submit_text="Отправить сообщение",
		submit_class="btn btn-primary"
	)

	return render(request, 'contact_form.html', {'form': form_html})
```

### Шаблон

```html
{% extends 'base.html' %} {% block content %}
<div class="row">
    <div class="cell-md-8">
        <h2>Свяжитесь с нами</h2>
        {{ form|safe }}
    </div>
    <div class="cell-md-4">
        <h3>Контактная информация</h3>
        <p><strong>Email:</strong> info@example.com</p>
        <p><strong>Телефон:</strong> +7 (123) 456-78-90</p>
        <p><strong>Адрес:</strong> ул. Примерная, 123</p>
    </div>
</div>
{% endblock %}
```

## Навигационное меню

### Представление

```python
from metroui5.components import render_navigation, render_breadcrumb


def navigation_example(request):
	# Основное меню
	nav_items = [
		{'text': 'Главная', 'url': '/', 'icon': 'home'},
		{'text': 'О нас', 'url': '/about/', 'icon': 'info'},
		{'text': 'Услуги', 'url': '/services/', 'icon': 'cog'},
		{'text': 'Контакты', 'url': '/contact/', 'icon': 'mail'},
	]

	# Хлебные крошки
	breadcrumb_items = [
		{'text': 'Главная', 'url': '/'},
		{'text': 'Услуги', 'url': '/services/'},
		{'text': 'Веб-разработка', 'url': None},
	]

	context = {
		'main_navigation': render_navigation(nav_items),
		'breadcrumbs': render_breadcrumb(breadcrumb_items),
	}

	return render(request, 'navigation_example.html', context)
```

### Шаблон

```html
{% extends 'base.html' %} {% block content %} {{ breadcrumbs|safe }}

<div class="row">
    <div class="cell-md-3">{{ main_navigation|safe }}</div>
    <div class="cell-md-9">
        <h1>Веб-разработка</h1>
        <p>Содержимое страницы...</p>
    </div>
</div>
{% endblock %}
```

## Модальное окно

### Представление

```python
from metroui5.components import render_modal, render_button


def modal_example(request):
	# Кнопка для открытия модального окна
	open_button = render_button(
		"Открыть модальное окно",
		button_type="primary",
		**{"data-role": "button", "data-toggle": "modal", "data-target": "#exampleModal"}
	)

	# Модальное окно
	modal = render_modal(
		title="Пример модального окна",
		content="""
            <p>Это содержимое модального окна.</p>
            <p>Вы можете добавить любую разметку HTML.</p>
        """,
		modal_id="exampleModal"
	)

	context = {
		'open_button': open_button,
		'modal': modal,
	}

	return render(request, 'modal_example.html', context)
```

### Шаблон

```html
{% extends 'base.html' %} {% block content %}
<h1>Пример модального окна</h1>

{{ open_button|safe }} {{ modal|safe }} {% endblock %}
```

## Таблица с данными

### Представление

```python
from metroui5.components import render_table, render_button, render_badge


def table_example(request):
	# Данные для таблицы
	users = [
		{
			'id': 1,
			'name': 'Иван Иванов',
			'email': 'ivan@example.com',
			'status': 'Активен',
			'actions': 'Действия'
		},
		{
			'id': 2,
			'name': 'Петр Петров',
			'email': 'petr@example.com',
			'status': 'Неактивен',
			'actions': 'Действия'
		},
		{
			'id': 3,
			'name': 'Сидор Сидоров',
			'email': 'sidor@example.com',
			'status': 'Активен',
			'actions': 'Действия'
		},
	]

	# Преобразуем данные для таблицы
	table_rows = []
	for user in users:
		status_badge = render_badge(
			user['status'],
			badge_type="success" if user['status'] == 'Активен' else "alert"
		)

		action_buttons = [
			render_button("Редактировать", button_type="secondary", size="small"),
			render_button("Удалить", button_type="alert", size="small"),
		]

		row = [
			user['id'],
			user['name'],
			user['email'],
			status_badge,
			" ".join([btn for btn in action_buttons])
		]
		table_rows.append(row)

	context = {
		'users_table': render_table(
			headers=['ID', 'Имя', 'Email', 'Статус', 'Действия'],
			rows=table_rows,
			**{"class": "table-border"}
		)
	}

	return render(request, 'table_example.html', context)
```

### Шаблон

```html
{% extends 'base.html' %} {% block content %}
<h1>Пользователи</h1>

{{ users_table|safe }} {% endblock %}
```

## Комбинированный пример

### Представление

```python
from metroui5.components import *
from metroui5.forms import render_form


def comprehensive_example(request):
	# Создаем комплексную страницу с различными компонентами

	# Алерт
	welcome_alert = render_alert(
		"Добро пожаловать в комплексный пример MetroUI5!",
		alert_type="success",
		dismissible=True
	)

	# Карточки с информацией
	info_cards = [
		render_card(
			header="Статистика",
			content="<p>Общее количество пользователей: <strong>1,234</strong></p>",
			footer="Обновлено сегодня"
		),
		render_card(
			header="Быстрые действия",
			content="<p>Выберите действие для продолжения работы</p>",
			footer="Доступно 24/7"
		),
	]

	# Кнопки действий
	action_buttons = [
		render_button("Создать", button_type="primary", icon="plus"),
		render_button("Редактировать", button_type="secondary", icon="edit"),
		render_button("Удалить", button_type="alert", icon="trash"),
	]

	# Прогресс-бары
	progress_bars = [
		render_progress(75, color="blue", **{"data-label": "Задача 1"}),
		render_progress(45, color="green", **{"data-label": "Задача 2"}),
		render_progress(90, color="orange", **{"data-label": "Задача 3"}),
	]

	# Плитки
	tiles = [
		render_tile("Пользователи", "1,234", "blue", "medium", "users"),
		render_tile("Заказы", "567", "green", "medium", "cart"),
		render_tile("Доход", "$12,345", "orange", "medium", "dollar"),
	]

	context = {
		'welcome_alert': welcome_alert,
		'info_cards': info_cards,
		'action_buttons': action_buttons,
		'progress_bars': progress_bars,
		'tiles': tiles,
	}

	return render(request, 'comprehensive_example.html', context)
```

### Шаблон

```html
{% extends 'base.html' %} {% block content %} {{ welcome_alert|safe }}

<div class="row">
    <div class="cell-md-8">
        <h2>Информация</h2>
        {% for card in info_cards %} {{ card|safe }}
        <br/>
        {% endfor %}

        <h3>Прогресс задач</h3>
        {% for progress in progress_bars %} {{ progress|safe }}
        <br/>
        {% endfor %}
    </div>

    <div class="cell-md-4">
        <h3>Быстрые действия</h3>
        {% for button in action_buttons %}
        <div class="mb-2">{{ button|safe }}</div>
        {% endfor %}

        <h3>Статистика</h3>
        <div class="row">
            {% for tile in tiles %}
            <div class="cell-md-4">{{ tile|safe }}</div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}
```

## Следующие шаги

Эти примеры демонстрируют основные возможности MetroUI5 Django. Для более детального изучения:

1. Изучите [компоненты](../components/) для понимания всех доступных возможностей
2. Ознакомьтесь с [API справочником](../api-reference/) для детальной информации
3. Создайте свой собственный проект, используя эти примеры как основу
4. Экспериментируйте с различными комбинациями компонентов
