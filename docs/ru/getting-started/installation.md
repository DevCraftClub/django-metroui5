# Установка

Подробное руководство по установке MetroUI5 Django в ваш проект.

## Требования

### Системные требования

- **Python**: 3.10 или выше (ниже не тестировалось)
- **Django**: 4.1 или выше (рекомендуем 5.2.17+; в CI проверяем с 4.1 по 6.1)
- **Операционная система**: Windows, macOS, Linux

### Зависимости

- `django` >= 4.1 (рекомендуем >= 5.2.17)
- `django-crispy-forms` (опционально, для расширенной работы с формами)

## Способы установки

### 1. Установка через pip (рекомендуется)

```bash
pip install django-metroui5
```

### 2. Установка из исходного кода

```bash
git clone https://github.com/your-repo/django-metroui5.git
cd django-metroui5
pip install -e .
```

### 3. Установка конкретной версии

```bash
pip install django-metroui5==1.0.0
```

## Настройка Django проекта

### 1. Добавление в INSTALLED_APPS

Откройте `settings.py` и добавьте `metroui5`:

```python
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# Ваши приложения
	'myapp',

	# MetroUI5
	'metroui5',
]
```

### 2. Настройка статических файлов

Убедитесь, что у вас правильно настроены статические файлы:

```python
# settings.py

# Базовый URL для статических файлов
STATIC_URL = '/static/'

# Дополнительные директории для статических файлов
STATICFILES_DIRS = [
	BASE_DIR / "static",
]

# Директория для collectstatic
STATIC_ROOT = BASE_DIR / "staticfiles"

# Настройки для разработки
if DEBUG:
	STATICFILES_DIRS = [
		BASE_DIR / "static",
	]
```

### 3. Настройка шаблонов

Добавьте директорию шаблонов MetroUI5:

```python
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			BASE_DIR / "templates",
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]
```

### 4. Настройка URL

Добавьте URL для статических файлов в `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# Ваши URL паттерны
	path('admin/', admin.site.urls),
	path('', include('myapp.urls')),
]

# Добавляем статические файлы для разработки
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## Настройка MetroUI5

### 1. Базовые настройки

Добавьте настройки MetroUI5 в `settings.py`:

```python
# MetroUI5 настройки
METROUI5 = {
	'CDN_MODE': False,  # Использовать локальные файлы
}
```

### 2. Настройки CDN

Если хотите использовать CDN:

```python
METROUI5 = {
	'CDN_MODE': True,
	'CDN_URL': 'https://cdn.metroui.org.ua/current',
	'THEME': 'default',
}
```

#### Доступные CDN файлы

MetroUI5 доступен через официальный CDN по следующим URL:

- **JavaScript**: `https://cdn.metroui.org.ua/current/metro.js`
- **CSS**: `https://cdn.metroui.org.ua/current/metro.css`
- **Иконки**: `https://cdn.metroui.org.ua/current/icons.css`

#### Новый CDN режим (рекомендуется)

```python
METROUI5 = {
	'use_cdn': True,  # Включить CDN режим

	# Опционально: перезаписать CDN URL
	'cdn_js_url': 'https://your-cdn.com/metro.js',
	'cdn_css_url': 'https://your-cdn.com/metro.css',
	'cdn_icons_url': 'https://your-cdn.com/icons.css',
}
```

Если `cdn_*_url` не указаны, будут использованы дефолтные CDN URL.

#### Устаревший CDN режим

При использовании `cdn_mode: True` пакет автоматически подставит правильные URL для каждого типа файла.

### 3. Кастомные CSS/JS файлы

```python
METROUI5 = {
	'CUSTOM_CSS_FILES': [
		'css/custom.css',
		'css/theme.css',
	],
	'CUSTOM_JS_FILES': [
		'js/custom.js',
		'js/plugins.js',
	],
}
```

## Проверка установки

### 1. Сбор статических файлов

```bash
python manage.py collectstatic
```

### 2. Запуск сервера

```bash
python manage.py runserver
```

### 3. Проверка в браузере

Откройте `http://127.0.0.1:8000/` и проверьте:

- В исходном коде страницы есть ссылки на MetroUI5 CSS/JS
- В консоли браузера нет ошибок
- Стили MetroUI5 применяются

## Обновление

### Обновление до новой версии

```bash
pip install --upgrade django-metroui5
```

### Обновление статических файлов

```bash
python manage.py collectstatic --clear
```

## Удаление

### Удаление пакета

```bash
pip uninstall django-metroui5
```

### Очистка настроек

Удалите `metroui5` из `INSTALLED_APPS` и настройки `METROUI5` из `settings.py`.

## Решение проблем

### Ошибка "No module named 'metroui5'"

```bash
pip install django-metroui5
python manage.py check
```

### Статические файлы не загружаются

```bash
python manage.py collectstatic
python manage.py runserver --insecure
```

### Шаблонные теги не работают

1. Проверьте `INSTALLED_APPS`
2. Перезапустите сервер
3. Проверьте синтаксис шаблона

### Конфликт с другими CSS фреймворками

MetroUI5 может конфликтовать с Bootstrap, Foundation и другими CSS фреймворками. Используйте только один фреймворк на
странице.

## Следующие шаги

После успешной установки:

1. Изучите [базовое использование](basic-usage.md)
2. Ознакомьтесь с [примерами](examples.md)
3. Изучите доступные [компоненты](../components/)
4. Изучите [API справочник](../api-reference/)
5. Вставьте первый блок: [аккордеон для сборки страницы](../for-users/accordions.md) и [аккордеон для разработчика](../components/accordions.md)
