"""
MetroUI Drop Menu Component

The Drop Menu component provides a flexible and interactive dropdown menu system that can be 
attached to any element. It supports nested menus, positioning options, and customizable styling.
Unlike the dropdown component, in which the drop element is positioning absolutely, 
drop-menu has static position.
"""

from .base import ComplexComponent
import uuid


class DropMenuComponent(ComplexComponent):
    """
    MetroUI Drop Menu component.

    Provides a flexible and interactive dropdown menu system with nested menus,
    positioning options, and customizable styling.
    """

    def __init__(self):
        super().__init__(
            component_name="drop_menu",
            base_css_class=None,  # Drop menu doesn't have a base CSS class
            component_params=[
                # Basic parameters
                'items', 'button_text', 'height', 'align',
                # Special behavior parameters
                'keep_open', 'stay_open', 'ignore_document_click',
                # Button styling
                'button_class',
                # Event handlers
                'on_menu_create'
                # Note: cls_* parameters are handled automatically by base class
            ]
        )

    def render(self, items=None, button_text="Menu", **attrs):
        """
        Render the drop menu component.

        Args:
            items: List of menu items (list of strings or dicts with 'text', 'href', 'class', 'submenu')
            button_text: Text for the toggle button (string, default: "Menu")
            **attrs: Component attributes including:
                - height: Maximum height of the menu (string/number, default: "auto")
                - align: Horizontal alignment ("left" or "right", default: "left")
                - keep_open: Prevents menu from closing when clicking elsewhere (boolean)
                - stay_open: Alternative to keep_open (boolean)
                - ignore_document_click: Another alternative to keep_open (boolean)
                - button_class: Additional CSS class for button (string)
                - on_menu_create: Callback when menu is created (string)
                - cls_drop_menu: Additional CSS class for drop menu (string)
                - cls_button: Additional CSS class for button (string)
                - cls_menu: Additional CSS class for menu (string)
                - cls_item: Additional CSS class for menu items (string)
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Add items and button_text to component_attrs for processing
        component_attrs['items'] = items
        component_attrs['button_text'] = button_text
        
        # Build data attributes for the menu
        data_attrs = {"data-role": "dropmenu"}
        
        # Map component parameters to data attributes
        data_attr_mapping = {
            'height': 'data-height',
            'align': 'data-align',
            'on_menu_create': 'data-on-menu-create'
        }
        
        for param, data_attr in data_attr_mapping.items():
            if param in component_attrs:
                value = component_attrs[param]
                if isinstance(value, bool):
                    data_attrs[data_attr] = "true" if value else "false"
                elif isinstance(value, (int, float)):
                    data_attrs[data_attr] = str(value)
                else:
                    data_attrs[data_attr] = value
        
        # Handle special CSS classes
        css_classes = []
        if component_attrs.get('keep_open'):
            css_classes.append('keep-open')
        if component_attrs.get('stay_open'):
            css_classes.append('stay-open')
        if component_attrs.get('ignore_document_click'):
            css_classes.append('ignore-document-click')
        
        # Add any CSS classes from cls attributes
        for key, value in cls_attrs.items():
            if key == 'cls_menu':
                css_classes.append(value)
        
        # Build final menu attributes
        menu_attrs = {**data_attrs, **standard_attrs}
        
        if css_classes:
            menu_attrs['class'] = ' '.join(css_classes)
        
        # Generate ID for debugging and initialization if not provided
        if 'id' not in standard_attrs:
            menu_attrs['id'] = f"dropmenu-{uuid.uuid4().hex[:8]}"
        
        # Build menu content
        menu_content = self.build_menu_content(component_attrs.get('items', []))
        
        # Build button
        button_html = self.build_button(component_attrs, cls_attrs)
        
        # Build menu
        menu_html = self.render_component('ul', menu_attrs, menu_content)
        
        # Return as direct siblings without wrapper
        return button_html + menu_html
    
    def build_button(self, component_attrs, cls_attrs):
        """Build the toggle button HTML."""
        button_attrs = {'class': 'button menu-toggle'}
        
        # Add button-specific CSS classes
        if component_attrs.get('button_class'):
            button_attrs['class'] += ' ' + component_attrs['button_class']
        
        if cls_attrs.get('cls_button'):
            button_attrs['class'] += ' ' + cls_attrs['cls_button']
        
        button_text = component_attrs.get('button_text', 'Menu')
        return self.render_component('button', button_attrs, button_text)
    
    def build_menu_content(self, items):
        """Build the menu content HTML from items list."""
        if not items:
            return ""
        
        content = ""
        for item in items:
            if isinstance(item, str):
                # Simple string item
                link_html = self.render_component('a', {'href': '#'}, item)
                content += self.render_component('li', {}, link_html)
            elif isinstance(item, dict):
                # Dictionary item with options
                item_content = self.build_menu_item(item)
                
                # Build list item with any custom classes
                li_attrs = {}
                if item.get('class'):
                    li_attrs['class'] = item['class']
                
                content += self.render_component('li', li_attrs, item_content)
        
        return content
    
    def build_menu_item(self, item):
        """Build individual menu item HTML."""
        link_attrs = {'href': item.get('href', '#')}
        
        # Handle submenu
        if item.get('submenu'):
            link_attrs['class'] = 'menu-toggle'
            
            # Build submenu content
            submenu_content = self.build_submenu_content(item['submenu'])
            submenu_attrs = {'data-role-dropmenu': True}
            
            # Build item with link and submenu
            link_html = self.render_component('a', link_attrs, item.get('text', ''))
            submenu_html = self.render_component('ul', submenu_attrs, submenu_content)
            
            return link_html + submenu_html
        else:
            # Simple menu item
            return self.render_component('a', link_attrs, item.get('text', ''))
    
    def build_submenu_content(self, submenu_items):
        """Build submenu content HTML recursively."""
        content = ""
        for subitem in submenu_items:
            if isinstance(subitem, str):
                link_html = self.render_component('a', {'href': '#'}, subitem)
                content += self.render_component('li', {}, link_html)
            elif isinstance(subitem, dict):
                if subitem.get('submenu'):
                    # Handle nested submenu
                    sub_item_content = self.build_menu_item(subitem)
                    content += self.render_component('li', {}, sub_item_content)
                else:
                    # Simple submenu item
                    link_attrs = {'href': subitem.get('href', '#')}
                    link_html = self.render_component('a', link_attrs, subitem.get('text', ''))
                    content += self.render_component('li', {}, link_html)
        
        return content


# Create component instance
_drop_menu_component = DropMenuComponent()


def render_drop_menu(items=None, button_text="Menu", **attrs):
    """
    Renders MetroUI drop menu using the base component class.

    Args:
        items: List of menu items (list of strings or dicts)
        button_text: Text for the toggle button (string, default: "Menu")
        **attrs: Component attributes (see DropMenuComponent.render for details)
    """
    return _drop_menu_component.render(items=items, button_text=button_text, **attrs)
