# HTML утилиты (HTML)

API справочник для модуля HTML утилит MetroUI5 Django.

## Обзор

Модуль `html` содержит функции для генерации HTML тегов, ссылок, скриптов и других HTML элементов.

## Функции

### `render_tag(tag, attrs=None, content=None, close=True)`

Создает HTML тег с указанными атрибутами и содержимым.

#### Параметры

- `tag` (str) - имя HTML тега
- `attrs` (dict, опционально) - атрибуты тега
- `content` (str, опционально) - содержимое тега
- `close` (bool, опционально) - закрывать ли тег. По умолчанию `True`

#### Возвращает

HTML строку

#### Примеры

```python
from metroui5.html import render_tag

# Простой div
div_tag = render_tag("div", {"class": "container"}, "Содержимое")
# Результат: <div class="container">Содержимое</div>

# Тег без содержимого
hr_tag = render_tag("hr", {"class": "divider"}, close=False)
# Результат: <hr class="divider">

# Тег с множественными атрибутами
button_tag = render_tag(
	"button",
	{"class": "btn", "type": "submit", "id": "submitBtn"},
	"Отправить"
)
# Результат: <button class="btn" type="submit" id="submitBtn">Отправить</button>
```

### `render_link_tag(url, **attrs)`

Создает HTML тег `<link>` для подключения внешних ресурсов.

#### Параметры

- `url` (str) - URL ресурса
- `**attrs` - дополнительные атрибуты

#### Возвращает

HTML строку для тега `<link>`

#### Примеры

```python
from metroui5.html import render_link_tag

# CSS файл
css_link = render_link_tag(
	"/static/css/style.css",
	rel="stylesheet",
	type="text/css"
)
# Результат: <link href="/static/css/style.css" rel="stylesheet" type="text/css">

# Иконка
icon_link = render_link_tag(
	"/favicon.ico",
	rel="icon",
	type="image/x-icon"
)
# Результат: <link href="/favicon.ico" rel="icon" type="image/x-icon">

# Предзагрузка
preload_link = render_link_tag(
	"/static/js/app.js",
	rel="preload",
as ="script"
)
# Результат: <link href="/static/js/app.js" rel="preload" as="script">
```

### `render_script_tag(url, **attrs)`

Создает HTML тег `<script>` для подключения JavaScript файлов.

#### Параметры

- `url` (str) - URL JavaScript файла
- `**attrs` - дополнительные атрибуты

#### Возвращает

HTML строку для тега `<script>`

#### Примеры

```python
from metroui5.html import render_script_tag

# Обычный скрипт
script_tag = render_script_tag("/static/js/app.js")
# Результат: <script src="/static/js/app.js"></script>

# Скрипт с атрибутами
script_tag = render_script_tag(
	"/static/js/app.js",
	defer=True,
async=True
)
# Результат: <script src="/static/js/app.js" defer async></script>

# Скрипт с типом
script_tag = render_script_tag(
	"/static/js/app.js",
	type="module"
)
# Результат: <script src="/static/js/app.js" type="module"></script>
```

### `render_custom_css_files(css_files)`

Генерирует HTML теги `<link>` для кастомных CSS файлов.

#### Параметры

- `css_files` (list) - список URL CSS файлов

#### Возвращает

HTML строку с тегами `<link>`

#### Примеры

```python
from metroui5.html import render_custom_css_files

# Список CSS файлов
css_files = [
	"/static/css/custom.css",
	"/static/css/theme.css",
	"/static/css/responsive.css"
]

# Генерация HTML
css_html = render_custom_css_files(css_files)
# Результат:
# <link href="/static/css/custom.css" rel="stylesheet" type="text/css">
# <link href="/static/css/theme.css" rel="stylesheet" type="text/css">
# <link href="/static/css/responsive.css" rel="stylesheet" type="text/css">
```

### `render_custom_javascript_files(js_files)`

Генерирует HTML теги `<script>` для кастомных JavaScript файлов.

#### Параметры

- `js_files` (list) - список URL JavaScript файлов

#### Возвращает

HTML строку с тегами `<script>`

#### Примеры

```python
from metroui5.html import render_custom_javascript_files

# Список JavaScript файлов
js_files = [
	"/static/js/custom.js",
	"/static/js/plugins.js",
	"/static/js/analytics.js"
]

# Генерация HTML
js_html = render_custom_javascript_files(js_files)
# Результат:
# <script src="/static/js/custom.js"></script>
# <script src="/static/js/plugins.js"></script>
# <script src="/static/js/analytics.js"></script>
```

## Примеры использования

### Создание кастомных компонентов

```python
from metroui5.html import render_tag


def render_custom_alert(message, alert_type="info"):
	"""Создает кастомный алерт"""
	classes = f"alert alert-{alert_type} custom-alert"

	return render_tag(
		"div",
		{"class": classes, "role": "alert"},
		f"""
            <span class="alert-icon">!</span>
            <span class="alert-message">{message}</span>
            <button class="alert-close" onclick="this.parentElement.remove()">×</button>
        """
	)


# Использование
alert = render_custom_alert("Важное сообщение", "warning")
```

### Генерация навигационного меню

```python
from metroui5.html import render_tag


def render_nav_menu(items):
	"""Создает навигационное меню"""
	menu_items = []

	for item in items:
		if item.get('active'):
			classes = "nav-item active"
		else:
			classes = "nav-item"

		link = render_tag(
			"a",
			{"href": item['url'], "class": "nav-link"},
			item['text']
		)

		menu_item = render_tag("li", {"class": classes}, link)
		menu_items.append(menu_item)

	return render_tag("ul", {"class": "nav-menu"}, "".join(menu_items))


# Использование
nav_items = [
	{"text": "Главная", "url": "/", "active": True},
	{"text": "О нас", "url": "/about/", "active": False},
	{"text": "Контакты", "url": "/contact/", "active": False},
]

nav_menu = render_nav_menu(nav_items)
```

### Создание таблицы

```python
from metroui5.html import render_tag


def render_data_table(headers, rows, table_class="table"):
	"""Создает HTML таблицу"""
	# Заголовки
	header_cells = []
	for header in headers:
		th = render_tag("th", {}, header)
		header_cells.append(th)

	header_row = render_tag("tr", {}, "".join(header_cells))

	# Строки данных
	data_rows = []
	for row in rows:
		cells = []
		for cell in row:
			td = render_tag("td", {}, str(cell))
			cells.append(td)
		tr = render_tag("tr", {}, "".join(cells))
		data_rows.append(tr)

	# Собираем таблицу
	thead = render_tag("thead", {}, header_row)
	tbody = render_tag("tbody", {}, "".join(data_rows))

	return render_tag("table", {"class": table_class}, thead + tbody)


# Использование
headers = ["Имя", "Email", "Статус"]
rows = [
	["Иван", "ivan@example.com", "Активен"],
	["Петр", "petr@example.com", "Неактивен"],
]

table = render_data_table(headers, rows, "table table-striped")
```

### Генерация форм

```python
from metroui5.html import render_tag


def render_form_field(field_name, field_type="text", **attrs):
	"""Создает поле формы"""
	default_attrs = {
		"name": field_name,
		"id": field_name,
		"type": field_type,
		"class": "form-control"
	}

	# Объединяем атрибуты
	final_attrs = {**default_attrs, **attrs}

	return render_tag("input", final_attrs, close=False)


def render_form_group(label_text, field_html, help_text=None):
	"""Создает группу формы с меткой и полем"""
	label = render_tag("label", {"for": "field", "class": "form-label"}, label_text)

	group_content = label + field_html

	if help_text:
		help_element = render_tag("div", {"class": "form-text"}, help_text)
		group_content += help_element

	return render_tag("div", {"class": "form-group"}, group_content)


# Использование
name_field = render_form_field("name", placeholder="Введите имя")
email_field = render_form_field("email", "email", placeholder="Введите email")

name_group = render_form_group("Имя:", name_field, "Введите ваше полное имя")
email_group = render_form_group("Email:", email_field, "Будет использован для связи")

form = render_tag("form", {"method": "post"}, name_group + email_group)
```

## Кастомизация

### Создание собственных HTML утилит

```python
from metroui5.html import render_tag


def render_icon(icon_name, size="16px", color="currentColor"):
	"""Создает SVG иконку"""
	svg_attrs = {
		"width": size,
		"height": size,
		"fill": color,
		"viewBox": "0 0 24 24"
	}

	# Здесь можно добавить SVG path для иконки
	path = render_tag("path", {
		"d": "M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"},
					  close=False)

	return render_tag("svg", svg_attrs, path)


def render_badge(text, badge_type="default"):
	"""Создает бейдж"""
	classes = f"badge badge-{badge_type}"
	return render_tag("span", {"class": classes}, text)


# Использование
star_icon = render_icon("star", "24px", "#ffd700")
badge = render_badge("Новое", "success")
```

### Расширение существующих функций

```python
from metroui5.html import render_tag


def render_enhanced_tag(tag, attrs=None, content=None, close=True, **kwargs):
	"""Расширенная версия render_tag с дополнительными возможностями"""

	# Добавляем data-атрибуты
	if 'data' in kwargs:
		for key, value in kwargs['data'].items():
			if attrs is None:
				attrs = {}
			attrs[f"data-{key}"] = value

	# Добавляем aria-атрибуты
	if 'aria' in kwargs:
		for key, value in kwargs['aria'].items():
			if attrs is None:
				attrs = {}
			attrs[f"aria-{key}"] = value

	# Добавляем события
	if 'events' in kwargs:
		for event, handler in kwargs['events'].items():
			if attrs is None:
				attrs = {}
			attrs[f"on{event}"] = handler

	return render_tag(tag, attrs, content, close)


# Использование
enhanced_div = render_enhanced_tag(
	"div",
	{"class": "enhanced-element"},
	"Содержимое",
	data={"id": "123", "type": "info"},
	aria={"label": "Описание", "hidden": "false"},
	events={"click": "handleClick()", "mouseover": "handleHover()"}
)
```

## Лучшие практики

### 1. Используйте семантические теги

```python
# Хорошо
article = render_tag("article", {"class": "blog-post"}, content)
section = render_tag("section", {"class": "content"}, section_content)

# Плохо
div = render_tag("div", {"class": "blog-post"}, content)
div = render_tag("div", {"class": "content"}, section_content)
```

### 2. Добавляйте атрибуты доступности

```python
# Хорошо
button = render_tag(
	"button",
	{
		"class": "btn",
		"aria-label": "Закрыть модальное окно",
		"aria-expanded": "false"
	},
	"Закрыть"
)

# Плохо
button = render_tag("button", {"class": "btn"}, "Закрыть")
```

### 3. Используйте константы для повторяющихся значений

```python
# Хорошо
FORM_CLASSES = "form-control"
BUTTON_CLASSES = "btn btn-primary"

name_field = render_tag("input", {"class": FORM_CLASSES, "name": "name"})
submit_button = render_tag("button", {"class": BUTTON_CLASSES, "type": "submit"}, "Отправить")

# Плохо
name_field = render_tag("input", {"class": "form-control", "name": "name"})
submit_button = render_tag("button", {"class": "btn btn-primary", "type": "submit"}, "Отправить")
```

### 4. Обрабатывайте ошибки

```python
def safe_render_tag(tag, attrs=None, content=None, close=True):
	"""Безопасная версия render_tag с обработкой ошибок"""
	try:
		return render_tag(tag, attrs, content, close)
	except Exception as e:
		logger.error(f"Ошибка рендеринга тега {tag}: {e}")
		# Возвращаем fallback
		return f"<{tag}>Ошибка рендеринга</{tag}>"
```

## Тестирование

### Модульные тесты

```python
from django.test import TestCase
from metroui5.html import render_tag, render_link_tag, render_script_tag


class HTMLTestCase(TestCase):

	def test_render_tag_basic(self):
		"""Тест базового рендеринга тега"""
		result = render_tag("div", {"class": "test"}, "content")
		expected = '<div class="test">content</div>'
		self.assertEqual(result, expected)

	def test_render_tag_no_close(self):
		"""Тест тега без закрытия"""
		result = render_tag("hr", {"class": "divider"}, close=False)
		expected = '<hr class="divider">'
		self.assertEqual(result, expected)

	def test_render_link_tag(self):
		"""Тест рендеринга link тега"""
		result = render_link_tag("/style.css", rel="stylesheet")
		expected = '<link href="/style.css" rel="stylesheet">'
		self.assertEqual(result, expected)

	def test_render_script_tag(self):
		"""Тест рендеринга script тега"""
		result = render_script_tag("/app.js", defer=True)
		expected = '<script src="/app.js" defer></script>'
		self.assertEqual(result, expected)
```

## Связанные модули

- [Основные функции](core.md) - для получения настроек
- [CSS утилиты](css.md) - для работы с CSS классами
- [Компоненты](components.md) - для рендеринга UI компонентов

## Следующие шаги

Теперь, когда вы освоили HTML утилиты:

1. Изучите [CSS утилиты](css.md) для работы со стилями
2. Ознакомьтесь с [компонентами](components.md) для создания UI
3. Создайте собственные HTML утилиты для специфических задач
4. Интегрируйте HTML утилиты в ваши Django представления!
