# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2025-09-02

### Added

- Custom initials avatar generation system with PIL (Pillow) integration
- Responsive avatar output with automatic size generation (small, medium, large, xlarge)
- Geologica font integration for professional avatar typography
- Automatic file saving to `/media/avatars/initials/{initial}/{size}.{format}`
- Support for multiple image formats (PNG, JPG, WebP)
- Responsive HTML output using `<figure>` and `<picture>` elements
- Comprehensive avatar documentation with usage examples
- Custom development integration guide for Django templatetags

### Changed

- Consolidated parameter naming across avatar functions for consistency
- Updated avatar documentation to reflect custom development nature
- Improved text centering in generated avatar images
- Enhanced font loading with fallback system

### Fixed

- Resolved parameter naming inconsistencies (`icon_size` → `size`, `background_color` → `bg_color`, `icon_color` → `text_color`)
- Updated documentation to clarify MetroUI core vs custom development functions

## [0.1.1] - 2025-09-01

### Added

- Comprehensive documentation system with bilingual support (English/Russian)
- Complete API reference documentation for all modules
- Component documentation with rendered output examples
- Django template usage guides and examples
- Getting started guides and tutorials
- Form rendering system documentation
- CSS utilities and HTML generation documentation
- Template tag reference with usage examples
- Enhanced form rendering capabilities
- Additional MetroUI5 component support
- Improved CSS class management utilities
- Extended template tag functionality

### Changed

- Updated template tag prefixes from `metroui_` to `metroui5_` for consistency
- Improved documentation structure and organization
- Enhanced code examples with practical usage patterns
- Updated Python version support to include 3.13
- Enhanced Django compatibility to 5.2+
- Improved component rendering performance

### Fixed

- Corrected API reference documentation to match actual codebase
- Fixed template tag rendering issues
- Resolved documentation inconsistencies between English and Russian versions
- CSS class merging functionality
- Form field validation display

## [0.1.0] - 2025-08-31

### Added

- Initial version of django-metroui5 package
- MetroUI v5 integration with Django 5.2.5+
- Template tags for all major MetroUI components
- Automatic form rendering with MetroUI styling
- Support for MetroUI components: tiles, cards, buttons, alerts, progress bars
- Renderer system for forms, fields, and formsets
- Configuration system with default settings
- Full Python 3.13+ support
- Demo application with usage examples

### Technical Details

- Created base package with proper structure
- Implemented all major template tags
- Added form rendering system
- Created utilities for CSS classes and HTML
- Added MetroUI component support
- Created testing system
- Added initial documentation and examples

---

## Version Notes

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backwards compatible manner
- **PATCH** version for backwards compatible bug fixes
