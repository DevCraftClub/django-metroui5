# Installation

Detailed guide for installing MetroUI5 Django in your project.

## Requirements

### System Requirements

- **Python**: 3.10 or higher (lower versions not tested)
- **Django**: 4.1 or higher (recommended 5.2.17+; CI tests from 4.1 through 6.1)
- **Operating System**: Windows, macOS, Linux

### Dependencies

- `django` >= 4.1 (recommended >= 5.2.17)
- `django-crispy-forms` (optional, for extended form functionality)

## Installation Methods

### 1. Installation via pip (recommended)

```bash
pip install django-metroui5
```

### 2. Installation from source code

```bash
git clone https://github.com/your-repo/django-metroui5.git
cd django-metroui5
pip install -e .
```

### 3. Installation of specific version

```bash
pip install django-metroui5==1.0.0
```

## Django Project Configuration

### 1. Adding to INSTALLED_APPS

Open `settings.py` and add `metroui5`:

```python
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# Your applications
	'myapp',

	# MetroUI5
	'metroui5',
]
```

### 2. Static Files Configuration

Make sure you have static files properly configured:

```python
# settings.py

# Base URL for static files
STATIC_URL = '/static/'

# Additional directories for static files
STATICFILES_DIRS = [
	BASE_DIR / "static",
]

# Directory for collectstatic
STATIC_ROOT = BASE_DIR / "staticfiles"

# Development settings
if DEBUG:
	STATICFILES_DIRS = [
		BASE_DIR / "static",
	]
```

### 3. Template Configuration

Add MetroUI5 template directory:

```python
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			BASE_DIR / "templates",
		],
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
```

### 4. URL Configuration

Add URL for static files in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# Your URL patterns
	path('admin/', admin.site.urls),
	path('', include('myapp.urls')),
]

# Add static files for development
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## MetroUI5 Configuration

### 1. Basic Settings

Add MetroUI5 settings to `settings.py`:

```python
# MetroUI5 settings
METROUI5 = {
	'CDN_MODE': False,  # Use local files
}
```

### 2. CDN Settings

If you want to use CDN:

```python
METROUI5 = {
	'CDN_MODE': True,
	'CDN_URL': 'https://cdn.metroui.org.ua/current',
	'THEME': 'default',
}
```

#### Available CDN Files

MetroUI5 is available through the official CDN at the following URLs:

- **JavaScript**: `https://cdn.metroui.org.ua/current/metro.js`
- **CSS**: `https://cdn.metroui.org.ua/current/metro.css`
- **Icons**: `https://cdn.metroui.org.ua/current/icons.css`

#### New CDN Mode (recommended)

```python
METROUI5 = {
	'use_cdn': True,  # Enable CDN mode

	# Optionally: override CDN URLs
	'cdn_js_url': 'https://your-cdn.com/metro.js',
	'cdn_css_url': 'https://your-cdn.com/metro.css',
	'cdn_icons_url': 'https://your-cdn.com/icons.css',
}
```

If `cdn_*_url` are not specified, default CDN URLs will be used.

#### Legacy CDN Mode

When using `cdn_mode: True`, the package will automatically substitute the correct URLs for each file type.

### 3. Custom CSS/JS Files

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

## Installation Verification

### 1. Collect Static Files

```bash
python manage.py collectstatic
```

### 2. Start Server

```bash
python manage.py runserver
```

### 3. Browser Verification

Open `http://127.0.0.1:8000/` and check:

- Page source code has links to MetroUI5 CSS/JS
- Browser console has no errors
- MetroUI5 styles are applied

## Updating

### Update to New Version

```bash
pip install --upgrade django-metroui5
```

### Update Static Files

```bash
python manage.py collectstatic --clear
```

## Removal

### Remove Package

```bash
pip uninstall django-metroui5
```

### Clean Settings

Remove `metroui5` from `INSTALLED_APPS` and `METROUI5` settings from `settings.py`.

## Troubleshooting

### Error "No module named 'metroui5'"

```bash
pip install django-metroui5
python manage.py check
```

### Static Files Not Loading

```bash
python manage.py collectstatic
python manage.py runserver --insecure
```

### Template Tags Not Working

1. Check `INSTALLED_APPS`
2. Restart server
3. Check template syntax

### Conflict with Other CSS Frameworks

MetroUI5 may conflict with Bootstrap, Foundation and other CSS frameworks. Use only one framework per page.

## Next Steps

After successful installation:

1. Study [basic usage](basic-usage.md)
2. Check out [examples](examples.md)
3. Study available [components](../components/)
4. Study [API reference](../api-reference/)
5. Insert the first piece: [accordion for page builders](../for-users/accordions.md) and [accordion for developers](../components/accordions.md)
