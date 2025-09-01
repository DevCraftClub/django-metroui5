# Значки

MetroUI5 Django предоставляет гибкую систему компонентов значков для отображения индикаторов статуса, счетчиков, меток и небольших фрагментов информации.

## Базовое использование

```python
from metroui5.components import render_badge

# Простой значок
badge_html = render_badge("Новый")
```

## Параметры

### `render_badge(content, badge_type="default", **attrs)`

- **content** (str): Текстовое содержимое значка
- **badge_type** (str): Тип/стиль значка (default, primary, success, warning, danger, info)
- **attrs** (dict): Дополнительные HTML атрибуты

## Примеры

### Базовые значки

```python
from metroui5.components import render_badge

# Значок по умолчанию
badge = render_badge("По умолчанию")

# Основной значок
badge = render_badge("Основной", badge_type="primary")

# Значок успеха
badge = render_badge("Успех", badge_type="success")

# Предупреждающий значок
badge = render_badge("Предупреждение", badge_type="warning")

# Опасный значок
badge = render_badge("Опасность", badge_type="danger")

# Информационный значок
badge = render_badge("Информация", badge_type="info")
```

### Значок с пользовательскими атрибутами

```python
badge = render_badge(
    "Пользовательский",
    badge_type="primary",
    id="custom-badge",
    class="badge-large"
)
```

### Значок с иконками

```python
def create_icon_badge(content, badge_type="default", icon=None):
    """Создание значка с иконкой."""

    if icon:
        content = f'<span class="mif-{icon}"></span> {content}'

    return render_badge(content, badge_type)

# Использование
icon_badge = create_icon_badge("5", "danger", "mail")
```

## Классы значков MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации значков:

### Классы типов

- `badge` - Базовый класс значка
- `badge-primary` - Основной стиль значка
- `badge-secondary` - Вторичный стиль значка
- `badge-success` - Стиль значка успеха (зеленый)
- `badge-warning` - Стиль предупреждающего значка (желтый)
- `badge-danger` - Стиль опасного значка (красный)
- `badge-info` - Стиль информационного значка (синий)
- `badge-light` - Светлый стиль значка
- `badge-dark` - Темный стиль значка

### Классы размеров

- `badge-small` - Маленький значок
- `badge-large` - Большой значок
- `badge-mini` - Мини значок

### Классы стилей

- `badge-rounded` - Скругленный значок
- `badge-pill` - Значок в форме пилюли
- `badge-outline` - Контурный значок
- `badge-glow` - Светящийся значок

## Типы значков

### Значки статуса

```python
def create_status_badge(status):
    """Создание значка статуса на основе значения статуса."""

    status_map = {
        "active": ("Активный", "success"),
        "inactive": ("Неактивный", "default"),
        "pending": ("В ожидании", "warning"),
        "error": ("Ошибка", "danger"),
        "completed": ("Завершено", "success"),
        "cancelled": ("Отменено", "danger"),
        "processing": ("Обработка", "info")
    }

    text, badge_type = status_map.get(status.lower(), ("Неизвестно", "default"))
    return render_badge(text, badge_type)

# Использование
active_badge = create_status_badge("active")
pending_badge = create_status_badge("pending")
error_badge = create_status_badge("error")
```

### Значки счетчиков

```python
def create_count_badge(count, max_count=None, badge_type="primary"):
    """Создание значка счетчика с опциональным максимальным лимитом."""

    if max_count and count > max_count:
        display_count = f"{max_count}+"
        badge_type = "warning"
    else:
        display_count = str(count)

    return render_badge(display_count, badge_type)

# Использование
message_count = create_count_badge(5)
notification_count = create_count_badge(12, max_count=10)
```

### Значки приоритета

```python
def create_priority_badge(priority):
    """Создание значка приоритета."""

    priority_map = {
        "high": ("Высокий", "danger"),
        "medium": ("Средний", "warning"),
        "low": ("Низкий", "info"),
        "critical": ("Критический", "danger"),
        "normal": ("Обычный", "default")
    }

    text, badge_type = priority_map.get(priority.lower(), ("Неизвестно", "default"))
    return render_badge(text, badge_type)

# Использование
high_priority = create_priority_badge("high")
critical_priority = create_priority_badge("critical")
```

### Значки категорий

```python
def create_category_badge(category, color_map=None):
    """Создание значка категории с пользовательским сопоставлением цветов."""

    if color_map is None:
        color_map = {
            "frontend": "primary",
            "backend": "success",
            "database": "warning",
            "devops": "info",
            "design": "danger"
        }

    badge_type = color_map.get(category.lower(), "default")
    return render_badge(category.title(), badge_type)

# Использование
frontend_badge = create_category_badge("frontend")
backend_badge = create_category_badge("backend")
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_badge "Новый" badge_type="primary" %}
```

## Расширенные примеры

### Значок с подсказкой

```python
def create_tooltip_badge(content, badge_type="default", tooltip=""):
    """Создание значка с подсказкой."""

    return render_badge(
        content,
        badge_type,
        class="badge-tooltip",
        data_tooltip=tooltip,
        data_tooltip_position="top"
    )

# Использование
tooltip_badge = create_tooltip_badge(
    "Бета",
    "warning",
    "Эта функция находится в бета-тестировании"
)
```

### Анимированный значок

```python
def create_animated_badge(content, badge_type="default", animation="pulse"):
    """Создание значка с анимацией."""

    return render_badge(
        content,
        badge_type,
        class=f"badge badge-{animation}"
    )

# Использование
pulse_badge = create_animated_badge("В прямом эфире", "danger", "pulse")
```

### Значок с кнопкой закрытия

```python
def create_dismissible_badge(content, badge_type="default", onclose=""):
    """Создание значка с кнопкой закрытия."""

    close_button = f'<button type="button" class="badge-close" onclick="{onclose}">&times;</button>'
    content_with_close = f"{content}{close_button}"

    return render_badge(
        content_with_close,
        badge_type,
        class="badge-dismissible"
    )

# Использование
dismissible_badge = create_dismissible_badge(
    "Закрываемый",
    "info",
    "closeBadge(this)"
)
```

### Группа значков

```python
def create_badge_group(badges, separator=" "):
    """Создание группы значков."""

    badge_htmls = []
    for badge in badges:
        if isinstance(badge, dict):
            badge_html = render_badge(
                badge['content'],
                badge.get('type', 'default'),
                **badge.get('attrs', {})
            )
        else:
            badge_html = render_badge(badge)
        badge_htmls.append(badge_html)

    return separator.join(badge_htmls)

# Использование
badge_group = create_badge_group([
    {"content": "Python", "type": "primary"},
    {"content": "Django", "type": "success"},
    {"content": "MetroUI5", "type": "info"}
])
```

### Условный значок

```python
def create_conditional_badge(condition, true_content, false_content, true_type="success", false_type="default"):
    """Создание значка, который изменяется в зависимости от условия."""

    if condition:
        return render_badge(true_content, true_type)
    else:
        return render_badge(false_content, false_type)

# Использование
online_badge = create_conditional_badge(
    user.is_online,
    "В сети",
    "Не в сети",
    "success",
    "default"
)
```

### Значок с прогрессом

```python
def create_progress_badge(content, progress, badge_type="info"):
    """Создание значка, показывающего прогресс."""

    progress_html = f"""
    <div class="badge-progress">
        <span class="badge-content">{content}</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress}%"></div>
        </div>
    </div>
    """

    return render_badge(
        progress_html,
        badge_type,
        class="badge-progress-container"
    )

# Использование
progress_badge = create_progress_badge("Загрузка", 75, "primary")
```

### Значок в навигации

```python
def create_nav_with_badges(nav_items):
    """Создание навигации со значками."""

    nav_html = "<nav class='nav nav-horizontal'>"

    for item in nav_items:
        badge_html = ""
        if item.get('badge'):
            badge_html = render_badge(
                item['badge']['content'],
                item['badge'].get('type', 'primary')
            )

        nav_html += f"""
        <a href="{item['url']}" class="nav-item">
            <span class="mif-{item['icon']}"></span>
            {item['text']}
            {badge_html}
        </a>
        """

    nav_html += "</nav>"
    return nav_html

# Использование
nav_items = [
    {"text": "Главная", "url": "/", "icon": "home"},
    {"text": "Сообщения", "url": "/messages/", "icon": "mail", "badge": {"content": "5", "type": "danger"}},
    {"text": "Уведомления", "url": "/notifications/", "icon": "bell", "badge": {"content": "12", "type": "warning"}},
    {"text": "Настройки", "url": "/settings/", "icon": "cog"}
]

nav_with_badges = create_nav_with_badges(nav_items)
```

### Значок в карточках

```python
def create_card_with_badge(title, content, badge_content, badge_type="primary"):
    """Создание карточки со значком в заголовке."""

    badge_html = render_badge(badge_content, badge_type)

    return f"""
    <div class="card">
        <div class="card-header">
            <h3>{title} {badge_html}</h3>
        </div>
        <div class="card-content">
            {content}
        </div>
    </div>
    """

# Использование
card_with_badge = create_card_with_badge(
    "Статус проекта",
    "Проект хорошо продвигается...",
    "Активный",
    "success"
)
```

### Значок в таблицах

```python
def create_table_with_badges(headers, rows_with_badges):
    """Создание таблицы со столбцами значков."""

    from metroui5.components import render_table

    # Обработка строк для включения HTML значков
    processed_rows = []
    for row in rows_with_badges:
        processed_row = []
        for i, cell in enumerate(row):
            if isinstance(cell, dict) and 'badge' in cell:
                badge_html = render_badge(
                    cell['badge']['content'],
                    cell['badge'].get('type', 'default')
                )
                processed_row.append(badge_html)
            else:
                processed_row.append(cell)
        processed_rows.append(processed_row)

    return render_table(headers, processed_rows, class="table table-border")

# Использование
headers = ["Название", "Статус", "Приоритет", "Категория"]
rows_with_badges = [
    ["Задача 1", {"badge": {"content": "Активная", "type": "success"}},
     {"badge": {"content": "Высокий", "type": "danger"}},
     {"badge": {"content": "Frontend", "type": "primary"}}],
    ["Задача 2", {"badge": {"content": "В ожидании", "type": "warning"}},
     {"badge": {"content": "Средний", "type": "warning"}},
     {"badge": {"content": "Backend", "type": "success"}}]
]

table_with_badges = create_table_with_badges(headers, rows_with_badges)
```

## Интеграция с JavaScript

### Динамические обновления значков

```javascript
// Обновление содержимого значка
function updateBadge(badgeId, newContent, newType) {
	const badge = document.querySelector(`#${badgeId}`);
	if (badge) {
		badge.textContent = newContent;
		badge.className = `badge badge-${newType}`;
	}
}

// Анимация счетчика значка
function animateBadgeCount(badgeId, targetCount) {
	const badge = document.querySelector(`#${badgeId}`);
	if (badge) {
		const currentCount = parseInt(badge.textContent) || 0;
		const increment = targetCount > currentCount ? 1 : -1;

		const animate = () => {
			if (currentCount !== targetCount) {
				currentCount += increment;
				badge.textContent = currentCount;
				setTimeout(animate, 50);
			}
		};

		animate();
	}
}
```

### События значков

```javascript
// Обработка кликов по значкам
document.querySelectorAll(".badge").forEach((badge) => {
	badge.addEventListener("click", function () {
		console.log("Значок нажат:", this.textContent);

		// Добавить эффект клика
		this.style.transform = "scale(1.1)";
		setTimeout(() => {
			this.style.transform = "scale(1)";
		}, 200);
	});
});

// Обработка закрываемых значков
document
	.querySelectorAll(".badge-dismissible .badge-close")
	.forEach((closeBtn) => {
		closeBtn.addEventListener("click", function () {
			const badge = this.parentElement;
			badge.style.opacity = "0";
			setTimeout(() => {
				badge.remove();
			}, 300);
		});
	});
```

### Фильтрация значков

```javascript
// Фильтрация элементов по типу значка
function filterByBadge(badgeType) {
	const elements = document.querySelectorAll(".badge");

	elements.forEach((element) => {
		if (
			badgeType === "all" ||
			element.classList.contains(`badge-${badgeType}`)
		) {
			element.style.display = "inline-block";
		} else {
			element.style.display = "none";
		}
	});
}
```

## Лучшие практики

1. **Используйте подходящие цвета**: Выбирайте цвета значков, которые передают правильный смысл
2. **Держите текст кратким**: Используйте короткий, понятный текст для содержимого значка
3. **Поддерживайте последовательность**: Используйте последовательные стили значков во всем приложении
4. **Учитывайте доступность**: Обеспечьте достаточный контраст и читаемость значков
5. **Используйте умеренно**: Не злоупотребляйте значками, так как они могут загромождать интерфейс
6. **Предоставляйте контекст**: Используйте значки для улучшения, а не замены важной информации
7. **Тестируйте на мобильных устройствах**: Убедитесь, что значки видны и читаемы на мобильных устройствах

## Связанные компоненты

- [Уведомления](alerts.md) - Для сообщений о статусе со значками
- [Навигация](navigation.md) - Для элементов навигации со значками
- [Карточки](cards.md) - Для карточек с заголовками значков
- [Таблицы](tables.md) - Для ячеек таблиц с индикаторами значков
