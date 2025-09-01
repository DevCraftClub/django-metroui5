# Формы

MetroUI5 Django предоставляет комплексные утилиты для рендеринга форм для создания форм в стиле MetroUI с правильной валидацией, обработкой ошибок и адаптивным дизайном.

## Базовое использование

```python
from metroui5.forms import render_form, render_field, render_formset

# Рендеринг полной формы
form_html = render_form(form)

# Рендеринг одного поля
field_html = render_field(form['username'])

# Рендеринг набора форм
formset_html = render_formset(formset)
```

## Функции

### `render_form(form, **kwargs)`

Рендерит полную Django форму со стилизацией MetroUI.

**Параметры:**

- `form`: Экземпляр Django формы
- `**kwargs`: Дополнительные опции рендеринга

**Возвращает:**

- `str`: Рендеренный HTML формы

**Пример:**

```python
from metroui5.forms import render_form
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

form = UserForm()
form_html = render_form(form)
```

### `render_field(field, **kwargs)`

Рендерит одно поле формы со стилизацией MetroUI.

**Параметры:**

- `field`: Экземпляр поля Django формы
- `**kwargs`: Дополнительные опции рендеринга

**Возвращает:**

- `str`: Рендеренный HTML поля

**Пример:**

```python
from metroui5.forms import render_field

# Рендеринг конкретного поля
username_field = form['username']
field_html = render_field(username_field, label_class="field-label", input_class="input")
```

### `render_formset(formset, **kwargs)`

Рендерит Django набор форм со стилизацией MetroUI.

**Параметры:**

- `formset`: Экземпляр Django набора форм
- `**kwargs`: Дополнительные опции рендеринга

**Возвращает:**

- `str`: Рендеренный HTML набора форм

**Пример:**

```python
from metroui5.forms import render_formset
from django.forms import formset_factory

UserFormSet = formset_factory(UserForm, extra=3)
formset = UserFormSet()
formset_html = render_formset(formset)
```

### `render_form_errors(form, type="all", **kwargs)`

Рендерит ошибки формы со стилизацией MetroUI.

**Параметры:**

- `form`: Экземпляр Django формы
- `type` (str): Тип ошибки ("all", "field", "non_field")
- `**kwargs`: Дополнительные опции рендеринга

**Возвращает:**

- `str`: Рендеренный HTML ошибок

**Пример:**

```python
from metroui5.forms import render_form_errors

# Рендеринг всех ошибок
errors_html = render_form_errors(form)

# Рендеринг только ошибок полей
field_errors = render_form_errors(form, type="field")

# Рендеринг только неполевых ошибок
non_field_errors = render_form_errors(form, type="non_field")
```

### `render_formset_errors(formset, **kwargs)`

Рендерит ошибки набора форм со стилизацией MetroUI.

**Параметры:**

- `formset`: Экземпляр Django набора форм
- `**kwargs`: Дополнительные опции рендеринга

**Возвращает:**

- `str`: Рендеренный HTML ошибок набора форм

**Пример:**

```python
from metroui5.forms import render_formset_errors

formset_errors = render_formset_errors(formset)
```

### `render_label(field, **kwargs)`

Рендерит метку поля формы со стилизацией MetroUI.

**Параметры:**

- `field`: Экземпляр поля Django формы
- `**kwargs`: Дополнительные опции рендеринга

**Возвращает:**

- `str`: Рендеренный HTML метки

**Пример:**

```python
from metroui5.forms import render_label

label_html = render_label(form['email'], class="field-label")
```

## Опции рендеринга форм

### Базовый рендеринг форм

```python
# Простая форма
form_html = render_form(form)

# Форма с пользовательскими классами
form_html = render_form(
    form,
    form_class="form-custom",
    field_class="field-custom",
    label_class="label-custom"
)
```

### Рендеринг конкретных полей

```python
# Рендеринг поля с пользовательскими опциями
field_html = render_field(
    form['username'],
    label_class="field-label",
    input_class="input input-large",
    help_text_class="help-text",
    error_class="error-message"
)
```

### Рендеринг набора форм

```python
# Рендеринг набора форм с управляющей формой
formset_html = render_formset(
    formset,
    formset_class="formset-custom",
    form_class="form-inline",
    add_button_text="Добавить еще",
    remove_button_text="Удалить"
)
```

## Расширенное использование

### Пользовательский макет формы

```python
def render_custom_form(form, layout="vertical"):
    """Рендеринг формы с пользовательскими опциями макета."""

    if layout == "horizontal":
        return render_form(
            form,
            form_class="form form-horizontal",
            field_class="field field-horizontal",
            label_class="label label-horizontal"
        )
    elif layout == "inline":
        return render_form(
            form,
            form_class="form form-inline",
            field_class="field field-inline"
        )
    else:
        return render_form(
            form,
            form_class="form form-vertical",
            field_class="field field-vertical"
        )

# Использование
vertical_form = render_custom_form(form, "vertical")
horizontal_form = render_custom_form(form, "horizontal")
inline_form = render_custom_form(form, "inline")
```

### Условный рендеринг полей

```python
def render_conditional_fields(form, user_permissions):
    """Рендеринг полей на основе разрешений пользователя."""

    rendered_fields = []

    for field_name, field in form.fields.items():
        # Проверка, есть ли у пользователя разрешение видеть это поле
        if hasattr(field, 'permission_required'):
            if field.permission_required not in user_permissions:
                continue

        # Рендеринг поля с условной стилизацией
        field_html = render_field(
            form[field_name],
            disabled=field_name in ['readonly_field1', 'readonly_field2'],
            readonly=field_name in ['readonly_field1', 'readonly_field2']
        )
        rendered_fields.append(field_html)

    return "\n".join(rendered_fields)

# Использование
user_perms = ['can_edit', 'can_view']
fields_html = render_conditional_fields(form, user_perms)
```

### Динамическая валидация форм

```python
def render_form_with_validation(form, validation_rules):
    """Рендеринг формы с пользовательскими правилами валидации."""

    form_html = render_form(form)

    # Добавление JavaScript валидации
    validation_js = """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const form = document.querySelector('#%s');
        if (form) {
            form.addEventListener('submit', function(e) {
                if (!validateForm(form, %s)) {
                    e.preventDefault();
                }
            });
        }
    });
    </script>
    """ % (form.auto_id, validation_rules)

    return form_html + validation_js

# Использование
validation_rules = {
    'username': {'required': True, 'min_length': 3},
    'email': {'required': True, 'email': True},
    'password': {'required': True, 'min_length': 8}
}

form_with_validation = render_form_with_validation(form, validation_rules)
```

### Адаптивный макет формы

```python
def render_responsive_form(form, breakpoints=None):
    """Рендеринг формы с адаптивным макетом."""

    if breakpoints is None:
        breakpoints = {
            'mobile': {'columns': 1, 'stack': True},
            'tablet': {'columns': 2, 'stack': False},
            'desktop': {'columns': 3, 'stack': False}
        }

    form_class = "form form-responsive"

    # Добавление адаптивных классов
    for breakpoint, config in breakpoints.items():
        if config['columns'] > 1:
            form_class += f" form-{breakpoint}-columns-{config['columns']}"
        if config['stack']:
            form_class += f" form-{breakpoint}-stack"

    return render_form(form, form_class=form_class)

# Использование
responsive_form = render_responsive_form(form)
```

## Типы полей форм

### Текстовые поля ввода

```python
# Текстовое поле
text_field = render_field(
    form['username'],
    input_class="input",
    placeholder="Введите имя пользователя"
)

# Поле email
email_field = render_field(
    form['email'],
    input_class="input",
    type="email",
    placeholder="Введите email адрес"
)

# Поле пароля
password_field = render_field(
    form['password'],
    input_class="input",
    type="password",
    placeholder="Введите пароль"
)
```

### Поля выбора

```python
# Выпадающий список
select_field = render_field(
    form['country'],
    input_class="select",
    data_role="select"
)

# Множественный выбор
multi_select_field = render_field(
    form['languages'],
    input_class="select",
    multiple=True,
    data_role="select"
)
```

### Поля флажков и радиокнопок

```python
# Флажок
checkbox_field = render_field(
    form['agree_terms'],
    input_class="checkbox",
    data_role="checkbox"
)

# Радиокнопки
radio_field = render_field(
    form['gender'],
    input_class="radio",
    data_role="radio"
)
```

### Поля текстовой области

```python
# Текстовая область
textarea_field = render_field(
    form['description'],
    input_class="textarea",
    rows=5,
    placeholder="Введите описание..."
)
```

## Обработка ошибок

### Ошибки на уровне полей

```python
def render_field_with_errors(field):
    """Рендеринг поля с обработкой ошибок."""

    field_html = render_field(field)

    if field.errors:
        error_html = render_form_errors(field.form, type="field")
        return field_html + error_html

    return field_html

# Использование
field_with_errors = render_field_with_errors(form['username'])
```

### Ошибки на уровне формы

```python
def render_form_with_error_summary(form):
    """Рендеринг формы с резюме ошибок вверху."""

    # Сначала рендеринг неполевых ошибок
    non_field_errors = render_form_errors(form, type="non_field")

    # Рендеринг формы
    form_html = render_form(form)

    return non_field_errors + form_html

# Использование
form_with_summary = render_form_with_error_summary(form)
```

## Лучшие практики

1. **Используйте семантические имена полей**: Выбирайте описательные имена полей
2. **Предоставляйте полезные метки**: Делайте метки ясными и описательными
3. **Включайте текст-заполнитель**: Используйте заполнители для руководства пользователями
4. **Обрабатывайте ошибки изящно**: Отображайте ошибки ясно и полезно
5. **Делайте формы доступными**: Включайте правильные ARIA метки и управление фокусом
6. **Тестируйте тщательно**: Тестируйте формы с различными комбинациями ввода
7. **Используйте последовательную стилизацию**: Применяйте последовательные классы во всем приложении

## Связанные функции

- [Компоненты](components.md) - Для компонентов, связанных с формами
- [HTML утилиты](html.md) - Для генерации HTML элементов
- [Рендереры](renderers.md) - Для расширенного рендеринга форм
