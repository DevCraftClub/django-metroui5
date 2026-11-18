"""
MetroUI Drag Items Component

The Drag Items component allows you to create draggable and reorderable items within a container. 
It provides a flexible way to implement drag-and-drop functionality for lists and other UI elements.
"""

from ..html import render_tag


def render_drag_items(items=None, **attrs):
    """
    Renders MetroUI drag items component with comprehensive features.

    Args:
        items: List of items to render (list of strings or dicts with 'content' and optional 'class')
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - drag_items_deferred: Delay in milliseconds before initialization (number, default: 0)
            - target: Target element for dropping items (string/object, default: null)
            - drag_item: Selector for draggable items (string, default: "li")
            - drag_marker: Selector for drag marker (string, default: ".drag-item-marker")
            - draw_drag_marker: Whether to draw drag markers (boolean, default: false)
            - can_drag: Whether dragging is enabled (boolean, default: true)
            
            # Event Handlers
            - on_drag_start_item: Triggered when dragging starts (string)
            - on_drag_move_item: Triggered when dragging moves (string)
            - on_drag_drop_item: Triggered when item is dropped (string)
            - on_target: Triggered when over a target (string)
            - on_target_in: Triggered when entering a target (string)
            - on_target_out: Triggered when leaving a target (string)
            - on_drag_items_create: Triggered when component is created (string)
            
            # CSS Classes
            - cls_drag_item_avatar: Additional CSS class for drag avatar (string)
            - cls_drag_item: Additional CSS class for drag item (string)
	Example:
		render_drag_items()

	Empty or invalid:
		`render_drag_items()` returns `<ul data-role="drag-items"></ul>`.

    """
    # Build data attributes only - MetroUI will handle CSS classes and rendering
    data_attrs = {
        "data-role": "drag-items"
    }
    
    # Map Python parameters to data attributes
    param_mapping = {
        'drag_items_deferred': 'data-drag-items-deferred',
        'target': 'data-target',
        'drag_item': 'data-drag-item',
        'drag_marker': 'data-drag-marker',
        'draw_drag_marker': 'data-draw-drag-marker',
        'can_drag': 'data-can-drag',
        'on_drag_start_item': 'data-on-drag-start-item',
        'on_drag_move_item': 'data-on-drag-move-item',
        'on_drag_drop_item': 'data-on-drag-drop-item',
        'on_target': 'data-on-target',
        'on_target_in': 'data-on-target-in',
        'on_target_out': 'data-on-target-out',
        'on_drag_items_create': 'data-on-drag-items-create',
        'cls_drag_item_avatar': 'data-cls-drag-item-avatar',
        'cls_drag_item': 'data-cls-drag-item'
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
    component_params = list(param_mapping.keys()) + ['items']

    for key, value in attrs.items():
        if key not in component_params:
            final_attrs[key] = value

    # Build the content with draggable items
    content = ""
    
    if items:
        for item in items:
            if isinstance(item, str):
                # Simple string item
                content += render_tag('li', {}, item)
            elif isinstance(item, dict):
                # Dictionary item with content and optional attributes
                item_attrs = {}
                if item.get('class'):
                    item_attrs['class'] = item['class']
                if item.get('id'):
                    item_attrs['id'] = item['id']
                
                # Add any other attributes from the item dict
                for key, value in item.items():
                    if key not in ['content', 'class', 'id']:
                        item_attrs[key] = value
                
                item_content = item.get('content', '')
                content += render_tag('li', item_attrs, item_content)
    
    # Determine the container tag based on drag_item parameter
    container_tag = "ul"
    if attrs.get('drag_item') == 'div' or attrs.get('drag_item') == '.item':
        container_tag = "div"
    
    # Render the drag items component - MetroUI will add classes and create the drag functionality
    return render_tag(container_tag, final_attrs, content)
