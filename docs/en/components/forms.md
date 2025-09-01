# Forms

Component for rendering Django forms with MetroUI5 styles.

## Basic Usage

### Form Rendering

```python
from metroui5.forms import render_form

# Render form with MetroUI5 styles
form_html = render_form(form)
```

### Form with Parameters

```python
# Form with additional parameters
form_html = render_form(
    form,
    layout='horizontal',
    submit_text="Submit",
    submit_class="btn btn-primary"
)
```

## Parameters

### `form` (required)

Django form to render.

```python
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


# Render form
form = ContactForm()
form_html = render_form(form)
```

### `layout` (optional)

Form layout. Available values:

- `"vertical"` (default) - vertical arrangement
- `"horizontal"` - horizontal arrangement

```python
form_html = render_form(form, layout='horizontal')
```

### `submit_text` (optional)

Submit button text. Default is "Submit".

```python
form_html = render_form(form, submit_text="Send Message")
```

### `submit_class` (optional)

CSS classes for submit button.

```python
form_html = render_form(
    form,
    submit_class="btn btn-primary btn-lg"
)
```

### `**kwargs` (optional)

Additional parameters for renderer.

```python
form_html = render_form(
    form,
    label_class="custom-label",
    field_class="custom-field",
    help_text_class="custom-help"
)
```

## Usage Examples

### In Views

```python
from django.shortcuts import render
from metroui5.forms import render_form
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form
            return redirect('success')
    else:
        form = ContactForm()

    # Render form with MetroUI5 styling
    form_html = render_form(
        form,
        layout='horizontal',
        submit_text="Send Message",
        submit_class="btn btn-primary btn-lg"
    )

    context = {'form_html': form_html}
    return render(request, 'contact.html', context)
```

### In Templates

```html
<!-- contact.html -->
{% load metroui5 %} {% block content %}
<h1>Contact Us</h1>

<!-- Direct HTML output -->
{{ form_html|safe }} {% endblock %}
```

## Field Rendering

### Rendering Individual Field

```python
from metroui5.forms import render_field

def field_view(request):
    form = ContactForm()

    # Render individual fields
    name_field = render_field(
        form['name'],
        label_class="custom-label",
        field_class="custom-input"
    )

    email_field = render_field(
        form['email'],
        placeholder="Enter your email",
        help_text="We'll never share your email"
    )

    context = {
        'name_field': name_field,
        'email_field': email_field
    }
    return render(request, 'field.html', context)
```

### Field with Custom Styling

```python
def styled_field_view(request):
    form = ContactForm()

    # Custom styled field
    styled_field = render_field(
        form['message'],
        label_class="form-label-large",
        field_class="form-control-custom",
        help_text_class="help-text-styled",
        wrapper_class="field-wrapper-custom"
    )

    context = {'styled_field': styled_field}
    return render(request, 'styled_field.html', context)
```

## Form Errors

### Rendering Form Errors

```python
from metroui5.forms import render_form_errors

def error_view(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        # Process form
        pass
    else:
        # Render form errors
        error_html = render_form_errors(form)

    context = {'error_html': error_html}
    return render(request, 'error.html', context)
```

### Custom Error Styling

```python
def custom_error_view(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        # Custom error styling
        error_html = render_form_errors(
            form,
            error_class="alert alert-danger",
            error_wrapper_class="error-container"
        )

    context = {'error_html': error_html}
    return render(request, 'custom_error.html', context)
```

## Formset Rendering

### Basic Formset

```python
from metroui5.forms import render_formset
from django.forms import formset_factory

def formset_view(request):
    ContactFormSet = formset_factory(ContactForm, extra=3)

    if request.method == 'POST':
        formset = ContactFormSet(request.POST)
        if formset.is_valid():
            # Process formset
            pass
    else:
        formset = ContactFormSet()

    # Render formset
    formset_html = render_formset(
        formset,
        layout='horizontal',
        submit_text="Submit All"
    )

    context = {'formset_html': formset_html}
    return render(request, 'formset.html', context)
```

### Formset with Management

```python
def managed_formset_view(request):
    ContactFormSet = formset_factory(ContactForm, extra=2, max_num=5)

    if request.method == 'POST':
        formset = ContactFormSet(request.POST)
        if formset.is_valid():
            # Process formset
            pass
    else:
        formset = ContactFormSet()

    # Render with management form
    formset_html = render_formset(
        formset,
        show_management_form=True,
        management_form_class="management-form"
    )

    context = {'formset_html': formset_html}
    return render(request, 'managed_formset.html', context)
```

## Advanced Examples

### Dynamic Form Generation

```python
def dynamic_form_view(request):
    # Dynamic form fields based on user permissions
    fields = ['name', 'email']  # Basic fields

    if request.user.is_staff:
        fields.extend(['phone', 'company'])

    if request.user.has_perm('app.can_see_sensitive'):
        fields.append('ssn')

    # Create dynamic form
    class DynamicContactForm(forms.Form):
        pass

    for field_name in fields:
        if field_name == 'email':
            DynamicContactForm.base_fields[field_name] = forms.EmailField()
        elif field_name == 'phone':
            DynamicContactForm.base_fields[field_name] = forms.CharField(max_length=20)
        elif field_name == 'ssn':
            DynamicContactForm.base_fields[field_name] = forms.CharField(max_length=11)
        else:
            DynamicContactForm.base_fields[field_name] = forms.CharField(max_length=100)

    form = DynamicContactForm()
    form_html = render_form(form)

    context = {'form_html': form_html}
    return render(request, 'dynamic_form.html', context)
```

### Conditional Form Rendering

```python
def conditional_form_view(request):
    user_type = request.GET.get('type', 'individual')

    if user_type == 'business':
        form_class = BusinessContactForm
        submit_text = "Submit Business Inquiry"
        layout = 'horizontal'
    else:
        form_class = IndividualContactForm
        submit_text = "Submit Personal Inquiry"
        layout = 'vertical'

    form = form_class()
    form_html = render_form(
        form,
        layout=layout,
        submit_text=submit_text,
        submit_class=f"btn btn-{user_type}"
    )

    context = {'form_html': form_html}
    return render(request, 'conditional_form.html', context)
```

## Best Practices

### 1. Consistent Styling

```python
# Define consistent form styling
FORM_STYLING = {
    'layout': 'horizontal',
    'label_class': 'form-label',
    'field_class': 'form-control',
    'help_text_class': 'form-help',
    'error_class': 'form-error'
}

def consistent_form_view(request):
    form = ContactForm()
    form_html = render_form(form, **FORM_STYLING)

    context = {'form_html': form_html}
    return render(request, 'consistent_form.html', context)
```

### 2. Error Handling

```python
def robust_form_view(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Process form
                return redirect('success')
        else:
            form = ContactForm()

        form_html = render_form(form)

    except Exception as e:
        # Handle rendering errors gracefully
        form_html = f'<div class="alert alert-danger">Form unavailable: {str(e)}</div>'

    context = {'form_html': form_html}
    return render(request, 'robust_form.html', context)
```

### 3. Performance Optimization

```python
from django.core.cache import cache

def cached_form_view(request):
    cache_key = f"form_{request.user.id}"

    # Try to get cached form
    form_html = cache.get(cache_key)

    if not form_html:
        form = ContactForm()
        form_html = render_form(form)

        # Cache for 5 minutes
        cache.set(cache_key, form_html, 300)

    context = {'form_html': form_html}
    return render(request, 'cached_form.html', context)
```

## Related Documentation

- [Components](components.md) - Component rendering functions
- [Template Tags](templatetags.md) - Django template integration
- [HTML Utilities](html.md) - HTML generation utilities
- [CSS Utilities](css.md) - CSS class management
