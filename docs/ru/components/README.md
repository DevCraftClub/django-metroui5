# Компоненты MetroUI5 Django

Обзор всех доступных компонентов для создания пользовательских интерфейсов.

## Основные компоненты

### 🚨 [Алерты](alerts.md)

Отображение информационных сообщений, предупреждений и ошибок.

**Основные возможности:**

- Различные типы: info, success, warning, error
- Закрываемые алерты
- Кастомизация стилей и атрибутов

**Пример использования:**

```python
from metroui5.components import render_alert

alert = render_alert(
	"Важное сообщение!",
	alert_type="warning",
	dismissible=True
)
```

### 🔘 [Кнопки](buttons.md)

Создание интерактивных кнопок различных типов и размеров.

**Основные возможности:**

- Типы: default, primary, secondary, success, alert, warning
- Размеры: small, default, large
- Контурные кнопки
- Иконки

**Пример использования:**

```python
from metroui5.components import render_button

button = render_button(
	"Нажми меня!",
	button_type="primary",
	size="large",
	icon="plus"
)
```

### 🃏 [Карточки](cards.md)

Информационные карточки с заголовком, содержимым и подвалом.

**Основные возможности:**

- Заголовок, содержимое и подвал
- HTML содержимое
- Кастомизация стилей

**Пример использования:**

```python
from metroui5.components import render_card

card = render_card(
	header="Заголовок",
	content="Содержимое карточки",
	footer="Подвал"
)
```

### 🧱 [Плитки](tiles.md)

Компактные информационные плитки с заголовком, содержимым и иконкой.

**Основные возможности:**

- Размеры: small, medium, large
- Цвета: blue, green, orange, red, purple, yellow, cyan, gray
- Иконки MetroUI

**Пример использования:**

```python
from metroui5.components import render_tile

tile = render_tile(
	title="Пользователи",
	content="1,234",
	color="blue",
	size="small",
	icon="users"
)
```

### 🎨 [Темы](themes.md)

Поддержка светлой и темной тем MetroUI 5 с автоматическим переключением.

**Основные возможности:**

- Встроенные темы: light, dark, auto
- Theme switcher компонент
- Автоматическое определение системной темы
- Кастомизация target элемента

**Пример использования:**

```python
# settings.py
METROUI5 = {
	'theme': 'dark',
	'theme_switcher_enabled': True,
}
```

```html
{% extends "metroui5/layout/base.html" %}
<!-- Автоматически применяется темная тема -->
```

### 📝 [Формы](forms.md)

Рендеринг Django форм с MetroUI5 стилями.

**Основные возможности:**

- Макеты: vertical, horizontal
- Кастомизация кнопок отправки
- Обработка ошибок валидации

**Пример использования:**

```python
from metroui5.forms import render_form

form_html = render_form(
	form,
	layout='horizontal',
	submit_text="Отправить",
	submit_class="btn btn-primary"
)
```

## Дополнительные компоненты

### 📊 [Таблицы](tables.md)

Создание HTML таблиц с данными.

**Основные возможности:**

- Заголовки и строки данных
- Кастомизация стилей
- Поддержка HTML в ячейках

### 🧭 [Навигация](navigation.md)

Навигационные меню и элементы.

**Основные возможности:**

- Навигационные списки
- Активные состояния
- Иконки

### 🪟 [Модальные окна](modals.md)

Всплывающие модальные окна.

**Основные возможности:**

- Заголовок и содержимое
- Кастомные ID
- JavaScript интеграция

### 📋 [Панели](panels.md)

Информационные панели с заголовком и содержимым.

**Основные возможности:**

- Заголовок и содержимое
- Различные стили
- Кастомизация

### 📈 [Прогресс-бары](progress.md)

Визуализация прогресса выполнения задач.

**Основные возможности:**

- Процентное значение
- Цвета: blue, green, orange, red
- Размеры: default, small, large

### 🪗 [Аккордеоны](accordions.md)

Сворачиваемые секции контента.

**Основные возможности:**

- Заголовки и содержимое
- Состояния открытия/закрытия
- Кастомизация

### 📅 [Календари](calendars.md)

Календарные виджеты.

**Основные возможности:**

- Отображение дат
- События
- Навигация по месяцам

### 💬 [Диалоги](dialogs.md)

Диалоговые окна для взаимодействия.

**Основные возможности:**

- Заголовок и содержимое
- Кнопки действий
- Кастомизация

### 📋 [Выпадающие списки](dropdowns.md)

Выпадающие меню и списки.

**Основные возможности:**

- Элементы списка
- Кнопка-триггер
- Кастомизация

### ⌨️ [Поля ввода](inputs.md)

HTML поля ввода различных типов.

**Основные возможности:**

- Типы: text, email, password, number
- Placeholder текст
- Кастомизация

### 📝 [Списки](lists.md)

HTML списки (ul, ol).

**Основные возможности:**

- Типы: ul, ol
- Элементы списка
- Кастомизация

### 🍽️ [Меню](menus.md)

Контекстные меню.

**Основные возможности:**

- Элементы меню
- Подменю
- Кастомизация

### 📱 [Боковые панели](sidebars.md)

Боковые навигационные панели.

**Основные возможности:**

- Навигационные элементы
- Группировка
- Кастомизация

### 🏷️ [Вкладки](tabs.md)

Табы для организации контента.

**Основные возможности:**

- Заголовки вкладок
- Содержимое вкладок
- Активные состояния

### 🛠️ [Панели инструментов](toolbars.md)

Панели с инструментами и действиями.

**Основные возможности:**

- Элементы инструментов
- Группировка
- Кастомизация

### 🍞 [Хлебные крошки](breadcrumbs.md)

Навигационные хлебные крошки.

**Основные возможности:**

- Навигационные элементы
- Разделители
- Кастомизация

### 📄 [Пагинация](pagination.md)

Навигация по страницам.

**Основные возможности:**

- Текущая страница
- Общее количество страниц
- Навигационные кнопки

### 🏷️ [Бейджи](badges.md)

Маленькие информационные метки.

**Основные возможности:**

- Типы: default, success, warning, alert
- Текст содержимого
- Кастомизация

### 👤 [Аватары](avatars.md)

Изображения профилей пользователей.

**Основные возможности:**

- URL изображения
- Размеры: small, medium, large
- Fallback изображения

### ⭐ [Рейтинги](ratings.md)

Системы оценки и рейтингов.

**Основные возможности:**

- Значение рейтинга
- Максимальное значение
- Визуальное представление

## Комбинирование компонентов

### Панель управления

```python
from metroui5.components import *


def dashboard_view(request):
	context = {
		# Статистика в плитках
		'stats_tiles': [
			render_tile("Пользователи", "1,234", "blue", "small", "users"),
			render_tile("Заказы", "567", "green", "small", "cart"),
			render_tile("Доход", "$12,345", "orange", "small", "dollar"),
		],

		# Информация в карточках
		'info_cards': [
			render_card("Последние заказы", "Список заказов..."),
			render_card("Активность", "График активности..."),
		],

		# Действия в кнопках
		'action_buttons': [
			render_button("Создать", "primary", icon="plus"),
			render_button("Импорт", "secondary", icon="upload"),
			render_button("Экспорт", "success", icon="download"),
		],

		# Прогресс задач
		'progress_bars': [
			render_progress(75, "blue", **{"data-label": "Задача 1"}),
			render_progress(45, "green", **{"data-label": "Задача 2"}),
		]
	}

	return render(request, 'dashboard.html', context)
```

### Форма с компонентами

```python
from metroui5.components import *
from metroui5.forms import render_form


def complex_form_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Обработка формы
			alert = render_alert("Форма отправлена!", "success")
		else:
			alert = render_alert("Исправьте ошибки!", "error")
	else:
		form = ContactForm()
		alert = None

	# Рендерим форму
	form_html = render_form(
		form,
		layout='horizontal',
		submit_text="Отправить",
		submit_class="btn btn-primary"
	)

	# Создаем карточку для формы
	form_card = render_card(
		header="Свяжитесь с нами",
		content=form_html,
		footer="Мы ответим в течение 24 часов"
	)

	context = {
		'alert': alert,
		'form_card': form_card,
	}

	return render(request, 'complex_form.html', context)
```

## Лучшие практики

### 1. Импортируйте только нужные компоненты

```python
# Хорошо - импортируем только нужные
from metroui5.components import render_button, render_card, render_alert

# Плохо - импортируем все
from metroui5.components import *
```

### 2. Группируйте связанные компоненты

```python
# Хорошо - группируем по назначению
context = {
	'header_components': {
		'alert': render_alert("Сообщение", "info"),
		'breadcrumb': render_breadcrumb(items),
	},
	'main_components': {
		'card': render_card(...),
		'table': render_table(...),
	},
	'footer_components': {
		'buttons': [render_button(...), render_button(...)],
	}
}
```

### 3. Используйте константы для повторяющихся значений

```python
# Хорошо
BUTTON_PRIMARY = "btn btn-primary"
TILE_COLORS = ["blue", "green", "orange", "red"]

tiles = [
	render_tile("Заголовок", "Содержимое", color)
	for color in TILE_COLORS
]

# Плохо
tiles = [
	render_tile("Заголовок", "Содержимое", "blue"),
	render_tile("Заголовок", "Содержимое", "green"),
	render_tile("Заголовок", "Содержимое", "orange"),
	render_tile("Заголовок", "Содержимое", "red"),
]
```

### 4. Обрабатывайте ошибки

```python
def safe_render_component(component_func, *args, **kwargs):
	"""Безопасный рендеринг компонента с обработкой ошибок"""
	try:
		return component_func(*args, **kwargs)
	except Exception as e:
		logger.error(f"Ошибка рендеринга компонента: {e}")
		return f"<div>Ошибка загрузки компонента</div>"


# Использование
button = safe_render_component(render_button, "Текст", "primary")
```

## Следующие шаги

Теперь, когда вы ознакомились с компонентами:

1. Изучите детальную документацию каждого компонента
2. Ознакомьтесь с [примерами](../../getting-started/examples.md)
3. Изучите [API справочник](../../api-reference/) для детальной информации
4. Создайте собственные компоненты на основе существующих
5. Построите полноценные пользовательские интерфейсы!

## Полезные ссылки

- [Начало работы](../../getting-started/) - основы использования
- [Примеры](../../getting-started/examples.md) - практические примеры
- [API справочник](../../api-reference/) - детальная документация
- [GitHub репозиторий](https://github.com/your-repo/django-metroui5) - исходный код
