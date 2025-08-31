# Быстрый старт

Этот раздел поможет вам быстро начать работу с MetroUI5 Django.

## Минимальная настройка

### 1. Установка

```bash
pip install django-metroui5
```

### 2. Добавление в Django проект

Добавьте `metroui5` в `INSTALLED_APPS` в вашем `settings.py`:

```python
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'metroui5',  # Добавьте эту строку
]
```

### 3. Настройка статических файлов

Убедитесь, что у вас настроены статические файлы в `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	BASE_DIR / "static",
]
```

### 4. Создание базового шаблона

Создайте `templates/base.html`:

```html
{% load metroui5 %}
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{% block title %}MetroUI5 Django{% endblock %}</title>

    {% metroui5_css %} {% metroui5_icons %}
</head>
<body>
<div class="container">{% block content %} {% endblock %}</div>

{% metroui5_javascript %}
</body>
</html>
```

### 5. Первый компонент

В вашем представлении (View):

```python
from metroui5.components import render_button


def home(request):
	button_html = render_button("Нажми меня!", button_type="primary")
	return render(request, 'home.html', {'button': button_html})
```

В шаблоне `home.html`:

```html
{% extends 'base.html' %} {% block content %} {{ button|safe }} {% endblock %}
```

## CDN или локальные файлы

MetroUI5 Django поддерживает два режима работы:

### Локальные файлы (по умолчанию)

Пакет автоматически копирует MetroUI5 файлы в вашу статическую директорию.

### CDN режим

Используйте официальный CDN для быстрого старта:

```python
# settings.py
METROUI5 = {
	'use_cdn': True,  # Включить CDN режим

	# Опционально: перезаписать CDN URL
	'cdn_js_url': 'https://your-cdn.com/metro.js',
	'cdn_css_url': 'https://your-cdn.com/metro.css',
	'cdn_icons_url': 'https://your-cdn.com/icons.css',
}
```

**Доступные CDN файлы:**

- JavaScript: `https://cdn.metroui.org.ua/current/metro.js`
- CSS: `https://cdn.metroui.org.ua/current/metro.css`
- Иконки: `https://cdn.metroui.org.ua/current/icons.css`

## Что дальше?

- Изучите [установку](installation.md) для детальной настройки
- Ознакомьтесь с [базовым использованием](basic-usage.md)
- Посмотрите [примеры](examples.md) для вдохновения
- Изучите доступные [компоненты](../components/)

## Быстрая проверка

Если все настроено правильно, вы должны увидеть:

1. MetroUI5 стили загружены (проверьте в DevTools)
2. Кнопка отображается с MetroUI5 стилями
3. В консоли браузера нет ошибок JavaScript

## Решение проблем

### Статические файлы не загружаются

```bash
python manage.py collectstatic
```

### Шаблонные теги не работают

Убедитесь, что `metroui5` добавлен в `INSTALLED_APPS` и перезапустите сервер.

### Стили не применяются

Проверьте, что CSS файлы MetroUI5 загружаются в `<head>` страницы.
