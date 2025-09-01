# Пагинация

MetroUI5 Django предоставляет комплексную систему компонентов пагинации для навигации по большим наборам данных и страницам контента.

## Базовое использование

```python
from metroui5.components import render_pagination

# Простая пагинация
pagination_html = render_pagination(current_page=1, total_pages=10)
```

## Параметры

### `render_pagination(current_page, total_pages, **attrs)`

- **current_page** (int): Номер текущей страницы (начиная с 1)
- **total_pages** (int): Общее количество страниц
- **attrs** (dict): Дополнительные HTML атрибуты

## Примеры

### Базовая пагинация

```python
from metroui5.components import render_pagination

# Простая пагинация
pagination = render_pagination(current_page=3, total_pages=10)
```

### Пагинация с пользовательскими классами

```python
pagination = render_pagination(
    current_page=5,
    total_pages=20,
    class="pagination pagination-large",
    id="main-pagination"
)
```

### Пагинация с пользовательскими атрибутами

```python
pagination = render_pagination(
    current_page=1,
    total_pages=15,
    data_role="pagination",
    data_ajax="true"
)
```

## Классы пагинации MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации пагинации:

### Классы стилей

- `pagination` - Базовый класс пагинации
- `pagination-primary` - Основной стиль пагинации
- `pagination-secondary` - Вторичный стиль пагинации
- `pagination-success` - Стиль пагинации успеха
- `pagination-warning` - Предупреждающий стиль пагинации
- `pagination-danger` - Опасный стиль пагинации
- `pagination-info` - Информационный стиль пагинации

### Классы размеров

- `pagination-small` - Маленькая пагинация
- `pagination-large` - Большая пагинация
- `pagination-mini` - Мини пагинация

### Классы макета

- `pagination-centered` - Центрированная пагинация
- `pagination-right` - Выровненная по правому краю пагинация
- `pagination-compact` - Компактная пагинация

## Типы пагинации

### Базовая числовая пагинация

```python
def create_numeric_pagination(current_page, total_pages, show_ellipsis=True):
    """Создание числовой пагинации с номерами страниц."""

    return render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-numeric"
    )

# Использование
numeric_pagination = create_numeric_pagination(5, 20)
```

### Пагинация с первой/последней страницей

```python
def create_full_pagination(current_page, total_pages):
    """Создание пагинации с кнопками первой, предыдущей, следующей и последней страницы."""

    pagination_html = f"""
    <nav class="pagination pagination-full">
        <ul class="pagination-list">
            <li class="pagination-item">
                <a href="?page=1" class="pagination-link {'disabled' if current_page == 1 else ''}">
                    <span class="mif-first"></span>
                </a>
            </li>
            <li class="pagination-item">
                <a href="?page={current_page - 1}" class="pagination-link {'disabled' if current_page == 1 else ''}">
                    <span class="mif-left"></span>
                </a>
            </li>
    """

    # Добавление номеров страниц
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)

    for page in range(start_page, end_page + 1):
        active_class = "active" if page == current_page else ""
        pagination_html += f"""
            <li class="pagination-item">
                <a href="?page={page}" class="pagination-link {active_class}">{page}</a>
            </li>
        """

    pagination_html += f"""
            <li class="pagination-item">
                <a href="?page={current_page + 1}" class="pagination-link {'disabled' if current_page == total_pages else ''}">
                    <span class="mif-right"></span>
                </a>
            </li>
            <li class="pagination-item">
                <a href="?page={total_pages}" class="pagination-link {'disabled' if current_page == total_pages else ''}">
                    <span class="mif-last"></span>
                </a>
            </li>
        </ul>
    </nav>
    """

    return pagination_html

# Использование
full_pagination = create_full_pagination(5, 20)
```

### Пагинация с информацией о странице

```python
def create_info_pagination(current_page, total_pages, total_items, items_per_page):
    """Создание пагинации с информацией о странице."""

    start_item = (current_page - 1) * items_per_page + 1
    end_item = min(current_page * items_per_page, total_items)

    info_html = f"""
    <div class="pagination-info">
        Показано с {start_item} по {end_item} из {total_items} записей
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-info"
    )

    return info_html + pagination_html

# Использование
info_pagination = create_info_pagination(3, 10, 95, 10)
```

### Пагинация с селектором размера страницы

```python
def create_pagination_with_size(current_page, total_pages, current_size=10, size_options=None):
    """Создание пагинации с селектором размера страницы."""

    if size_options is None:
        size_options = [10, 25, 50, 100]

    size_selector = f"""
    <div class="pagination-size">
        <label>Показать:</label>
        <select class="select" onchange="changePageSize(this.value)">
    """

    for size in size_options:
        selected = "selected" if size == current_size else ""
        size_selector += f'<option value="{size}" {selected}>{size}</option>'

    size_selector += """
        </select>
        <span>на странице</span>
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-size"
    )

    return size_selector + pagination_html

# Использование
pagination_with_size = create_pagination_with_size(2, 8, 25, [10, 25, 50])
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_pagination current_page=3 total_pages=10
class="pagination pagination-primary" %}
```

## Расширенные примеры

### Пагинация с AJAX

```python
def create_ajax_pagination(current_page, total_pages, ajax_url="/api/data/"):
    """Создание пагинации с AJAX загрузкой."""

    pagination_html = f"""
    <nav class="pagination pagination-ajax" data-ajax-url="{ajax_url}">
        <ul class="pagination-list">
    """

    # Кнопка "Предыдущая"
    if current_page > 1:
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="{current_page - 1}">
                    <span class="mif-left"></span>
                </a>
            </li>
        """

    # Номера страниц
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)

    if start_page > 1:
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="1">1</a>
            </li>
        """
        if start_page > 2:
            pagination_html += '<li class="pagination-item"><span class="pagination-ellipsis">...</span></li>'

    for page in range(start_page, end_page + 1):
        active_class = "active" if page == current_page else ""
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link {active_class}" data-page="{page}">{page}</a>
            </li>
        """

    if end_page < total_pages:
        if end_page < total_pages - 1:
            pagination_html += '<li class="pagination-item"><span class="pagination-ellipsis">...</span></li>'
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="{total_pages}">{total_pages}</a>
            </li>
        """

    # Кнопка "Следующая"
    if current_page < total_pages:
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="{current_page + 1}">
                    <span class="mif-right"></span>
                </a>
            </li>
        """

    pagination_html += """
        </ul>
    </nav>
    """

    return pagination_html

# Использование
ajax_pagination = create_ajax_pagination(5, 20, "/api/users/")
```

### Пагинация с переходом на страницу

```python
def create_jump_pagination(current_page, total_pages):
    """Создание пагинации с полем ввода для перехода на страницу."""

    jump_input = f"""
    <div class="pagination-jump">
        <label>Перейти на страницу:</label>
        <input type="number" class="input input-mini"
               min="1" max="{total_pages}" value="{current_page}"
               onchange="jumpToPage(this.value)">
        <button class="button button-mini" onclick="jumpToPage()">Перейти</button>
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-jump"
    )

    return pagination_html + jump_input

# Использование
jump_pagination = create_jump_pagination(5, 20)
```

### Пагинация с резюме результатов

```python
def create_summary_pagination(current_page, total_pages, total_items, items_per_page, search_term=""):
    """Создание пагинации с детальным резюме результатов."""

    start_item = (current_page - 1) * items_per_page + 1
    end_item = min(current_page * items_per_page, total_items)

    summary_html = f"""
    <div class="pagination-summary">
        <div class="summary-text">
            {f'Результаты для "{search_term}": ' if search_term else ''}
            Показано с {start_item} по {end_item} из {total_items} записей
        </div>
        <div class="summary-pages">
            Страница {current_page} из {total_pages}
        </div>
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-summary"
    )

    return summary_html + pagination_html

# Использование
summary_pagination = create_summary_pagination(
    current_page=3,
    total_pages=10,
    total_items=95,
    items_per_page=10,
    search_term="python"
)
```

### Пагинация с пользовательской стилизацией

```python
def create_custom_pagination(current_page, total_pages, theme="primary"):
    """Создание пагинации с пользовательской тематической стилизацией."""

    theme_classes = {
        "primary": "pagination-primary",
        "success": "pagination-success",
        "warning": "pagination-warning",
        "danger": "pagination-danger",
        "info": "pagination-info"
    }

    theme_class = theme_classes.get(theme, "pagination-primary")

    return render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class=f"pagination {theme_class} pagination-custom"
    )

# Использование
custom_pagination = create_custom_pagination(5, 20, "success")
```

### Пагинация с состояниями загрузки

```python
def create_loading_pagination(current_page, total_pages, loading=False):
    """Создание пагинации с состоянием загрузки."""

    loading_class = "pagination-loading" if loading else ""

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class=f"pagination {loading_class}"
    )

    if loading:
        loading_indicator = """
        <div class="pagination-loading-indicator">
            <span class="spinner"></span>
            Загрузка...
        </div>
        """
        return pagination_html + loading_indicator

    return pagination_html

# Использование
loading_pagination = create_loading_pagination(5, 20, loading=True)
```

### Адаптивная пагинация

```python
def create_responsive_pagination(current_page, total_pages):
    """Создание адаптивной пагинации, которая адаптируется к размеру экрана."""

    return render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-responsive"
    )

# Использование
responsive_pagination = create_responsive_pagination(5, 20)
```

## Интеграция с JavaScript

### AJAX пагинация

```javascript
// Обработка AJAX пагинации
document
	.querySelectorAll(".pagination-ajax .pagination-link")
	.forEach((link) => {
		link.addEventListener("click", function (e) {
			e.preventDefault();

			const page = this.getAttribute("data-page");
			const ajaxUrl =
				this.closest(".pagination-ajax").getAttribute("data-ajax-url");

			loadPageContent(page, ajaxUrl);
		});
	});

function loadPageContent(page, url) {
	// Показать состояние загрузки
	showPaginationLoading();

	// Выполнить AJAX запрос
	fetch(`${url}?page=${page}`)
		.then((response) => response.json())
		.then((data) => {
			// Обновить контент
			updateContent(data.content);

			// Обновить пагинацию
			updatePagination(data.pagination);

			// Скрыть состояние загрузки
			hidePaginationLoading();
		})
		.catch((error) => {
			console.error("Ошибка загрузки страницы:", error);
			hidePaginationLoading();
		});
}

function showPaginationLoading() {
	const pagination = document.querySelector(".pagination");
	pagination.classList.add("pagination-loading");
}

function hidePaginationLoading() {
	const pagination = document.querySelector(".pagination");
	pagination.classList.remove("pagination-loading");
}
```

### Переход на страницу

```javascript
// Обработка перехода на страницу
function jumpToPage(page) {
	const pageNum = parseInt(page);
	const totalPages = parseInt(
		document.querySelector(".pagination").getAttribute("data-total-pages")
	);

	if (pageNum >= 1 && pageNum <= totalPages) {
		// Перейти на страницу
		window.location.href = `?page=${pageNum}`;
	} else {
		alert(`Пожалуйста, введите номер страницы от 1 до ${totalPages}`);
	}
}
```

### Изменение размера страницы

```javascript
// Обработка изменения размера страницы
function changePageSize(newSize) {
	const currentUrl = new URL(window.location);
	currentUrl.searchParams.set("page_size", newSize);
	currentUrl.searchParams.set("page", "1"); // Сбросить на первую страницу

	window.location.href = currentUrl.toString();
}
```

### События пагинации

```javascript
// Обработка событий пагинации
document.querySelectorAll(".pagination").forEach((pagination) => {
	pagination.addEventListener("pagination-change", function (event) {
		console.log("Страница изменена на:", event.detail.page);

		// Обновить URL без перезагрузки страницы
		const url = new URL(window.location);
		url.searchParams.set("page", event.detail.page);
		window.history.pushState({}, "", url);
	});
});

// Пользовательское событие изменения пагинации
function triggerPaginationChange(page) {
	const pagination = document.querySelector(".pagination");
	const event = new CustomEvent("pagination-change", {
		detail: { page: page },
	});
	pagination.dispatchEvent(event);
}
```

### Навигация по пагинации с клавиатуры

```javascript
// Обработка навигации с клавиатуры
document.addEventListener("keydown", function (e) {
	const pagination = document.querySelector(".pagination");
	if (!pagination) return;

	const currentPage = parseInt(pagination.getAttribute("data-current-page"));
	const totalPages = parseInt(pagination.getAttribute("data-total-pages"));

	switch (e.key) {
		case "ArrowLeft":
			if (currentPage > 1) {
				navigateToPage(currentPage - 1);
			}
			break;
		case "ArrowRight":
			if (currentPage < totalPages) {
				navigateToPage(currentPage + 1);
			}
			break;
		case "Home":
			navigateToPage(1);
			break;
		case "End":
			navigateToPage(totalPages);
			break;
	}
});

function navigateToPage(page) {
	const pagination = document.querySelector(".pagination");
	const link = pagination.querySelector(`[data-page="${page}"]`);
	if (link) {
		link.click();
	}
}
```

## Лучшие практики

1. **Используйте соответствующие размеры страниц**: Выбирайте размеры страниц, которые балансируют производительность и удобство использования
2. **Предоставляйте четкую навигацию**: Делайте очевидным, как переходить между страницами
3. **Показывайте текущую позицию**: Всегда четко указывайте текущую страницу
4. **Обрабатывайте крайние случаи**: Учитывайте первую страницу, последнюю страницу и пустые результаты
5. **Используйте последовательную стилизацию**: Применяйте последовательные стили пагинации во всем приложении
6. **Учитывайте мобильных пользователей**: Обеспечивайте хорошую работу пагинации на мобильных устройствах
7. **Предоставляйте альтернативы**: Рассмотрите бесконечную прокрутку или "загрузить еще" для некоторых случаев использования

## Связанные компоненты

- [Таблицы](tables.md) - Для табличных данных с пагинацией
- [Списки](lists.md) - Для контента списков с пагинацией
- [Навигация](navigation.md) - Для навигации между страницами
- [Карточки](cards.md) - Для макетов карточек с пагинацией
