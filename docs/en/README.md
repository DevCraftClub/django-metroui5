# MetroUI5 Django Documentation

Welcome to the MetroUI5 Django documentation - a package for integrating MetroUI 5 with Django.

## Contents

### 🚀 [Getting Started](getting-started/)

- [Quick Start](getting-started/quick-start.md)
- [Installation](getting-started/installation.md)
- [Basic Usage](getting-started/basic-usage.md)
- [Examples](getting-started/examples.md)

### 🧩 [Components](components/)

- [Alerts](components/alerts.md)
- [Buttons](components/buttons.md)
- [Cards](components/cards.md)
- [Tiles](components/tiles.md)
- [Forms](components/forms.md)
- [Tables](components/tables.md)
- [Navigation](components/navigation.md)
- [Modals](components/modals.md)
- [Panels](components/panels.md)
- [Progress Bars](components/progress.md)
- [Accordions](components/accordions.md)
- [Calendars](components/calendars.md)
- [Dialogs](components/dialogs.md)
- [Dropdowns](components/dropdowns.md)
- [Input Fields](components/inputs.md)
- [Lists](components/lists.md)
- [Menus](components/menus.md)
- [Sidebars](components/sidebars.md)
- [Tabs](components/tabs.md)
- [Toolbars](components/toolbars.md)
- [Breadcrumbs](components/breadcrumbs.md)
- [Pagination](components/pagination.md)
- [Badges](components/badges.md)
- [Avatars](components/avatars.md)
- [Ratings](components/ratings.md)

### 📚 [API Reference](api-reference/)

- [Core Functions](api-reference/core.md)
- [HTML Utilities](api-reference/html.md)
- [CSS Utilities](api-reference/css.md)
- [Renderers](api-reference/renderers.md)
- [Forms](api-reference/forms.md)
- [Components](api-reference/components.md)
- [Template Tags](api-reference/templatetags.md)

## About MetroUI5

MetroUI5 Django is a package that provides convenient functions for creating modern web interfaces using MetroUI 5.1.17 in Django projects. The package includes:

- Ready-made components for quick UI creation
- Utilities for working with HTML, CSS and JavaScript
- Form rendering system
- Django template tags
- CDN and local file support

### CDN Support

The package supports the official MetroUI5 CDN with the ability to override URLs:

- **JavaScript**: `https://cdn.metroui.org.ua/current/metro.js`
- **CSS**: `https://cdn.metroui.org.ua/current/metro.css`
- **Icons**: `https://cdn.metroui.org.ua/current/icons.css`

Users can:

- Enable CDN mode via `USE_CDN: True`
- Override CDN URLs via `cdn_js_url`, `cdn_css_url`, `cdn_icons_url`
- Use default CDN URLs if override is not specified

## Requirements

- Python 3.8+
- Django 3.2+
- MetroUI 5.1.17+

## License

This project is distributed under the MIT license. See the [LICENSE](../LICENSE) file for more information.
