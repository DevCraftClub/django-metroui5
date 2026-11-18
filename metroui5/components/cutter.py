"""
MetroUI Cutter Component

This module provides the MetroUI Cutter component implementation.
The Cutter component is a visual separator that creates a zigzag pattern border with content in the center.
It's useful for creating visually distinct sections in your layout.

References:
    https://v5.metroui.org.ua/components/cutter/
"""

from .base import SimpleComponent


def render_cutter(content="", icon="", text="", **kwargs):
    """
    Renders MetroUI cutter component.
    
    The Cutter component is a visual separator that creates a zigzag pattern border
    with content in the center. It's useful for creating visually distinct sections
    in your layout.
    
    Args:
        content (str, optional): HTML content to display in the cutter. Defaults to "".
        icon (str, optional): Icon class to display in the cutter. Defaults to "".
        text (str, optional): Text content to display in the cutter. Defaults to "".
        **kwargs: Additional attributes for the cutter element.
    
    Returns:
        str: HTML string for the cutter component.
    
    References:
        https://v5.metroui.org.ua/components/cutter/
	Example:
		render_cutter()

	Empty or invalid:
		`render_cutter()` returns `<div class="cutter" id="cutter-component"><div class="content"></div></div>`.

    """
    component = CutterComponent()
    return component.render(content=content, icon=icon, text=text, **kwargs)


class CutterComponent(SimpleComponent):
    """
    MetroUI Cutter Component.
    
    A visual separator that creates a zigzag pattern border with content in the center.
    Useful for creating visually distinct sections in your layout.
    """
    
    def __init__(self):
        super().__init__(
            component_name="cutter",
            base_css_class="cutter",
            tag_name="div",
            component_params=['content', 'icon', 'text']
        )
    
    def render(self, content="", icon="", text="", **kwargs):
        """
        Renders the cutter component.
        
        Args:
            content (str): HTML content to display in the cutter
            icon (str): Icon class to display in the cutter
            text (str): Text content to display in the cutter
            **kwargs: Additional attributes
            
        Returns:
            str: HTML string for the cutter
        """
        # Separate attributes
        attrs, css_classes, data_attrs = self.separate_attributes(kwargs)
        
        # Build CSS classes - for cutter we just use any additional classes
        final_css_classes = [self.base_css_class]
        if css_classes:
            final_css_classes.extend(css_classes)
        if 'cls' in kwargs:
            final_css_classes.append(kwargs['cls'])
        css_classes_str = ' '.join(final_css_classes) if final_css_classes else self.base_css_class
        
        # Build data attributes
        data_attrs = self.build_data_attributes(attrs, {})
        
        # Build all attributes
        all_attrs = {**attrs, **data_attrs}
        if css_classes_str:
            all_attrs['class'] = css_classes_str
        
        # Generate unique ID
        cutter_id = self.build_id_attribute(attrs, {})
        all_attrs['id'] = cutter_id
        
        # Build content
        cutter_content = ""
        
        # If content is provided, use it directly
        if content:
            cutter_content = content
        else:
            # Build content from icon and text
            if icon:
                if isinstance(icon, str) and icon.startswith('<'):
                    # HTML content
                    cutter_content += icon
                else:
                    # Icon class
                    cutter_content += f'<span class="{icon}"></span>'
            
            if text:
                cutter_content += f' {text}'
        
        # Wrap content in content div
        if cutter_content:
            content_html = f'<div class="content">{cutter_content}</div>'
        else:
            content_html = '<div class="content"></div>'
        
        # Build the cutter HTML
        cutter_html = f'<{self.tag_name} {self._build_attributes_string(all_attrs)}>{content_html}</{self.tag_name}>'
        
        return cutter_html
    
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
            elif value is not False and value is not None:
                attr_pairs.append(f'{key}="{value}"')
        
        return ' '.join(attr_pairs)
