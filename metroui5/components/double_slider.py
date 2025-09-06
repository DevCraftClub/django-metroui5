"""
MetroUI Double Slider Component

The Double Slider component provides a range slider with two markers that allow users to select 
a range of values between a minimum and maximum. It's ideal for filtering data based on ranges 
like prices, dates, or any numeric values.
"""

from ..html import render_tag


def render_double_slider(**attrs):
    """
    Renders MetroUI double slider component with comprehensive features.

    Args:
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - min: Minimum value of the slider (number, default: 0)
            - max: Maximum value of the slider (number, default: 100)
            - accuracy: Decimal precision for values (0 = integers only) (number, default: 0)
            - round_value: Whether to round values according to accuracy (boolean, default: true)
            - value_min: Initial minimum value (defaults to min if not specified) (number, default: null)
            - value_max: Initial maximum value (defaults to max if not specified) (number, default: null)
            
            # Hint Parameters
            - hint: Show hints when dragging markers (boolean, default: false)
            - hint_always: Always show hints, not just when dragging (boolean, default: false)
            - hint_position_min: Position of the minimum value hint ("top" or "bottom") (string, default: "top")
            - hint_position_max: Position of the maximum value hint ("top" or "bottom") (string, default: "top")
            - hint_mask_min: Format for minimum value hint ($1 is replaced with the value) (string, default: "$1")
            - hint_mask_max: Format for maximum value hint ($1 is replaced with the value) (string, default: "$1")
            
            # Display Parameters
            - show_min_max: Show min and max values below/above the slider (boolean, default: false)
            - min_max_position: Position of min/max labels ("top" or "bottom") (string, default: "bottom")
            - target: Target element to display selected values (selector or DOM element) (string, default: null)
            - size: Width of the slider in pixels (0 = auto/100%) (number, default: 0)
            
            # Event Handlers
            - on_start: Triggered when the user starts dragging a marker (string)
            - on_stop: Triggered when the user stops dragging a marker (string)
            - on_move: Triggered continuously while dragging a marker (string)
            - on_change: Triggered when the slider value changes (string)
            - on_change_value: Triggered when the slider value changes (alias for onChange) (string)
            - on_focus: Triggered when a marker receives focus (string)
            - on_blur: Triggered when a marker loses focus (string)
            - on_double_slider_create: Triggered when the double slider is created (string)
            
            # CSS Classes
            - cls_slider: Custom class for the slider container (string)
            - cls_backside: Custom class for the background track (string)
            - cls_complete: Custom class for the filled portion (string)
            - cls_marker: Custom class for both markers (string)
            - cls_marker_min: Custom class for the minimum marker (string)
            - cls_marker_max: Custom class for the maximum marker (string)
            - cls_hint: Custom class for both hints (string)
            - cls_hint_min: Custom class for the minimum hint (string)
            - cls_hint_max: Custom class for the maximum hint (string)
            - cls_min_max: Custom class for the min/max labels container (string)
            - cls_min: Custom class for the minimum label (string)
            - cls_max: Custom class for the maximum label (string)
    """
    # Build data attributes only - MetroUI will handle CSS classes and rendering
    data_attrs = {
        "data-role": "double-slider"
    }
    
    # Map Python parameters to data attributes
    param_mapping = {
        'min': 'data-min',
        'max': 'data-max',
        'accuracy': 'data-accuracy',
        'round_value': 'data-round-value',
        'value_min': 'data-value-min',
        'value_max': 'data-value-max',
        'hint': 'data-hint',
        'hint_always': 'data-hint-always',
        'hint_position_min': 'data-hint-position-min',
        'hint_position_max': 'data-hint-position-max',
        'hint_mask_min': 'data-hint-mask-min',
        'hint_mask_max': 'data-hint-mask-max',
        'show_min_max': 'data-show-min-max',
        'min_max_position': 'data-min-max-position',
        'target': 'data-target',
        'size': 'data-size',
        'on_start': 'data-on-start',
        'on_stop': 'data-on-stop',
        'on_move': 'data-on-move',
        'on_change': 'data-on-change',
        'on_change_value': 'data-on-change-value',
        'on_focus': 'data-on-focus',
        'on_blur': 'data-on-blur',
        'on_double_slider_create': 'data-on-double-slider-create',
        'cls_slider': 'data-cls-slider',
        'cls_backside': 'data-cls-backside',
        'cls_complete': 'data-cls-complete',
        'cls_marker': 'data-cls-marker',
        'cls_marker_min': 'data-cls-marker-min',
        'cls_marker_max': 'data-cls-marker-max',
        'cls_hint': 'data-cls-hint',
        'cls_hint_min': 'data-cls-hint-min',
        'cls_hint_max': 'data-cls-hint-max',
        'cls_min_max': 'data-cls-min-max',
        'cls_min': 'data-cls-min',
        'cls_max': 'data-cls-max'
    }

    for py_param, data_attr in param_mapping.items():
        if py_param in attrs:
            value = attrs[py_param]
            if isinstance(value, bool):
                data_attrs[data_attr] = "true" if value else "false"
            elif isinstance(value, (int, float)):
                data_attrs[data_attr] = str(value)
            else:
                data_attrs[data_attr] = value

    # Build final attributes - no CSS classes, just data attributes
    final_attrs = data_attrs.copy()

    # Add any additional HTML attributes that are not component-specific
    component_params = list(param_mapping.keys())

    for key, value in attrs.items():
        if key not in component_params:
            final_attrs[key] = value

    # Render the double slider component - MetroUI will add classes and create the UI
    return render_tag("input", final_attrs, "")
