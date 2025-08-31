"""
Django settings for example project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-example-key-for-development-only'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'metroui5',  # Django MetroUI5 package
    'demo',  # Demo app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'example_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'example_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MetroUI5 Configuration
METROUI5 = {
    # Core MetroUI files - you can customize these
    'css_url': {
        'url': 'metroui5/css/metro.all.css',
        'integrity': None,
        'crossorigin': None,
        'type': 'text/css',
        'media': 'all',
    },
    'javascript_url': {
        'url': 'metroui5/js/metro.all.js',
        'integrity': None,
        'crossorigin': None,
        'type': 'text/javascript',
        'defer': False,
        'async': False,
    },
    'icons_css_url': {
        'url': 'metroui5/icons/icons.css',
        'integrity': None,
        'crossorigin': None,
        'type': 'text/css',
        'media': 'all',
    },
    
    # Custom CSS/JS files (optional)
    'custom_css_files': [
        # 'css/custom-styles.css',  # Uncomment to add custom CSS
        # 'css/print.css',          # Uncomment to add print styles
    ],
    'custom_javascript_files': [
        # 'js/custom-functions.js', # Uncomment to add custom JS
        # 'js/analytics.js',        # Uncomment to add analytics
    ],
    
    # Advanced options
    'cdn_mode': False,              # Legacy CDN mode (deprecated)
    'use_cdn': False,               # New CDN mode - set to True to use CDN
    'minified': True,               # Use minified files
    'javascript_in_head': False,    # Load JS in head or body
    
    # Theme configuration
    'theme': 'light',               # 'light', 'dark', or 'auto'
    'theme_target': 'html',         # Target element for theme class
    'theme_switcher_enabled': False, # Enable built-in theme switcher
    
    # Form rendering options
    'wrapper_class': 'mb-3',
    'inline_wrapper_class': '',
    'horizontal_label_class': 'col-sm-2',
    'horizontal_field_class': 'col-sm-10',
    'horizontal_field_offset_class': 'offset-sm-2',
    'set_placeholder': True,
    'required_css_class': 'required',
    'error_css_class': 'error',
    'success_css_class': 'success',
    'server_side_validation': True,
}

# Example CDN configuration (uncomment to use)
# METROUI5.update({
#     # New CDN mode (recommended)
#     'use_cdn': True,
#     
#     # Custom CDN URLs (optional - if not set, defaults will be used)
#     'cdn_css_url': 'https://cdn.metroui.org.ua/current/metro.css',
#     'cdn_js_url': 'https://cdn.metroui.org.ua/current/metro.js',
#     'cdn_icons_url': 'https://cdn.metroui.org.ua/current/icons.css',
#     
#     # Legacy CDN mode (deprecated)
#     'cdn_mode': True,
#     'css_url': {
#         'url': 'https://cdn.jsdelivr.net/npm/metro-ui@5.1.17/css/metro.all.css',
#         'crossorigin': 'anonymous',
#     },
#     'javascript_url': {
#         'url': 'https://cdn.jsdelivr.net/npm/metro-ui@5.1.17/js/metro.all.js',
#         'crossorigin': 'anonymous',
#     },
#     'icons_css_url': {
#         'url': 'https://cdn.jsdelivr.net/npm/metro-ui@5.1.17/icons/icons.css',
#         'crossorigin': 'anonymous',
#     },
# })
