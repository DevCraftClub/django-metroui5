"""
MetroUI Custom Checkbox Component

This module provides the MetroUI Custom Checkbox component implementation.
The Custom Checkbox component provides a highly customizable checkbox that allows you to define
custom icons and captions for checked and unchecked states. It's designed to be flexible and easy to style.

References:
    https://v5.metroui.org.ua/components/custom-checkbox/
"""

from .base import SimpleComponent


def render_custom_checkbox(state_on="✓", state_off="✗", caption_on="", caption_off="", 
                          caption_position="right", name="", value="", checked=False, disabled=False, **kwargs):
    """
    Renders MetroUI custom checkbox component.
    
    The Custom Checkbox component provides a highly customizable checkbox that allows you to define
    custom icons and captions for checked and unchecked states. It's designed to be flexible and easy to style.
    
    Args:
        state_on (str, optional): Symbol or HTML for the checked state. Defaults to "✓".
        state_off (str, optional): Symbol or HTML for the unchecked state. Defaults to "✗".
        caption_on (str, optional): Text displayed when checkbox is checked. Defaults to "".
        caption_off (str, optional): Text displayed when checkbox is unchecked. Defaults to "".
        caption_position (str, optional): Position of the caption ("right" or "left"). Defaults to "right".
        name (str, optional): Name attribute for the checkbox. Defaults to "".
        value (str, optional): Value attribute for the checkbox. Defaults to "".
        checked (bool, optional): Whether the checkbox is initially checked. Defaults to False.
        disabled (bool, optional): Whether the checkbox is disabled. Defaults to False.
        **kwargs: Additional attributes for the checkbox element.
    
    Returns:
        str: HTML string for the custom checkbox component.
    
    References:
        https://v5.metroui.org.ua/components/custom-checkbox/
    """
    component = CustomCheckboxComponent()
    return component.render(
        state_on=state_on,
        state_off=state_off,
        caption_on=caption_on,
        caption_off=caption_off,
        caption_position=caption_position,
        name=name,
        value=value,
        checked=checked,
        disabled=disabled,
        **kwargs
    )


class CustomCheckboxComponent(SimpleComponent):
    """
    MetroUI Custom Checkbox Component.
    
    Provides a highly customizable checkbox that allows you to define custom icons
    and captions for checked and unchecked states. It's designed to be flexible and easy to style.
    """
    
    def __init__(self):
        super().__init__(
            component_name="custom_checkbox",
            base_css_class="",
            tag_name="input",
            component_params=[
                'state_on', 'state_off', 'caption_on', 'caption_off', 'caption_position',
                'name', 'value', 'checked', 'disabled'
            ],
            data_attr_mapping={
                'state_on': 'data-state-on',
                'state_off': 'data-state-off',
                'caption_on': 'data-caption-on',
                'caption_off': 'data-caption-off',
                'caption_position': 'data-caption-position',
                'name': 'name',
                'value': 'value',
                'checked': 'checked',
                'disabled': 'disabled'
            },
            default_data_attrs={
                'state_on': '✓',
                'state_off': '✗',
                'caption_on': '',
                'caption_off': '',
                'caption_position': 'right',
                'name': '',
                'value': '',
                'checked': False,
                'disabled': False
            }
        )
    
    def render(self, state_on="✓", state_off="✗", caption_on="", caption_off="", 
               caption_position="right", name="", value="", checked=False, disabled=False, **kwargs):
        """
        Renders the custom checkbox component.
        
        Args:
            state_on (str): Symbol or HTML for the checked state
            state_off (str): Symbol or HTML for the unchecked state
            caption_on (str): Text displayed when checkbox is checked
            caption_off (str): Text displayed when checkbox is unchecked
            caption_position (str): Position of the caption ("right" or "left")
            name (str): Name attribute for the checkbox
            value (str): Value attribute for the checkbox
            checked (bool): Whether the checkbox is initially checked
            disabled (bool): Whether the checkbox is disabled
            **kwargs: Additional attributes
            
        Returns:
            str: HTML string for the custom checkbox
        """
        # Separate attributes
        attrs, css_classes, data_attrs = self.separate_attributes(kwargs)
        
        # Build CSS classes - for custom checkbox we just use any additional classes
        final_css_classes = []
        if css_classes:
            final_css_classes.extend(css_classes)
        if 'cls' in kwargs:
            final_css_classes.append(kwargs['cls'])
        css_classes_str = ' '.join(final_css_classes) if final_css_classes else ''
        
        # Build data attributes
        data_attrs = self.build_data_attributes(attrs, self.data_attr_mapping)
        
        # Set specific data attributes
        data_attrs['data-role'] = 'custom-checkbox'
        data_attrs['data-state-on'] = state_on
        data_attrs['data-state-off'] = state_off
        data_attrs['data-caption-position'] = caption_position
        
        # Handle caption attributes
        if caption_on:
            data_attrs['data-caption-on'] = caption_on
        if caption_off:
            data_attrs['data-caption-off'] = caption_off
        
        # Handle form attributes
        if name:
            data_attrs['name'] = name
        if value:
            data_attrs['value'] = value
        
        # Handle boolean attributes
        if checked:
            data_attrs['checked'] = 'checked'
        if disabled:
            data_attrs['disabled'] = 'disabled'
        
        # Set input type
        data_attrs['type'] = 'checkbox'
        
        # Build all attributes
        all_attrs = {**attrs, **data_attrs}
        if css_classes_str:
            all_attrs['class'] = css_classes_str
        
        # Generate unique ID
        checkbox_id = self.build_id_attribute(attrs, {})
        all_attrs['id'] = checkbox_id
        
        # Build the custom checkbox HTML
        checkbox_html = f'<{self.tag_name} {self._build_attributes_string(all_attrs)}>'
        
        return checkbox_html
    
    def _build_attributes_string(self, attrs):
        """
        Builds HTML attributes string from dictionary.
        
        Args:
            attrs (dict): Attributes dictionary
            
        Returns:
            str: HTML attributes string
        """
        if not attrs:
            return ""
        
        attr_pairs = []
        for key, value in attrs.items():
            if value is True:
                attr_pairs.append(key)
            elif value is False and key in ['checked', 'disabled']:
                # Skip false boolean attributes for form elements
                continue
            elif value is not False and value is not None:
                attr_pairs.append(f'{key}="{value}"')
        
        return ' '.join(attr_pairs)
