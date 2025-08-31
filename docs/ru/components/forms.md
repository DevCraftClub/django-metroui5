# Формы (Forms)

Компонент для рендеринга Django форм с MetroUI5 стилями.

## Основное использование

### Рендеринг формы

```python
from metroui5.forms import render_form

# Рендеринг формы с MetroUI5 стилями
form_html = render_form(form)
```

### Форма с параметрами

```python
# Форма с дополнительными параметрами
form_html = render_form(
	form,
	layout='horizontal',
	submit_text="Отправить",
	submit_class="btn btn-primary"
)
```

## Параметры

### `form` (обязательный)

Django форма для рендеринга.

```python
from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)


# Рендеринг формы
form = ContactForm()
form_html = render_form(form)
```

### `layout` (опционально)

Макет формы. Доступные значения:

- `"vertical"` (по умолчанию) - вертикальное расположение
- `"horizontal"` - горизонтальное расположение

```python
form_html = render_form(form, layout='horizontal')
```

### `submit_text` (опционально)

Текст кнопки отправки. По умолчанию "Submit".

```python
form_html = render_form(form, submit_text="Отправить сообщение")
```

### `submit_class` (опционально)

CSS классы для кнопки отправки.

```python
form_html = render_form(
	form,
	submit_class="btn btn-primary btn-lg"
)
```

### `**kwargs` (опционально)

Дополнительные параметры для рендерера.

```python
form_html = render_form(
	form,
	label_class="custom-label",
	field_class="custom-field",
	help_text_class="custom-help"
)
```

## Примеры использования

### В представлении

```python
from django.shortcuts import render
from metroui5.forms import render_form
from .forms import ContactForm


def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Обработка формы
			return redirect('success')
	else:
		form = ContactForm()

	# Рендерим форму с MetroUI5 стилями
	form_html = render_form(
		form,
		layout='horizontal',
		submit_text="Отправить сообщение",
		submit_class="btn btn-primary"
	)

	return render(request, 'contact.html', {'form': form_html})
```

### В шаблоне

```html
{% extends 'base.html' %} {% block content %}
<h2>Свяжитесь с нами</h2>

{{ form|safe }} {% endblock %}
```

### Рендеринг отдельного поля

```python
from metroui5.forms import render_field


def custom_form_view(request):
	form = ContactForm()

	# Рендерим только определенные поля
	name_field = render_field(
		form['name'],
		placeholder="Введите ваше имя",
		label_class="custom-label"
	)

	email_field = render_field(
		form['email'],
		placeholder="Введите email",
		label_class="custom-label"
	)

	context = {
		'name_field': name_field,
		'email_field': email_field,
	}

	return render(request, 'custom_form.html', context)
```

### Рендеринг ошибок формы

```python
from metroui5.forms import render_form_errors


def form_with_errors(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Обработка формы
			pass
		else:
			# Рендерим ошибки
			errors_html = render_form_errors(form)
	else:
		form = ContactForm()
		errors_html = None

	form_html = render_form(form)

	context = {
		'form': form_html,
		'errors': errors_html,
	}

	return render(request, 'form_with_errors.html', context)
```

## Кастомизация

### Дополнительные CSS классы

```python
form_html = render_form(
	form,
	**{
		"form_class": "custom-form",
		"label_class": "custom-label",
		"field_class": "custom-field",
		"help_text_class": "custom-help"
	}
)
```

### Атрибуты для JavaScript

```python
form_html = render_form(
	form,
	**{
		"form_attrs": {
			"data-form-id": "contact",
			"data-ajax": "true"
		},
		"submit_attrs": {
			"onclick": "validateForm()",
			"data-loading": "Отправка..."
		}
	}
)
```

### Стилизация через CSS

```css
/* Кастомные стили для форм */
.custom-form {
    background: #f8f9fa;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.custom-label {
    font-weight: bold;
    color: #495057;
    margin-bottom: 0.5rem;
}

.custom-field {
    border: 2px solid #dee2e6;
    border-radius: 4px;
    padding: 0.75rem;
    transition: border-color 0.3s ease;
}

.custom-field:focus {
    border-color: #007bff;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.custom-help {
    font-size: 0.875rem;
    color: #6c757d;
    margin-top: 0.25rem;
}
```

## Макеты форм

### Вертикальный макет (по умолчанию)

```python
form_html = render_form(form, layout='vertical')
```

Результат:

```html

<form method="post">
    <div class="form-group">
        <label for="id_name">Имя:</label>
        <input type="text" name="name" id="id_name" class="form-control"/>
        <div class="help-text">Введите ваше имя</div>
    </div>

    <div class="form-group">
        <label for="id_email">Email:</label>
        <input type="email" name="email" id="id_email" class="form-control"/>
        <div class="help-text">Введите ваш email</div>
    </div>

    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
```

### Горизонтальный макет

```python
form_html = render_form(form, layout='horizontal')
```

Результат:

```html

<form method="post">
    <div class="form-group row">
        <label for="id_name" class="col-sm-2 col-form-label">Имя:</label>
        <div class="col-sm-10">
            <input type="text" name="name" id="id_name" class="form-control"/>
            <div class="help-text">Введите ваше имя</div>
        </div>
    </div>

    <div class="form-group row">
        <label for="id_email" class="col-sm-2 col-form-label">Email:</label>
        <div class="col-sm-10">
            <input type="email" name="email" id="id_email" class="form-control"/>
            <div class="help-text">Введите ваш email</div>
        </div>
    </div>

    <div class="form-group row">
        <div class="col-sm-10 offset-sm-2">
            <button type="submit" class="btn btn-primary">Отправить</button>
        </div>
    </div>
</form>
```

## Работа с ошибками

### Отображение ошибок поля

```python
from metroui5.forms import render_field


def field_with_errors(request):
	form = ContactForm(request.POST or None)

	if form.is_valid():
		# Обработка формы
		pass

	# Рендерим поле с ошибками
	name_field = render_field(
		form['name'],
		show_errors=True,
		error_class="alert alert-danger"
	)

	return render(request, 'field_with_errors.html', {'field': name_field})
```

### Кастомные сообщения об ошибках

```python
def custom_error_messages(request):
	form = ContactForm(request.POST or None)

	if form.is_valid():
		# Обработка формы
		pass

	# Рендерим форму с кастомными сообщениями об ошибках
	form_html = render_form(
		form,
		error_class="alert alert-danger",
		error_icon="exclamation-triangle"
	)

	return render(request, 'custom_errors.html', {'form': form_html})
```

## Лучшие практики

### 1. Используйте подходящие макеты

```python
# Хорошо - горизонтальный макет для длинных форм
long_form = render_form(
	form_with_many_fields,
	layout='horizontal'
)

# Хорошо - вертикальный макет для коротких форм
short_form = render_form(
	simple_form,
	layout='vertical'
)
```

### 2. Добавляйте понятные тексты кнопок

```python
# Хорошо
form_html = render_form(
	form,
	submit_text="Сохранить изменения",
	submit_class="btn btn-success"
)

# Плохо
form_html = render_form(form, submit_text="Submit")
```

### 3. Группируйте связанные поля

```python
def grouped_form_view(request):
	form = ComplexForm()

	# Группируем поля по категориям
	personal_fields = [form['first_name'], form['last_name'], form['email']]
	address_fields = [form['street'], form['city'], form['zip_code']]

	personal_html = "".join([render_field(field) for field in personal_fields])
	address_html = "".join([render_field(field) for field in address_fields])

	context = {
		'personal_section': render_field_group("Личная информация", personal_html),
		'address_section': render_field_group("Адрес", address_html),
	}

	return render(request, 'grouped_form.html', context)
```

### 4. Обрабатывайте валидацию

```python
def form_validation_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Обработка успешной валидации
			messages.success(request, "Форма успешно отправлена!")
			return redirect('success')
		else:
			# Обработка ошибок валидации
			messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
	else:
		form = ContactForm()

	form_html = render_form(
		form,
		submit_text="Отправить",
		submit_class="btn btn-primary"
	)

	return render(request, 'form_validation.html', {'form': form_html})
```

## Решение проблем

### Форма не отображается

1. Проверьте, что функция `render_form` импортирована
2. Убедитесь, что в шаблоне используется `|safe` фильтр
3. Проверьте, что форма передана в контекст

### Стили не применяются

1. Убедитесь, что MetroUI5 CSS загружен
2. Проверьте, что нет конфликтующих CSS правил
3. Используйте инспектор браузера для проверки применяемых стилей

### Ошибки валидации не отображаются

1. Убедитесь, что форма содержит данные (POST)
2. Проверьте, что `show_errors=True` установлен
3. Убедитесь, что форма имеет ошибки валидации

## Связанные компоненты

- [Кнопки](buttons.md) - для кнопок отправки
- [Алерты](alerts.md) - для отображения ошибок
- [Карточки](cards.md) - для группировки форм
- [Поля ввода](inputs.md) - для отдельных полей

## Следующие шаги

Теперь, когда вы освоили формы:

1. Изучите другие [компоненты](../) для создания полноценных интерфейсов
2. Ознакомьтесь с [примерами](../../getting-started/examples.md)
3. Изучите [API справочник](../../api-reference/) для детальной информации
4. Создайте интерактивные и красивые формы!
