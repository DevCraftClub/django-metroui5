# Calendars

Component for creating interactive calendar widgets with date selection, events, and scheduling functionality.

## Basic Usage

### Simple Calendar

```python
from metroui5.components import render_calendar

# Basic calendar
calendar_html = render_calendar()
```

### Calendar with Options

```python
# Calendar with custom options
calendar_html = render_calendar(
    id="my-calendar",
    date="2024-01-15",
    format="%Y-%m-%d",
    locale="en"
)
```

### Calendar with Events

```python
# Calendar with events
events = [
    {"date": "2024-01-15", "title": "Meeting", "color": "blue"},
    {"date": "2024-01-20", "title": "Birthday", "color": "red"},
    {"date": "2024-01-25", "title": "Deadline", "color": "orange"}
]

calendar_html = render_calendar(
    id="events-calendar",
    events=events,
    show_events=True
)
```

## Rendered Output

### Basic Calendar

```html
<!-- Input -->
render_calendar()

<!-- Output -->
<div class="calendar" data-role="calendar"></div>
```

### Calendar with Events

```html
<!-- Input -->
render_calendar(events=events, show_events=True)

<!-- Output -->
<div
	class="calendar"
	data-role="calendar"
	data-events='[{"date":"2024-01-15","title":"Meeting","color":"blue"}]'
></div>
```

### Calendar with Custom Format

```html
<!-- Input -->
render_calendar(format="%d/%m/%Y", locale="en")

<!-- Output -->
<div
	class="calendar"
	data-role="calendar"
	data-format="%d/%m/%Y"
	data-locale="en"
></div>
```

## Django Template Usage

### Using Template Tags

```html
{% load metroui5 %}

<!-- Basic calendar -->
{% metroui5_calendar %}

<!-- Calendar with options -->
{% metroui5_calendar id="my-calendar" date="2024-01-15" %}

<!-- Calendar with events -->
{% metroui5_calendar events=calendar_events show_events=True %}
```

### Using in Views

```python
# views.py
from metroui5.components import render_calendar

def calendar_view(request):
    # Create calendar with events
    events = [
        {"date": "2024-01-15", "title": "Team Meeting", "color": "blue"},
        {"date": "2024-01-20", "title": "Project Deadline", "color": "red"},
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
<!-- Direct HTML output -->
{{ calendar_html|safe }}

<!-- Or use template tag -->
{% metroui5_calendar events=calendar_events show_events=True %} {% endblock %}
```

## Parameters

### `id` (optional)

Unique identifier for the calendar element.

**Default**: Auto-generated ID

**Example**:

```python
calendar_html = render_calendar(id="my-calendar")
```

### `date` (optional)

Initial date to display. Format depends on the `format` parameter.

**Default**: Current date

**Example**:

```python
calendar_html = render_calendar(date="2024-01-15")
```

### `format` (optional)

Date format for display and input. Uses strftime format.

**Default**: `"%Y-%m-%d"`

**Example**:

```python
calendar_html = render_calendar(format="%d/%m/%Y")
```

### `locale` (optional)

Locale for date formatting and language.

**Default**: `"en"`

**Example**:

```python
calendar_html = render_calendar(locale="ru")
```

### `events` (optional)

List of events to display on the calendar.

**Format**:

```python
events = [
    {
        "date": "2024-01-15",
        "title": "Event Title",
        "color": "blue",  # Optional
        "description": "Event description"  # Optional
    }
]
```

**Example**:

```python
events = [
    {"date": "2024-01-15", "title": "Meeting", "color": "blue"},
    {"date": "2024-01-20", "title": "Birthday", "color": "red"},
]
calendar_html = render_calendar(events=events)
```

### `show_events` (optional)

Whether to display events on the calendar.

**Default**: `False`

**Example**:

```python
calendar_html = render_calendar(events=events, show_events=True)
```

### `readonly` (optional)

Whether the calendar is read-only.

**Default**: `False`

**Example**:

```python
calendar_html = render_calendar(readonly=True)
```

### `class` (optional)

Additional CSS classes for styling.

**Example**:

```python
calendar_html = render_calendar(class="calendar-large")
```

## Advanced Examples

### Event Management Calendar

```python
def create_event_calendar(events, user_id):
    """Create calendar with user-specific events."""

    # Process events for calendar
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

### Multi-Language Calendar

```python
def create_localized_calendar(locale="en"):
    """Create calendar with specific locale."""

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

### Booking Calendar

```python
def create_booking_calendar(bookings, available_dates):
    """Create calendar for booking system."""

    # Create events from bookings
    events = []
    for booking in bookings:
        events.append({
            "date": booking.date.strftime("%Y-%m-%d"),
            "title": f"Booked: {booking.customer_name}",
            "color": "red"
        })

    # Add available dates as different colored events
    for date in available_dates:
        events.append({
            "date": date.strftime("%Y-%m-%d"),
            "title": "Available",
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

### Date Range Calendar

```python
def create_date_range_calendar(start_date, end_date):
    """Create calendar with date range selection."""

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

## Styling

### CSS Classes

#### Base Classes

- `calendar` - Base calendar class
- `calendar-primary` - Primary calendar style
- `calendar-secondary` - Secondary calendar style

#### Size Classes

- `calendar-small` - Small calendar
- `calendar-large` - Large calendar
- `calendar-compact` - Compact calendar

#### Theme Classes

- `calendar-dark` - Dark theme
- `calendar-light` - Light theme
- `calendar-colorful` - Colorful theme

### Custom Styling

```css
/* Custom calendar styling */
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

/* Event styling */
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

## JavaScript Integration

### Basic Calendar Events

```javascript
// Initialize calendar
$(document).ready(function () {
	$(".calendar").calendar({
		onSelect: function (date, element) {
			console.log("Selected date:", date);
			updateSelectedDate(date);
		},
		onShow: function () {
			console.log("Calendar shown");
		},
		onHide: function () {
			console.log("Calendar hidden");
		},
	});
});
```

### Event Management

```javascript
// Add event to calendar
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

// Remove event from calendar
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

### Date Range Selection

```javascript
// Handle date range selection
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
	$("#date-range-display").text(`${range.start} to ${range.end}`);
}
```

### AJAX Event Loading

```javascript
// Load events via AJAX
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
			console.error("Error loading events:", error);
		},
	});
}

function updateCalendarEvents(events) {
	const calendar = $(".calendar").data("calendar");
	calendar.options.events = events;
	calendar.draw();
}
```

### Calendar Navigation

```javascript
// Navigate to specific month/year
function navigateToMonth(month, year) {
	const calendar = $(".calendar").data("calendar");
	calendar.setDate(new Date(year, month - 1, 1));
}

// Go to today
function goToToday() {
	const calendar = $(".calendar").data("calendar");
	calendar.setDate(new Date());
}

// Go to previous/next month
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

### Event Click Handling

```javascript
// Handle event clicks
function handleEventClick(event) {
	const eventData = event.data;

	// Show event details modal
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

## Best Practices

### 1. Event Data Structure

```python
# Consistent event structure
def create_event_data(event):
    """Create standardized event data for calendar."""
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

### 2. Date Formatting

```python
# Use consistent date formatting
def format_date_for_calendar(date, format="%Y-%m-%d"):
    """Format date consistently for calendar use."""
    if isinstance(date, str):
        return date
    return date.strftime(format)
```

### 3. Event Color Coding

```python
# Color coding for different event types
EVENT_COLORS = {
    "meeting": "blue",
    "deadline": "red",
    "birthday": "green",
    "reminder": "orange",
    "holiday": "purple"
}

def get_event_color(event_type):
    """Get color for event type."""
    return EVENT_COLORS.get(event_type, "gray")
```

### 4. Performance Optimization

```python
# Load events efficiently
def get_calendar_events(user_id, month, year):
    """Get events for specific month efficiently."""
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

## Related Components

- [Modals](modals.md) - For event detail popups
- [Forms](forms.md) - For event creation forms
- [Alerts](alerts.md) - For calendar notifications
- [Navigation](navigation.md) - For calendar navigation


## metroui5_calendar

```python
render_calendar()
```

Empty or invalid: `render_calendar()` returns `<div class="calendar" data-role="calendar"></div>`.

```django
{% metroui5_calendar %}
```
