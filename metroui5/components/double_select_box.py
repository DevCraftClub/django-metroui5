"""
MetroUI Double Select Box Component

The Double Select Box component provides a user interface for moving items between two select boxes. 
It's useful for scenarios where users need to select items from a list and move them to another list, 
such as assigning permissions, selecting features, or organizing items into categories.
"""

from ..html import render_tag


def render_double_select_box(left_options=None, right_options=None, **attrs):
    """
    Renders MetroUI double select box component with comprehensive features.

    Args:
        left_options: List of options for the left select box (list of dicts with 'value', 'text', optional 'template')
        right_options: List of options for the right select box (list of dicts with 'value', 'text', optional 'template')
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - height: Height of the select boxes (string, default: "auto")
            - multi_select: Allows selecting multiple items at once (boolean, default: false)
            - move_right_icon: Icon for the move right button (string, default: "›")
            - move_right_all_icon: Icon for the move all right button (string, default: "»")
            - move_left_icon: Icon for the move left button (string, default: "‹")
            - move_left_all_icon: Icon for the move all left button (string, default: "«")
            
            # Event Handlers
            - on_double_select_box_create: Triggered when the component is created (string)
            
            # CSS Classes
            - cls_box: Additional CSS class for the component container (string)
            - cls_move_button: Additional CSS class for all move buttons (string)
            - cls_move_right_button: Additional CSS class for the move right button (string)
            - cls_move_right_all_button: Additional CSS class for the move all right button (string)
            - cls_move_left_button: Additional CSS class for the move left button (string)
            - cls_move_left_all_button: Additional CSS class for the move all left button (string)
            - cls_list_left: Additional CSS class for the left list (string)
            - cls_list_right: Additional CSS class for the right list (string)
    """
    # Build data attributes only - MetroUI will handle CSS classes and rendering
    data_attrs = {
        "data-role": "double-select-box"
    }
    
    # Add double select box specific data attributes
    if attrs.get('height'):
        data_attrs['data-height'] = attrs['height']
    
    if attrs.get('multi_select') is not None:
        data_attrs['data-multi-select'] = "true" if attrs['multi_select'] else "false"
    
    if attrs.get('move_right_icon'):
        data_attrs['data-move-right-icon'] = attrs['move_right_icon']
    
    if attrs.get('move_right_all_icon'):
        data_attrs['data-move-right-all-icon'] = attrs['move_right_all_icon']
    
    if attrs.get('move_left_icon'):
        data_attrs['data-move-left-icon'] = attrs['move_left_icon']
    
    if attrs.get('move_left_all_icon'):
        data_attrs['data-move-left-all-icon'] = attrs['move_left_all_icon']
    
    # CSS class data attributes
    if attrs.get('cls_box'):
        data_attrs['data-cls-box'] = attrs['cls_box']
    
    if attrs.get('cls_move_button'):
        data_attrs['data-cls-move-button'] = attrs['cls_move_button']
    
    if attrs.get('cls_move_right_button'):
        data_attrs['data-cls-move-right-button'] = attrs['cls_move_right_button']
    
    if attrs.get('cls_move_right_all_button'):
        data_attrs['data-cls-move-right-all-button'] = attrs['cls_move_right_all_button']
    
    if attrs.get('cls_move_left_button'):
        data_attrs['data-cls-move-left-button'] = attrs['cls_move_left_button']
    
    if attrs.get('cls_move_left_all_button'):
        data_attrs['data-cls-move-left-all-button'] = attrs['cls_move_left_all_button']
    
    if attrs.get('cls_list_left'):
        data_attrs['data-cls-list-left'] = attrs['cls_list_left']
    
    if attrs.get('cls_list_right'):
        data_attrs['data-cls-list-right'] = attrs['cls_list_right']
    
    # Event handlers
    if attrs.get('on_double_select_box_create'):
        data_attrs['data-on-double-select-box-create'] = attrs['on_double_select_box_create']
    
    # Build final attributes - no CSS classes, just data attributes
    final_attrs = data_attrs.copy()
    
    # Add any additional HTML attributes that are not component-specific
    component_params = [
        'height', 'multi_select', 'move_right_icon', 'move_right_all_icon',
        'move_left_icon', 'move_left_all_icon', 'on_double_select_box_create',
        'cls_box', 'cls_move_button', 'cls_move_right_button', 'cls_move_right_all_button',
        'cls_move_left_button', 'cls_move_left_all_button', 'cls_list_left', 'cls_list_right'
    ]
    
    for key, value in attrs.items():
        if key not in component_params:
            final_attrs[key] = value
    
    # Build the content with two select elements
    content = ""
    
    # Left select box
    left_select_content = ""
    if left_options:
        for option in left_options:
            option_attrs = {
                'value': option.get('value', '')
            }
            if option.get('template'):
                option_attrs['data-template'] = option['template']
            
            left_select_content += render_tag('option', option_attrs, option.get('text', ''))
    
    content += render_tag('select', {}, left_select_content)
    
    # Right select box
    right_select_content = ""
    if right_options:
        for option in right_options:
            option_attrs = {
                'value': option.get('value', '')
            }
            if option.get('template'):
                option_attrs['data-template'] = option['template']
            
            right_select_content += render_tag('option', option_attrs, option.get('text', ''))
    
    content += render_tag('select', {}, right_select_content)
    
    # Render the double select box component - MetroUI will add classes and create the UI
    return render_tag("div", final_attrs, content)
