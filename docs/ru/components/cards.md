# Карточки (Cards)

Компонент для создания информационных карточек с заголовком, содержимым и подвалом.

## Основное использование

### Простая карточка

```python
from metroui5.components import render_card

# Базовая карточка
card = render_card("Заголовок", "Содержимое карточки")
```

### Карточка с подвалом

```python
# Карточка с заголовком, содержимым и подвалом
card = render_card(
	header="Заголовок карточки",
	content="Основное содержимое карточки",
	footer="Подвал карточки"
)
```

### Карточка только с содержимым

```python
# Карточка без заголовка и подвала
card = render_card(content="Только содержимое")
```

## Параметры

### `header` (опционально)

Заголовок карточки. Если не указан, заголовок не отображается.

```python
card = render_card(header="Заголовок", content="Содержимое")
```

### `content` (опционально)

Основное содержимое карточки. Если не указано, содержимое не отображается.

```python
card = render_card(header="Заголовок", content="Содержимое")
```

### `footer` (опционально)

Подвал карточки. Если не указан, подвал не отображается.

```python
card = render_card(
	header="Заголовок",
	content="Содержимое",
	footer="Подвал"
)
```

### `**attrs` (опционально)

Дополнительные HTML атрибуты.

```python
card = render_card(
	header="Заголовок",
	content="Содержимое",
	**{"class": "custom-card", "id": "myCard"}
)
```

## Примеры использования

### В представлении

```python
from metroui5.components import render_card


def dashboard(request):
	context = {
		'info_card': render_card(
			header="Информация",
			content="Это информационная карточка с важными данными.",
			footer="Обновлено сегодня"
		),
		'stats_card': render_card(
			header="Статистика",
			content="""
                <div class="row">
                    <div class="cell-md-6">
                        <strong>Пользователи:</strong> 1,234
                    </div>
                    <div class="cell-md-6">
                        <strong>Заказы:</strong> 567
                    </div>
                </div>
            """
		),
		'action_card': render_card(
			header="Действия",
			content="Выберите действие для продолжения работы",
			footer="Доступно 24/7"
		)
	}
	return render(request, 'dashboard.html', context)
```

### В шаблоне

```html
{% extends 'base.html' %} {% block content %}
<div class="row">
    <div class="cell-md-4">{{ info_card|safe }}</div>
    <div class="cell-md-4">{{ stats_card|safe }}</div>
    <div class="cell-md-4">{{ action_card|safe }}</div>
</div>
{% endblock %}
```

### Карточки с HTML содержимым

```python
def rich_content_view(request):
	# Карточка с HTML содержимым
	html_content = """
        <div class="alert alert-info">
            <strong>Внимание!</strong> Это важная информация.
        </div>
        <p>Дополнительный текст с <em>форматированием</em>.</p>
        <ul>
            <li>Пункт 1</li>
            <li>Пункт 2</li>
            <li>Пункт 3</li>
        </ul>
    """

	rich_card = render_card(
		header="Богатое содержимое",
		content=html_content,
		footer="HTML поддерживается"
	)

	return render(request, 'rich_content.html', {'card': rich_card})
```

### Карточки с кнопками в подвале

```python
from metroui5.components import render_card, render_button


def action_cards_view(request):
	# Кнопки для подвала
	action_buttons = [
		render_button("Редактировать", button_type="secondary", size="small"),
		render_button("Удалить", button_type="alert", size="small"),
	]

	# Карточка с кнопками в подвале
	action_card = render_card(
		header="Управление",
		content="Выберите действие для этого элемента",
		footer=" ".join([btn for btn in action_buttons])
	)

	return render(request, 'action_cards.html', {'card': action_card})
```

## Кастомизация

### Дополнительные CSS классы

```python
card = render_card(
	header="Кастомная карточка",
	content="Содержимое",
	**{"class": "card-custom my-card"}
)
```

### Атрибуты для JavaScript

```python
card = render_card(
	header="Интерактивная карточка",
	content="Содержимое",
	**{
		"data-card-id": "123",
		"data-type": "info",
		"onclick": "handleCardClick(this)"
	}
)
```

### Стилизация через CSS

```css
/* Кастомные стили для карточек */
.card-custom {
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
}

.my-card {
    border-left: 4px solid #007bff;
}

.my-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}

/* Стили для заголовка */
.card-custom .card-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-weight: bold;
}

/* Стили для подвала */
.card-custom .card-footer {
    background-color: #f8f9fa;
    border-top: 1px solid #dee2e6;
}
```

## Группировка карточек

### Сетка карточек

```python
def grid_cards_view(request):
	# Создаем несколько карточек
	cards = []
	for i in range(6):
		card = render_card(
			header=f"Карточка {i + 1}",
			content=f"Содержимое карточки номер {i + 1}",
			footer=f"Подвал {i + 1}"
		)
		cards.append(card)

	return render(request, 'grid_cards.html', {'cards': cards})
```

### Шаблон для сетки

```html
{% extends 'base.html' %} {% block content %}
<div class="row">
    {% for card in cards %}
    <div class="cell-md-4 cell-lg-3">{{ card|safe }}</div>
    {% endfor %}
</div>
{% endblock %}
```

## Лучшие практики

### 1. Используйте заголовки для ясности

```python
# Хорошо
card = render_card(
	header="Статистика продаж",
	content="Данные за текущий месяц"
)

# Плохо
card = render_card(content="Статистика продаж - данные за текущий месяц")
```

### 2. Группируйте связанную информацию

```python
def user_profile_view(request):
	# Карточка с основной информацией
	profile_card = render_card(
		header="Профиль пользователя",
		content=f"""
            <p><strong>Имя:</strong> {user.first_name} {user.last_name}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Дата регистрации:</strong> {user.date_joined}</p>
        """
	)

	# Карточка с настройками
	settings_card = render_card(
		header="Настройки",
		content="Управление настройками профиля",
		footer="Нажмите для изменения"
	)

	context = {
		'profile_card': profile_card,
		'settings_card': settings_card,
	}
	return render(request, 'user_profile.html', context)
```

### 3. Используйте подвал для действий

```python
def product_card_view(request):
	# Кнопки действий
	action_buttons = [
		render_button("Просмотр", button_type="primary", size="small"),
		render_button("В корзину", button_type="success", size="small"),
	]

	# Карточка товара
	product_card = render_card(
		header=product.name,
		content=f"""
            <img src="{product.image.url}" alt="{product.name}" class="product-image">
            <p><strong>Цена:</strong> ${product.price}</p>
            <p>{product.description}</p>
        """,
		footer=" ".join([btn for btn in action_buttons])
	)

	return render(request, 'product.html', {'card': product_card})
```

### 4. Адаптируйте содержимое

```python
def responsive_cards_view(request):
	# Различное содержимое для разных размеров экрана
	mobile_content = "Краткая информация для мобильных устройств"
	desktop_content = """
        <div class="row">
            <div class="cell-md-6">
                <h4>Детальная информация</h4>
                <p>Полное описание для больших экранов</p>
            </div>
            <div class="cell-md-6">
                <h4>Дополнительные данные</h4>
                <p>Дополнительная информация</p>
            </div>
        </div>
    """

	context = {
		'mobile_card': render_card(
			header="Информация",
			content=mobile_content,
			**{"class": "d-block d-md-none"}
		),
		'desktop_card': render_card(
			header="Информация",
			content=desktop_content,
			**{"class": "d-none d-md-block"}
		)
	}

	return render(request, 'responsive_cards.html', context)
```

## Решение проблем

### Карточка не отображается

1. Проверьте, что функция `render_card` импортирована
2. Убедитесь, что в шаблоне используется `|safe` фильтр
3. Проверьте консоль браузера на ошибки

### Стили не применяются

1. Убедитесь, что MetroUI5 CSS загружен
2. Проверьте, что нет конфликтующих CSS правил
3. Используйте инспектор браузера для проверки применяемых стилей

### HTML не рендерится

1. Убедитесь, что в шаблоне используется `|safe` фильтр
2. Проверьте, что HTML разметка корректна
3. Убедитесь, что нет конфликтов с Django template tags

## Связанные компоненты

- [Кнопки](buttons.md) - для действий в подвале карточек
- [Алерты](alerts.md) - для важных сообщений в карточках
- [Таблицы](tables.md) - для структурированных данных
- [Плитки](tiles.md) - для компактного отображения информации

## Следующие шаги

Теперь, когда вы освоили карточки:

1. Изучите другие [компоненты](../) для создания полноценных интерфейсов
2. Ознакомьтесь с [примерами](../../getting-started/examples.md)
3. Изучите [API справочник](../../api-reference/) для детальной информации
4. Создайте информативные и красивые карточки!


## metroui5_card

```python
render_card()
```

Пустое или неверное значение: `render_card()` даёт `<div class="card"><div class="card-content"></div></div>`.

```django
{% metroui5_card %}
```
