# Справочник API рендереров

MetroUI5 Django предоставляет классы рендереров для рендеринга форм и полей со стилизацией MetroUI5.

## Обзор

Модуль рендереров предоставляет классы для рендеринга Django форм, полей и наборов форм с разметкой MetroUI5. Каждый рендерер обрабатывает преобразование объектов Django форм в HTML с правильными классами и атрибутами MetroUI5.

```python
from metroui5.renderers import BaseRenderer, FieldRenderer, FormRenderer, FormsetRenderer
from metroui5.css import merge_css_classes
from metroui5.html import render_tag
```

## Базовые классы

### `BaseRenderer`

Базовый класс для всех рендереров MetroUI с общей функциональностью.

**Методы:**

#### `__init__(self, form_or_field, **kwargs)`

Инициализирует рендерер с параметрами конфигурации.

**Параметры:**

- `form_or_field`: Экземпляр Django формы, поля или набора форм
- `**kwargs`: Параметры конфигурации рендерера

#### `get_widget_attrs(self, widget)`

Получает атрибуты виджета с классами MetroUI.

**Параметры:**

- `widget`: Экземпляр виджета Django формы

**Возвращает:** Словарь атрибутов виджета

**Пример:**

```python
class CustomRenderer(BaseRenderer):
    def render(self, **kwargs):
        widget_attrs = self.get_widget_attrs(self.field.field.widget)
        return render_tag("input", widget_attrs, close=False)
```

#### `get_field_classes(self, field)`

Получает CSS классы для поля формы.

**Параметры:**

- `field`: Экземпляр поля Django формы

**Возвращает:** Строку CSS классов

**Пример:**

```python
class FormRenderer(BaseRenderer):
    def render_field(self, field, **kwargs):
        field_classes = self.get_field_classes(field)
        
        return render_tag(
            "div",
            {"class": f"form-field {field_classes}"},
            field.as_widget(attrs=self.get_widget_attrs(field.field.widget))
        )
```

#### `render_errors(self, errors)`

Рендерит ошибки поля.

**Параметры:**

- `errors`: Список сообщений об ошибках

**Возвращает:** HTML строку

#### `render_help_text(self, help_text)`

Рендерит текст помощи для поля.

**Параметры:**

- `help_text`: Строка текста помощи

**Возвращает:** HTML строку

## Рендерер полей

### `FieldRenderer`

Рендерер для отдельных полей форм.

**Наследует от:** `BaseRenderer`

**Методы:**

#### `render(self)`

Рендерит поле формы в разметке MetroUI.

**Возвращает:** HTML строку

**Пример:**

```python
from metroui5.renderers import FieldRenderer

# Рендеринг одного поля
field_renderer = FieldRenderer(field, layout="horizontal")
field_html = field_renderer.render()
```

#### `render_label(self)`

Рендерит метку поля.

**Возвращает:** HTML строку

#### `render_widget(self)`

Рендерит виджет поля.

**Возвращает:** HTML строку

## Рендерер форм

### `FormRenderer`

Рендерер для Django форм.

**Наследует от:** `BaseRenderer`

**Методы:**

#### `render(self)`

Рендерит форму в разметке MetroUI.

**Возвращает:** HTML строку

**Пример:**

```python
from metroui5.renderers import FormRenderer

# Рендеринг полной формы
form_renderer = FormRenderer(form, layout="horizontal")
form_html = form_renderer.render()
```

#### `render_non_field_errors(self)`

Рендерит ошибки формы (не связанные с полями).

**Возвращает:** HTML строку

#### `render_hidden_fields(self)`

Рендерит скрытые поля формы.

**Возвращает:** HTML строку

#### `render_visible_fields(self)`

Рендерит видимые поля формы.

**Возвращает:** HTML строку

#### `render_errors(self, type="all")`

Рендерит ошибки формы.

**Параметры:**

- `type` (str): Тип ошибки - "all", "non_field"

**Возвращает:** HTML строку

## Рендерер наборов форм

### `FormsetRenderer`

Рендерер для Django наборов форм.

**Наследует от:** `BaseRenderer`

**Методы:**

#### `render(self)`

Рендерит набор форм в разметке MetroUI.

**Возвращает:** HTML строку

**Пример:**

```python
from metroui5.renderers import FormsetRenderer

# Рендеринг набора форм
formset_renderer = FormsetRenderer(formset)
formset_html = formset_renderer.render()
```

#### `render_formset_errors(self)`

Рендерит ошибки набора форм.

**Возвращает:** HTML строку

#### `render_management_form(self)`

Рендерит управляющую форму набора форм.

**Возвращает:** HTML строку

#### `render_errors(self)`

Рендерит ошибки набора форм.

**Возвращает:** HTML строку

## Параметры конфигурации

Все рендереры принимают эти параметры конфигурации:

### Параметры макета

- `layout` (str): Макет формы - "vertical" (по умолчанию) или "horizontal"
- `size` (str): Размер поля ввода - "mini", "small", "large"

### CSS классы

- `horizontal_label_class` (str): CSS класс для меток горизонтального макета
- `horizontal_field_class` (str): CSS класс для полей горизонтального макета
- `horizontal_field_offset_class` (str): CSS класс для отступов полей горизонтального макета
- `wrapper_class` (str): CSS класс для обертки поля
- `inline_wrapper_class` (str): CSS класс для встроенной обертки поля

### Параметры поведения

- `set_placeholder` (bool): Устанавливать ли текст-заполнитель
- `required_css_class` (str): CSS класс для обязательных полей
- `error_css_class` (str): CSS класс для полей с ошибками
- `success_css_class` (str): CSS класс для полей с состоянием успеха

## Примеры использования

### Базовый рендеринг поля

```python
from metroui5.renderers import FieldRenderer

def render_custom_field(field, **kwargs):
    """Рендерит поле с пользовательской стилизацией."""
    renderer = FieldRenderer(field, **kwargs)
    return renderer.render()

# Использование
field_html = render_custom_field(
    form['username'],
    layout="horizontal",
    size="large"
)
```

### Пользовательский рендерер формы

```python
from metroui5.renderers import FormRenderer

class CustomFormRenderer(FormRenderer):
    def render(self):
        """Пользовательский рендеринг формы с дополнительной стилизацией."""
        form_html = super().render()
        
        # Добавляем пользовательскую обертку
        return render_tag(
            "div",
            {"class": "custom-form-wrapper"},
            form_html
        )

# Использование
custom_renderer = CustomFormRenderer(form, layout="horizontal")
form_html = custom_renderer.render()
```

### Набор форм с пользовательской стилизацией

```python
from metroui5.renderers import FormsetRenderer

class StyledFormsetRenderer(FormsetRenderer):
    def render(self):
        """Рендерит набор форм с пользовательской стилизацией."""
        formset_html = super().render()
        
        # Добавляем контейнер набора форм
        return render_tag(
            "div",
            {"class": "styled-formset", "data-role": "formset"},
            formset_html
        )

# Использование
styled_renderer = StyledFormsetRenderer(formset)
formset_html = styled_renderer.render()
```

### Поле с пользовательскими атрибутами виджета

```python
from metroui5.renderers import FieldRenderer

class EnhancedFieldRenderer(FieldRenderer):
    def get_widget_attrs(self, widget):
        """Получает атрибуты виджета с улучшениями."""
        attrs = super().get_widget_attrs(widget)
        
        # Добавляем пользовательские атрибуты
        attrs.update({
            "data-role": "input",
            "data-validate": "true"
        })
        
        return attrs

# Использование
enhanced_renderer = EnhancedFieldRenderer(field)
field_html = enhanced_renderer.render()
```

## Лучшие практики

### 1. Последовательная конфигурация

```python
# Определяем общую конфигурацию рендерера
COMMON_RENDERER_CONFIG = {
    "layout": "horizontal",
    "size": "medium",
    "wrapper_class": "form-group",
    "error_css_class": "has-error",
    "success_css_class": "has-success"
}

# Используем в рендерерах
renderer = FormRenderer(form, **COMMON_RENDERER_CONFIG)
```

### 2. Пользовательская обработка ошибок

```python
class SafeFieldRenderer(FieldRenderer):
    def render(self):
        """Рендерит поле с обработкой ошибок."""
        try:
            return super().render()
        except Exception as e:
            # Логируем ошибку и возвращаем запасной вариант
            logger.error(f"Ошибка рендеринга поля: {e}")
            return f'<div class="field-error">Поле недоступно</div>'
```

### 3. Оптимизация производительности

```python
from functools import lru_cache

class CachedFormRenderer(FormRenderer):
    @lru_cache(maxsize=128)
    def get_cached_field_classes(self, field_id):
        """Кэширует классы полей для лучшей производительности."""
        field = self.form.fields.get(field_id)
        if field:
            return self.get_field_classes(field)
        return ""
```

## Связанная документация

- [API форм](forms.md) - Функции рендеринга форм
- [CSS утилиты](css.md) - Управление CSS классами
- [HTML утилиты](html.md) - Утилиты генерации HTML
- [Теги шаблонов](templatetags.md) - Интеграция с Django шаблонами
