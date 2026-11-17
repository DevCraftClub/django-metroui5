# Диалоги

Компонент для создания модальных диалогов и всплывающих окон для взаимодействия с пользователем, подтверждений и отображения контента.

## Базовое использование

### Простой диалог

```python
from metroui5.components import render_dialog

# Базовый диалог
dialog_html = render_dialog(
    title="Подтверждение",
    content="Вы уверены, что хотите продолжить?"
)
```

### Диалог с действиями

```python
# Диалог с кнопками действий
dialog_html = render_dialog(
    title="Удалить элемент",
    content="Это действие нельзя отменить. Вы уверены?",
    actions=[
        {"text": "Отмена", "class": "button-secondary"},
        {"text": "Удалить", "class": "button-danger"}
    ]
)
```

### Пользовательский диалог

```python
# Пользовательский диалог с определенными опциями
dialog_html = render_dialog(
    title="Информация о пользователе",
    content="<p>Имя: Иван Иванов</p><p>Email: ivan@example.com</p>",
    id="user-dialog",
    class="dialog-large",
    close_button=True,
    overlay=True
)
```

## Результат рендеринга

### Базовый диалог

```html
<!-- Ввод -->
render_dialog(title="Подтверждение", content="Вы уверены?")

<!-- Вывод -->
<div class="dialog" data-role="dialog" id="dialog-1">
	<div class="dialog-title">Подтверждение</div>
	<div class="dialog-content">Вы уверены?</div>
	<div class="dialog-actions">
		<button class="button" data-role="close">OK</button>
	</div>
</div>
```

### Диалог с действиями

```html
<!-- Ввод -->
render_dialog(title="Удалить", content="Подтвердить удаление", actions=[{"text":
"Отмена"}, {"text": "Удалить"}])

<!-- Вывод -->
<div class="dialog" data-role="dialog" id="dialog-2">
	<div class="dialog-title">Удалить</div>
	<div class="dialog-content">Подтвердить удаление</div>
	<div class="dialog-actions">
		<button class="button button-secondary">Отмена</button>
		<button class="button button-danger">Удалить</button>
	</div>
</div>
```

### Диалог с оверлеем

```html
<!-- Ввод -->
render_dialog(title="Модальный", content="Содержимое", overlay=True)

<!-- Вывод -->
<div class="dialog-overlay" data-role="overlay">
	<div class="dialog" data-role="dialog" id="dialog-3">
		<div class="dialog-title">Модальный</div>
		<div class="dialog-content">Содержимое</div>
		<div class="dialog-actions">
			<button class="button" data-role="close">OK</button>
		</div>
	</div>
</div>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

```html
{% load metroui5 %}

<!-- Базовый диалог -->
{% metroui5_dialog title="Подтверждение" content="Вы уверены?" %}

<!-- Диалог с действиями -->
{% metroui5_dialog title="Удалить" content="Подтвердить удаление"
actions=action_buttons %}

<!-- Пользовательский диалог -->
{% metroui5_dialog title="Информация" content="Информация" class="dialog-custom"
%}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_dialog

def confirmation_view(request):
    # Создать диалог подтверждения
    confirm_dialog = render_dialog(
        title="Подтвердить действие",
        content="Это действие повлияет на ваши данные. Продолжить?",
        actions=[
            {"text": "Отмена", "class": "button-secondary", "onclick": "cancelAction()"},
            {"text": "Продолжить", "class": "button-primary", "onclick": "proceedAction()"}
        ],
        id="confirm-dialog"
    )

    context = {
        'confirm_dialog': confirm_dialog,
        'action_buttons': [
            {"text": "Отмена", "class": "button-secondary"},
            {"text": "Продолжить", "class": "button-primary"}
        ]
    }
    return render(request, 'confirmation.html', context)
```

```html
<!-- confirmation.html -->
{% load metroui5 %} {% block content %}
<!-- Прямой HTML вывод -->
{{ confirm_dialog|safe }}

<!-- Или используйте тег шаблона -->
{% metroui5_dialog title="Подтвердить действие" content="Продолжить?"
actions=action_buttons %} {% endblock %}
```

## Параметры

### `title` (опционально)

Заголовок, отображаемый в заголовке диалога.

**По умолчанию**: None

**Пример**:

```python
dialog_html = render_dialog(title="Важное уведомление")
```

### `content` (обязательно)

Содержимое для отображения в теле диалога. Может быть HTML.

**Пример**:

```python
dialog_html = render_dialog(content="Простой текстовый контент")
dialog_html = render_dialog(content="<p>HTML контент</p>")
```

### `actions` (опционально)

Список кнопок действий для диалога.

**Формат**:

```python
actions = [
    {
        "text": "Текст кнопки",
        "class": "button-primary",  # Опционально
        "onclick": "function()",    # Опционально
        "id": "button-id"           # Опционально
    }
]
```

**Пример**:

```python
actions = [
    {"text": "Отмена", "class": "button-secondary"},
    {"text": "Сохранить", "class": "button-primary", "onclick": "saveData()"}
]
dialog_html = render_dialog(content="Сохранить изменения?", actions=actions)
```

### `id` (опционально)

Уникальный идентификатор для элемента диалога.

**По умолчанию**: Автоматически сгенерированный ID

**Пример**:

```python
dialog_html = render_dialog(id="my-dialog", content="Содержимое")
```

### `class` (опционально)

Дополнительные CSS классы для стилизации.

**Пример**:

```python
dialog_html = render_dialog(class="dialog-large", content="Содержимое")
```

### `close_button` (опционально)

Показывать ли кнопку закрытия.

**По умолчанию**: `True`

**Пример**:

```python
dialog_html = render_dialog(close_button=False, content="Содержимое")
```

### `overlay` (опционально)

Показывать ли фоновый оверлей.

**По умолчанию**: `False`

**Пример**:

```python
dialog_html = render_dialog(overlay=True, content="Модальное содержимое")
```

### `width` (опционально)

Ширина диалога.

**По умолчанию**: Авто

**Пример**:

```python
dialog_html = render_dialog(width="500px", content="Содержимое")
```

### `height` (опционально)

Высота диалога.

**По умолчанию**: Авто

**Пример**:

```python
dialog_html = render_dialog(height="300px", content="Содержимое")
```

## Продвинутые примеры

### Диалог подтверждения

```python
def create_confirmation_dialog(message, on_confirm, on_cancel=None):
    """Создать диалог подтверждения."""

    actions = [
        {"text": "Отмена", "class": "button-secondary"}
    ]

    if on_cancel:
        actions[0]["onclick"] = on_cancel

    actions.append({
        "text": "Подтвердить",
        "class": "button-danger",
        "onclick": on_confirm
    })

    return render_dialog(
        title="Подтверждение",
        content=message,
        actions=actions,
        overlay=True,
        class="dialog-confirmation"
    )
```

### Диалог с формой

```python
def create_form_dialog(title, form_html, submit_url):
    """Создать диалог с содержимым формы."""

    actions = [
        {"text": "Отмена", "class": "button-secondary", "onclick": "closeDialog()"},
        {"text": "Отправить", "class": "button-primary", "onclick": f"submitForm('{submit_url}')"}
    ]

    return render_dialog(
        title=title,
        content=form_html,
        actions=actions,
        overlay=True,
        class="dialog-form",
        width="600px"
    )
```

### Диалог-уведомление

```python
def create_alert_dialog(message, alert_type="info"):
    """Создать диалог в стиле уведомления."""

    type_classes = {
        "info": "dialog-info",
        "success": "dialog-success",
        "warning": "dialog-warning",
        "error": "dialog-error"
    }

    return render_dialog(
        title="Уведомление",
        content=f'<div class="alert alert-{alert_type}">{message}</div>',
        class=type_classes.get(alert_type, "dialog-info"),
        close_button=True
    )
```

### Диалог загрузки

```python
def create_loading_dialog(message="Загрузка..."):
    """Создать диалог загрузки."""

    content = f"""
    <div class="loading-dialog">
        <div class="spinner"></div>
        <p>{message}</p>
    </div>
    """

    return render_dialog(
        content=content,
        class="dialog-loading",
        close_button=False,
        overlay=True
    )
```

### Многошаговый диалог

```python
def create_multi_step_dialog(steps):
    """Создать диалог с несколькими шагами."""

    step_content = ""
    for i, step in enumerate(steps):
        step_content += f"""
        <div class="dialog-step" id="step-{i}" style="display: {'block' if i == 0 else 'none'};">
            <h3>{step['title']}</h3>
            <div>{step['content']}</div>
        </div>
        """

    actions = [
        {"text": "Предыдущий", "class": "button-secondary", "onclick": "previousStep()", "id": "prev-btn", "style": "display: none;"},
        {"text": "Следующий", "class": "button-primary", "onclick": "nextStep()", "id": "next-btn"},
        {"text": "Завершить", "class": "button-success", "onclick": "finishSteps()", "id": "finish-btn", "style": "display: none;"}
    ]

    return render_dialog(
        title="Многошаговый процесс",
        content=step_content,
        actions=actions,
        overlay=True,
        class="dialog-multi-step",
        width="700px"
    )
```

## Стилизация

### CSS классы

#### Базовые классы

- `dialog` - Базовый класс диалога
- `dialog-primary` - Основной стиль диалога
- `dialog-secondary` - Вторичный стиль диалога

#### Классы размеров

- `dialog-small` - Маленький диалог
- `dialog-large` - Большой диалог
- `dialog-fullscreen` - Полноэкранный диалог

#### Классы типов

- `dialog-info` - Информационный диалог
- `dialog-success` - Диалог успеха
- `dialog-warning` - Диалог предупреждения
- `dialog-error` - Диалог ошибки

#### Классы макета

- `dialog-centered` - Центрированный диалог
- `dialog-top` - Диалог, выровненный по верху
- `dialog-bottom` - Диалог, выровненный по низу

### Пользовательская стилизация

```css
/* Пользовательская стилизация диалога */
.dialog-custom {
	border-radius: 12px;
	box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
	border: none;
}

.dialog-custom .dialog-title {
	background: linear-gradient(135deg, #007acc, #005a99);
	color: white;
	padding: 20px;
	border-radius: 12px 12px 0 0;
	font-size: 1.2em;
	font-weight: bold;
}

.dialog-custom .dialog-content {
	padding: 30px;
	line-height: 1.6;
}

.dialog-custom .dialog-actions {
	padding: 20px;
	border-top: 1px solid #eee;
	text-align: right;
}

/* Стилизация оверлея */
.dialog-overlay {
	background: rgba(0, 0, 0, 0.5);
	backdrop-filter: blur(5px);
}

/* Диалог загрузки */
.dialog-loading .loading-dialog {
	text-align: center;
	padding: 40px;
}

.dialog-loading .spinner {
	width: 40px;
	height: 40px;
	border: 4px solid #f3f3f3;
	border-top: 4px solid #007acc;
	border-radius: 50%;
	animation: spin 1s linear infinite;
	margin: 0 auto 20px;
}

@keyframes spin {
	0% {
		transform: rotate(0deg);
	}
	100% {
		transform: rotate(360deg);
	}
}
```

## Интеграция с JavaScript

### Базовые события диалога

```javascript
// Инициализация диалога
$(document).ready(function () {
	$(".dialog").dialog({
		onShow: function () {
			console.log("Диалог показан");
		},
		onHide: function () {
			console.log("Диалог скрыт");
		},
		onAction: function (action) {
			console.log("Действие нажато:", action);
		},
	});
});
```

### Управление диалогами

```javascript
// Показать диалог
function showDialog(dialogId) {
	const dialog = $(`#${dialogId}`).data("dialog");
	if (dialog) {
		dialog.show();
	}
}

// Скрыть диалог
function hideDialog(dialogId) {
	const dialog = $(`#${dialogId}`).data("dialog");
	if (dialog) {
		dialog.hide();
	}
}

// Закрыть все диалоги
function closeAllDialogs() {
	$(".dialog").each(function () {
		const dialog = $(this).data("dialog");
		if (dialog) {
			dialog.hide();
		}
	});
}
```

### Динамическая загрузка контента

```javascript
// Загрузить контент динамически
function loadDialogContent(dialogId, url) {
	$.ajax({
		url: url,
		method: "GET",
		success: function (data) {
			const dialog = $(`#${dialogId}`);
			dialog.find(".dialog-content").html(data);
			showDialog(dialogId);
		},
		error: function (xhr, status, error) {
			console.error("Ошибка загрузки контента:", error);
			showErrorDialog("Не удалось загрузить контент");
		},
	});
}

// Обновить содержимое диалога
function updateDialogContent(dialogId, content) {
	const dialog = $(`#${dialogId}`);
	dialog.find(".dialog-content").html(content);
}
```

### Обработка форм

```javascript
// Обработать отправку формы в диалоге
function handleDialogForm(dialogId, formData) {
	$.ajax({
		url: "/api/submit-form/",
		method: "POST",
		data: formData,
		success: function (response) {
			if (response.success) {
				hideDialog(dialogId);
				showSuccessDialog("Форма успешно отправлена");
			} else {
				showErrorDialog(response.error);
			}
		},
		error: function (xhr, status, error) {
			showErrorDialog("Произошла ошибка");
		},
	});
}

// Валидировать форму диалога
function validateDialogForm(dialogId) {
	const dialog = $(`#${dialogId}`);
	const form = dialog.find("form");
	const inputs = form.find(
		"input[required], select[required], textarea[required]"
	);

	let isValid = true;
	inputs.each(function () {
		if (!$(this).val().trim()) {
			$(this).addClass("input-error");
			isValid = false;
		} else {
			$(this).removeClass("input-error");
		}
	});

	return isValid;
}
```

### Навигация по многошаговому диалогу

```javascript
// Обработать навигацию по многошаговому диалогу
let currentStep = 0;
const totalSteps = $(".dialog-step").length;

function nextStep() {
	if (currentStep < totalSteps - 1) {
		$(`#step-${currentStep}`).hide();
		currentStep++;
		$(`#step-${currentStep}`).show();
		updateStepButtons();
	}
}

function previousStep() {
	if (currentStep > 0) {
		$(`#step-${currentStep}`).hide();
		currentStep--;
		$(`#step-${currentStep}`).show();
		updateStepButtons();
	}
}

function updateStepButtons() {
	const prevBtn = $("#prev-btn");
	const nextBtn = $("#next-btn");
	const finishBtn = $("#finish-btn");

	prevBtn.toggle(currentStep > 0);
	nextBtn.toggle(currentStep < totalSteps - 1);
	finishBtn.toggle(currentStep === totalSteps - 1);
}

function finishSteps() {
	// Обработать финальный шаг
	const formData = collectFormData();
	handleDialogForm("multi-step-dialog", formData);
}
```

### Действия диалога

```javascript
// Обработать клики по действиям диалога
function handleDialogAction(action, dialogId) {
	switch (action) {
		case "confirm":
			hideDialog(dialogId);
			executeConfirmedAction();
			break;
		case "cancel":
			hideDialog(dialogId);
			break;
		case "save":
			if (validateDialogForm(dialogId)) {
				saveDialogData(dialogId);
			}
			break;
		default:
			console.log("Неизвестное действие:", action);
	}
}

// Выполнить подтвержденное действие
function executeConfirmedAction() {
	// Выполнить действие, которое было подтверждено
	console.log("Действие подтверждено и выполнено");
}

// Сохранить данные диалога
function saveDialogData(dialogId) {
	const dialog = $(`#${dialogId}`);
	const formData = new FormData(dialog.find("form")[0]);

	$.ajax({
		url: "/api/save-data/",
		method: "POST",
		data: formData,
		processData: false,
		contentType: false,
		success: function (response) {
			hideDialog(dialogId);
			showSuccessDialog("Данные успешно сохранены");
		},
		error: function (xhr, status, error) {
			showErrorDialog("Не удалось сохранить данные");
		},
	});
}
```

### Утилитарные функции

```javascript
// Показать диалог успеха
function showSuccessDialog(message) {
    const dialog = render_dialog(
        title="Успех",
        content=message,
        class="dialog-success"
    );
    $('body').append(dialog);
    showDialog('success-dialog');
}

// Показать диалог ошибки
function showErrorDialog(message) {
    const dialog = render_dialog(
        title="Ошибка",
        content=message,
        class="dialog-error"
    );
    $('body').append(dialog);
    showDialog('error-dialog');
}

// Показать диалог подтверждения
function showConfirmationDialog(message, onConfirm) {
    const dialog = render_dialog(
        title="Подтверждение",
        content=message,
        actions=[
            {"text": "Отмена", "class": "button-secondary"},
            {"text": "Подтвердить", "class": "button-danger", "onclick": onConfirm}
        ]
    );
    $('body').append(dialog);
    showDialog('confirm-dialog');
}
```

## Лучшие практики

### 1. Именование диалогов

```python
# Использовать описательные ID диалогов
def create_user_dialog(user_id):
    return render_dialog(
        id=f"user-dialog-{user_id}",
        title="Детали пользователя",
        content=get_user_content(user_id)
    )
```

### 2. Обработка действий

```python
# Консистентная структура действий
def create_standard_actions(primary_action, secondary_action=None):
    actions = []
    if secondary_action:
        actions.append(secondary_action)
    actions.append(primary_action)
    return actions
```

### 3. Валидация контента

```python
# Валидировать содержимое диалога
def validate_dialog_content(content):
    """Валидировать содержимое диалога для безопасности."""
    if not content or len(content.strip()) == 0:
        raise ValueError("Содержимое диалога не может быть пустым")
    return content.strip()
```

### 4. Доступность

```python
# Обеспечить доступность диалогов
def create_accessible_dialog(title, content, actions=None):
    return render_dialog(
        title=title,
        content=content,
        actions=actions,
        **{
            "aria-label": title,
            "role": "dialog",
            "aria-modal": "true"
        }
    )
```

## Связанные компоненты

- [Модальные окна](modals.md) - Для модальных диалогов и оверлеев
- [Формы](forms.md) - Для содержимого форм в диалогах
- [Уведомления](alerts.md) - Для диалогов в стиле уведомлений
- [Кнопки](buttons.md) - Для кнопок действий диалога


## metroui5_dialog

```python
render_dialog()
```

Пустое или неверное значение: `render_dialog()` даёт `<div class="dialog" id="dialog-component" data-role="dialog"><div class="dialog-actions"><button class="button js-dialog-close" data-action="ok">OK</button><button class="button js-dialog-close" data-action="cancel">Canc...`.

```django
{% metroui5_dialog %}
```
