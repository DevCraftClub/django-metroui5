# CSS утилиты

MetroUI5 Django предоставляет CSS утилиты для управления CSS классами и стилями.

## Базовое использование

```python
from metroui5.css import merge_css_classes, add_css_class, remove_css_class

# Объединение CSS классов
classes = merge_css_classes("button", "button-primary", "button-large")

# Добавление CSS класса
button_with_primary = add_css_class("button", "button-primary")

# Удаление CSS класса
button_without_primary = remove_css_class("button button-primary", "button-primary")
```

## Доступные функции

### `merge_css_classes(*args)`

Объединяет несколько CSS классов в одну строку, обрабатывая дубликаты и пустые значения.

**Параметры:**

- `*args`: Переменное количество строк CSS классов, списков или кортежей

**Возвращает:**

- `str`: Объединенная строка CSS классов

**Пример:**

```python
from metroui5.css import merge_css_classes

# Базовое объединение
classes = merge_css_classes("button", "button-primary", "button-large")
# Результат: "button button-primary button-large"

# Обработка дубликатов
classes = merge_css_classes("button", "button", "button-primary")
# Результат: "button button-primary"

# Обработка пустых значений
classes = merge_css_classes("button", "", None, "button-primary")
# Результат: "button button-primary"

# Смешивание строк и списков
classes = merge_css_classes("button", ["button-primary", "button-large"])
# Результат: "button button-primary button-large"
```

### `add_css_class(classes, new_class)`

Добавляет новый CSS класс к существующим.

**Параметры:**

- `classes`: Существующие CSS классы (строка, список или кортеж)
- `new_class` (str): Новый CSS класс для добавления

**Возвращает:**

- `str`: Строка с обновленными CSS классами

**Пример:**

```python
from metroui5.css import add_css_class

# Добавление класса к существующим классам
button_with_primary = add_css_class("button", "button-primary")
# Результат: "button button-primary"

# Добавление класса к списку классов
button_with_size = add_css_class(["button", "button-primary"], "button-large")
# Результат: "button button-primary button-large"

# Обработка дубликатов (не добавит, если уже присутствует)
button_no_duplicate = add_css_class("button button-primary", "button-primary")
# Результат: "button button-primary"
```

### `remove_css_class(classes, class_to_remove)`

Удаляет CSS класс из существующих.

**Параметры:**

- `classes`: Существующие CSS классы (строка, список или кортеж)
- `class_to_remove` (str): CSS класс для удаления

**Возвращает:**

- `str`: Строка с обновленными CSS классами

**Пример:**

```python
from metroui5.css import remove_css_class

# Удаление класса из существующих классов
button_without_primary = remove_css_class("button button-primary", "button-primary")
# Результат: "button"

# Удаление класса из списка классов
button_without_size = remove_css_class(["button", "button-primary", "button-large"], "button-large")
# Результат: "button button-primary"

# Обработка несуществующего класса (без изменений)
button_unchanged = remove_css_class("button button-primary", "button-large")
# Результат: "button button-primary"
```

## Внутренние функции

### `_css_class_list(classes)`

Преобразует CSS классы в список (внутренняя утилита).

**Параметры:**

- `classes`: CSS классы как строка, список или кортеж

**Возвращает:**

- `list`: Список CSS классов

**Примечание:** Это внутренняя функция, используемая другими CSS утилитами.

## Примеры использования

### Базовое управление классами

```python
from metroui5.css import merge_css_classes, add_css_class, remove_css_class

# Начинаем с базовых классов
base_classes = "button"

# Добавляем основной стиль
button_classes = add_css_class(base_classes, "button-primary")

# Добавляем размер
button_classes = add_css_class(button_classes, "button-large")

# Удаляем размер
button_classes = remove_css_class(button_classes, "button-large")

print(button_classes)  # Вывод: "button button-primary"
```

### Динамическое построение классов

```python
from metroui5.css import merge_css_classes

def build_button_classes(button_type="default", size=None, disabled=False):
    """Динамически строит CSS классы кнопки."""
    classes = ["button"]

    if button_type != "default":
        classes.append(f"button-{button_type}")

    if size:
        classes.append(f"button-{size}")

    if disabled:
        classes.append("button-disabled")

    return merge_css_classes(*classes)

# Использование
primary_button = build_button_classes("primary", "large")
# Результат: "button button-primary button-large"

disabled_button = build_button_classes("secondary", disabled=True)
# Результат: "button button-secondary button-disabled"
```

### Управление классами компонентов

```python
from metroui5.css import merge_css_classes, add_css_class

class ComponentCSSManager:
    def __init__(self, base_class):
        self.base_class = base_class
        self.classes = [base_class]

    def add_modifier(self, modifier):
        """Добавляет класс-модификатор."""
        if modifier:
            self.classes.append(f"{self.base_class}-{modifier}")
        return self

    def add_state(self, state):
        """Добавляет класс состояния."""
        if state:
            self.classes.append(f"{self.base_class}-{state}")
        return self

    def get_classes(self):
        """Получает финальную строку CSS классов."""
        return merge_css_classes(*self.classes)

# Использование
button_css = ComponentCSSManager("button")
button_css.add_modifier("primary").add_state("hover")
final_classes = button_css.get_classes()
# Результат: "button button-primary button-hover"
```

### Классы полей форм

```python
from metroui5.css import merge_css_classes, add_css_class

def get_field_classes(field_type="text", size="medium", has_error=False):
    """Получает CSS классы для полей форм."""
    base_classes = ["form-control", f"form-control-{field_type}"]

    if size != "medium":
        base_classes.append(f"form-control-{size}")

    if has_error:
        base_classes.append("form-control-error")

    return merge_css_classes(*base_classes)

# Использование
text_field = get_field_classes("text", "large")
# Результат: "form-control form-control-text form-control-large"

error_field = get_field_classes("email", has_error=True)
# Результат: "form-control form-control-email form-control-error"
```

## Лучшие практики

### 1. Последовательное именование

```python
# Используйте последовательные паттерны именования классов
def get_button_classes(variant="default", size="medium"):
    """Получает классы кнопки с последовательным именованием."""
    classes = ["btn"]

    if variant != "default":
        classes.append(f"btn-{variant}")

    if size != "medium":
        classes.append(f"btn-{size}")

    return merge_css_classes(*classes)
```

### 2. Обработка граничных случаев

```python
def safe_add_class(existing_classes, new_class):
    """Безопасно добавляет CSS класс с обработкой ошибок."""
    if not new_class or not isinstance(new_class, str):
        return existing_classes

    try:
        return add_css_class(existing_classes, new_class)
    except Exception:
        return existing_classes
```

### 3. Оптимизация производительности

```python
# Кэширование часто используемых комбинаций классов
from functools import lru_cache

@lru_cache(maxsize=128)
def get_cached_button_classes(variant, size):
    """Кэширует комбинации классов кнопок для лучшей производительности."""
    return get_button_classes(variant, size)
```

## Связанная документация

- [Компоненты](components.md) - Функции рендеринга компонентов
- [HTML утилиты](html.md) - Утилиты генерации HTML
- [Теги шаблонов](templatetags.md) - Интеграция с Django шаблонами
