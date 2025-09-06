"""
MetroUI Drop Menu Component

The Drop Menu component provides a flexible and interactive dropdown menu system that can be 
attached to any element. It supports nested menus, positioning options, and customizable styling.
Unlike the dropdown component, in which the drop element is positioning absolutely, 
drop-menu has static position.
"""

from ..html import render_tag


def render_drop_menu(items=None, button_text="Menu", **attrs):
    """
    Renders MetroUI drop menu component with comprehensive features.

    Args:
        items: List of menu items (list of strings or dicts with 'text', 'href', 'class', 'submenu')
        button_text: Text for the toggle button (string, default: "Menu")
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - height: Maximum height of the menu. Can be "auto" or a specific pixel value (string/number, default: "auto")
            - align: Horizontal alignment of the menu. Can be "left" or "right" (string, default: "left")
            
            # Event Handlers
            - on_menu_create: Callback function that fires when the menu is created (string)
            
            # Special Classes (can be added via class attribute)
            - keep_open: Prevents the menu from closing when clicking elsewhere (boolean)
            - stay_open: Alternative to keep_open (boolean)
            - ignore_document_click: Another alternative to keep_open (boolean)
    """
    # Build data attributes only - MetroUI will handle CSS classes and rendering
    data_attrs = {
        "data-role": "dropmenu"
    }
    
    # Map Python parameters to data attributes
    param_mapping = {
        'height': 'data-height',
        'align': 'data-align',
        'on_menu_create': 'data-on-menu-create'
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

    # Handle special classes
    css_classes = []
    if attrs.get('keep_open'):
        css_classes.append('keep-open')
    if attrs.get('stay_open'):
        css_classes.append('stay-open')
    if attrs.get('ignore_document_click'):
        css_classes.append('ignore-document-click')
    
    # Add any additional CSS classes from the class attribute
    if attrs.get('class'):
        css_classes.append(attrs['class'])
    
    if css_classes:
        final_attrs['class'] = ' '.join(css_classes)

    # Add any additional HTML attributes that are not component-specific
    component_params = list(param_mapping.keys()) + ['items', 'button_text', 'keep_open', 'stay_open', 'ignore_document_click', 'button_class']

    for key, value in attrs.items():
        if key not in component_params:
            final_attrs[key] = value

    # Build the menu content
    content = ""
    
    if items:
        for item in items:
            if isinstance(item, str):
                # Simple string item
                content += render_tag('li', {}, render_tag('a', {'href': '#'}, item))
            elif isinstance(item, dict):
                # Dictionary item with options
                item_content = ""
                link_attrs = {'href': item.get('href', '#')}
                
                # Handle submenu
                if item.get('submenu'):
                    link_attrs['class'] = 'menu-toggle'
                    
                    # Build submenu recursively
                    submenu_content = ""
                    for subitem in item['submenu']:
                        if isinstance(subitem, str):
                            submenu_content += render_tag('li', {}, render_tag('a', {'href': '#'}, subitem))
                        elif isinstance(subitem, dict):
                            if subitem.get('submenu'):
                                # Handle nested submenu
                                sub_link_attrs = {'href': subitem.get('href', '#'), 'class': 'menu-toggle'}
                                sub_submenu_content = ""
                                for sub_subitem in subitem['submenu']:
                                    if isinstance(sub_subitem, str):
                                        sub_submenu_content += render_tag('li', {}, render_tag('a', {'href': '#'}, sub_subitem))
                                    elif isinstance(sub_subitem, dict):
                                        sub_sub_link_attrs = {'href': sub_subitem.get('href', '#')}
                                        sub_submenu_content += render_tag('li', {}, render_tag('a', sub_sub_link_attrs, sub_subitem.get('text', '')))
                                
                                sub_submenu_attrs = {'data-role-dropmenu': ''}
                                sub_item_content = render_tag('a', sub_link_attrs, subitem.get('text', ''))
                                sub_item_content += render_tag('ul', sub_submenu_attrs, sub_submenu_content)
                                submenu_content += render_tag('li', {}, sub_item_content)
                            else:
                                sub_link_attrs = {'href': subitem.get('href', '#')}
                                submenu_content += render_tag('li', {}, render_tag('a', sub_link_attrs, subitem.get('text', '')))
                    
                    submenu_attrs = {'data-role-dropmenu': ''}
                    item_content = render_tag('a', link_attrs, item.get('text', ''))
                    item_content += render_tag('ul', submenu_attrs, submenu_content)
                else:
                    item_content = render_tag('a', link_attrs, item.get('text', ''))
                
                # Build list item
                li_attrs = {}
                if item.get('class'):
                    li_attrs['class'] = item['class']
                
                content += render_tag('li', li_attrs, item_content)

    # Create the complete drop menu structure
    # Button + Menu as sibling elements (matching MetroUI5 format)
    button_attrs = {
        'class': 'button menu-toggle'
    }
    
    # Add button-specific attributes
    if attrs.get('button_class'):
        button_attrs['class'] += ' ' + attrs['button_class']
    
    button = render_tag('button', button_attrs, button_text)
    menu = render_tag('ul', final_attrs, content)
    
    # Return both button and menu without container wrapper to match raw HTML format
    return button + menu
