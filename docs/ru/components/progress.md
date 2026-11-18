# Полосы прогресса

MetroUI5 Django предоставляет гибкую систему компонентов полос прогресса для отображения состояний загрузки, процентов завершения и индикаторов прогресса.

## Базовое использование

```python
from metroui5.components import render_progress

# Простая полоса прогресса
progress_html = render_progress(value=75, max_value=100)
```

## Параметры

### `render_progress(value, max_value=100, color="blue", size="default", **attrs)`

- **value** (int): Текущее значение прогресса
- **max_value** (int): Максимальное значение прогресса (по умолчанию: 100)
- **color** (str): Цвет полосы прогресса (blue, green, red, yellow, etc.)
- **size** (str): Размер полосы прогресса (small, default, large)
- **attrs** (dict): Дополнительные HTML атрибуты

## Примеры

### Базовая полоса прогресса

```python
from metroui5.components import render_progress

# 75% прогресса
progress = render_progress(value=75)
```

### Полоса прогресса с пользовательским цветом

```python
# Зеленая полоса прогресса
progress = render_progress(value=60, color="green")

# Красная полоса прогресса
progress = render_progress(value=25, color="red")

# Желтая полоса прогресса
progress = render_progress(value=45, color="yellow")
```

### Полоса прогресса с пользовательским размером

```python
# Маленькая полоса прогресса
progress = render_progress(value=50, size="small")

# Большая полоса прогресса
progress = render_progress(value=80, size="large")
```

### Полоса прогресса с пользовательскими атрибутами

```python
progress = render_progress(
    value=65,
    color="blue",
    size="default",
    id="upload-progress",
    class="progress-bar-custom"
)
```

## Классы прогресса MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации полос прогресса:

### Классы цветов

- `bg-blue` - Синяя полоса прогресса
- `bg-green` - Зеленая полоса прогресса
- `bg-red` - Красная полоса прогресса
- `bg-yellow` - Желтая полоса прогресса
- `bg-orange` - Оранжевая полоса прогресса
- `bg-purple` - Фиолетовая полоса прогресса
- `bg-pink` - Розовая полоса прогресса
- `bg-cyan` - Голубая полоса прогресса
- `bg-teal` - Бирюзовая полоса прогресса
- `bg-indigo` - Индиго полоса прогресса

### Классы размеров

- `progress-small` - Маленькая полоса прогресса
- `progress-large` - Большая полоса прогресса
- `progress-thin` - Тонкая полоса прогресса
- `progress-thick` - Толстая полоса прогресса

### Классы стилей

- `progress-striped` - Полосатая полоса прогресса
- `progress-animated` - Анимированная полоса прогресса
- `progress-rounded` - Скругленная полоса прогресса

## Типы полос прогресса

### Определенная полоса прогресса

```python
# Показывает точный процент прогресса
progress = render_progress(
    value=75,
    max_value=100,
    color="blue"
)
```

### Неопределенная полоса прогресса

```python
# Показывает состояние загрузки без конкретного процента
progress = render_progress(
    value=0,
    max_value=0,
    color="blue",
    class="progress-indeterminate"
)
```

### Полоса прогресса с пользовательским диапазоном

```python
# Полоса прогресса с пользовательским диапазоном (например, 0-50)
progress = render_progress(
    value=25,
    max_value=50,
    color="green"
)
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_progress value=75 color="blue" size="default" %}
```

## Расширенные примеры

### Прогресс загрузки файла

```python
def create_upload_progress(current_bytes, total_bytes):
    percentage = int((current_bytes / total_bytes) * 100) if total_bytes > 0 else 0

    progress = render_progress(
        value=percentage,
        color="blue",
        id="upload-progress",
        class="progress-upload"
    )

    return f"""
    <div class="upload-status">
        <p>Загрузка файла... {percentage}%</p>
        {progress}
        <p>{current_bytes} / {total_bytes} байт</p>
    </div>
    """

upload_status = create_upload_progress(1024 * 1024, 5 * 1024 * 1024)  # 1МБ / 5МБ
```

### Многошаговый прогресс

```python
def create_multi_step_progress(current_step, total_steps):
    percentage = int((current_step / total_steps) * 100)

    steps = ["Настройка", "Конфигурация", "Установка", "Тестирование", "Завершено"]
    current_step_name = steps[current_step - 1] if current_step <= len(steps) else "Завершено"

    progress = render_progress(
        value=percentage,
        color="green",
        class="progress-multi-step"
    )

    return f"""
    <div class="multi-step-progress">
        <h4>Шаг {current_step} из {total_steps}: {current_step_name}</h4>
        {progress}
        <div class="step-indicators">
            {''.join([f'<span class="step {"active" if i < current_step else ""}">{step}</span>' for i, step in enumerate(steps)])}
        </div>
    </div>
    """

multi_progress = create_multi_step_progress(3, 5)
```

### Анимированная полоса прогресса

```python
def create_animated_progress(value, color="blue"):
    return render_progress(
        value=value,
        color=color,
        class="progress-animated progress-striped"
    )

animated_progress = create_animated_progress(60, "green")
```

### Полоса прогресса с метками

```python
def create_labeled_progress(value, label, color="blue"):
    progress = render_progress(
        value=value,
        color=color,
        class="progress-labeled"
    )

    return f"""
    <div class="progress-container">
        <div class="progress-label">{label}</div>
        {progress}
        <div class="progress-value">{value}%</div>
    </div>
    """

labeled_progress = create_labeled_progress(85, "Завершение задачи", "green")
```

### Полоса прогресса с текстом статуса

```python
def create_status_progress(value, status_text, color="blue"):
    progress = render_progress(
        value=value,
        color=color,
        class="progress-status"
    )

    return f"""
    <div class="status-progress">
        <div class="status-header">
            <span class="status-text">{status_text}</span>
            <span class="status-percentage">{value}%</span>
        </div>
        {progress}
    </div>
    """

status_progress = create_status_progress(45, "Обработка данных...", "orange")
```

## Интеграция с JavaScript

### Динамическое обновление прогресса

```javascript
// Обновление значения прогресса
function updateProgress(value) {
	const progressBar = document.querySelector("#my-progress");
	const progressFill = progressBar.querySelector(".progress-bar");
	const percentage = (value / 100) * 100;

	progressFill.style.width = percentage + "%";
	progressFill.setAttribute("aria-valuenow", value);
}

// Пример использования
updateProgress(75);
```

### Анимированные обновления прогресса

```javascript
// Анимация прогресса от 0 до целевого значения
function animateProgress(targetValue, duration = 1000) {
	const progressBar = document.querySelector("#my-progress");
	const progressFill = progressBar.querySelector(".progress-bar");
	let currentValue = 0;
	const increment = targetValue / (duration / 16); // 60fps

	const animate = () => {
		currentValue += increment;
		if (currentValue >= targetValue) {
			currentValue = targetValue;
		}

		const percentage = (currentValue / 100) * 100;
		progressFill.style.width = percentage + "%";

		if (currentValue < targetValue) {
			requestAnimationFrame(animate);
		}
	};

	animate();
}

// Пример использования
animateProgress(80, 2000); // Анимация до 80% за 2 секунды
```

## Лучшие практики

1. **Используйте соответствующие цвета**: Выбирайте цвета, которые соответствуют теме вашего приложения
2. **Предоставляйте контекст**: Включайте метки или текст для объяснения того, что представляет прогресс
3. **Обрабатывайте крайние случаи**: Учитывайте состояния 0% и 100%
4. **Делайте доступным**: Включайте правильные ARIA атрибуты для экранных читателей
5. **Используйте последовательные размеры**: Применяйте последовательные классы размеров во всем приложении
6. **Учитывайте мобильные устройства**: Обеспечивайте видимость полос прогресса на мобильных устройствах
7. **Добавляйте анимации**: Используйте анимации для лучшего пользовательского опыта

## Связанные компоненты

- [Уведомления](alerts.md) - Для сообщений о статусе
- [Кнопки](buttons.md) - Для кнопок действий
- [Карточки](cards.md) - Для содержания полос прогресса
- [Формы](forms.md) - Для индикаторов прогресса, связанных с формами


## metroui5_progress

```python
render_progress(0)
```

Пустое или неверное значение: `render_progress(0)` даёт `<div class="progress progress-blue" data-role="progress" data-value="0" data-max="100"></div>`. Пустой вызов даёт `<div class="progress progress-blue progress-0" data-role="progress" data-value="0" data-max="0"></div>`.

```django
{% metroui5_progress value="Text" %}
```
