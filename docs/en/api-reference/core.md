# Core Functions

API reference for the main MetroUI5 Django module.

## Overview

The `core` module contains main functions for working with MetroUI5, including settings, URL generation and utilities.

## Functions

### `get_metroui5_setting(name, default=None)`

Gets MetroUI5 setting value from Django settings.

#### Parameters

- `name` (str) - setting name
- `default` - default value if setting not found

#### Returns

Setting value or `default`

#### Examples

```python
from metroui5.core import get_metroui5_setting

# Get CDN setting
cdn_mode = get_metroui5_setting('CDN_MODE', False)

# Get theme
theme = get_metroui5_setting('THEME', 'default')

# Get version
version = get_metroui5_setting('VERSION', '5.0.0')
```

### `javascript_url()`

Generates URL for MetroUI5 JavaScript file.

#### Returns

URL string for JavaScript file

#### Examples

```python
from metroui5.core import javascript_url

# Get JavaScript URL
js_url = javascript_url()
# Result: '/static/metroui5/js/metro.all.js' or CDN URL
```

### `css_url()`

Generates URL for MetroUI5 CSS file.

#### Returns

URL string for CSS file

#### Examples

```python
from metroui5.core import css_url

# Get CSS URL
css_url = css_url()
# Result: '/static/metroui5/css/metro.all.css' or CDN URL
```

### `icons_css_url()`

Generates URL for MetroUI5 icons CSS file.

#### Returns

URL string for icons CSS file

#### Examples

```python
from metroui5.core import icons_css_url

# Get icons URL
icons_url = icons_css_url()
# Result: '/static/metroui5/icons/icons.css' or CDN URL
```

### `custom_css_files()`

Gets list of custom CSS files from settings.

#### Returns

List of URLs for custom CSS files

#### Examples

```python
from metroui5.core import custom_css_files

# Get custom CSS files
custom_css = custom_css_files()
# Result: ['/static/css/custom.css', '/static/css/theme.css']
```

### `custom_javascript_files()`

Gets list of custom JavaScript files from settings.

#### Returns

List of URLs for custom JavaScript files

#### Examples

```python
from metroui5.core import custom_javascript_files

# Get custom JavaScript files
custom_js = custom_javascript_files()
# Result: ['/static/js/custom.js', '/static/js/plugins.js']
```

### `is_cdn_mode()`

Checks if CDN mode is enabled (legacy method).

#### Returns

`True` if CDN mode is enabled, otherwise `False`

#### Examples

```python
from metroui5.core import is_cdn_mode

# Check CDN mode
if is_cdn_mode():
	print("Using CDN")
else:
	print("Using local files")
```

### `is_use_cdn()`

Checks if new CDN mode is enabled.

#### Returns

`True` if CDN mode is enabled, otherwise `False`

#### Examples

```python
from metroui5.core import is_use_cdn

# Check CDN mode
if is_use_cdn():
	print("Using CDN")
else:
	print("Using local files")
```

## Internal Functions

### `_validate_url_config(config, config_type)`

Validates URL configuration for MetroUI5.

#### Parameters

- `config` - configuration to check
- `config_type` (str) - configuration type

#### Returns

Valid configuration or raises exception

#### Examples

```python
from metroui5.core import _validate_url_config

# Configuration validation (internal use)
try:
	valid_config = _validate_url_config(my_config, 'css')
except ValueError as e:
	print(f"Configuration error: {e}")
```

### `_get_file_url(config, config_type)`

Generates file URL based on configuration.

#### Parameters

- `config` - file configuration
- `config_type` (str) - file type

#### Returns

URL string for file

#### Examples

```python
from metroui5.core import _get_file_url

# File URL generation (internal use)
file_url = _get_file_url(file_config, 'js')
```

## Settings

### Basic Settings

```python
# settings.py

METROUI5 = {
	'CDN_MODE': False,  # Use local files
}
```

### CDN Settings

```python
METROUI5 = {
	'CDN_MODE': True,
	'CDN_URL': 'https://cdn.metroui.org.ua/current',
}
```

### Custom Files

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

### Advanced Settings

```python
METROUI5 = {
	'CDN_MODE': False,
	'THEME': 'dark',
	'VERSION': '5.1.17',
	'STATIC_URL': '/static/metroui5/',
	'FILE_EXTENSIONS': {
		'css': '.css',
		'js': '.js',
	},
	'CACHE_BUSTING': True,
}
```

## Error Handling

### Configuration Errors

```python
from metroui5.core import get_metroui5_setting

try:
	cdn_url = get_metroui5_setting('CDN_URL')
	if not cdn_url:
		raise ValueError("CDN_URL not configured")
except Exception as e:
	# Error handling
	print(f"MetroUI5 configuration error: {e}")
	# Use default values
	cdn_url = 'https://default-cdn.com/metro5'
```

### File Availability Check

```python
import os
from metroui5.core import css_url, javascript_url


def check_files_exist():
	"""Checks if MetroUI5 files exist"""
	css_path = css_url().replace('/static/', 'static/')
	js_path = javascript_url().replace('/static/', 'static/')

	if not os.path.exists(css_path):
		print(f"CSS file not found: {css_path}")

	if not os.path.exists(js_path):
		print(f"JavaScript file not found: {js_path}")
```

## Best Practices

### 1. Use Default Values

```python
# Good
theme = get_metroui5_setting('THEME', 'default')

# Bad
theme = get_metroui5_setting('THEME')  # May return None
```

### 2. Check CDN Mode

```python
if is_cdn_mode():
	# Use CDN URLs
	base_url = get_metroui5_setting('CDN_URL')
else:
	# Use local files
	base_url = '/static/metroui5/'
```

### 3. Cache URLs

```python
from functools import lru_cache


@lru_cache(maxsize=1)
def get_cached_css_url():
	return css_url()


@lru_cache(maxsize=1)
def get_cached_js_url():
	return javascript_url()
```

### 4. Handle Errors

```python
def safe_get_setting(name, default=None):
	"""Safely gets setting with error handling"""
	try:
		return get_metroui5_setting(name, default)
	except Exception as e:
		logger.error(f"Error getting setting {name}: {e}")
		return default
```

## Testing

### Unit Tests

```python
from django.test import TestCase
from unittest.mock import patch
from metroui5.core import get_metroui5_setting, is_cdn_mode


class CoreTestCase(TestCase):

	def test_get_setting_default(self):
		"""Test getting setting with default value"""
		value = get_metroui5_setting('NONEXISTENT', 'default')
		self.assertEqual(value, 'default')

	@patch('metroui5.core.get_metroui5_setting')
	def test_cdn_mode(self, mock_get_setting):
		"""Test CDN mode check"""
		mock_get_setting.return_value = True
		self.assertTrue(is_cdn_mode())
```

## Related Modules

- [HTML Utilities](html.md) - for generating HTML tags
- [CSS Utilities](css.md) - for working with CSS classes
- [Components](components.md) - for rendering UI components

## Next Steps

Now that you've mastered the core functions:

1. Study [HTML utilities](html.md) for HTML generation
2. Check out [CSS utilities](css.md) for working with styles
3. Study [components](components.md) for creating UI
4. Create your own utilities based on the core module!
