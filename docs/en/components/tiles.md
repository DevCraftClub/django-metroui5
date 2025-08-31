# Плитки (Tiles)

Компонент для создания информационных плиток с заголовком, содержимым и иконкой.

## Основное использование

### Простая плитка

```python
from metroui5.components import render_tile

# Базовая плитка
tile = render_tile("Заголовок", "Содержимое")
```

### Плитка с цветом и размером

```python
# Плитка с цветом и размером
tile = render_tile(
	title="Пользователи",
	content="1,234",
	color="blue",
	size="medium"
)
```

### Плитка с иконкой

```python
# Плитка с иконкой
tile = render_tile(
	title="Заказы",
	content="567",
	color="green",
	size="large",
	icon="cart"
)
```

## Параметры

### `title` (обязательный)

Заголовок плитки.

```python
tile = render_tile("Заголовок плитки")
```

### `content` (опционально)

Содержимое плитки. Если не указано, содержимое не отображается.

```python
tile = render_tile("Заголовок", "Содержимое")
```

### `size` (опционально)

Размер плитки. Доступные значения:

- `"small"` - маленькая
- `"medium"` (по умолчанию) - средняя
- `"large"` - большая

```python
tile = render_tile("Заголовок", size="large")
```

### `color` (опционально)

Цвет плитки. Доступные значения:

- `"blue"` (по умолчанию) - синий
- `"green"` - зеленый
- `"orange"` - оранжевый
- `"red"` - красный
- `"purple"` - фиолетовый
- `"yellow"` - желтый
- `"cyan"` - голубой
- `"gray"` - серый

```python
tile = render_tile("Заголовок", color="green")
```

### `icon` (опционально)

Иконка для плитки (имя иконки MetroUI).

```python
tile = render_tile("Заголовок", icon="users")
```

### `**attrs` (опционально)

Дополнительные HTML атрибуты.

```python
tile = render_tile(
	"Заголовок",
	**{"class": "custom-tile", "id": "myTile"}
)
```

## Примеры использования

### В представлении

```python
from metroui5.components import render_tile


def dashboard(request):
	context = {
		'stats_tiles': [
			render_tile(
				title="Пользователи",
				content="1,234",
				color="blue",
				size="small",
				icon="users"
			),
			render_tile(
				title="Заказы",
				content="567",
				color="green",
				size="small",
				icon="cart"
			),
			render_tile(
				title="Доход",
				content="$12,345",
				color="orange",
				size="small",
				icon="dollar"
			),
			render_tile(
				title="Товары",
				content="89",
				color="red",
				size="small",
				icon="package"
			)
		]
	}
	return render(request, 'dashboard.html', context)
```

### В шаблоне

```html
{% extends 'base.html' %} {% block content %}
<div class="row">
    {% for tile in stats_tiles %}
    <div class="cell-md-3">{{ tile|safe }}</div>
    {% endfor %}
</div>
{% endblock %}
```

### Плитки с различными размерами

```python
def size_examples_view(request):
	context = {
		'size_tiles': [
			render_tile("Маленькая", "Small", size="small", color="blue"),
			render_tile("Средняя", "Medium", size="medium", color="green"),
			render_tile("Большая", "Large", size="large", color="orange"),
		]
	}
	return render(request, 'size_examples.html', context)
```

### Плитки с различными цветами

```python
def color_examples_view(request):
	colors = ["blue", "green", "orange", "red", "purple", "yellow", "cyan", "gray"]

	context = {
		'color_tiles': [
			render_tile(f"Цвет {color.title()}", color, color=color)
			for color in colors
		]
	}
	return render(request, 'color_examples.html', context)
```

## Кастомизация

### Дополнительные CSS классы

```python
tile = render_tile(
	"Кастомная плитка",
	**{"class": "tile-custom my-tile"}
)
```

### Атрибуты для JavaScript

```python
tile = render_tile(
	"Интерактивная плитка",
	**{
		"data-tile-id": "123",
		"data-type": "stat",
		"onclick": "handleTileClick(this)"
	}
)
```

### Стилизация через CSS

```css
/* Кастомные стили для плиток */
.tile-custom {
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.my-tile {
    border: 2px solid transparent;
}

.my-tile:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    border-color: #007bff;
}

/* Стили для заголовка */
.tile-custom .tile-title {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

/* Стили для содержимого */
.tile-custom small {
    font-size: 1.5em;
    color: #666;
}
```

## Группировка плиток

### Сетка плиток

```python
def grid_tiles_view(request):
	# Создаем сетку плиток
	tiles = []
	for i in range(8):
		tile = render_tile(
			title=f"Плитка {i + 1}",
			content=f"Контент {i + 1}",
			color=["blue", "green", "orange", "red"][i % 4],
			size="small"
		)
		tiles.append(tile)

	return render(request, 'grid_tiles.html', {'tiles': tiles})
```

### Шаблон для сетки

```html
{% extends 'base.html' %} {% block content %}
<div class="row">
    {% for tile in tiles %}
    <div class="cell-md-3 cell-lg-2">{{ tile|safe }}</div>
    {% endfor %}
</div>
{% endblock %}
```

### Плитки в карточке

```python
from metroui5.components import render_tile, render_card


def tiles_in_card_view(request):
	# Создаем плитки
	tiles = [
		render_tile("Пользователи", "1,234", "blue", "small"),
		render_tile("Заказы", "567", "green", "small"),
		render_tile("Доход", "$12,345", "orange", "small"),
	]

	# Размещаем плитки в карточке
	tiles_html = "".join([f"<div class='cell-md-4'>{tile}</div>" for tile in tiles])

	card = render_card(
		header="Статистика",
		content=f"<div class='row'>{tiles_html}</div>"
	)

	return render(request, 'tiles_in_card.html', {'card': card})
```

## Лучшие практики

### 1. Используйте подходящие размеры

```python
# Хорошо - маленькие плитки для статистики
stats_tiles = [
	render_tile("Пользователи", "1,234", "blue", "small"),
	render_tile("Заказы", "567", "green", "small"),
]

# Хорошо - большие плитки для важной информации
feature_tiles = [
	render_tile("Новая функция", "Описание", "orange", "large"),
	render_tile("Обновление", "Детали", "green", "large"),
]
```

### 2. Выбирайте подходящие цвета

```python
# Хорошо - семантические цвета
tiles = [
	render_tile("Успех", "100%", "green"),  # Зеленый для успеха
	render_tile("Внимание", "75%", "orange"),  # Оранжевый для предупреждения
	render_tile("Ошибка", "25%", "red"),  # Красный для ошибки
	render_tile("Информация", "50%", "blue"),  # Синий для информации
]
```

### 3. Добавляйте иконки для ясности

```python
# Хорошо
tiles = [
	render_tile("Пользователи", "1,234", "blue", icon="users"),
	render_tile("Заказы", "567", "green", icon="cart"),
	render_tile("Доход", "$12,345", "orange", icon="dollar"),
]

# Плохо
tiles = [
	render_tile("Пользователи", "1,234", "blue"),
	render_tile("Заказы", "567", "green"),
	render_tile("Доход", "$12,345", "orange"),
]
```

### 4. Группируйте связанные плитки

```python
def dashboard_tiles_view(request):
	# Плитки статистики
	stats_tiles = [
		render_tile("Пользователи", "1,234", "blue", "small", "users"),
		render_tile("Заказы", "567", "green", "small", "cart"),
		render_tile("Доход", "$12,345", "orange", "small", "dollar"),
		render_tile("Товары", "89", "red", "small", "package"),
	]

	# Плитки действий
	action_tiles = [
		render_tile("Создать", "Новый проект", "blue", "medium", "plus"),
		render_tile("Импорт", "Загрузить данные", "green", "medium", "upload"),
		render_tile("Экспорт", "Скачать отчет", "orange", "medium", "download"),
	]

	context = {
		'stats_tiles': stats_tiles,
		'action_tiles': action_tiles,
	}

	return render(request, 'dashboard_tiles.html', context)
```

## Решение проблем

### Плитка не отображается

1. Проверьте, что функция `render_tile` импортирована
2. Убедитесь, что в шаблоне используется `|safe` фильтр
3. Проверьте консоль браузера на ошибки

### Стили не применяются

1. Убедитесь, что MetroUI5 CSS загружен
2. Проверьте, что нет конфликтующих CSS правил
3. Используйте инспектор браузера для проверки применяемых стилей

### Иконки не отображаются

1. Убедитесь, что CSS иконок MetroUI загружен
2. Проверьте правильность названия иконки
3. Убедитесь, что иконка существует в MetroUI

## Связанные компоненты

- [Карточки](cards.md) - для группировки плиток
- [Кнопки](buttons.md) - для действий в плитках
- [Алерты](alerts.md) - для важных сообщений
- [Таблицы](tables.md) - для структурированных данных

## Следующие шаги

Теперь, когда вы освоили плитки:

1. Изучите другие [компоненты](../) для создания полноценных интерфейсов
2. Ознакомьтесь с [примерами](../../getting-started/examples.md)
3. Изучите [API справочник](../../api-reference/) для детальной информации
4. Создайте информативные и красивые плитки для ваших проектов!
