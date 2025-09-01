# Аватары

MetroUI предоставляет несколько типов компонентов аватаров для отображения изображений профиля пользователей, иконок или инициалов.

## Аватары с инициалами

Компонент аватара с инициалами генерирует фактические файлы изображений из имен с использованием PIL (Pillow), с поддержкой нескольких форматов и адаптивного дизайна. По умолчанию изображения автоматически генерируются для всех размеров и сохраняются в `/media/avatars/initials/{initial}/{size}.{format}`, с адаптивным HTML-выводом с использованием элементов `<figure>` и `<picture>`.

> **⚠️ Уведомление о пользовательской разработке**: Функциональность `initials_avatar` является **пользовательской разработкой** и не является частью MetroUI core. Она предоставляет расширенные возможности генерации изображений, выходящие за рамки стандартной системы аватаров MetroUI.

## Базовое использование

### Аватар с инициалами (пользовательская разработка)

````python
from metroui5.components import render_initials_avatar

# Базовый аватар с инициалами
avatar_html = render_initials_avatar("Джон Доу")

# Или используйте Django тег шаблона
{% load metroui5 %}
{% avatar_initials "Джон Доу" %}

#### **Создание собственного тега шаблона**

Для использования в Django шаблонах вам нужно создать собственный тег шаблона. Вот как:

1. **Создайте директорию templatetags** в вашем приложении:
```bash
mkdir myapp/templatetags
touch myapp/templatetags/__init__.py
touch myapp/templatetags/avatar_tags.py
````

2. **Определите тег шаблона** в `avatar_tags.py`:

```python
from django import template
from django.utils.safestring import mark_safe
from metroui5.components import render_initials_avatar

register = template.Library()

@register.simple_tag
def avatar_initials(name, **kwargs):
    """Рендерит аватар с инициалами."""
    return mark_safe(render_initials_avatar(name, **kwargs))
```

3. **Загрузите и используйте в шаблонах**:

```django
{% load avatar_tags %}

{% avatar_initials "Джон Доу" %}
{% avatar_initials "Джейн Смит" size="large" bg_color="#e74c3c" %}
```

````

### Базовый аватар MetroUI (изображения)

```python
from metroui5.components import render_avatar

# Базовый аватар с изображением
avatar_html = render_avatar("/static/images/user.jpg")
````

### Аватар с иконкой MetroUI

```python
from metroui5.components import render_icon_avatar

# Аватар с иконкой
avatar_html = render_icon_avatar("user", size="large")
```

## Вывод HTML

### Аватар с инициалами (пользовательская разработка)

```html
<!-- Ввод -->
render_initials_avatar("Джон Доу")

<!-- Вывод -->
<figure class="avatar-figure">
	<picture>
		<source
			media="(max-width: 480px)"
			srcset="/media/avatars/initials/ДД/small.png"
		/>
		<source
			media="(max-width: 768px)"
			srcset="/media/avatars/initials/ДД/medium.png"
		/>
		<source
			media="(max-width: 1024px)"
			srcset="/media/avatars/initials/ДД/large.png"
		/>
		<source
			media="(min-width: 1025px)"
			srcset="/media/avatars/initials/ДД/xlarge.png"
		/>
		<img
			src="/media/avatars/initials/ДД/medium.png"
			alt="Аватар для Джона Доу"
			class="avatar-img"
		/>
	</picture>
</figure>
```

### Базовый аватар MetroUI (изображения)

```html
<!-- Ввод -->
render_avatar("/static/images/user.jpg")

<!-- Вывод -->
<img src="/static/images/user.jpg" alt="" />
```

### Аватар с иконкой MetroUI

```html
<!-- Ввод -->
render_icon_avatar("user", size="large")

<!-- Вывод -->
<span class="mif-user mif-large"></span>
```

## Использование в Django шаблонах

### Использование тегов шаблонов

**Примечание**: Функциональность `initials_avatar` является пользовательской разработкой и не является частью MetroUI core. Вы можете использовать её напрямую в Python коде или создать собственный тег шаблона.

#### **Пользовательский тег шаблона (если вы создали один)**

```html
{% load avatar_tags %}

<!-- Базовый аватар с инициалами -->
{% avatar_initials "Джон Доу" %}

<!-- С пользовательским размером -->
{% avatar_initials "Джейн Смит" size="large" %}

<!-- С пользовательскими цветами -->
{% avatar_initials "Боб Уилсон" bg_color="#e74c3c" text_color="white" %}
```

#### **Стандартные теги MetroUI**

```html
{% load metroui5 %}

<!-- Базовый аватар с изображением -->
{% metroui5_avatar "/static/images/user.jpg" %}

<!-- Аватар с иконкой -->
{% metroui5_icon_avatar "user" size="medium" %}
```

### Использование в представлениях

```python
# views.py
from metroui5.components import render_avatar

def profile_view(request):
    user = request.user

    # Создание аватара пользователя
    if user.profile_picture:
        avatar_html = render_avatar(
            src=user.profile_picture.url,
            alt=f"{user.first_name} {user.last_name}",
            size="large"
        )
    else:
        # Резервный вариант с инициалами
        initials = f"{user.first_name[0]}{user.last_name[0]}" if user.first_name and user.last_name else "П"
        avatar_html = render_avatar(
            initials=initials,
            background_color=get_user_color(user.id),
            size="large"
        )

    context = {
        'avatar_html': avatar_html,
        'user': user
    }
    return render(request, 'profile.html', context)
```

```html
<!-- profile.html -->
{% load metroui5 %} {% block content %}
<div class="profile-header">
	<!-- Прямой HTML вывод -->
	{{ avatar_html|safe }}

	<!-- Или используйте тег шаблона -->
	{% if user.profile_picture %} {% metroui5_avatar src=user.profile_picture.url
	alt=user.get_full_name size="large" %} {% else %} {% metroui5_avatar
	initials=user.initials background_color=user.avatar_color %} {% endif %}

	<h1>{{ user.get_full_name }}</h1>
</div>
{% endblock %}
```

## Параметры

### **Параметры для `render_initials_avatar` (пользовательская разработка)**

| Параметр        | Тип    | По умолчанию                 | Описание                                                 |
| --------------- | ------ | ---------------------------- | -------------------------------------------------------- |
| `name`          | string | обязательный                 | Полное имя для генерации инициалов                       |
| `size`          | string | "medium"                     | Размер аватара: "small", "medium", "large", "xlarge"     |
| `bg_color`      | string | автоматически генерируется   | Цвет фона (hex код или название цвета)                   |
| `text_color`    | string | "white"                      | Цвет текста (hex код или название цвета)                 |
| `font_size`     | int    | автоматически рассчитывается | Размер шрифта в пикселях                                 |
| `font_weight`   | string | "bold"                       | Жирность шрифта                                          |
| `shape`         | string | "circle"                     | Форма аватара: "circle", "square", "rounded"             |
| `max_initials`  | int    | 2                            | Максимальное количество инициалов для показа             |
| `output_format` | string | "png"                        | Формат изображения: "png", "jpg", "webp"                 |
| `save_path`     | string | None                         | Путь к файлу для сохранения сгенерированного изображения |

### **Параметры для `render_icon_avatar` (MetroUI core)**

| Параметр     | Тип    | По умолчанию | Описание                        |
| ------------ | ------ | ------------ | ------------------------------- |
| `icon_name`  | string | обязательный | Идентификатор иконки MetroUI    |
| `size`       | string | None         | Множитель размера иконки (1-10) |
| `bg_color`   | string | None         | Цвет фона                       |
| `text_color` | string | None         | Цвет текста/иконки              |

### **Параметры для `render_avatar` (MetroUI core)**

| Параметр    | Тип    | По умолчанию | Описание                |
| ----------- | ------ | ------------ | ----------------------- |
| `image_url` | string | обязательный | URL изображения аватара |

## 🔗 **MetroUI Core vs Пользовательская разработка**

### **Функции MetroUI Core**

Это стандартные функции аватаров MetroUI, которые поставляются с фреймворком:

- **`render_avatar`**: Базовое отображение аватара с изображением (для существующих файлов изображений)
- **`render_icon_avatar`**: Аватары на основе иконок с использованием шрифта иконок MetroUI

### **Функции пользовательской разработки**

Это дополнительные функции, которые вы разработали:

- **`render_initials_avatar`**: Расширенный аватар с инициалами с генерацией изображений
- **`render_image_avatar`**: Простой рендерер тегов изображений
- **`render_responsive_avatar`**: Генератор адаптивной HTML-структуры

### **Стратегия интеграции**

- Используйте функции MetroUI core для стандартных элементов UI
- Используйте пользовательские функции для расширенных требований к аватарам с инициалами
- Комбинируйте оба для комплексных систем аватаров

## Расширенные примеры

### Аватар пользователя с резервными вариантами

```python
def create_user_avatar(user, size="medium"):
    """Создание аватара пользователя с несколькими резервными вариантами."""

    # Сначала попробовать изображение профиля
    if hasattr(user, 'profile') and user.profile.picture:
        return render_avatar(user.profile.picture.url)

    # Резервный вариант с инициалами
    if user.first_name and user.last_name:
        return render_initials_avatar(
            user.get_full_name(),
            size=size
        )

    # Финальный резервный вариант с иконкой
    return render_icon_avatar(
        "user",
        size=size,
        bg_color="#6c757d"
    )
```

### Группа аватаров

```python
def create_avatar_group(users, max_display=3):
    """Создание группы аватаров с индикатором переполнения."""

    avatars = []
    display_users = users[:max_display]

    for user in display_users:
        avatars.append(create_user_avatar(user, size="small"))

    # Добавить индикатор переполнения
    if len(users) > max_display:
        overflow_count = len(users) - max_display
        avatars.append(render_initials_avatar(
            f"+{overflow_count}",
            size="small",
            bg_color="#dee2e6",
            text_color="#495057"
        ))

    return avatars
```

### Аватар со статусом

```python
def create_status_avatar(user, online_status=None):
    """Создание аватара с индикатором онлайн статуса."""

    avatar_html = create_user_avatar(user)

    if online_status:
        status_class = f"avatar-status-{online_status}"  # online, away, busy, offline
        avatar_html = avatar_html.replace(
            'class="avatar"',
            f'class="avatar avatar-with-status {status_class}"'
        )

    return avatar_html
```

### Редактируемый аватар

```python
def create_editable_avatar(user, editable=True):
    """Создание аватара с функцией редактирования."""

    avatar_html = create_user_avatar(user, size="large")

    if editable:
        edit_overlay = """
        <div class="avatar-edit-overlay">
            <button class="avatar-edit-btn" onclick="editAvatar()">
                <span class="mif-camera"></span>
            </button>
        </div>
        """
        avatar_html = avatar_html.replace("</div>", f"{edit_overlay}</div>")

    return avatar_html
```

### Список аватаров команды

```python
def create_team_avatars(team_members):
    """Создание списка аватаров членов команды."""

    team_avatars = []

    for member in team_members:
        member_avatar = {
            "avatar": create_user_avatar(member.user),
            "name": member.user.get_full_name(),
            "role": member.role,
            "status": member.status
        }
        team_avatars.append(member_avatar)

    return team_avatars
```

## Стилизация

### CSS классы

#### Базовые классы

- `avatar` - Базовый контейнер аватара
- `avatar-image` - Аватар с изображением
- `avatar-initials` - Аватар с инициалами
- `avatar-icon` - Аватар с иконкой

#### Классы размеров

- `avatar-small` - Маленький аватар (32px)
- `avatar-medium` - Средний аватар (48px) - по умолчанию
- `avatar-large` - Большой аватар (64px)
- `avatar-xlarge` - Очень большой аватар (96px)

#### Классы форм

- `avatar-circle` - Круглый аватар (по умолчанию)
- `avatar-square` - Квадратный аватар
- `avatar-rounded` - Скругленный квадратный аватар

#### Классы функций

- `avatar-bordered` - Аватар с границей
- `avatar-with-status` - Аватар с индикатором статуса
- `avatar-editable` - Редактируемый аватар с наложением

### Пользовательская стилизация

```css
/* Пользовательская стилизация аватара */
.avatar-custom {
	position: relative;
	display: inline-block;
	border: 3px solid #fff;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
	transition: all 0.3s ease;
}

.avatar-custom:hover {
	transform: scale(1.05);
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.avatar-custom .avatar-image {
	width: 100%;
	height: 100%;
	object-fit: cover;
	border-radius: inherit;
}

.avatar-custom .avatar-text {
	font-weight: 600;
	font-size: 0.875em;
	text-transform: uppercase;
	letter-spacing: 0.5px;
}

/* Индикаторы статуса */
.avatar-with-status::after {
	content: "";
	position: absolute;
	bottom: 0;
	right: 0;
	width: 12px;
	height: 12px;
	border: 2px solid #fff;
	border-radius: 50%;
	background: #6c757d;
}

.avatar-status-online::after {
	background: #28a745;
}

.avatar-status-away::after {
	background: #ffc107;
}

.avatar-status-busy::after {
	background: #dc3545;
}

.avatar-status-offline::after {
	background: #6c757d;
}

/* Группа аватаров */
.avatar-group {
	display: flex;
	align-items: center;
}

.avatar-group .avatar {
	margin-right: -8px;
	border: 2px solid #fff;
	z-index: 1;
}

.avatar-group .avatar:hover {
	z-index: 2;
}

/* Редактируемый аватар */
.avatar-editable {
	cursor: pointer;
}

.avatar-edit-overlay {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background: rgba(0, 0, 0, 0.5);
	display: flex;
	align-items: center;
	justify-content: center;
	opacity: 0;
	transition: opacity 0.3s ease;
	border-radius: inherit;
}

.avatar-editable:hover .avatar-edit-overlay {
	opacity: 1;
}

.avatar-edit-btn {
	background: none;
	border: none;
	color: white;
	font-size: 20px;
	cursor: pointer;
}
```

## Интеграция с JavaScript

### Загрузка аватара

```javascript
// Обработка загрузки изображения аватара
$(".avatar-image").on("load", function () {
	$(this).closest(".avatar").removeClass("avatar-loading");
});

$(".avatar-image").on("error", function () {
	const avatar = $(this).closest(".avatar");
	const fallbackInitials = avatar.data("initials");
	const fallbackColor = avatar.data("color") || "#6c757d";

	// Заменить резервным вариантом с инициалами
	if (fallbackInitials) {
		avatar.html(`<span class="avatar-text">${fallbackInitials}</span>`);
		avatar.css("background-color", fallbackColor);
		avatar.addClass("avatar-initials");
	} else {
		// Заменить резервным вариантом с иконкой
		avatar.html('<span class="mif-user"></span>');
		avatar.addClass("avatar-icon");
	}
});
```

### Загрузка аватара

```javascript
// Обработка загрузки аватара
function handleAvatarUpload(input) {
	const file = input.files[0];
	if (!file) return;

	// Проверка типа файла
	if (!file.type.startsWith("image/")) {
		alert("Пожалуйста, выберите файл изображения");
		return;
	}

	// Проверка размера файла (лимит 2MB)
	if (file.size > 2 * 1024 * 1024) {
		alert("Размер изображения должен быть меньше 2MB");
		return;
	}

	// Показать предварительный просмотр
	const reader = new FileReader();
	reader.onload = function (e) {
		updateAvatarPreview(e.target.result);
	};
	reader.readAsDataURL(file);

	// Загрузить файл
	uploadAvatarFile(file);
}

function updateAvatarPreview(imageSrc) {
	$(".avatar-image").attr("src", imageSrc);
	$(".avatar")
		.removeClass("avatar-initials avatar-icon")
		.addClass("avatar-image");
}

function uploadAvatarFile(file) {
	const formData = new FormData();
	formData.append("avatar", file);

	$.ajax({
		url: "/api/upload-avatar/",
		method: "POST",
		data: formData,
		processData: false,
		contentType: false,
		success: function (response) {
			if (response.success) {
				updateAvatarPreview(response.avatar_url);
				showNotification("Аватар успешно обновлен", "success");
			} else {
				showNotification("Не удалось обновить аватар", "error");
			}
		},
		error: function () {
			showNotification("Ошибка загрузки аватара", "error");
		},
	});
}
```

### Обновления статуса аватара

```javascript
// Обновление статуса аватара
function updateAvatarStatus(userId, status) {
	const avatar = $(`.avatar[data-user-id="${userId}"]`);

	// Удалить существующие классы статуса
	avatar.removeClass(
		"avatar-status-online avatar-status-away avatar-status-busy avatar-status-offline"
	);

	// Добавить новый класс статуса
	if (status) {
		avatar.addClass("avatar-with-status").addClass(`avatar-status-${status}`);
	} else {
		avatar.removeClass("avatar-with-status");
	}
}

// Обновления статуса в реальном времени через WebSocket
function handleStatusUpdate(data) {
	updateAvatarStatus(data.user_id, data.status);
}
```

## Лучшие практики

### 1. Последовательные размеры

```python
# Использовать последовательные размеры аватаров во всем приложении
AVATAR_SIZES = {
    'thumbnail': 'small',    # 32px - для списков, комментариев
    'profile': 'medium',     # 48px - для профилей пользователей
    'header': 'large',       # 64px - для заголовков страниц
    'hero': 'xlarge'         # 96px - для главных разделов
}

def create_consistent_avatar(user, context='profile'):
    size = AVATAR_SIZES.get(context, 'medium')
    return create_user_avatar(user, size=size)
```

### 2. Генерация цветов

```python
# Генерация последовательных цветов для пользователей
def generate_user_color(user_id):
    """Генерация последовательного цвета на основе ID пользователя."""
    colors = [
        '#007acc', '#28a745', '#dc3545', '#ffc107',
        '#17a2b8', '#6f42c1', '#fd7e14', '#20c997'
    ]
    return colors[user_id % len(colors)]
```

### 3. Доступность

```python
# Обеспечение доступности аватаров
def create_accessible_avatar(user, **kwargs):
    return render_avatar(
        alt=f"Аватар для {user.get_full_name()}",
        **kwargs,
        **{
            "role": "img",
            "aria-label": f"Фотография профиля {user.get_full_name()}"
        }
    )
```

### 4. Оптимизация производительности

```python
# Оптимизация загрузки аватаров
def create_optimized_avatar(user, size="medium"):
    if user.profile_picture:
        # Использовать соответствующий размер изображения
        image_url = get_thumbnail_url(user.profile_picture, size)
        return render_avatar(
            src=image_url,
            alt=user.get_full_name(),
            size=size,
            loading="lazy"  # Ленивая загрузка для производительности
        )

    return render_avatar(
        initials=get_user_initials(user),
        background_color=generate_user_color(user.id),
        size=size
    )
```

## Связанные компоненты

- [Кнопки](buttons.md) - Для кнопок редактирования аватара
- [Иконки](icons.md) - Для иконок аватара и индикаторов статуса
- [Изображения](images.md) - Для обработки изображений аватара
- [Значки](badges.md) - Для значков статуса аватара
