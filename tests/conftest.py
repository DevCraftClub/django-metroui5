"""
Конфигурация pytest для django-metroui5
"""
import pytest
from django.conf import settings
from django.test import RequestFactory

# Настройки Django для тестов
pytest_plugins = ["pytest_django"]


@pytest.fixture
def rf():
    """RequestFactory для создания тестовых запросов"""
    return RequestFactory()


@pytest.fixture
def settings_with_metroui5():
    """Настройки Django с конфигурацией MetroUI5"""
    return {
        'METROUI5': {
            'css_url': {
                'url': 'metroui5/css/metro.all.css',
                'integrity': 'test-integrity',
                'crossorigin': 'anonymous',
            },
            'javascript_url': {
                'url': 'metroui5/js/metro.all.js',
                'defer': True,
            },
            'icons_css_url': {
                'url': 'metroui5/icons/icons.css',
            },
            'wrapper_class': 'test-wrapper',
            'horizontal_label_class': 'col-sm-3',
            'horizontal_field_class': 'col-sm-9',
            'theme': 'dark',
            'cdn_mode': True,
        }
    }


@pytest.fixture
def sample_form_data():
    """Тестовые данные для форм"""
    return {
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'Test message',
        'agree': True,
    }


@pytest.fixture
def sample_field_data():
    """Тестовые данные для полей форм"""
    return {
        'name': 'test_field',
        'label': 'Test Field',
        'value': 'test_value',
        'help_text': 'Help text for field',
        'errors': ['This field is required'],
    }
