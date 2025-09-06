"""
MetroUI Dropdown Component

The Dropdown component provides a flexible way to create dropdown menus and lists that can be 
toggled to show or hide content. It supports various positioning options and can be customized 
through configuration options and CSS variables.
"""

from .base import ComplexComponent


class DropdownComponent(ComplexComponent):
    """
    MetroUI Dropdown component.

    Provides a flexible way to create dropdown menus and lists that can be toggled
    to show or hide content with various positioning options.
    """

    def __init__(self):
        super().__init__(
            component_name="dropdown",
            base_css_class="dropdown",
            component_params=[
                # Basic parameters
                'content', 'button_text', 'toggle_element', 'items',
                # Configuration parameters
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

    def render(self, content="", button_text="", toggle_element=None, items=None, **attrs):
        """
        Render the dropdown component.

        Args:
            content: The HTML content to be displayed in the dropdown (string)
            button_text: Text for the dropdown toggle button (string, default: "")
            toggle_element: Custom toggle element HTML (string, default: None)
            items: List of dropdown items to auto-generate menu (list, default: None)
            **attrs: Component attributes including:
                - dropdown_deferred: Delay before dropdown appears (number, default: 0)
                - drop_filter: CSS selector to filter dropdowns (string, default: null)
                - toggle_element_selector: CSS selector for toggle element (string, default: null)
                - align: Alignment ("left" or "right", default: "left")
                - no_close: Won't close when clicking outside (boolean, default: false)
                - duration: Animation duration in milliseconds (number, default: 50)
                - open_mode: How dropdown opens ("auto", "up", default: "auto")
                - open_func: Function for opening animation (string, default: "show")
                - close_func: Function for closing animation (string, default: "hide")
                - height: Height of dropdown (string, default: "auto")
                - drop_left: Position to left of toggle (boolean)
                - drop_right: Position to right of toggle (boolean)
                - drop_up: Position above toggle (boolean)
                - drop_up_left: Position above and left of toggle (boolean)
                - drop_up_right: Position above and right of toggle (boolean)
                - drop_down: Position below toggle (boolean, default)
                - drop_down_left: Position below and left of toggle (boolean)
                - drop_down_right: Position below and right of toggle (boolean)
                - keep_open: Prevent closing when clicking outside (boolean)
                - on_drop: Triggered when dropdown is opened (string)
                - on_up: Triggered when dropdown is closed (string)
                - on_dropdown_create: Triggered when dropdown is created (string)
                - cls_dropdown: Additional CSS class for dropdown (string)
                - cls_toggle: Additional CSS class for toggle (string)
                - cls_content: Additional CSS class for content (string)
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Add method parameters to component_attrs for processing
        component_attrs['content'] = content
        component_attrs['button_text'] = button_text
        component_attrs['toggle_element'] = toggle_element
        component_attrs['items'] = items
        
        # Build CSS classes including positioning classes
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
        
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
                css_classes.append(css_class)
        
        # Build data attributes
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
        
        # Build final dropdown attributes
        dropdown_attrs = {
            "class": " ".join(css_classes),
            **data_attrs,
            **standard_attrs
        }
        
        # Build dropdown content
        dropdown_content = self.build_dropdown_content(component_attrs)
        
        # Build dropdown HTML
        dropdown_html = self.render_component('div', dropdown_attrs, dropdown_content)
        
        # Create the complete dropdown structure
        return self.build_dropdown_structure(component_attrs, cls_attrs, dropdown_html)
    
    def build_dropdown_content(self, component_attrs):
        """Build the dropdown content from various sources."""
        content = component_attrs.get('content', '')
        items = component_attrs.get('items')
        
        # Auto-generate content from items if provided and no content
        if items and not content:
            if any(isinstance(item, dict) and 'href' in item for item in items):
                # Generate as list menu
                menu_items = []
                for item in items:
                    if isinstance(item, dict):
                        text = item.get('text', '')
                        href = item.get('href', '#')
                        item_attrs = {k: v for k, v in item.items() if k not in ['text', 'href']}
                        
                        if item_attrs:
                            item_attrs_str = ' '.join([f'{k}="{v}"' for k, v in item_attrs.items()])
                            menu_items.append(f'<li {item_attrs_str}><a href="{href}">{text}</a></li>')
                        else:
                            menu_items.append(f'<li><a href="{href}">{text}</a></li>')
                    else:
                        menu_items.append(f'<li><a href="#">{item}</a></li>')
                
                return f'<ul>{"".join(menu_items)}</ul>'
            else:
                # Generate as simple div content
                return '<div>' + '<br>'.join([str(item) for item in items]) + '</div>'
        
        return content
    
    def build_dropdown_structure(self, component_attrs, cls_attrs, dropdown_html):
        """Build the complete dropdown structure with toggle element."""
        toggle_element = component_attrs.get('toggle_element')
        button_text = component_attrs.get('button_text')
        
        if toggle_element:
            # Use custom toggle element with nested dropdown
            if '</button>' in toggle_element:
                return toggle_element.replace('</button>', dropdown_html + '</button>')
            elif '</div>' in toggle_element:
                return toggle_element.replace('</div>', dropdown_html + '</div>')
            else:
                # Fallback: wrap in div
                container_attrs = {'class': 'dropdown-toggle'}
                return self.render_component('div', container_attrs, toggle_element + dropdown_html)
        elif button_text:
            # Create button toggle with dropdown in container
            button_attrs = {'class': 'button'}
            
            # Add toggle-specific CSS classes
            if cls_attrs.get('cls_toggle'):
                button_attrs['class'] += ' ' + cls_attrs['cls_toggle']
            
            button_html = self.render_component('button', button_attrs, button_text)
            container_attrs = {'class': 'dropdown-toggle'}
            
            return self.render_component('div', container_attrs, button_html + dropdown_html)
        else:
            # Create default div toggle with nested dropdown
            container_attrs = {'class': 'dropdown-toggle'}
            return self.render_component('div', container_attrs, 'Click me' + dropdown_html)


# Create component instance
_dropdown_component = DropdownComponent()


def render_dropdown(content="", button_text="", toggle_element=None, items=None, **attrs):
    """
    Renders MetroUI dropdown using the base component class.

    Args:
        content: The HTML content to be displayed in the dropdown (string)
        button_text: Text for the dropdown toggle button (string, default: "")
        toggle_element: Custom toggle element HTML (string, default: None)
        items: List of dropdown items to auto-generate menu (list, default: None)
        **attrs: Component attributes (see DropdownComponent.render for details)
    """
    return _dropdown_component.render(
        content=content, 
        button_text=button_text, 
        toggle_element=toggle_element, 
        items=items, 
        **attrs
    )
