# MetroUI5 Django Documentation

Welcome to the MetroUI5 Django documentation! This package provides convenient functions for creating modern web interfaces using MetroUI 5.1.17 in Django projects.

## Documentation Structure

This documentation is available in two languages:

### 🇷🇺 [Russian Documentation](ru/index.md)

Complete documentation in Russian language, including:

- [Getting Started](ru/getting-started/) - installation and basic usage
- [Components](ru/components/) - UI components and their usage
- [API Reference](ru/api-reference/) - detailed API documentation

### 🇺🇸 [English Documentation](en/index.md)

Complete documentation in English language, including:

- [Getting Started](en/getting-started/) - installation and basic usage
- [Components](en/components/) - UI components and their usage
- [API Reference](en/api-reference/) - detailed API documentation

## Quick Navigation

### 🚀 Getting Started

- **Installation** - [RU](ru/getting-started/installation.md) | [EN](en/getting-started/installation.md)
- **Quick Start** - [RU](ru/getting-started/quick-start.md) | [EN](en/getting-started/quick-start.md)
- **Basic Usage** - [RU](ru/getting-started/basic-usage.md) | [EN](en/getting-started/basic-usage.md)
- **Examples** - [RU](ru/getting-started/examples.md) | [EN](en/getting-started/examples.md)

### 🧩 Components

- **Overview** - [RU](ru/components/README.md) | [EN](en/components/README.md)
- **Alerts** - [RU](ru/components/alerts.md) | [EN](en/components/alerts.md)
- **Buttons** - [RU](ru/components/buttons.md) | [EN](en/components/buttons.md)
- **Cards** - [RU](ru/components/cards.md) | [EN](en/components/cards.md)
- **Forms** - [RU](ru/components/forms.md) | [EN](en/components/forms.md)
- **Tiles** - [RU](ru/components/tiles.md) | [EN](en/components/tiles.md)
- **Themes** - [RU](ru/components/themes.md) | [EN](en/components/themes.md)

### 📚 API Reference

- **Core Functions** - [RU](ru/api-reference/core.md) | [EN](en/api-reference/core.md)
- **HTML Utilities** - [RU](ru/api-reference/html.md) | [EN](en/api-reference/html.md)
- **Template Tags** - [RU](ru/api-reference/templatetags.md) | [EN](en/api-reference/templatetags.md)

## About MetroUI5 Django

MetroUI5 Django is a package that provides:

- **Ready-made components** for quick UI creation
- **Utilities** for working with HTML, CSS and JavaScript
- **Form rendering system** with MetroUI5 styles
- **Django template tags** for easy integration
- **CDN and local file support** for flexibility

### Key Features

- 🎨 **Modern UI Components** - Buttons, cards, alerts, forms, and more
- 🔧 **Easy Integration** - Simple template tags and Python functions
- 📱 **Responsive Design** - Built on MetroUI 5 framework
- 🌐 **CDN Support** - Use official CDN or local files
- 🎭 **Theme Support** - Light and dark themes with auto-switching
- 🚀 **Performance** - Optimized for Django applications

## Requirements

- **Python**: 3.10 or higher
- **Django**: 5.2 or higher
- **MetroUI**: 5.1.17 or higher

## Quick Start

1. **Install the package:**

   ```bash
   pip install django-metroui5
   ```

2. **Add to INSTALLED_APPS:**

   ```python
   INSTALLED_APPS = [
       # ... other apps
       'metroui5',
   ]
   ```

3. **Use in templates:**

   ```html
   {% load metroui5 %}
   <head>
   	{% metroui5_css %} {% metroui5_icons %}
   </head>
   <body>
   	<!-- Your content -->
   	{% metroui5_javascript %}
   </body>
   ```

4. **Create components in views:**

   ```python
   from metroui5.components import render_button, render_alert

   def my_view(request):
       context = {
           'button': render_button("Click me!", button_type="primary"),
           'alert': render_alert("Welcome!", alert_type="success")
       }
       return render(request, 'my_template.html', context)
   ```

## Documentation Language Selection

Choose your preferred language:

- **🇷🇺 [Russian](ru/index.md)** - Полная документация на русском языке
- **🇺🇸 [English](en/index.md)** - Complete documentation in English

Both language versions contain identical information and examples, so you can choose based on your preference.

## Contributing

If you find any issues or want to contribute to the documentation:

1. Check the existing documentation in both languages
2. Ensure consistency between Russian and English versions
3. Follow the established structure and formatting
4. Update both language versions when making changes

## Support

- **GitHub Issues**: Report bugs or request features
- **Documentation**: Check both language versions for answers
- **Examples**: See practical usage examples in the getting-started section

---

**Note**: This documentation is maintained in both Russian and English to serve our diverse community. Both versions are kept synchronized and contain the same information.
