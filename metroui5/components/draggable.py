"""
MetroUI Draggable Component

The Draggable component allows you to make any element draggable within a specified area. 
It provides a simple way to implement drag-and-drop functionality with customizable options 
for boundaries, drag handles, and event callbacks.
"""

from ..html import render_tag


def render_draggable(content="", **attrs):
    """
    Renders MetroUI draggable component with comprehensive features.

    Args:
        content: Content inside the draggable element (string)
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - drag_context: Context object passed to event callbacks (object, default: null)
            - draggable_deferred: Delay in milliseconds before initialization (number, default: 0)
            - drag_element: Selector for the drag handle element. Use "self" to make the entire element draggable (string, default: "self")
            - drag_area: Selector for the container that limits the draggable area. Can be "parent", "body", or any valid CSS selector (string, default: "parent")
            - timeout: Timeout for initialization (number, default: 0)
            - boundary_restriction: When true, restricts dragging within the boundaries of the dragArea (boolean, default: true)
            
            # Event Handlers
            - on_can_drag: Callback function that determines if dragging is allowed. Should return true to allow dragging (string)
            - on_drag_start: Callback function triggered when dragging starts (string)
            - on_drag_stop: Callback function triggered when dragging stops (string)
            - on_drag_move: Callback function triggered during dragging movement (string)
            - on_draggable_create: Callback function triggered when the draggable component is created (string)
	Example:
		render_draggable()

	Empty or invalid:
		`render_draggable()` returns `<div data-role="draggable"></div>`.

    """
    # Build data attributes only - MetroUI will handle CSS classes and rendering
    data_attrs = {
        "data-role": "draggable"
    }
    
    # Map Python parameters to data attributes
    param_mapping = {
        'drag_context': 'data-drag-context',
        'draggable_deferred': 'data-draggable-deferred',
        'drag_element': 'data-drag-element',
        'drag_area': 'data-drag-area',
        'timeout': 'data-timeout',
        'boundary_restriction': 'data-boundary-restriction',
        'on_can_drag': 'data-on-can-drag',
        'on_drag_start': 'data-on-drag-start',
        'on_drag_stop': 'data-on-drag-stop',
        'on_drag_move': 'data-on-drag-move',
        'on_draggable_create': 'data-on-draggable-create'
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
    component_params = list(param_mapping.keys()) + ['content']

    for key, value in attrs.items():
        if key not in component_params:
            final_attrs[key] = value

    # Render the draggable component - MetroUI will add classes and create the drag functionality
    return render_tag("div", final_attrs, content)
