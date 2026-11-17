# Календари

Компонент для создания интерактивных виджетов календаря с выбором даты, событиями и функциональностью планирования.

## Базовое использование

### Простой календарь

```python
from metroui5.components import render_calendar

# Базовый календарь
calendar_html = render_calendar()
```

### Календарь с опциями

```python
# Календарь с пользовательскими опциями
calendar_html = render_calendar(
    id="my-calendar",
    date="2024-01-15",
    format="%Y-%m-%d",
    locale="ru"
)
```

### Календарь с событиями

```python
# Календарь с событиями
events = [
    {"date": "2024-01-15", "title": "Встреча", "color": "blue"},
    {"date": "2024-01-20", "title": "День рождения", "color": "red"},
    {"date": "2024-01-25", "title": "Дедлайн", "color": "orange"}
]

calendar_html = render_calendar(
    id="events-calendar",
    events=events,
    show_events=True
)
```

## Результат рендеринга

### Базовый календарь

```html
<!-- Ввод -->
render_calendar()

<!-- Вывод -->
<div class="calendar" data-role="calendar"></div>
```

### Календарь с событиями

```html
<!-- Ввод -->
render_calendar(events=events, show_events=True)

<!-- Вывод -->
<div
	class="calendar"
	data-role="calendar"
	data-events='[{"date":"2024-01-15","title":"Встреча","color":"blue"}]'
></div>
```

### Календарь с пользовательским форматом

```html
<!-- Ввод -->
render_calendar(format="%d/%m/%Y", locale="ru")

<!-- Вывод -->
<div
	class="calendar"
	data-role="calendar"
	data-format="%d/%m/%Y"
	data-locale="ru"
></div>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовый календарь -->
{% metroui5_calendar %}

<!-- Календарь с опциями -->
{% metroui5_calendar id="my-calendar" date="2024-01-15" %}

<!-- Календарь с событиями -->
{% metroui5_calendar events=calendar_events show_events=True %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_calendar

def calendar_view(request):
    # Создать календарь с событиями
    events = [
        {"date": "2024-01-15", "title": "Командная встреча", "color": "blue"},
        {"date": "2024-01-20", "title": "Дедлайн проекта", "color": "red"},
    ]

    calendar_html = render_calendar(
        id="main-calendar",
        events=events,
        show_events=True,
        format="%Y-%m-%d"
    )

    context = {
        'calendar_html': calendar_html,
        'calendar_events': events
    }
    return render(request, 'calendar.html', context)
```

```html
<!-- calendar.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ calendar_html|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_calendar events=calendar_events show_events=True %} {% endblock %}
```

## Параметры

### `id` (опционально)

Уникальный идентификатор для элемента календаря.

**По умолчанию**: Автоматически сгенерированный ID

**Пример**:

```python
calendar_html = render_calendar(id="my-calendar")
```

### `date` (опционально)

Начальная дата для отображения. Формат зависит от параметра `format`.

**По умолчанию**: Текущая дата

**Пример**:

```python
calendar_html = render_calendar(date="2024-01-15")
```

### `format` (опционально)

Формат даты для отображения и ввода. Использует формат strftime.

**По умолчанию**: `"%Y-%m-%d"`

**Пример**:

```python
calendar_html = render_calendar(format="%d/%m/%Y")
```

### `locale` (опционально)

Локаль для форматирования даты и языка.

**По умолчанию**: `"en"`

**Пример**:

```python
calendar_html = render_calendar(locale="ru")
```

### `events` (опционально)

Список событий для отображения в календаре.

**Формат**:

```python
events = [
    {
        "date": "2024-01-15",
        "title": "Название события",
        "color": "blue",  # Опционально
        "description": "Описание события"  # Опционально
    }
]
```

**Пример**:

```python
events = [
    {"date": "2024-01-15", "title": "Встреча", "color": "blue"},
    {"date": "2024-01-20", "title": "День рождения", "color": "red"},
]
calendar_html = render_calendar(events=events)
```

### `show_events` (опционально)

Отображать ли события в календаре.

**По умолчанию**: `False`

**Пример**:

```python
calendar_html = render_calendar(events=events, show_events=True)
```

### `readonly` (опционально)

Только для чтения ли календарь.

**По умолчанию**: `False`

**Пример**:

```python
calendar_html = render_calendar(readonly=True)
```

### `class` (опционально)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
calendar_html = render_calendar(class="calendar-large")
```

## Продвинутые примеры

### Календарь управления событиями

```python
def create_event_calendar(events, user_id):
    """Создать календарь с пользовательскими событиями."""

    # Обработать события для календаря
    calendar_events = []
    for event in events:
        calendar_events.append({
            "date": event.date.strftime("%Y-%m-%d"),
            "title": event.title,
            "color": event.get_color_display(),
            "description": event.description,
            "id": event.id
        })

    return render_calendar(
        id=f"user-calendar-{user_id}",
        events=calendar_events,
        show_events=True,
        format="%Y-%m-%d",
        class="calendar-events"
    )
```

### Многоязычный календарь

```python
def create_localized_calendar(locale="ru"):
    """Создать календарь с определенной локалью."""

    locale_formats = {
        "en": "%m/%d/%Y",
        "ru": "%d.%m.%Y",
        "de": "%d.%m.%Y",
        "fr": "%d/%m/%Y"
    }

    return render_calendar(
        id=f"calendar-{locale}",
        locale=locale,
        format=locale_formats.get(locale, "%Y-%m-%d"),
        class="calendar-localized"
    )
```

### Календарь бронирования

```python
def create_booking_calendar(bookings, available_dates):
    """Создать календарь для системы бронирования."""

    # Создать события из бронирований
    events = []
    for booking in bookings:
        events.append({
            "date": booking.date.strftime("%Y-%m-%d"),
            "title": f"Забронировано: {booking.customer_name}",
            "color": "red"
        })

    # Добавить доступные даты как события другого цвета
    for date in available_dates:
        events.append({
            "date": date.strftime("%Y-%m-%d"),
            "title": "Доступно",
            "color": "green"
        })

    return render_calendar(
        id="booking-calendar",
        events=events,
        show_events=True,
        format="%Y-%m-%d",
        class="calendar-booking"
    )
```

### Календарь диапазона дат

```python
def create_date_range_calendar(start_date, end_date):
    """Создать календарь с выбором диапазона дат."""

    return render_calendar(
        id="range-calendar",
        date=start_date.strftime("%Y-%m-%d"),
        format="%Y-%m-%d",
        class="calendar-range",
        **{
            "data-range": "true",
            "data-range-start": start_date.strftime("%Y-%m-%d"),
            "data-range-end": end_date.strftime("%Y-%m-%d")
        }
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `calendar` - Базовый класс календаря
- `calendar-primary` - Основной стиль календаря
- `calendar-secondary` - Вторичный стиль календаря

#### Классы размеров

- `calendar-small` - Маленький календарь
- `calendar-large` - Большой календарь
- `calendar-compact` - Компактный календарь

#### Классы тем

- `calendar-dark` - Темная тема
- `calendar-light` - Светлая тема
- `calendar-colorful` - Цветная тема

### Пользовательская стилизация

```css
/* Пользовательская стилизация календаря */
.calendar-custom {
	border: 2px solid #007acc;
	border-radius: 8px;
	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.calendar-custom .calendar-header {
	background: linear-gradient(135deg, #007acc, #005a99);
	color: white;
	padding: 15px;
	border-radius: 6px 6px 0 0;
}

.calendar-custom .calendar-body {
	padding: 20px;
}

/* Стилизация событий */
.calendar-event {
	background: #007acc;
	color: white;
	padding: 2px 6px;
	border-radius: 3px;
	font-size: 0.8em;
	margin: 1px;
}

.calendar-event.red {
	background: #dc3545;
}

.calendar-event.green {
	background: #28a745;
}

.calendar-event.orange {
	background: #fd7e14;
}
```

## Интеграция с JavaScript

### Базовые события календаря

```javascript
// Инициализация календаря
$(document).ready(function () {
	$(".calendar").calendar({
		onSelect: function (date, element) {
			console.log("Выбранная дата:", date);
			updateSelectedDate(date);
		},
		onShow: function () {
			console.log("Календарь показан");
		},
		onHide: function () {
			console.log("Календарь скрыт");
		},
	});
});
```

### Управление событиями

```javascript
// Добавить событие в календарь
function addCalendarEvent(date, title, color) {
	const calendar = $(".calendar").data("calendar");
	const events = calendar.options.events || [];

	events.push({
		date: date,
		title: title,
		color: color,
	});

	calendar.options.events = events;
	calendar.draw();
}

// Удалить событие из календаря
function removeCalendarEvent(date, title) {
	const calendar = $(".calendar").data("calendar");
	const events = calendar.options.events || [];

	const filteredEvents = events.filter(
		(event) => !(event.date === date && event.title === title)
	);

	calendar.options.events = filteredEvents;
	calendar.draw();
}
```

### Выбор диапазона дат

```javascript
// Обработка выбора диапазона дат
function handleDateRangeSelection() {
	$(".calendar-range").calendar({
		onSelect: function (date, element) {
			const selectedDates = getSelectedDateRange();
			updateDateRangeDisplay(selectedDates);
		},
	});
}

function getSelectedDateRange() {
	const calendar = $(".calendar-range").data("calendar");
	return {
		start: calendar.options.rangeStart,
		end: calendar.options.rangeEnd,
	};
}

function updateDateRangeDisplay(range) {
	$("#date-range-display").text(`${range.start} до ${range.end}`);
}
```

### Загрузка событий через AJAX

```javascript
// Загрузить события через AJAX
function loadCalendarEvents(calendarId, month, year) {
	$.ajax({
		url: "/api/calendar-events/",
		method: "GET",
		data: {
			calendar_id: calendarId,
			month: month,
			year: year,
		},
		success: function (data) {
			updateCalendarEvents(data.events);
		},
		error: function (xhr, status, error) {
			console.error("Ошибка загрузки событий:", error);
		},
	});
}

function updateCalendarEvents(events) {
	const calendar = $(".calendar").data("calendar");
	calendar.options.events = events;
	calendar.draw();
}
```

### Навигация по календарю

```javascript
// Перейти к определенному месяцу/году
function navigateToMonth(month, year) {
	const calendar = $(".calendar").data("calendar");
	calendar.setDate(new Date(year, month - 1, 1));
}

// Перейти к сегодняшнему дню
function goToToday() {
	const calendar = $(".calendar").data("calendar");
	calendar.setDate(new Date());
}

// Перейти к предыдущему/следующему месяцу
function goToPreviousMonth() {
	const calendar = $(".calendar").data("calendar");
	const currentDate = calendar.getDate();
	const newDate = new Date(
		currentDate.getFullYear(),
		currentDate.getMonth() - 1,
		1
	);
	calendar.setDate(newDate);
}

function goToNextMonth() {
	const calendar = $(".calendar").data("calendar");
	const currentDate = calendar.getDate();
	const newDate = new Date(
		currentDate.getFullYear(),
		currentDate.getMonth() + 1,
		1
	);
	calendar.setDate(newDate);
}
```

### Обработка кликов по событиям

```javascript
// Обработка кликов по событиям
function handleEventClick(event) {
	const eventData = event.data;

	// Показать модальное окно с деталями события
	showEventModal({
		title: eventData.title,
		date: eventData.date,
		description: eventData.description,
		color: eventData.color,
	});
}

function showEventModal(eventData) {
	const modal = $("#event-modal");
	modal.find(".modal-title").text(eventData.title);
	modal.find(".event-date").text(eventData.date);
	modal.find(".event-description").text(eventData.description);
	modal.find(".event-color").css("background-color", eventData.color);

	modal.modal("show");
}
```

## Лучшие практики

### 1. Структура данных событий

```python
# Консистентная структура событий
def create_event_data(event):
    """Создать стандартизированные данные события для календаря."""
    return {
        "date": event.date.strftime("%Y-%m-%d"),
        "title": event.title,
        "color": event.get_color_display(),
        "description": event.description,
        "id": event.id,
        "type": event.type,
        "priority": event.priority
    }
```

### 2. Форматирование дат

```python
# Использовать консистентное форматирование дат
def format_date_for_calendar(date, format="%Y-%m-%d"):
    """Форматировать дату консистентно для использования в календаре."""
    if isinstance(date, str):
        return date
    return date.strftime(format)
```

### 3. Цветовое кодирование событий

```python
# Цветовое кодирование для разных типов событий
EVENT_COLORS = {
    "meeting": "blue",
    "deadline": "red",
    "birthday": "green",
    "reminder": "orange",
    "holiday": "purple"
}

def get_event_color(event_type):
    """Получить цвет для типа события."""
    return EVENT_COLORS.get(event_type, "gray")
```

### 4. Оптимизация производительности

```python
# Эффективно загружать события
def get_calendar_events(user_id, month, year):
    """Получить события для определенного месяца эффективно."""
    start_date = datetime.date(year, month, 1)
    if month == 12:
        end_date = datetime.date(year + 1, 1, 1)
    else:
        end_date = datetime.date(year, month + 1, 1)

    return Event.objects.filter(
        user_id=user_id,
        date__gte=start_date,
        date__lt=end_date
    ).select_related('category')
```

## Связанные компоненты

- [Модальные окна](modals.md) - Для всплывающих окон с деталями событий
- [Формы](forms.md) - Для форм создания событий
- [Уведомления](alerts.md) - Для уведомлений календаря
- [Навигация](navigation.md) - Для навигации по календарю


## metroui5_calendar

```python
render_calendar()
```

Пустое или неверное значение: `render_calendar()` даёт `<div class="calendar" data-role="calendar"></div>`.

```django
{% metroui5_calendar %}
```
