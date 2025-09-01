# Использование компонентов MetroUI5 в шаблонах Django

Это руководство показывает, как эффективно использовать компоненты MetroUI5 в шаблонах Django, включая как теги шаблонов, так и подходы на основе представлений.

## Теги шаблонов против компонентов на основе представлений

MetroUI5 предоставляет два основных способа использования компонентов в Django:

1. **Теги шаблонов** - Использование компонентов непосредственно в шаблонах
2. **На основе представлений** - Создание компонентов в представлениях и передача в шаблоны

## Подход с тегами шаблонов

### Базовое использование

```html
{% load metroui5 %}

<!-- Базовое уведомление -->
{% metroui5_alert "Добро пожаловать в наше приложение!" alert_type="success" %}

<!-- Кнопка с иконкой -->
{% metroui5_button "Сохранить изменения" button_type="primary" icon="checkmark"
%}

<!-- Иконка -->
{% metroui5_icon "home" size="2x" %}
```

### Примеры тегов шаблонов

#### Уведомления

```html
{% load metroui5 %}

<!-- Уведомление об успехе -->
{% metroui5_alert "Операция успешно завершена!" alert_type="success"
dismissible=True %}

<!-- Предупреждающее уведомление -->
{% metroui5_alert "Пожалуйста, проверьте ваш ввод" alert_type="warning" %}

<!-- Уведомление об ошибке -->
{% metroui5_alert "Произошла ошибка" alert_type="danger" dismissible=True %}
```

#### Кнопки

```html
{% load metroui5 %}

<!-- Основная кнопка -->
{% metroui5_button "Отправить" button_type="primary" %}

<!-- Кнопка с иконкой -->
{% metroui5_button "Скачать" button_type="success" icon="download" %}

<!-- Контурная кнопка -->
{% metroui5_button "Отмена" button_type="secondary" outline=True %}
```

#### Иконки

```html
{% load metroui5 %}

<!-- Базовая иконка -->
{% metroui5_icon "user" %}

<!-- Иконка с размером -->
{% metroui5_icon "mail" size="3x" %}

<!-- Иконка с пользовательскими классами -->
{% metroui5_icon "heart" class="icon-red" %}
```

## Подход на основе представлений

### Создание компонентов в представлениях

```python
# views.py
from metroui5.components import render_alert, render_button
from metroui5.templatetags.metroui5 import metroui5_icon

def dashboard_view(request):
    # Создание уведомлений
    welcome_alert = render_alert(
        "Добро пожаловать обратно, {}!".format(request.user.first_name),
        alert_type="success",
        dismissible=True
    )

    # Создание кнопок
    save_button = render_button(
        "Сохранить настройки",
        button_type="primary",
        icon="checkmark"
    )

    # Создание иконок
    user_icon = metroui5_icon("user", size="2x", class="icon-primary")

    context = {
        'welcome_alert': welcome_alert,
        'save_button': save_button,
        'user_icon': user_icon,
    }
    return render(request, 'dashboard.html', context)
```

### Использование в шаблонах

```html
<!-- dashboard.html -->
{% load metroui5 %} {% block content %}
<!-- Отображение уведомления -->
{{ welcome_alert|safe }}

<!-- Отображение кнопки -->
{{ save_button|safe }}

<!-- Отображение иконки -->
{{ user_icon|safe }} {% endblock %}
```

## Расширенные паттерны

### Условные компоненты

```python
# views.py
def profile_view(request):
    components = []

    # Добавление уведомлений на основе статуса пользователя
    if not request.user.email_verified:
        components.append(render_alert(
            "Пожалуйста, подтвердите ваш email адрес",
            alert_type="warning",
            dismissible=True
        ))

    if request.user.is_new:
        components.append(render_alert(
            "Завершите настройку вашего профиля",
            alert_type="info",
            dismissible=True
        ))

    # Добавление кнопок действий
    action_buttons = [
        render_button("Редактировать профиль", button_type="primary", icon="edit"),
        render_button("Изменить пароль", button_type="secondary", icon="key"),
    ]

    context = {
        'alerts': components,
        'action_buttons': action_buttons,
    }
    return render(request, 'profile.html', context)
```

```html
<!-- profile.html -->
{% load metroui5 %} {% block content %}
<!-- Отображение условных уведомлений -->
{% for alert in alerts %} {{ alert|safe }} {% endfor %}

<!-- Отображение кнопок действий -->
<div class="button-group">
	{% for button in action_buttons %} {{ button|safe }} {% endfor %}
</div>
{% endblock %}
```

### Динамические списки компонентов

```python
# views.py
def navigation_view(request):
    nav_items = [
        {
            "text": "Панель управления",
            "icon": metroui5_icon("dashboard"),
            "url": "/dashboard/",
            "active": request.path == "/dashboard/"
        },
        {
            "text": "Пользователи",
            "icon": metroui5_icon("users"),
            "url": "/users/",
            "active": request.path.startswith("/users/")
        },
        {
            "text": "Настройки",
            "icon": metroui5_icon("cog"),
            "url": "/settings/",
            "active": request.path.startswith("/settings/")
        },
    ]

    context = {'nav_items': nav_items}
    return render(request, 'navigation.html', context)
```

```html
<!-- navigation.html -->
{% load metroui5 %}

<nav class="nav nav-horizontal">
	{% for item in nav_items %}
	<a
		href="{{ item.url }}"
		class="nav-item {% if item.active %}active{% endif %}"
	>
		{{ item.icon|safe }} {{ item.text }}
	</a>
	{% endfor %}
</nav>
```

### Компоненты форм

```python
# views.py
def form_view(request):
    if request.method == 'POST':
        # Обработка формы
        submit_button = render_button(
            "Обработка...",
            button_type="primary",
            disabled=True
        )
        status_alert = render_alert(
            "Форма успешно отправлена!",
            alert_type="success"
        )
    else:
        submit_button = render_button(
            "Отправить форму",
            button_type="primary",
            icon="checkmark"
        )
        status_alert = None

    context = {
        'submit_button': submit_button,
        'status_alert': status_alert,
    }
    return render(request, 'form.html', context)
```

```html
<!-- form.html -->
{% load metroui5 %} {% block content %} {% if status_alert %} {{
status_alert|safe }} {% endif %}

<form method="post">
	<!-- Поля формы -->
	<div class="form-group">
		<label>Имя:</label>
		<input type="text" name="name" class="input" required />
	</div>

	<div class="form-group">
		<label>Email:</label>
		<input type="email" name="email" class="input" required />
	</div>

	<!-- Кнопка отправки -->
	<div class="form-actions">
		{{ submit_button|safe }} {% metroui5_button "Сброс" button_type="secondary"
		type="reset" %}
	</div>
</form>
{% endblock %}
```

### Смешивание компонентов

```python
# views.py
def mixed_components_view(request):
    # Смешивание тегов шаблонов и компонентов на основе представлений
    view_alert = render_alert(
        "Это уведомление было создано в представлении",
        alert_type="info"
    )

    view_button = render_button(
        "Кнопка представления",
        button_type="primary"
    )

    context = {
        'view_alert': view_alert,
        'view_button': view_button,
    }
    return render(request, 'mixed.html', context)
```

```html
<!-- mixed.html -->
{% load metroui5 %} {% block content %}
<!-- Компоненты на основе представлений -->
{{ view_alert|safe }} {{ view_button|safe }}

<!-- Компоненты тегов шаблонов -->
{% metroui5_alert "Это уведомление было создано с помощью тегов шаблонов"
alert_type="success" %} {% metroui5_button "Кнопка шаблона"
button_type="secondary" %}

<!-- Смешивание обоих подходов -->
<div class="component-group">
	{{ view_alert|safe }} {% metroui5_button "Кнопка тега шаблона"
	button_type="info" %}
</div>
{% endblock %}
```

## Лучшие практики

### 1. Выбор правильного подхода

**Используйте теги шаблонов когда:**

- Компоненты статичны или просты
- Вы хотите сохранить логику в шаблонах
- Компоненты не зависят от сложной логики представлений

**Используйте подход на основе представлений когда:**

- Компоненты зависят от данных пользователя или разрешений
- Вам нужна условная логика
- Компоненты являются частью сложной бизнес-логики

### 2. Последовательная стилизация

```python
# views.py
def consistent_styling_view(request):
    # Использование последовательной стилизации кнопок
    primary_buttons = [
        render_button("Сохранить", button_type="primary", icon="checkmark"),
        render_button("Обновить", button_type="primary", icon="edit"),
        render_button("Создать", button_type="primary", icon="plus"),
    ]

    # Использование последовательной стилизации уведомлений
    alerts = [
        render_alert("Сообщение об успехе", alert_type="success"),
        render_alert("Предупреждающее сообщение", alert_type="warning"),
        render_alert("Сообщение об ошибке", alert_type="danger"),
    ]

    context = {
        'primary_buttons': primary_buttons,
        'alerts': alerts,
    }
    return render(request, 'consistent.html', context)
```

### 3. Переиспользование компонентов

```python
# utils.py
from metroui5.components import render_alert, render_button
from metroui5.templatetags.metroui5 import metroui5_icon

def create_status_alert(status, message):
    """Создание последовательных уведомлений о статусе."""
    status_map = {
        'success': 'success',
        'error': 'danger',
        'warning': 'warning',
        'info': 'info'
    }

    return render_alert(
        message,
        alert_type=status_map.get(status, 'info'),
        dismissible=True
    )

def create_action_button(text, action_type, icon=None):
    """Создание последовательных кнопок действий."""
    type_map = {
        'save': 'primary',
        'delete': 'danger',
        'edit': 'info',
        'cancel': 'secondary'
    }

    return render_button(
        text,
        button_type=type_map.get(action_type, 'default'),
        icon=icon
    )
```

```python
# views.py
from .utils import create_status_alert, create_action_button

def reusable_components_view(request):
    alerts = [
        create_status_alert('success', 'Операция завершена'),
        create_status_alert('warning', 'Пожалуйста, проверьте ваши данные'),
    ]

    buttons = [
        create_action_button('Сохранить', 'save', 'checkmark'),
        create_action_button('Удалить', 'delete', 'delete'),
        create_action_button('Редактировать', 'edit', 'edit'),
    ]

    context = {
        'alerts': alerts,
        'buttons': buttons,
    }
    return render(request, 'reusable.html', context)
```

### 4. Соображения производительности

```python
# views.py
def performance_view(request):
    # Кэширование часто используемых компонентов
    if not hasattr(request, '_cached_components'):
        request._cached_components = {
            'user_icon': metroui5_icon("user", class="nav-icon"),
            'home_icon': metroui5_icon("home", class="nav-icon"),
            'settings_icon': metroui5_icon("cog", class="nav-icon"),
        }

    context = {
        'cached_icons': request._cached_components,
    }
    return render(request, 'performance.html', context)
```

## Общие паттерны

### 1. Панель управления с множественными компонентами

```python
# views.py
def dashboard_view(request):
    # Уведомления о статусе
    alerts = []
    if request.user.is_new:
        alerts.append(render_alert(
            "Добро пожаловать! Завершите ваш профиль.",
            alert_type="info",
            dismissible=True
        ))

    # Кнопки действий
    action_buttons = [
        render_button("Новый проект", button_type="primary", icon="plus"),
        render_button("Импорт данных", button_type="secondary", icon="upload"),
    ]

    # Иконки навигации
    nav_icons = {
        'dashboard': metroui5_icon("dashboard", class="nav-icon"),
        'projects': metroui5_icon("folder", class="nav-icon"),
        'settings': metroui5_icon("cog", class="nav-icon"),
    }

    context = {
        'alerts': alerts,
        'action_buttons': action_buttons,
        'nav_icons': nav_icons,
    }
    return render(request, 'dashboard.html', context)
```

### 2. Форма с динамическими компонентами

```python
# views.py
def dynamic_form_view(request):
    form_data = request.POST if request.method == 'POST' else {}

    # Динамическая кнопка отправки на основе состояния формы
    if form_data:
        submit_button = render_button(
            "Сохранение...",
            button_type="primary",
            disabled=True
        )
    else:
        submit_button = render_button(
            "Сохранить изменения",
            button_type="primary",
            icon="checkmark"
        )

    # Динамические уведомления на основе валидации формы
    alerts = []
    if 'email' in form_data and '@' not in form_data['email']:
        alerts.append(render_alert(
            "Пожалуйста, введите корректный email адрес",
            alert_type="danger"
        ))

    context = {
        'submit_button': submit_button,
        'alerts': alerts,
    }
    return render(request, 'dynamic_form.html', context)
```

Это комплексное руководство показывает, как эффективно использовать компоненты MetroUI5 в шаблонах Django, охватывая как теги шаблонов, так и подходы на основе представлений с практическими примерами и лучшими практиками.
