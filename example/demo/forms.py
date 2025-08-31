"""
Demo forms для демонстрации MetroUI5.
"""

from django import forms


class ContactForm(forms.Form):
    """Форма контактов для демонстрации."""
    
    name = forms.CharField(
        label="Имя",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите ваше имя',
            'class': 'input-lg'
        })
    )
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com',
            'class': 'input-lg'
        })
    )
    
    subject = forms.CharField(
        label="Тема",
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Тема сообщения'
        })
    )
    
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'Введите ваше сообщение...',
            'class': 'textarea'
        })
    )
    
    newsletter = forms.BooleanField(
        label="Подписаться на новости",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox'
        })
    )
    
    priority = forms.ChoiceField(
        label="Приоритет",
        choices=[
            ('low', 'Низкий'),
            ('medium', 'Средний'),
            ('high', 'Высокий'),
        ],
        widget=forms.Select(attrs={
            'class': 'select'
        })
    )


class UserProfileForm(forms.Form):
    """Форма профиля пользователя для демонстрации."""
    
    username = forms.CharField(
        label="Имя пользователя",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя'
        })
    )
    
    first_name = forms.CharField(
        label="Имя",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя'
        })
    )
    
    last_name = forms.CharField(
        label="Фамилия",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите фамилию'
        })
    )
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com'
        })
    )
    
    bio = forms.CharField(
        label="О себе",
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Расскажите о себе...'
        })
    )
    
    avatar = forms.ImageField(
        label="Аватар",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'file-input'
        })
    )
    
    is_active = forms.BooleanField(
        label="Активный пользователь",
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox'
        })
    )
