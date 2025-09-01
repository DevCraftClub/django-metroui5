# Иконки

MetroUI5 Django предоставляет комплексную систему иконок, используя встроенный шрифт иконок MetroUI, позволяя легко добавлять иконки по всему приложению.

## Базовое использование

```python
from metroui5.templatetags.metroui5 import metroui5_icon

# Простая иконка
icon_html = metroui5_icon("home")
```

## Результат рендеринга

### Базовая иконка

```html
<!-- Ввод -->
metroui5_icon("home")

<!-- Вывод -->
<span class="mif home"></span>
```

### Иконка с размером

```html
<!-- Ввод -->
metroui5_icon("user", size="2x")

<!-- Вывод -->
<span class="mif user mif-2x"></span>
```

### Иконка с пользовательскими классами

```html
<!-- Ввод -->
metroui5_icon("mail", class="icon-primary", id="mail-icon")

<!-- Вывод -->
<span class="mif mail icon-primary" id="mail-icon"></span>
```

## Использование в шаблонах

```html
{% load metroui5 %}

<!-- Базовая иконка -->
{% metroui5_icon "home" %}

<!-- Иконка с размером -->
{% metroui5_icon "user" size="2x" %}

<!-- Иконка с пользовательскими атрибутами -->
{% metroui5_icon "mail" class="icon-primary" id="mail-icon" %}
```

## Параметры

### `metroui5_icon(icon_name, size=None, **kwargs)`

- **icon_name** (str): Название иконки MetroUI
- **size** (str, optional): Размер иконки (1x, 2x, 3x, 4x, 5x)
- **kwargs**: Дополнительные HTML атрибуты

## Примеры

### Базовые иконки

```html
{% load metroui5 %}

<!-- Навигационные иконки -->
{% metroui5_icon "home" %} {% metroui5_icon "user" %} {% metroui5_icon
"settings" %} {% metroui5_icon "mail" %} {% metroui5_icon "phone" %}
```

### Иконки с размерами

```html
<!-- Разные размеры -->
{% metroui5_icon "star" size="1x" %} {% metroui5_icon "star" size="2x" %} {%
metroui5_icon "star" size="3x" %} {% metroui5_icon "star" size="4x" %} {%
metroui5_icon "star" size="5x" %}
```

### Иконки с пользовательским стилем

```html
<!-- Иконки с пользовательскими классами -->
{% metroui5_icon "heart" class="icon-red" %} {% metroui5_icon "checkmark"
class="icon-green" %} {% metroui5_icon "warning" class="icon-yellow" %} {%
metroui5_icon "info" class="icon-blue" %}
```

## CSS классы иконок MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации иконок:

### Классы размеров

- `mif-1x` - размер 1x (по умолчанию)
- `mif-2x` - размер 2x
- `mif-Nx` - размер Nx (число вместо N)
- `mif-10x` - размер 10x (максимальный размер)

### Классы цветов

- `icon-primary` - Основной цвет
- `icon-secondary` - Вторичный цвет
- `icon-success` - Цвет успеха (зеленый)
- `icon-warning` - Цвет предупреждения (желтый)
- `icon-danger` - Цвет опасности (красный)
- `icon-info` - Информационный цвет (синий)
- `icon-light` - Светлый цвет
- `icon-dark` - Темный цвет

### Классы стилей

- `icon-spin` - Анимация вращения
- `icon-pulse` - Анимация пульсации
- `icon-bounce` - Анимация подпрыгивания
- `icon-flip` - Анимация переворота

## Общие категории иконок

### Навигационные иконки

```html
{% load metroui5 %}

<!-- Основная навигация -->
{% metroui5_icon "home" %} {% metroui5_icon "dashboard" %} {% metroui5_icon
"menu" %} {% metroui5_icon "back" %} {% metroui5_icon "forward" %} {%
metroui5_icon "up" %} {% metroui5_icon "down" %} {% metroui5_icon "left" %} {%
metroui5_icon "right" %}
```

### Иконки пользовательского интерфейса

```html
<!-- Элементы UI -->
{% metroui5_icon "user" %} {% metroui5_icon "users" %} {% metroui5_icon
"settings" %} {% metroui5_icon "cog" %} {% metroui5_icon "gear" %} {%
metroui5_icon "search" %} {% metroui5_icon "filter" %} {% metroui5_icon "sort"
%}
```

### Иконки связи

```html
<!-- Связь -->
{% metroui5_icon "mail" %} {% metroui5_icon "phone" %} {% metroui5_icon "chat"
%} {% metroui5_icon "comment" %} {% metroui5_icon "bell" %} {% metroui5_icon
"notification" %}
```

### Иконки файлов и документов

```html
<!-- Файлы и документы -->
{% metroui5_icon "file" %} {% metroui5_icon "folder" %} {% metroui5_icon
"download" %} {% metroui5_icon "upload" %} {% metroui5_icon "attachment" %} {%
metroui5_icon "document" %} {% metroui5_icon "image" %} {% metroui5_icon "video"
%}
```

### Иконки действий

```html
<!-- Действия -->
{% metroui5_icon "plus" %} {% metroui5_icon "minus" %} {% metroui5_icon "edit"
%} {% metroui5_icon "delete" %} {% metroui5_icon "save" %} {% metroui5_icon
"copy" %} {% metroui5_icon "cut" %} {% metroui5_icon "paste" %}
```

### Иконки статуса

```html
<!-- Индикаторы статуса -->
{% metroui5_icon "checkmark" %} {% metroui5_icon "cross" %} {% metroui5_icon
"warning" %} {% metroui5_icon "info" %} {% metroui5_icon "question" %} {%
metroui5_icon "exclamation" %}
```

## Использование в Django шаблонах

### Использование в представлениях

```python
# views.py
from metroui5.templatetags.metroui5 import metroui5_icon

def my_view(request):
    # Создание иконок в представлении
    home_icon = metroui5_icon("home", size="2x")
    user_icon = metroui5_icon("user", class="icon-primary")

    context = {
        'home_icon': home_icon,
        'user_icon': user_icon,
        'navigation_icons': [
            metroui5_icon("dashboard", class="nav-icon"),
            metroui5_icon("settings", class="nav-icon"),
            metroui5_icon("logout", class="nav-icon"),
        ]
    }
    return render(request, 'my_template.html', context)
```

```html
<!-- my_template.html -->
{% load metroui5 %}

<!-- Прямой HTML вывод -->
{{ home_icon|safe }} {{ user_icon|safe }}

<!-- Цикл по иконкам -->
{% for icon in navigation_icons %} {{ icon|safe }} {% endfor %}
```

### Иконки в навигации

```python
# views.py
def navigation_view(request):
    nav_items = [
        {"text": "Home", "icon": metroui5_icon("home"), "url": "/"},
        {"text": "Dashboard", "icon": metroui5_icon("dashboard"), "url": "/dashboard/"},
        {"text": "Settings", "icon": metroui5_icon("cog"), "url": "/settings/"},
    ]

    context = {'nav_items': nav_items}
    return render(request, 'navigation.html', context)
```

```html
<!-- navigation.html -->
{% load metroui5 %}

<nav class="nav nav-horizontal">
	{% for item in nav_items %}
	<a href="{{ item.url }}" class="nav-item">
		{{ item.icon|safe }} {{ item.text }}
	</a>
	{% endfor %}
</nav>
```

### Условные иконки

```python
# views.py
def status_view(request):
    items = [
        {"name": "Task 1", "status": "completed"},
        {"name": "Task 2", "status": "pending"},
        {"name": "Task 3", "status": "failed"},
    ]

    for item in items:
        if item["status"] == "completed":
            item["icon"] = metroui5_icon("checkmark", class="icon-success")
        elif item["status"] == "pending":
            item["icon"] = metroui5_icon("clock", class="icon-warning")
        else:
            item["icon"] = metroui5_icon("cross", class="icon-danger")

    context = {'items': items}
    return render(request, 'status.html', context)
```

```html
<!-- status.html -->
{% load metroui5 %}

<ul class="list">
	{% for item in items %}
	<li class="list-item">{{ item.icon|safe }} {{ item.name }}</li>
	{% endfor %}
</ul>
```

## Продвинутые примеры

### Иконки в кнопках

```html
{% load metroui5 %}

<!-- Кнопка с иконкой -->
<button class="button button-primary">{% metroui5_icon "save" %} Save</button>

<!-- Кнопка только с иконкой -->
<button class="button button-mini">{% metroui5_icon "edit" %}</button>

<!-- Кнопка с иконкой и текстом -->
<a href="#" class="button button-success">
	{% metroui5_icon "download" size="2x" %} Download File
</a>
```

### Иконки в навигации

```html
{% load metroui5 %}

<nav class="nav nav-horizontal">
	<a href="/" class="nav-item"> {% metroui5_icon "home" %} Home </a>
	<a href="/about/" class="nav-item"> {% metroui5_icon "info" %} About </a>
	<a href="/contact/" class="nav-item"> {% metroui5_icon "mail" %} Contact </a>
</nav>
```

### Иконки в списках

```html
{% load metroui5 %}

<ul class="list">
	<li>{% metroui5_icon "user" class="icon-primary" %} John Doe</li>
	<li>{% metroui5_icon "mail" class="icon-info" %} john@example.com</li>
	<li>{% metroui5_icon "phone" class="icon-success" %} +1-555-0123</li>
</ul>
```

### Анимированные иконки

```html
{% load metroui5 %}

<!-- Вращающаяся иконка загрузки -->
{% metroui5_icon "spinner" class="icon-spin" %}

<!-- Пульсирующая иконка уведомления -->
{% metroui5_icon "bell" class="icon-pulse" %}

<!-- Подпрыгивающая иконка успеха -->
{% metroui5_icon "checkmark" class="icon-bounce" %}
```

### Иконки с подсказками

```html
{% load metroui5 %}

<!-- Иконка с подсказкой -->
<span class="tooltip" data-tooltip="Click to edit">
	{% metroui5_icon "edit" class="icon-primary" %}
</span>

<!-- Иконка с пользовательской подсказкой -->
<span
	class="tooltip"
	data-tooltip="Delete this item"
	data-tooltip-position="top"
>
	{% metroui5_icon "delete" class="icon-danger" %}
</span>
```

### Адаптивные иконки

```html
{% load metroui5 %}

<!-- Адаптивные размеры иконок -->
<div class="icon-responsive">
	{% metroui5_icon "home" size="2x" class="icon-mobile-small icon-tablet-medium
	icon-desktop-large" %}
</div>
```

### Иконки в карточках

```html
{% load metroui5 %}

<div class="card">
	<div class="card-header">
		<h3>{% metroui5_icon "user" class="icon-primary" %} User Profile</h3>
	</div>
	<div class="card-content">
		<p>{% metroui5_icon "mail" %} user@example.com</p>
		<p>{% metroui5_icon "phone" %} +1-555-0123</p>
	</div>
</div>
```

### Иконки в уведомлениях

```html
{% load metroui5 %}

<!-- Уведомление об успехе с иконкой -->
<div class="alert alert-success">
	{% metroui5_icon "checkmark" class="icon-success" %} Operation completed
	successfully!
</div>

<!-- Уведомление-предупреждение с иконкой -->
<div class="alert alert-warning">
	{% metroui5_icon "warning" class="icon-warning" %} Please review your input.
</div>

<!-- Уведомление об ошибке с иконкой -->
<div class="alert alert-danger">
	{% metroui5_icon "cross" class="icon-danger" %} An error occurred.
</div>
```

## Пользовательская стилизация иконок

### CSS настройка

```css
/* Пользовательские цвета иконок */
.icon-custom-red {
	color: #ff4444;
}

.icon-custom-blue {
	color: #4444ff;
}

.icon-custom-green {
	color: #44ff44;
}

/* Пользовательские размеры иконок */
.icon-tiny {
	font-size: 0.5em;
}

.icon-huge {
	font-size: 4em;
}

/* Пользовательские эффекты иконок */
.icon-glow {
	text-shadow: 0 0 10px currentColor;
}

.icon-shadow {
	text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
```

### Использование пользовательских классов

```html
{% load metroui5 %}

<!-- Иконки с пользовательскими цветами -->
{% metroui5_icon "heart" class="icon-custom-red" %} {% metroui5_icon "star"
class="icon-custom-blue" %} {% metroui5_icon "leaf" class="icon-custom-green" %}

<!-- Иконки с пользовательскими размерами -->
{% metroui5_icon "home" class="icon-tiny" %} {% metroui5_icon "home"
class="icon-huge" %}

<!-- Иконки с эффектами -->
{% metroui5_icon "star" class="icon-glow" %} {% metroui5_icon "heart"
class="icon-shadow" %}
```

## Интеграция с JavaScript

### Динамическое обновление иконок

```javascript
// Изменение иконки динамически
function changeIcon(element, newIcon) {
	const iconElement = element.querySelector(".mif");
	if (iconElement) {
		// Удаление старого класса иконки
		const oldClasses = Array.from(iconElement.classList).filter((cls) =>
			cls.startsWith("mif-")
		);
		oldClasses.forEach((cls) => iconElement.classList.remove(cls));

		// Добавление нового класса иконки
		iconElement.classList.add(`mif-${newIcon}`);
	}
}

// Пример использования
const button = document.querySelector("#my-button");
changeIcon(button, "checkmark");
```

### Анимации иконок

```javascript
// Добавление анимации к иконке
function animateIcon(iconElement, animation) {
	iconElement.classList.add(`icon-${animation}`);

	// Удаление анимации после завершения
	setTimeout(() => {
		iconElement.classList.remove(`icon-${animation}`);
	}, 1000);
}

// Пример использования
const icon = document.querySelector(".mif-heart");
animateIcon(icon, "bounce");
```

### События клика по иконкам

```javascript
// Обработка кликов по иконкам
document.querySelectorAll(".mif").forEach((icon) => {
	icon.addEventListener("click", function () {
		const iconName = this.classList[1]; // Получение названия иконки из класса
		console.log(`Clicked icon: ${iconName}`);

		// Добавление эффекта клика
		this.style.transform = "scale(1.2)";
		setTimeout(() => {
			this.style.transform = "scale(1)";
		}, 200);
	});
});
```

## Лучшие практики

1. **Используйте семантические иконки**: Выбирайте иконки, которые четко представляют их функцию
2. **Поддерживайте консистентность**: Используйте одну и ту же иконку для одного и того же действия по всему приложению
3. **Учитывайте доступность**: Предоставляйте текстовые альтернативы для кнопок только с иконками
4. **Используйте соответствующие размеры**: Выбирайте размеры иконок, которые хорошо подходят к вашему контенту
5. **Ограничивайте анимации**: Используйте анимации экономно, чтобы не перегружать пользователей
6. **Тестируйте на мобильных**: Убедитесь, что иконки видны и пригодны для использования на мобильных устройствах
7. **Используйте цвет осмысленно**: Используйте цвета для передачи статуса или важности

## Справочник иконок

MetroUI5 включает сотни иконок. Вот некоторые часто используемые:

### Базовые иконки

- `home`, `user`, `settings`, `search`, `menu`, `close`, `checkmark`, `cross`
- `plus`, `minus`, `edit`, `delete`, `save`, `copy`, `cut`, `paste`
- `mail`, `phone`, `chat`, `bell`, `notification`, `comment`

### Иконки файлов

- `file`, `folder`, `document`, `image`, `video`, `audio`, `archive`
- `download`, `upload`, `attachment`, `link`, `bookmark`

### Навигационные иконки

- `back`, `forward`, `up`, `down`, `left`, `right`, `arrow-up`, `arrow-down`
- `arrow-left`, `arrow-right`, `chevron-up`, `chevron-down`

### Иконки статуса

- `warning`, `info`, `question`, `exclamation`, `checkmark`, `cross`
- `star`, `heart`, `like`, `dislike`, `flag`, `bookmark`

## Связанные компоненты

- [Кнопки](buttons.md) - Для кнопок с иконками
- [Навигация](navigation.md) - Для навигации с иконками
- [Уведомления](alerts.md) - Для уведомлений со статусными иконками
- [Карточки](cards.md) - Для карточек с иконками в заголовке
