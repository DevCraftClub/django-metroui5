# Темы MetroUI 5

MetroUI 5 поддерживает встроенные темы `light` и `dark` для компонентов. Вы можете переключать темы в соответствии с
системой или использовать встроенный theme switcher.

## О темах

MetroUI 5 поддерживает встроенные темы `light` и `dark` для компонентов. По умолчанию тема установлена в `light`. Для
изменения темы добавьте класс `.dark-side` к тегу `<html>` для глобального применения или к конкретному `<element>` для
локального.

### Глобальное применение

```html
<!-- Глобально -->
<html class="dark-side">
<div data-role="calendar"></div>
</html>
```

### Локальное применение

```html
<!-- Локально -->
<div class="dark-side">
    <div data-role="calendar"></div>
</div>
```

## Настройка тем

### Базовые настройки

```python
# settings.py
METROUI5 = {
	'theme': 'light',  # 'light', 'dark', или 'auto'
	'theme_target': 'html',  # Target элемент для класса темы
	'theme_switcher_enabled': False,  # Включить встроенный theme switcher
}
```

### Доступные значения темы

- **`light`** - светлая тема (по умолчанию)
- **`dark`** - темная тема
- **`auto`** - автоматическое определение по системным настройкам

### Target элемент

- **`html`** - применять тему к тегу `<html>` (по умолчанию)
- **`body`** - применять тему к тегу `<body>`
- **Любой CSS селектор** - например `#app`, `.container`

## Автоматическое определение темы

Вы можете использовать функцию `prefers-color-scheme` для определения, запросил ли пользователь использование светлой
или темной цветовой темы в системе. Для использования этой функции добавьте meta тег `metroui:theme` с содержимым `auto`
в `<head>` страницы.

```html

<meta name="metroui:theme" content="auto"/>
```

Также вы можете использовать значения `light` и `dark` для установки конкретной темы.

## Theme Switcher

MetroUI 5 имеет встроенный theme switcher, который позволяет переключаться между `light` и `dark` темами. Вы можете
использовать компонент `theme-switcher` для добавления элемента управления переключением между светлой и темной темами.

### Включение Theme Switcher

```python
# settings.py
METROUI5 = {
	'theme_switcher_enabled': True,  # Включить theme switcher
}
```

### Режимы переключателя

Вы можете использовать атрибут `data-mode` для установки режима theme switcher.

#### Switch режим

```html
<input type="checkbox" data-role="theme-switcher"/>
```

#### Button режим

```html
<input type="checkbox" data-role="theme-switcher" data-mode="button"/>
```

### Использование в шаблонах

#### Базовый theme switcher

```html
{% load metroui5 %}

<!-- Полный theme switcher с контейнером -->
{% metroui5_theme_switcher %}
```

#### Switch режим

```html
{% load metroui5 %}

<!-- Только checkbox в switch режиме -->
{% metroui5_theme_switcher_switch %}
```

#### Button режим

```html
{% load metroui5 %}

<!-- Только checkbox в button режиме -->
{% metroui5_theme_switcher_button %}
```

## Шаблонные теги

### `metroui5_theme_meta`

Возвращает meta тег для конфигурации темы.

```html
{% load metroui5 %}
<head>
    {% metroui5_theme_meta %}
</head>
```

### `metroui5_theme_class`

Возвращает CSS класс темы для применения к target элементу.

```html
{% load metroui5 %}
<html{%
if
metroui5_theme_class
%}
class="{{ metroui5_theme_class }}"
{%
endif
%}
></html{%>
```

### `metroui5_theme_switcher`

Возвращает HTML для компонента theme switcher.

```html
{% load metroui5 %} {% metroui5_theme_switcher %}
```

### `metroui5_theme_switcher_switch`

Возвращает HTML для theme switcher в switch режиме.

```html
{% load metroui5 %} {% metroui5_theme_switcher_switch %}
```

### `metroui5_theme_switcher_button`

Возвращает HTML для theme switcher в button режиме.

```html
{% load metroui5 %} {% metroui5_theme_switcher_button %}
```

### `metroui5_theme_info`

Возвращает информацию о теме для отладки.

```html
{% load metroui5 %} {% metroui5_theme_info as theme_info %}
<p>Текущая тема: {{ theme_info.theme }}</p>
<p>Target элемент: {{ theme_info.target }}</p>
<p>
    Theme switcher: {{ theme_info.switcher_enabled|yesno:"включен,выключен" }}
</p>
```

## Базовый шаблон

Используйте базовый шаблон MetroUI 5 с поддержкой тем:

```html
{% extends "metroui5/layout/base.html" %} {% block content %}
<!-- Ваш контент здесь -->
<div class="container">
    <h1>Привет, мир!</h1>
    <p>Эта страница автоматически поддерживает темы MetroUI 5.</p>
</div>
{% endblock %}
```

## Программное управление темами

### Получение настроек темы

```python
from metroui5.core import get_theme, get_theme_target, is_theme_switcher_enabled

# Получить текущую тему
theme = get_theme()  # 'light', 'dark', или 'auto'

# Получить target элемент
target = get_theme_target()  # 'html', 'body', или пользовательский

# Проверить, включен ли theme switcher
switcher_enabled = is_theme_switcher_enabled()
```

### Получение HTML элементов

```python
from metroui5.core import get_theme_meta_tag, get_theme_class, get_theme_switcher_html

# Получить meta тег
meta_tag = get_theme_meta_tag()

# Получить CSS класс темы
theme_class = get_theme_class()

# Получить HTML для theme switcher
switcher_html = get_theme_switcher_html()
```

## Примеры использования

### Простая страница с темной темой

```python
# settings.py
METROUI5 = {
	'theme': 'dark',
	'theme_switcher_enabled': True,
}
```

```html
{% extends "metroui5/layout/base.html" %} {% block content %}
<div class="container">
    <h1>Темная тема</h1>
    <p>Эта страница использует темную тему MetroUI 5.</p>
</div>
{% endblock %}
```

### Страница с автоматическим определением темы

```python
# settings.py
METROUI5 = {
	'theme': 'auto',
	'theme_switcher_enabled': True,
}
```

### Страница с пользовательским target

```python
# settings.py
METROUI5 = {
	'theme': 'light',
	'theme_target': '#app',
	'theme_switcher_enabled': True,
}
```

```html

<div id="app">
    <!-- Тема будет применена к этому элементу -->
    <div data-role="calendar"></div>
</div>
```

## Примечания

⚠️ **Важно!** Компонент `theme-switcher` не будет работать, если используется meta-тег!

- Для автоматического определения темы используйте `theme: 'auto'` и meta тег
- Для ручного переключения используйте `theme_switcher_enabled: True`
- Не используйте оба метода одновременно

## CSS классы

- **`.dark-side`** - применяет темную тему
- **Без класса** - применяет светлую тему (по умолчанию)

## JavaScript API

MetroUI 5 автоматически обрабатывает переключение тем через компонент `theme-switcher`. При изменении темы автоматически
добавляется/убирается класс `.dark-side` к указанному target элементу.
