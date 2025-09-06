"""
MetroUI Donut Component

The Donut component is a circular progress indicator that displays a value as a filled arc. 
It can be used to show progress, percentages, or any other numerical value in a visually appealing way.
"""

from ..html import render_tag


def render_donut(**attrs):
    """
    Renders MetroUI donut component with comprehensive features.

    Args:
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - size: Size of the donut in pixels (number, default: 100)
            - hole: Size of the hole (0 to 1, where 0.8 means 80% of the radius) (number, default: 0.8)
            - value: Initial value (number, default: 0)
            - background: Background color of the element (string, default: "transparent")
            - color: Text color (defaults to fill color if empty) (string, default: "")
            - stroke: Color of the background circle (string, default: "#d1d8e7")
            - fill: Color of the value circle (string, default: "#49649f")
            - font_size: Font size (0 means auto-calculated) (number, default: 0)
            - total: Total value (for percentage calculation) (number, default: 100)
            - cap: Suffix for the displayed value (string, default: "%")
            - show_text: Whether to show text (boolean, default: true)
            - show_value: Whether to show the actual value instead of percentage (boolean, default: false)
            - animate: Animation duration in milliseconds (number, default: 0)
            
            # Event Handlers
            - on_donut_create: Triggered when the donut is created (string)
            - on_change: Triggered when the donut value changes (string)
            - on_draw_value: Callback for custom formatting of the displayed value (string)
            
            # CSS Classes
            - cls_donut: Additional CSS class for donut element (string)
    """
    # Build data attributes only - MetroUI will handle CSS classes and rendering
    data_attrs = {
        "data-role": "donut"
    }
    
    # Add donut-specific data attributes
    if attrs.get('size'):
        data_attrs['data-size'] = str(attrs['size'])
    
    if attrs.get('hole') is not None:
        data_attrs['data-hole'] = str(attrs['hole'])
    
    if attrs.get('value') is not None:
        data_attrs['data-value'] = str(attrs['value'])
    
    if attrs.get('background'):
        data_attrs['data-background'] = attrs['background']
    
    if attrs.get('color'):
        data_attrs['data-color'] = attrs['color']
    
    if attrs.get('stroke'):
        data_attrs['data-stroke'] = attrs['stroke']
    
    if attrs.get('fill'):
        data_attrs['data-fill'] = attrs['fill']
    
    if attrs.get('font_size'):
        data_attrs['data-font-size'] = str(attrs['font_size'])
    
    if attrs.get('total'):
        data_attrs['data-total'] = str(attrs['total'])
    
    if attrs.get('cap'):
        data_attrs['data-cap'] = attrs['cap']
    
    if attrs.get('show_text') is not None:
        data_attrs['data-show-text'] = "true" if attrs['show_text'] else "false"
    
    if attrs.get('show_value') is not None:
        data_attrs['data-show-value'] = "true" if attrs['show_value'] else "false"
    
    if attrs.get('animate'):
        data_attrs['data-animate'] = str(attrs['animate'])
    
    # Event handlers
    if attrs.get('on_donut_create'):
        data_attrs['data-on-donut-create'] = attrs['on_donut_create']
    
    if attrs.get('on_change'):
        data_attrs['data-on-change'] = attrs['on_change']
    
    if attrs.get('on_draw_value'):
        data_attrs['data-on-draw-value'] = attrs['on_draw_value']
    
    # Build final attributes - no CSS classes, just data attributes
    final_attrs = data_attrs.copy()
    
    # Add custom CSS class if provided
    css_classes = []
    if attrs.get('cls_donut'):
        css_classes.append(attrs['cls_donut'])
    
    # Add predefined color classes if provided
    color_classes = [
        'donut-lime', 'donut-green', 'donut-emerald', 'donut-blue', 'donut-teal', 'donut-cyan',
        'donut-cobalt', 'donut-indigo', 'donut-violet', 'donut-pink', 'donut-magenta',
        'donut-crimson', 'donut-red', 'donut-orange', 'donut-amber', 'donut-yellow',
        'donut-brown', 'donut-olive', 'donut-steel', 'donut-mauve', 'donut-taupe',
        'donut-khaki', 'donut-charcoal', 'donut-bronze', 'donut-windstorm',
        'donut-nude', 'donut-terracotta', 'donut-coral', 'donut-army', 'donut-seashell', 'donut-sand',
        'donut-primary', 'donut-secondary', 'donut-success', 'donut-alert', 'donut-warning',
        'donut-info', 'donut-dark', 'donut-light'
    ]
    
    for class_name in color_classes:
        if attrs.get('class') and class_name in attrs['class']:
            css_classes.append(class_name)
    
    if css_classes:
        final_attrs['class'] = ' '.join(css_classes)
    
    # Add any additional HTML attributes that are not component-specific
    component_params = [
        'size', 'hole', 'value', 'background', 'color', 'stroke', 'fill', 'font_size',
        'total', 'cap', 'show_text', 'show_value', 'animate', 'on_donut_create',
        'on_change', 'on_draw_value', 'cls_donut'
    ]
    
    for key, value in attrs.items():
        if key not in component_params and key != 'class':
            final_attrs[key] = value
    
    # Render the donut component - MetroUI will add classes and create the SVG
    return render_tag("div", final_attrs, "")
