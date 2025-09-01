# Модальные окна

MetroUI5 Django предоставляет комплексную систему компонентов модальных окон для создания наложенных диалогов, всплывающих окон и интерактивных отображений контента.

## Базовое использование

```python
from metroui5.components import render_modal

# Простое модальное окно
modal_html = render_modal(
    title="Подтверждение",
    content="Вы уверены, что хотите удалить этот элемент?",
    id="confirm-modal"
)
```

## Параметры

### `render_modal(title, content, **attrs)`

- **title** (str): Заголовок модального окна
- **content** (str): Содержимое модального окна (может быть HTML)
- **attrs** (dict): Дополнительные HTML атрибуты для модального окна

## Примеры

### Базовое модальное окно

```python
from metroui5.components import render_modal

modal = render_modal(
    title="Добро пожаловать",
    content="Добро пожаловать в наше приложение!",
    id="welcome-modal"
)
```

### Модальное окно с пользовательскими классами

```python
modal = render_modal(
    title="Профиль пользователя",
    content="""
    <div class="user-info">
        <p><strong>Имя:</strong> Джон Доу</p>
        <p><strong>Email:</strong> john@example.com</p>
        <p><strong>Роль:</strong> Администратор</p>
    </div>
    """,
    class="modal modal-large",
    id="profile-modal"
)
```

### Модальное окно с действиями

```python
def create_modal_with_actions():
    content = """
    <p>Это действие нельзя отменить. Вы уверены, что хотите продолжить?</p>
    <div class="button-group">
        <button class="button button-danger" onclick="confirmDelete()">Удалить</button>
        <button class="button" onclick="Metro.dialog.close('#confirm-modal')">Отмена</button>
    </div>
    """

    return render_modal(
        title="Подтвердить удаление",
        content=content,
        id="confirm-modal",
        class="modal"
    )

modal = create_modal_with_actions()
```

## Классы модальных окон MetroUI

MetroUI5 предоставляет несколько CSS классов для стилизации модальных окон:

### Классы размеров

- `modal-small` - Маленькое модальное окно
- `modal-large` - Большое модальное окно
- `modal-wide` - Широкое модальное окно
- `modal-tall` - Высокое модальное окно

### Классы стилей

- `modal-dark` - Модальное окно с темной темой
- `modal-light` - Модальное окно со светлой темой
- `modal-rounded` - Скругленные углы
- `modal-shadow` - Улучшенная тень

### Классы позиционирования

- `modal-top` - Модальное окно позиционировано сверху
- `modal-center` - Модальное окно по центру (по умолчанию)
- `modal-bottom` - Модальное окно позиционировано снизу

## Типы модальных окон

### Модальное окно подтверждения

```python
def create_confirmation_modal(message, action_url):
    content = f"""
    <p>{message}</p>
    <div class="button-group">
        <button class="button button-danger" onclick="window.location.href='{action_url}'">
            Подтвердить
        </button>
        <button class="button" onclick="Metro.dialog.close('#confirm-modal')">
            Отмена
        </button>
    </div>
    """

    return render_modal(
        title="Подтвердить действие",
        content=content,
        id="confirm-modal",
        class="modal"
    )

modal = create_confirmation_modal(
    "Вы уверены, что хотите удалить этого пользователя?",
    "/users/delete/123/"
)
```

### Модальное окно с формой

```python
def create_form_modal():
    content = """
    <form id="user-form" method="post">
        <div class="form-group">
            <label for="name">Имя:</label>
            <input type="text" id="name" name="name" class="input" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" class="input" required>
        </div>
        <div class="button-group">
            <button type="submit" class="button button-primary">Сохранить</button>
            <button type="button" class="button" onclick="Metro.dialog.close('#form-modal')">Отмена</button>
        </div>
    </form>
    """

    return render_modal(
        title="Добавить нового пользователя",
        content=content,
        id="form-modal",
        class="modal modal-large"
    )

modal = create_form_modal()
```

### Модальное окно с предупреждением

```python
def create_alert_modal(message, alert_type="info"):
    icon_map = {
        "success": "checkmark",
        "warning": "warning",
        "error": "cross",
        "info": "info"
    }

    icon = icon_map.get(alert_type, "info")

    content = f"""
    <div class="alert alert-{alert_type}">
        <span class="mif-{icon}"></span>
        {message}
    </div>
    <div class="button-group">
        <button class="button" onclick="Metro.dialog.close('#alert-modal')">OK</button>
    </div>
    """

    return render_modal(
        title=f"Предупреждение {alert_type.title()}",
        content=content,
        id="alert-modal",
        class="modal"
    )

success_modal = create_alert_modal("Операция успешно завершена!", "success")
error_modal = create_alert_modal("Произошла ошибка. Попробуйте еще раз.", "error")
```

## Использование в шаблонах

```html
{% load metroui5 %} {% metroui5_modal title="Подтверждение" content="Вы
уверены?" id="confirm-modal" %}
```

## Расширенные примеры

### Модальное окно с динамическим содержимым

```python
def create_dynamic_modal(user_data):
    content = f"""
    <div class="user-details">
        <div class="avatar">
            <img src="{user_data.get('avatar', '/static/default-avatar.png')}" alt="Аватар">
        </div>
        <div class="info">
            <h3>{user_data['name']}</h3>
            <p><strong>Email:</strong> {user_data['email']}</p>
            <p><strong>Роль:</strong> {user_data['role']}</p>
            <p><strong>Последний вход:</strong> {user_data['last_login']}</p>
        </div>
    </div>
    <div class="button-group">
        <button class="button button-primary" onclick="editUser({user_data['id']})">Редактировать</button>
        <button class="button" onclick="Metro.dialog.close('#user-modal')">Закрыть</button>
    </div>
    """

    return render_modal(
        title="Детали пользователя",
        content=content,
        id="user-modal",
        class="modal modal-large"
    )

user_modal = create_dynamic_modal({
    'id': 123,
    'name': 'Джон Доу',
    'email': 'john@example.com',
    'role': 'Администратор',
    'last_login': '2024-01-15 10:30 AM',
    'avatar': '/static/avatars/john.jpg'
})
```

### Модальное окно с состоянием загрузки

```python
def create_loading_modal():
    content = """
    <div class="loading-content">
        <div class="spinner"></div>
        <p>Загрузка данных, пожалуйста, подождите...</p>
    </div>
    """

    return render_modal(
        title="Загрузка",
        content=content,
        id="loading-modal",
        class="modal modal-small"
    )

loading_modal = create_loading_modal()
```

### Модальное окно с вкладками

```python
def create_tabbed_modal():
    content = """
    <div class="tabs" data-role="tabs">
        <ul class="tabs-nav">
            <li><a href="#tab1">Общие</a></li>
            <li><a href="#tab2">Настройки</a></li>
            <li><a href="#tab3">Дополнительно</a></li>
        </ul>
        <div class="tabs-content">
            <div id="tab1">
                <p>Содержимое общих настроек...</p>
            </div>
            <div id="tab2">
                <p>Содержимое настроек...</p>
            </div>
            <div id="tab3">
                <p>Содержимое дополнительных настроек...</p>
            </div>
        </div>
    </div>
    <div class="button-group">
        <button class="button button-primary">Сохранить</button>
        <button class="button" onclick="Metro.dialog.close('#settings-modal')">Отмена</button>
    </div>
    """

    return render_modal(
        title="Настройки",
        content=content,
        id="settings-modal",
        class="modal modal-large"
    )

settings_modal = create_tabbed_modal()
```

## Интеграция с JavaScript

### Открытие модальных окон

```javascript
// Открыть модальное окно по ID
Metro.dialog.open("#my-modal");

// Открыть модальное окно с пользовательскими опциями
Metro.dialog.open("#my-modal", {
	width: 600,
	height: 400,
	overlay: true,
	overlayClose: true,
});
```

### Закрытие модальных окон

```javascript
// Закрыть модальное окно по ID
Metro.dialog.close("#my-modal");

// Закрыть все модальные окна
Metro.dialog.closeAll();
```

### События модальных окон

```javascript
// Слушать события модальных окон
$("#my-modal").on("dialogopen", function () {
	console.log("Модальное окно открыто");
});

$("#my-modal").on("dialogclose", function () {
	console.log("Модальное окно закрыто");
});
```

## Лучшие практики

1. **Используйте описательные заголовки**: Делайте заголовки модальных окон ясными и описательными
2. **Держите содержимое сфокусированным**: Не перегружайте модальные окна слишком большим количеством контента
3. **Предоставляйте четкие действия**: Всегда включайте четкие кнопки действий
4. **Обрабатывайте события клавиатуры**: Убедитесь, что модальные окна можно закрыть клавишей Escape
5. **Делайте доступным**: Включайте правильные ARIA метки и управление фокусом
6. **Используйте соответствующие размеры**: Выбирайте размер модального окна на основе содержимого
7. **Тестируйте на мобильных устройствах**: Убедитесь, что модальные окна хорошо работают на мобильных устройствах

## Связанные компоненты

- [Диалоги](dialogs.md) - Для более простых диалоговых окон
- [Уведомления](alerts.md) - Для сообщений-предупреждений
- [Формы](forms.md) - Для содержимого форм в модальных окнах
- [Кнопки](buttons.md) - Для кнопок действий модальных окон
