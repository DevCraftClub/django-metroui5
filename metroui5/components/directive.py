"""
MetroUI Directive Component

The Directive component creates styled directive boxes for displaying notes, warnings, tips, and other informational content in your application.
"""

from ..html import render_tag


def render_directive(content="", **attrs):
    """
    Renders MetroUI directive component with comprehensive features.

    Args:
        content: Directive content text (string)
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - directive: Type of directive. Options: "note", "info", "warning", "caution", "tip", "success", "important", "bug", "shit", "air", "fuck" (string, default: "note")
            - show_icon: Whether to show an icon (boolean, default: true)
            - title: Title of the directive. If set to "default", it will use the localized label for the directive type (string, default: "default")
            - style: Style of the directive. Options: 1, 2, 3 (number, default: 1)
            
            # Event Handlers
            - on_directive_create: Event fired when directive is created (string)
            
            # Styling Parameters
            - cls_directive: Additional CSS class for directive element (string)
            - cls_title: Additional CSS class for title element (string)
            - cls_content: Additional CSS class for content element (string)
    """
    # Build data attributes only - MetroUI will handle CSS classes
    data_attrs = {
        "data-role": "directive"
    }
    
    # Add directive-specific data attributes
    if attrs.get('directive'):
        data_attrs['data-directive'] = attrs['directive']
    
    if attrs.get('show_icon') is not None:
        data_attrs['data-show-icon'] = "true" if attrs['show_icon'] else "false"
    
    if attrs.get('title'):
        data_attrs['data-title'] = attrs['title']
    
    if attrs.get('style'):
        data_attrs['data-style'] = str(attrs['style'])
    
    if attrs.get('on_directive_create'):
        data_attrs['data-on-directive-create'] = attrs['on_directive_create']
    
    if attrs.get('cls_directive'):
        data_attrs['data-cls-directive'] = attrs['cls_directive']
    
    if attrs.get('cls_title'):
        data_attrs['data-cls-title'] = attrs['cls_title']
    
    if attrs.get('cls_content'):
        data_attrs['data-cls-content'] = attrs['cls_content']
    
    # Build final attributes - no CSS classes, just data attributes
    final_attrs = data_attrs.copy()
    
    # Add any additional HTML attributes that are not component-specific
    component_params = [
        'directive', 'show_icon', 'title', 'style', 'on_directive_create',
        'cls_directive', 'cls_title', 'cls_content'
    ]
    
    for key, value in attrs.items():
        if key not in component_params:
            final_attrs[key] = value
    
    # Render the directive component with content inside - MetroUI will add classes
    return render_tag("div", final_attrs, content)
