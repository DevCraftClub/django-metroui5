# Основные функции (Core)

API справочник для основного модуля MetroUI5 Django.

## Обзор

Модуль `core` содержит основные функции для работы с MetroUI5, включая настройки, URL-генерацию и утилиты.

## Функции

### `get_metroui5_setting(name, default=None)`

Получает значение настройки MetroUI5 из Django settings.

#### Параметры

- `name` (str) - имя настройки
- `default` - значение по умолчанию, если настройка не найдена

#### Возвращает

Значение настройки или `default`

#### Примеры

```python
from metroui5.core import get_metroui5_setting

# Получить настройку CDN
cdn_mode = get_metroui5_setting('CDN_MODE', False)

# Получить тему
theme = get_metroui5_setting('THEME', 'default')

# Получить версию
version = get_metroui5_setting('VERSION', '5.0.0')
```

### `javascript_url()`

Генерирует URL для JavaScript файла MetroUI5.

#### Возвращает

URL строку для JavaScript файла

#### Примеры

```python
from metroui5.core import javascript_url

# Получить URL для JavaScript
js_url = javascript_url()
# Результат: '/static/metroui5/js/metro.all.js' или CDN URL
```

### `css_url()`

Генерирует URL для CSS файла MetroUI5.

#### Возвращает

URL строку для CSS файла

#### Примеры

```python
from metroui5.core import css_url

# Получить URL для CSS
css_url = css_url()
# Результат: '/static/metroui5/css/metro.all.css' или CDN URL
```

### `icons_css_url()`

Генерирует URL для CSS файла иконок MetroUI5.

#### Возвращает

URL строку для CSS файла иконок

#### Примеры

```python
from metroui5.core import icons_css_url

# Получить URL для иконок
icons_url = icons_css_url()
# Результат: '/static/metroui5/icons/icons.css' или CDN URL
```

### `custom_css_files()`

Получает список кастомных CSS файлов из настроек.

#### Возвращает

Список URL для кастомных CSS файлов

#### Примеры

```python
from metroui5.core import custom_css_files

# Получить кастомные CSS файлы
custom_css = custom_css_files()
# Результат: ['/static/css/custom.css', '/static/css/theme.css']
```

### `custom_javascript_files()`

Получает список кастомных JavaScript файлов из настроек.

#### Возвращает

Список URL для кастомных JavaScript файлов

#### Примеры

```python
from metroui5.core import custom_javascript_files

# Получить кастомные JavaScript файлы
custom_js = custom_javascript_files()
# Результат: ['/static/js/custom.js', '/static/js/plugins.js']
```

### `is_cdn_mode()`

Проверяет, включен ли режим CDN (устаревший способ).

#### Возвращает

`True`, если CDN режим включен, иначе `False`

#### Примеры

```python
from metroui5.core import is_cdn_mode

# Проверить CDN режим
if is_cdn_mode():
	print("Используется CDN")
else:
	print("Используются локальные файлы")
```

### `is_use_cdn()`

Проверяет, включен ли новый режим CDN.

#### Возвращает

`True`, если CDN режим включен, иначе `False`

#### Примеры

```python
from metroui5.core import is_use_cdn

# Проверить CDN режим
if is_use_cdn():
	print("Используется CDN")
else:
	print("Используются локальные файлы")
```

## Внутренние функции

### `_validate_url_config(config, config_type)`

Валидирует конфигурацию URL для MetroUI5.

#### Параметры

- `config` - конфигурация для проверки
- `config_type` (str) - тип конфигурации

#### Возвращает

Валидную конфигурацию или вызывает исключение

#### Примеры

```python
from metroui5.core import _validate_url_config

# Валидация конфигурации (внутреннее использование)
try:
	valid_config = _validate_url_config(my_config, 'css')
except ValueError as e:
	print(f"Ошибка конфигурации: {e}")
```

### `_get_file_url(config, config_type)`

Генерирует URL для файла на основе конфигурации.

#### Параметры

- `config` - конфигурация файла
- `config_type` (str) - тип файла

#### Возвращает

URL строку для файла

#### Примеры

```python
from metroui5.core import _get_file_url

# Генерация URL файла (внутреннее использование)
file_url = _get_file_url(file_config, 'js')
```

## Настройки

### Базовые настройки

```python
# settings.py

METROUI5 = {
	'CDN_MODE': False,  # Использовать локальные файлы
}
```

### CDN настройки

```python
METROUI5 = {
	'CDN_MODE': True,
	'CDN_URL': 'https://cdn.metroui.org.ua/current',
}
```

### Кастомные файлы

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

### Расширенные настройки

```python
METROUI5 = {
	'CDN_MODE': False,
	'THEME': 'dark',
	'VERSION': '5.1.17',
	'STATIC_URL': '/static/metroui5/',
	'FILE_EXTENSIONS': {
		'css': '.css',
		'js': '.js',
	},
	'CACHE_BUSTING': True,
}
```

## Обработка ошибок

### Ошибки конфигурации

```python
from metroui5.core import get_metroui5_setting

try:
	cdn_url = get_metroui5_setting('CDN_URL')
	if not cdn_url:
		raise ValueError("CDN_URL не настроен")
except Exception as e:
	# Обработка ошибки
	print(f"Ошибка конфигурации MetroUI5: {e}")
	# Использовать значения по умолчанию
	cdn_url = 'https://default-cdn.com/metro5'
```

### Проверка доступности файлов

```python
import os
from metroui5.core import css_url, javascript_url


def check_files_exist():
	"""Проверяет существование файлов MetroUI5"""
	css_path = css_url().replace('/static/', 'static/')
	js_path = javascript_url().replace('/static/', 'static/')

	if not os.path.exists(css_path):
		print(f"CSS файл не найден: {css_path}")

	if not os.path.exists(js_path):
		print(f"JavaScript файл не найден: {js_path}")
```

## Лучшие практики

### 1. Используйте значения по умолчанию

```python
# Хорошо
theme = get_metroui5_setting('THEME', 'default')

# Плохо
theme = get_metroui5_setting('THEME')  # Может вернуть None
```

### 2. Проверяйте CDN режим

```python
if is_cdn_mode():
	# Используйте CDN URL
	base_url = get_metroui5_setting('CDN_URL')
else:
	# Используйте локальные файлы
	base_url = '/static/metroui5/'
```

### 3. Кэшируйте URL

```python
from functools import lru_cache


@lru_cache(maxsize=1)
def get_cached_css_url():
	return css_url()


@lru_cache(maxsize=1)
def get_cached_js_url():
	return javascript_url()
```

### 4. Обрабатывайте ошибки

```python
def safe_get_setting(name, default=None):
	"""Безопасно получает настройку с обработкой ошибок"""
	try:
		return get_metroui5_setting(name, default)
	except Exception as e:
		logger.error(f"Ошибка получения настройки {name}: {e}")
		return default
```

## Тестирование

### Модульные тесты

```python
from django.test import TestCase
from unittest.mock import patch
from metroui5.core import get_metroui5_setting, is_cdn_mode


class CoreTestCase(TestCase):

	def test_get_setting_default(self):
		"""Тест получения настройки с значением по умолчанию"""
		value = get_metroui5_setting('NONEXISTENT', 'default')
		self.assertEqual(value, 'default')

	@patch('metroui5.core.get_metroui5_setting')
	def test_cdn_mode(self, mock_get_setting):
		"""Тест проверки CDN режима"""
		mock_get_setting.return_value = True
		self.assertTrue(is_cdn_mode())
```

## Связанные модули

- [HTML утилиты](html.md) - для генерации HTML тегов
- [CSS утилиты](css.md) - для работы с CSS классами
- [Компоненты](components.md) - для рендеринга UI компонентов

## Следующие шаги

Теперь, когда вы освоили основные функции:

1. Изучите [HTML утилиты](html.md) для генерации HTML
2. Ознакомьтесь с [CSS утилитами](css.md) для работы со стилями
3. Изучите [компоненты](components.md) для создания UI
4. Создайте собственные утилиты на основе core модуля!
