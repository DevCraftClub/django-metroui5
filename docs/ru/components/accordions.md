# Аккордеоны

MetroUI5 Django предоставляет гибкую систему компонентов аккордеона для создания сворачиваемых секций контента, которые могут быть развернуты и свернуты независимо.

## Вызов

```python
from metroui5.components import render_accordion

render_accordion([{"title": "Один", "content": "Текст"}])
```

Пустой список даёт `<div class="accordion" id="accordion-component" data-role="accordion"></div>`. `None` вызывает `TypeError`.

В шаблоне тот же список передаётся как `items`:

```django
{% metroui5_accordion items %}
```

## Базовое использование

```python
from metroui5.components import render_accordion

# Простой аккордеон
items = [
    {"title": "Секция 1", "content": "Содержимое для секции 1"},
    {"title": "Секция 2", "content": "Содержимое для секции 2"},
    {"title": "Секция 3", "content": "Содержимое для секции 3"}
]

accordion_html = render_accordion(items)
```

## Параметры

### `render_accordion(items, **attrs)`

- **items** (list): Список элементов аккордеона, каждый содержит:
  - `title` (str): Заголовок секции
  - `content` (str): Содержимое секции (может быть HTML)
  - `active` (bool, optional): Активна ли эта секция изначально
  - `disabled` (bool, optional): Отключена ли эта секция
- **attrs** (dict): Дополнительные HTML атрибуты для контейнера аккордеона

## Примеры

### Базовый аккордеон

```python
from metroui5.components import render_accordion

items = [
    {"title": "Что такое MetroUI5?", "content": "MetroUI5 - это современный UI фреймворк для создания адаптивных веб-приложений."},
    {"title": "Как его установить?", "content": "Вы можете установить MetroUI5 через npm, CDN или скачать файлы напрямую."},
    {"title": "Это бесплатно?", "content": "Да, MetroUI5 - это открытый исходный код и бесплатен для использования в ваших проектах."}
]

accordion = render_accordion(items)
```

### Аккордеон с активной секцией

```python
items = [
    {"title": "Начало работы", "content": "Содержимое для начала работы...", "active": True},
    {"title": "Конфигурация", "content": "Содержимое конфигурации..."},
    {"title": "Продвинутое использование", "content": "Содержимое продвинутого использования..."}
]

accordion = render_accordion(items, class="accordion accordion-primary")
```

### Аккордеон с пользовательскими классами

```python
accordion = render_accordion(
    items=[
        {"title": "Секция 1", "content": "Содержимое 1"},
        {"title": "Секция 2", "content": "Содержимое 2"},
        {"title": "Секция 3", "content": "Содержимое 3"}
    ],
    class="accordion accordion-large",
    id="main-accordion"
)
```

## CSS классы аккордеона MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации аккордеона:

### Классы стилей

- `accordion` - Базовый класс аккордеона
- `accordion-primary` - Основной стиль аккордеона
- `accordion-secondary` - Вторичный стиль аккордеона
- `accordion-success` - Стиль аккордеона успеха
- `accordion-warning` - Стиль аккордеона предупреждения
- `accordion-danger` - Стиль аккордеона опасности
- `accordion-info` - Информационный стиль аккордеона

### Классы размеров

- `accordion-small` - Маленький аккордеон
- `accordion-large` - Большой аккордеон
- `accordion-compact` - Компактный аккордеон

### Классы поведения

- `accordion-multiple` - Разрешить открытие нескольких секций
- `accordion-single` - Только одна секция открыта одновременно
- `accordion-closeable` - Разрешить закрытие всех секций

## Типы аккордеонов

### FAQ аккордеон

```python
def create_faq_accordion(faq_items):
    """Создать FAQ аккордеон с общими вопросами."""

    return render_accordion(
        faq_items,
        class="accordion accordion-faq"
    )

# Использование
faq_items = [
    {
        "title": "Как начать работу с MetroUI5?",
        "content": "Чтобы начать, включите CSS и JavaScript файлы MetroUI5 в ваш проект и начните использовать компоненты."
    },
    {
        "title": "Адаптивен ли MetroUI5?",
        "content": "Да, MetroUI5 полностью адаптивен и отлично работает на настольных компьютерах, планшетах и мобильных устройствах."
    },
    {
        "title": "Могу ли я настроить тему?",
        "content": "Абсолютно! MetroUI5 предоставляет обширные возможности темизации и CSS переменные для настройки."
    },
    {
        "title": "Какие браузеры поддерживаются?",
        "content": "MetroUI5 поддерживает все современные браузеры, включая Chrome, Firefox, Safari и Edge."
    }
]

faq_accordion = create_faq_accordion(faq_items)
```

### Аккордеон настроек

```python
def create_settings_accordion(settings_groups):
    """Создать аккордеон настроек с сгруппированными опциями."""

    items = []
    for group in settings_groups:
        content = "<form class='settings-form'>"
        for setting in group['settings']:
            if setting['type'] == 'checkbox':
                content += f"""
                <div class='form-group'>
                    <label class='checkbox'>
                        <input type='checkbox' data-role='checkbox' {'checked' if setting.get('value') else ''}>
                        <span class='check'></span>
                        {setting['label']}
                    </label>
                </div>
                """
            elif setting['type'] == 'select':
                content += f"""
                <div class='form-group'>
                    <label>{setting['label']}:</label>
                    <select class='select' data-role='select'>
                        {''.join([f'<option value="{opt["value"]}" {"selected" if opt["value"] == setting.get("value") else ""}>{opt["label"]}</option>' for opt in setting['options']])}
                    </select>
                </div>
                """
        content += "</form>"

        items.append({
            "title": group['title'],
            "content": content,
            "active": group.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-settings")

# Использование
settings_groups = [
    {
        "title": "Общие настройки",
        "active": True,
        "settings": [
            {"type": "checkbox", "label": "Включить уведомления", "value": True},
            {"type": "select", "label": "Язык", "value": "ru", "options": [
                {"value": "ru", "label": "Русский"},
                {"value": "en", "label": "Английский"},
                {"value": "de", "label": "Немецкий"}
            ]}
        ]
    },
    {
        "title": "Настройки конфиденциальности",
        "settings": [
            {"type": "checkbox", "label": "Разрешить сбор данных", "value": False},
            {"type": "checkbox", "label": "Делиться статистикой использования", "value": True}
        ]
    }
]

settings_accordion = create_settings_accordion(settings_groups)
```

### Аккордеон документации

```python
def create_docs_accordion(doc_sections):
    """Создать аккордеон документации с примерами кода."""

    items = []
    for section in doc_sections:
        content = f"""
        <div class='doc-section'>
            <p>{section['description']}</p>
            <h4>Пример:</h4>
            <pre><code>{section['code_example']}</code></pre>
            {f"<p><strong>Примечание:</strong> {section['note']}</p>" if section.get('note') else ""}
        </div>
        """

        items.append({
            "title": section['title'],
            "content": content,
            "active": section.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-docs")

# Использование
doc_sections = [
    {
        "title": "Базовое использование",
        "active": True,
        "description": "Узнайте, как создать базовый компонент аккордеона.",
        "code_example": """from metroui5.components import render_accordion

items = [
    {"title": "Секция 1", "content": "Содержимое 1"},
    {"title": "Секция 2", "content": "Содержимое 2"}
]

accordion = render_accordion(items)""",
        "note": "Убедитесь, что включены CSS и JavaScript файлы MetroUI5."
    },
    {
        "title": "Продвинутая конфигурация",
        "description": "Настройка поведения и стилизации аккордеона.",
        "code_example": """accordion = render_accordion(
    items,
    class="accordion accordion-multiple",
    data_role="accordion"
)""",
        "note": "Используйте 'accordion-multiple' чтобы разрешить открытие нескольких секций."
    }
]

docs_accordion = create_docs_accordion(doc_sections)
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_accordion items=accordion_items class="accordion
accordion-primary" %}
```

## Продвинутые примеры

### Аккордеон с иконками

```python
def create_icon_accordion(items_with_icons):
    """Создать аккордеон с иконками в заголовках."""

    items = []
    for item in items_with_icons:
        title_with_icon = f"""
        <span class='accordion-title'>
            <span class='mif-{item['icon']}'></span>
            {item['title']}
        </span>
        """

        items.append({
            "title": title_with_icon,
            "content": item['content'],
            "active": item.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-with-icons")

# Использование
icon_items = [
    {"icon": "user", "title": "Профиль", "content": "Управление настройками профиля..."},
    {"icon": "cog", "title": "Настройки", "content": "Настройка параметров приложения..."},
    {"icon": "shield", "title": "Безопасность", "content": "Опции безопасности и конфиденциальности..."},
    {"icon": "bell", "title": "Уведомления", "content": "Предпочтения уведомлений..."}
]

icon_accordion = create_icon_accordion(icon_items)
```

### Аккордеон с индикаторами прогресса

```python
def create_progress_accordion(progress_items):
    """Создать аккордеон, показывающий прогресс через шаги."""

    items = []
    for i, item in enumerate(progress_items):
        progress = item.get('progress', 0)
        status_class = "success" if progress == 100 else "warning" if progress > 0 else "default"

        title_with_progress = f"""
        <span class='accordion-title'>
            {item['title']}
            <span class='progress-indicator badge badge-{status_class}'>{progress}%</span>
        </span>
        """

        content = f"""
        <div class='step-content'>
            <p>{item['description']}</p>
            <div class='progress-bar'>
                <div class='progress-fill' style='width: {progress}%'></div>
            </div>
            {item['content']}
        </div>
        """

        items.append({
            "title": title_with_progress,
            "content": content,
            "active": item.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-progress")

# Использование
progress_items = [
    {
        "title": "Настройка",
        "description": "Начальная настройка проекта",
        "progress": 100,
        "content": "Настройка проекта успешно завершена."
    },
    {
        "title": "Конфигурация",
        "description": "Настройка параметров приложения",
        "progress": 75,
        "content": "Большинство настроек сконфигурированы, некоторые опциональные настройки остались."
    },
    {
        "title": "Тестирование",
        "description": "Запуск тестов и валидация",
        "progress": 25,
        "content": "Базовые тесты завершены, комплексное тестирование в процессе."
    },
    {
        "title": "Развертывание",
        "description": "Развертывание в продакшн",
        "progress": 0,
        "content": "Готово к началу процесса развертывания."
    }
]

progress_accordion = create_progress_accordion(progress_items)
```

### Аккордеон с валидацией форм

```python
def create_form_accordion(form_sections):
    """Создать аккордеон с секциями форм и валидацией."""

    items = []
    for section in form_sections:
        content = f"""
        <form class='accordion-form' data-section='{section['id']}'>
            {section['form_content']}
            <div class='form-actions'>
                <button type='button' class='button button-primary' onclick='validateSection("{section['id']}")'>
                    Проверить секцию
                </button>
                <button type='button' class='button button-secondary' onclick='saveSection("{section['id']}")'>
                    Сохранить секцию
                </button>
            </div>
        </form>
        """

        items.append({
            "title": section['title'],
            "content": content,
            "active": section.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-form")

# Использование
form_sections = [
    {
        "id": "personal-info",
        "title": "Личная информация",
        "active": True,
        "form_content": """
        <div class='form-group'>
            <label>Имя:</label>
            <input type='text' class='input' name='first_name' required>
        </div>
        <div class='form-group'>
            <label>Фамилия:</label>
            <input type='text' class='input' name='last_name' required>
        </div>
        <div class='form-group'>
            <label>Email:</label>
            <input type='email' class='input' name='email' required>
        </div>
        """
    },
    {
        "id": "contact-info",
        "title": "Контактная информация",
        "form_content": """
        <div class='form-group'>
            <label>Телефон:</label>
            <input type='tel' class='input' name='phone'>
        </div>
        <div class='form-group'>
            <label>Адрес:</label>
            <textarea class='textarea' name='address'></textarea>
        </div>
        """
    }
]

form_accordion = create_form_accordion(form_sections)
```

### Вложенный аккордеон

```python
def create_nested_accordion(main_sections):
    """Создать аккордеон с вложенными подсекциями."""

    items = []
    for section in main_sections:
        if section.get('subsections'):
            # Создать вложенный аккордеон для подсекций
            nested_items = []
            for subsection in section['subsections']:
                nested_items.append({
                    "title": subsection['title'],
                    "content": subsection['content']
                })

            nested_accordion = render_accordion(nested_items, class="accordion accordion-nested")
            content = f"""
            <div class='main-section'>
                <p>{section.get('description', '')}</p>
                {nested_accordion}
            </div>
            """
        else:
            content = section['content']

        items.append({
            "title": section['title'],
            "content": content,
            "active": section.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-nested")

# Использование
nested_sections = [
    {
        "title": "Фронтенд разработка",
        "description": "Технологии и инструменты фронтенд разработки.",
        "subsections": [
            {"title": "HTML/CSS", "content": "Основы HTML5 и CSS3..."},
            {"title": "JavaScript", "content": "Современная разработка на JavaScript..."},
            {"title": "Фреймворки", "content": "React, Vue, Angular фреймворки..."}
        ]
    },
    {
        "title": "Бэкенд разработка",
        "description": "Технологии и инструменты бэкенд разработки.",
        "subsections": [
            {"title": "Python", "content": "Веб-разработка на Python..."},
            {"title": "Node.js", "content": "Node.js и Express..."},
            {"title": "Базы данных", "content": "SQL и NoSQL базы данных..."}
        ]
    }
]

nested_accordion = create_nested_accordion(nested_sections)
```

## Интеграция с JavaScript

### Управление аккордеоном

```javascript
// Программно открыть/закрыть секции аккордеона
function toggleAccordionSection(accordionId, sectionIndex) {
	const accordion = document.querySelector(`#${accordionId}`);
	if (accordion) {
		const sections = accordion.querySelectorAll(".accordion-section");
		const section = sections[sectionIndex];
		if (section) {
			section.classList.toggle("active");
		}
	}
}

// Открыть все секции
function openAllSections(accordionId) {
	const accordion = document.querySelector(`#${accordionId}`);
	if (accordion) {
		const sections = accordion.querySelectorAll(".accordion-section");
		sections.forEach((section) => section.classList.add("active"));
	}
}

// Закрыть все секции
function closeAllSections(accordionId) {
	const accordion = document.querySelector(`#${accordionId}`);
	if (accordion) {
		const sections = accordion.querySelectorAll(".accordion-section");
		sections.forEach((section) => section.classList.remove("active"));
	}
}
```

### События аккордеона

```javascript
// Обработка событий аккордеона
document.querySelectorAll(".accordion").forEach((accordion) => {
	accordion.addEventListener("accordion-open", function (event) {
		console.log("Секция аккордеона открыта:", event.detail.section);
	});

	accordion.addEventListener("accordion-close", function (event) {
		console.log("Секция аккордеона закрыта:", event.detail.section);
	});

	accordion.addEventListener("accordion-toggle", function (event) {
		console.log("Секция аккордеона переключена:", event.detail.section);
	});
});
```

### Валидация аккордеона

```javascript
// Валидация секций формы аккордеона
function validateAccordionSection(sectionId) {
	const section = document.querySelector(`[data-section="${sectionId}"]`);
	if (section) {
		const form = section.querySelector("form");
		const inputs = form.querySelectorAll(
			"input[required], select[required], textarea[required]"
		);

		let isValid = true;
		inputs.forEach((input) => {
			if (!input.value.trim()) {
				input.classList.add("input-error");
				isValid = false;
			} else {
				input.classList.remove("input-error");
			}
		});

		return isValid;
	}
	return false;
}

// Сохранить секцию аккордеона
function saveSection(sectionId) {
	if (validateAccordionSection(sectionId)) {
		const form = document.querySelector(`[data-section="${sectionId}"] form`);
		const formData = new FormData(form);

		// Отправить данные на сервер
		fetch("/save-section/", {
			method: "POST",
			body: formData,
		}).then((response) => {
			if (response.ok) {
				showNotification("Секция успешно сохранена!", "success");
			} else {
				showNotification("Ошибка сохранения секции", "error");
			}
		});
	} else {
		showNotification("Пожалуйста, заполните все обязательные поля", "warning");
	}
}
```

## Лучшие практики

1. **Используйте четкие заголовки**: Делайте заголовки секций описательными и краткими
2. **Организуйте логично**: Группируйте связанный контент в одной секции
3. **Ограничивайте количество секций**: Не создавайте слишком много секций (рекомендуется максимум 5-7)
4. **Предоставляйте визуальную обратную связь**: Используйте иконки или индикаторы для показа статуса секции
5. **Обрабатывайте состояния загрузки**: Показывайте индикаторы загрузки для динамического контента
6. **Делайте доступным**: Убедитесь, что навигация с клавиатуры работает правильно
7. **Используйте консистентную стилизацию**: Применяйте консистентные классы по всему приложению

## Связанные компоненты

- [Панели](panels.md) - Для сворачиваемых областей контента
- [Вкладки](tabs.md) - Для организации контента по вкладкам
- [Карточки](cards.md) - Для организации контента на основе карточек
- [Формы](forms.md) - Для содержимого форм в аккордеонах
