"""
MetroUI Dropdown Button Component

The Dropdown Button component combines the functionality of the Button and Dropdown components 
to create a button that toggles a dropdown menu. It provides a convenient way to create 
dropdown menus triggered by button clicks.
"""

from .base import ComplexComponent


class DropdownButtonComponent(ComplexComponent):
    """
    MetroUI Dropdown Button component.

    Combines button and dropdown functionality to create a button that toggles
    a dropdown menu when clicked.
    """

    def __init__(self):
        super().__init__(
            component_name="dropdown_button",
            base_css_class="dropdown-button",
            component_params=[
                # Basic parameters
                'button_text', 'items', 'content',
                # Button styling parameters
                'button_style', 'button_size', 'outline', 'flat', 'rounded',
                'icon', 'icon_position',
                # Dropdown configuration parameters (inherited from Dropdown)
                'dropdown_deferred', 'drop_filter', 'toggle_element_selector',
                'align', 'no_close', 'duration', 'open_mode', 'open_func',
                'close_func', 'height',
                # Positioning parameters
                'drop_left', 'drop_right', 'drop_up', 'drop_up_left',
                'drop_up_right', 'drop_down', 'drop_down_left', 'drop_down_right',
                'keep_open',
                # Event handlers
                'on_drop', 'on_up', 'on_dropdown_create'
                # Note: cls_* parameters are handled automatically by base class
            ]
        )

    def render(self, button_text="Options", items=None, content="", **attrs):
        """
        Render the dropdown button component.

        Args:
            button_text: Text for the dropdown toggle button (string, default: "Options")
            items: List of dropdown menu items (list of strings or dicts, default: None)
            content: Custom HTML content for dropdown (string, default: "")
            **attrs: Component attributes including:
                # Button styling
                - button_style: Button style ("primary", "success", "warning", "danger", "info", "dark", "light")
                - button_size: Button size ("large", "small", "mini")
                - outline: Outline button style (boolean)
                - flat: Flat button style (boolean)
                - rounded: Rounded button style (boolean)
                - icon: Icon class for button (string)
                - icon_position: Icon position ("left", "right", default: "left")
                
                # Dropdown configuration
                - dropdown_deferred: Delay before dropdown appears (number, default: 0)
                - drop_filter: CSS selector to filter dropdowns (string, default: null)
                - toggle_element_selector: CSS selector for toggle element (string, default: null)
                - align: Dropdown alignment ("left" or "right", default: "left")
                - no_close: Won't close when clicking outside (boolean, default: false)
                - duration: Animation duration in milliseconds (number, default: 50)
                - open_mode: How dropdown opens ("auto", "up", default: "auto")
                - open_func: Function for opening animation (string, default: "show")
                - close_func: Function for closing animation (string, default: "hide")
                - height: Height of dropdown (string, default: "auto")
                
                # Positioning
                - drop_left: Position to left of toggle (boolean)
                - drop_right: Position to right of toggle (boolean)
                - drop_up: Position above toggle (boolean)
                - drop_up_left: Position above and left of toggle (boolean)
                - drop_up_right: Position above and right of toggle (boolean)
                - drop_down: Position below toggle (boolean, default)
                - drop_down_left: Position below and left of toggle (boolean)
                - drop_down_right: Position below and right of toggle (boolean)
                - keep_open: Prevent closing when clicking outside (boolean)
                
                # Events
                - on_drop: Triggered when dropdown is opened (string)
                - on_up: Triggered when dropdown is closed (string)
                - on_dropdown_create: Triggered when dropdown is created (string)
                
                # CSS classes
                - cls_dropdown_button: Additional CSS class for dropdown button container (string)
                - cls_button: Additional CSS class for button (string)
                - cls_dropdown: Additional CSS class for dropdown menu (string)
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Add method parameters to component_attrs for processing
        component_attrs['button_text'] = button_text
        component_attrs['items'] = items
        component_attrs['content'] = content
        
        # Build container CSS classes
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
        
        # Build the dropdown button container
        container_attrs = {
            "class": " ".join(css_classes),
            **standard_attrs
        }
        
        # Build the toggle button
        button_html = self.build_toggle_button(component_attrs, cls_attrs)
        
        # Build the dropdown menu
        dropdown_html = self.build_dropdown_menu(component_attrs, cls_attrs)
        
        # Combine button and dropdown
        content_html = button_html + dropdown_html
        
        return self.render_component('div', container_attrs, content_html)
    
    def build_toggle_button(self, component_attrs, cls_attrs):
        """Build the dropdown toggle button HTML."""
        button_classes = ['button', 'dropdown-toggle']
        
        # Add button style classes
        if component_attrs.get('button_style'):
            button_classes.append(f'button-{component_attrs["button_style"]}')
        
        if component_attrs.get('button_size'):
            if component_attrs['button_size'] == 'large':
                button_classes.append('large')
            elif component_attrs['button_size'] == 'small':
                button_classes.append('small')
            elif component_attrs['button_size'] == 'mini':
                button_classes.append('mini')
        
        if component_attrs.get('outline'):
            button_classes.append('outline')
        
        if component_attrs.get('flat'):
            button_classes.append('flat')
        
        if component_attrs.get('rounded'):
            button_classes.append('rounded')
        
        # Add custom button CSS classes
        if cls_attrs.get('cls_button'):
            button_classes.append(cls_attrs['cls_button'])
        
        # Build button content with optional icon
        button_content = ""
        icon = component_attrs.get('icon')
        button_text = component_attrs.get('button_text', 'Options')
        icon_position = component_attrs.get('icon_position', 'left')
        
        if icon:
            icon_html = f'<span class="{icon}"></span>'
            if icon_position == 'right':
                button_content = f'{button_text} {icon_html}'
            else:
                button_content = f'{icon_html} {button_text}'
        else:
            button_content = button_text
        
        button_attrs = {
            'class': ' '.join(button_classes)
        }
        
        return self.render_component('button', button_attrs, button_content)
    
    def build_dropdown_menu(self, component_attrs, cls_attrs):
        """Build the dropdown menu HTML."""
        dropdown_classes = ['d-menu']
        
        # Add positioning classes
        positioning_classes = {
            'drop_left': 'drop-left',
            'drop_right': 'drop-right', 
            'drop_up': 'drop-up',
            'drop_up_left': 'drop-up-left',
            'drop_up_right': 'drop-up-right',
            'drop_down': 'drop-down',
            'drop_down_left': 'drop-down-left',
            'drop_down_right': 'drop-down-right',
            'keep_open': 'keep-open'
        }
        
        for py_param, css_class in positioning_classes.items():
            if component_attrs.get(py_param):
                dropdown_classes.append(css_class)
        
        # Add custom dropdown CSS classes
        if cls_attrs.get('cls_dropdown'):
            dropdown_classes.append(cls_attrs['cls_dropdown'])
        
        # Build data attributes for dropdown functionality
        data_attrs = {"data-role": "dropdown"}
        
        data_attr_mapping = {
            'dropdown_deferred': 'data-dropdown-deferred',
            'drop_filter': 'data-drop-filter', 
            'toggle_element_selector': 'data-toggle-element',
            'align': 'data-align',
            'no_close': 'data-no-close',
            'duration': 'data-duration',
            'open_mode': 'data-open-mode',
            'open_func': 'data-open-func',
            'close_func': 'data-close-func',
            'height': 'data-height',
            'on_drop': 'data-on-drop',
            'on_up': 'data-on-up',
            'on_dropdown_create': 'data-on-dropdown-create'
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
        
        # Build dropdown content
        dropdown_content = self.build_dropdown_content(component_attrs)
        
        # Build dropdown attributes
        dropdown_attrs = {
            "class": " ".join(dropdown_classes),
            **data_attrs
        }
        
        return self.render_component('ul', dropdown_attrs, dropdown_content)
    
    def build_dropdown_content(self, component_attrs):
        """Build the dropdown content from items or custom content."""
        items = component_attrs.get('items')
        content = component_attrs.get('content', '')
        
        # Use custom content if provided
        if content:
            return content
        
        # Auto-generate content from items
        if items:
            menu_items = []
            for item in items:
                if isinstance(item, str):
                    # Simple string item
                    menu_items.append(f'<li><a href="#">{item}</a></li>')
                elif isinstance(item, dict):
                    # Dictionary item with options
                    text = item.get('text', '')
                    href = item.get('href', '#')
                    item_attrs = {k: v for k, v in item.items() if k not in ['text', 'href']}
                    
                    if item_attrs:
                        item_attrs_str = ' '.join([f'{k}="{v}"' for k, v in item_attrs.items()])
                        menu_items.append(f'<li {item_attrs_str}><a href="{href}">{text}</a></li>')
                    else:
                        menu_items.append(f'<li><a href="{href}">{text}</a></li>')
            
            return ''.join(menu_items)
        
        # Default content if no items or content provided
        return '<li><a href="#">No items</a></li>'


# Create component instance
_dropdown_button_component = DropdownButtonComponent()


def render_dropdown_button(button_text="Options", items=None, content="", **attrs):
    """
    Renders MetroUI dropdown button using the base component class.

    Args:
        button_text: Text for the dropdown toggle button (string, default: "Options")
        items: List of dropdown menu items (list of strings or dicts, default: None)
        content: Custom HTML content for dropdown (string, default: "")
        **attrs: Component attributes (see DropdownButtonComponent.render for details)
    """
    return _dropdown_button_component.render(
        button_text=button_text,
        items=items,
        content=content,
        **attrs
    )
