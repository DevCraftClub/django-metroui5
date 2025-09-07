"""
MetroUI D-Menu Component

This module provides the MetroUI D-Menu component implementation.
The D-Menu component provides a versatile dropdown menu system for displaying 
contextual options, navigation items, and hierarchical menus. It supports icons, 
captions, hotkeys, and nested submenus.

References:
    https://v5.metroui.org.ua/components/d-menu/
"""

from .base import ComplexComponent
from ..html import render_tag


class DMenuComponent(ComplexComponent):
    """
    MetroUI D-Menu Component.
    
    A versatile dropdown menu system for displaying contextual options, navigation items, 
    and hierarchical menus. It supports icons, captions, hotkeys, and nested submenus.
    """
    
    def __init__(self):
        super().__init__(
            component_name="d_menu",
            base_css_class="d-menu",
            component_params=[
                'drop_filter', 'toggle_element', 'align', 'no_close', 'duration', 
                'open_mode', 'height', 'on_drop', 'on_up', 'on_dropdown_create',
                'cls_menu', 'cls_item', 'cls_divider', 'cls_icon', 'cls_caption', 'cls_hotkey'
            ]
        )
    
    def render(self, items=None, **attrs):
        """
        Renders the D-Menu component.
        
        Args:
            items (list, str, optional): List of menu items or JSON string. Each item can be:
                - str: Simple text item
                - dict: Complex item with keys:
                    - text (str): Item text
                    - href (str): Item link
                    - icon (str): Icon class
                    - caption (str): Caption text
                    - hotkey (str): Keyboard shortcut
                    - disabled (bool): Whether item is disabled
                    - divider (bool): Whether item is a divider
                    - submenu (list): Nested submenu items
            **attrs: Additional HTML attributes including:
                drop_filter (str): Filter for dropdown elements
                toggle_element (str): Element that toggles the dropdown
                align (str): Alignment of the dropdown menu ("left", "right")
                no_close (bool): If true, prevents the dropdown from closing when clicking outside
                duration (int): Animation duration in milliseconds
                open_mode (str): Opening mode ("auto", "up")
                height (str): Height of the dropdown menu
                on_drop (str): Callback function triggered when dropdown is opened
                on_up (str): Callback function triggered when dropdown is closed
                on_dropdown_create (str): Callback function triggered after dropdown is created
                cls_menu (str): Additional CSS class for the menu container
                cls_item (str): Additional CSS class for menu items
                cls_divider (str): Additional CSS class for divider items
                cls_icon (str): Additional CSS class for icons
                cls_caption (str): Additional CSS class for captions
                cls_hotkey (str): Additional CSS class for hotkeys
        
        Returns:
            str: HTML string for the D-Menu
        """
        # Parse items if it's a JSON string
        if isinstance(items, str):
            try:
                import json
                items = json.loads(items)
            except (json.JSONDecodeError, ValueError):
                # If JSON parsing fails, treat as simple string list
                items = [item.strip() for item in items.split(',')]
        
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Build base attributes - only add class and id if explicitly provided
        base_attrs = {}
        
        # Always include base class, plus any additional classes if provided
        css_classes = [self.base_css_class]
        
        # Check if there are explicit additional classes
        has_explicit_class = 'class' in standard_attrs or 'cls' in cls_attrs or any(key.startswith('cls_') for key in component_attrs)
        if has_explicit_class:
            # Handle class parameter from standard_attrs
            if 'class' in standard_attrs:
                # Move class to cls_attrs for processing
                cls_attrs['class'] = standard_attrs.pop('class')
            
            # Add classes from cls_attrs
            for key, value in cls_attrs.items():
                if key == 'class' or key == 'cls':
                    # Split and add individual classes
                    existing_classes = value.split()
                    css_classes.extend([cls for cls in existing_classes if cls not in css_classes])
                else:
                    css_classes.append(value)
            
            # Add component-specific class
            component_param_name = f'cls_{self.component_name}'
            if component_attrs.get(component_param_name):
                css_classes.append(component_attrs[component_param_name])
        
        # Always add the class attribute with base class
        base_attrs["class"] = " ".join(css_classes)
        
        # Add id only if explicitly provided
        if 'id' in standard_attrs:
            base_attrs["id"] = standard_attrs["id"]
        elif 'id' in component_attrs:
            base_attrs["id"] = component_attrs["id"]
        
        # Add other standard attributes
        for key, value in standard_attrs.items():
            if key not in ['class', 'cls', 'id']:
                base_attrs[key] = value
        
        # Add data-role attribute for dropdown functionality
        if component_attrs.get('toggle_element') or component_attrs.get('drop_filter'):
            base_attrs["data-role"] = "dropdown"
        
        # Add dropdown-specific data attributes
        if component_attrs.get('drop_filter'):
            base_attrs["data-drop-filter"] = component_attrs['drop_filter']
        
        if component_attrs.get('toggle_element'):
            base_attrs["data-toggle-element"] = component_attrs['toggle_element']
        
        if component_attrs.get('align'):
            base_attrs["data-align"] = component_attrs['align']
        
        if component_attrs.get('no_close') is not None:
            base_attrs["data-no-close"] = "true" if component_attrs['no_close'] else "false"
        
        if component_attrs.get('duration'):
            base_attrs["data-duration"] = str(component_attrs['duration'])
        
        if component_attrs.get('open_mode'):
            base_attrs["data-open-mode"] = component_attrs['open_mode']
        
        if component_attrs.get('height'):
            base_attrs["data-height"] = component_attrs['height']
        
        # Add callback functions
        if component_attrs.get('on_drop'):
            base_attrs["data-on-drop"] = component_attrs['on_drop']
        
        if component_attrs.get('on_up'):
            base_attrs["data-on-up"] = component_attrs['on_up']
        
        if component_attrs.get('on_dropdown_create'):
            base_attrs["data-on-dropdown-create"] = component_attrs['on_dropdown_create']
        
        # Build menu items
        menu_items_html = ""
        if items:
            for item in items:
                menu_items_html += self._render_menu_item(item, component_attrs)
        
        return render_tag("ul", attrs=base_attrs, content=menu_items_html)
    
    def _render_menu_item(self, item, component_attrs, level=1):
        """
        Renders a single menu item with support for nested submenus.
        
        Args:
            item: Menu item (str or dict)
            component_attrs: Component attributes
            level: Current nesting level
            
        Returns:
            str: HTML string for the menu item
        """
        if isinstance(item, str):
            # Simple text item
            return render_tag("li", {}, render_tag("a", {"href": "#"}, item))
        
        if not isinstance(item, dict):
            return ""
        
        # Check if item is a divider
        if item.get('divider'):
            divider_classes = ["divider"]
            if component_attrs.get('cls_divider'):
                divider_classes.append(component_attrs['cls_divider'])
            return render_tag("li", {"class": " ".join(divider_classes)}, "")
        
        # Check if item has submenu
        if item.get('submenu'):
            return self._render_submenu_item(item, component_attrs, level)
        
        # Regular menu item
        return self._render_regular_item(item, component_attrs)
    
    def _render_submenu_item(self, item, component_attrs, level):
        """
        Renders a menu item with submenu.
        
        Args:
            item: Menu item dictionary
            component_attrs: Component attributes
            level: Current nesting level
            
        Returns:
            str: HTML string for the submenu item
        """
        # Build toggle link
        toggle_content = self._build_item_content(item, component_attrs)
        toggle_classes = ["dropdown-toggle"]
        toggle_attrs = {"href": item.get('href', '#'), "class": " ".join(toggle_classes)}
        toggle_link = render_tag("a", toggle_attrs, toggle_content)
        
        # Build submenu
        submenu_items = []
        for submenu_item in item['submenu']:
            submenu_items.append(self._render_menu_item(submenu_item, component_attrs, level + 1))
        
        # Build submenu attributes
        submenu_attrs = {"class": "d-menu", "data-role": "dropdown"}
        
        # Add positioning classes for submenus
        if level > 1:
            submenu_attrs["class"] += " place-right"
        
        submenu_html = render_tag("ul", submenu_attrs, "".join(submenu_items))
        
        return render_tag("li", {}, toggle_link + submenu_html)
    
    def _render_regular_item(self, item, component_attrs):
        """
        Renders a regular menu item (no submenu).
        
        Args:
            item: Menu item dictionary
            component_attrs: Component attributes
            
        Returns:
            str: HTML string for the regular item
        """
        # Build item content
        item_content = self._build_item_content(item, component_attrs)
        
        # Build item attributes
        item_attrs = {"href": item.get('href', '#')}
        
        # Add disabled class if needed
        item_classes = []
        if item.get('disabled'):
            item_classes.append("disabled")
        if component_attrs.get('cls_item'):
            item_classes.append(component_attrs['cls_item'])
        
        if item_classes:
            item_attrs["class"] = " ".join(item_classes)
        
        return render_tag("li", {}, render_tag("a", item_attrs, item_content))
    
    def _build_item_content(self, item, component_attrs):
        """
        Builds the content for a menu item.
        
        Args:
            item: Menu item dictionary
            component_attrs: Component attributes
            
        Returns:
            str: HTML content for the item
        """
        content_parts = []
        
        # Add icon
        if item.get('icon'):
            icon_classes = ["icon", item['icon']]
            if component_attrs.get('cls_icon'):
                icon_classes.append(component_attrs['cls_icon'])
            content_parts.append(render_tag("span", {"class": " ".join(icon_classes)}, ""))
        
        # Add caption (text) - prioritize 'text' over 'caption' for consistency
        if item.get('text'):
            caption_text = item['text']
            caption_classes = ["caption"]
            if component_attrs.get('cls_caption'):
                caption_classes.append(component_attrs['cls_caption'])
            content_parts.append(render_tag("span", {"class": " ".join(caption_classes)}, caption_text))
        elif item.get('caption'):
            caption_text = item['caption']
            caption_classes = ["caption"]
            if component_attrs.get('cls_caption'):
                caption_classes.append(component_attrs['cls_caption'])
            content_parts.append(render_tag("span", {"class": " ".join(caption_classes)}, caption_text))
        
        # Add hotkey
        if item.get('hotkey'):
            hotkey_classes = ["hotkey"]
            if component_attrs.get('cls_hotkey'):
                hotkey_classes.append(component_attrs['cls_hotkey'])
            content_parts.append(render_tag("span", {"class": " ".join(hotkey_classes)}, item['hotkey']))
        
        return "".join(content_parts)


# Create component instance
_d_menu_component = DMenuComponent()


def render_d_menu(items=None, **attrs):
    """
    Renders MetroUI D-Menu component.
    
    The D-Menu component provides a versatile dropdown menu system for displaying 
    contextual options, navigation items, and hierarchical menus. It supports icons, 
    captions, hotkeys, and nested submenus.
    
    Args:
        items (list, str, optional): List of menu items or JSON string. Each item can be:
            - str: Simple text item
            - dict: Complex item with keys:
                - text (str): Item text
                - href (str): Item link
                - icon (str): Icon class
                - caption (str): Caption text
                - hotkey (str): Keyboard shortcut
                - disabled (bool): Whether item is disabled
                - divider (bool): Whether item is a divider
                - submenu (list): Nested submenu items
        **attrs: Additional HTML attributes including:
            drop_filter (str): Filter for dropdown elements
            toggle_element (str): Element that toggles the dropdown
            align (str): Alignment of the dropdown menu ("left", "right")
            no_close (bool): If true, prevents the dropdown from closing when clicking outside
            duration (int): Animation duration in milliseconds
            open_mode (str): Opening mode ("auto", "up")
            height (str): Height of the dropdown menu
            on_drop (str): Callback function triggered when dropdown is opened
            on_up (str): Callback function triggered when dropdown is closed
            on_dropdown_create (str): Callback function triggered after dropdown is created
            cls_menu (str): Additional CSS class for the menu container
            cls_item (str): Additional CSS class for menu items
            cls_divider (str): Additional CSS class for divider items
            cls_icon (str): Additional CSS class for icons
            cls_caption (str): Additional CSS class for captions
            cls_hotkey (str): Additional CSS class for hotkeys
    
    Returns:
        str: HTML string for the D-Menu
        
    References:
        .. _MetroUI D-Menu: https://v5.metroui.org.ua/components/d-menu/
        .. _MetroUI Documentation: https://v5.metroui.org.ua/
    """
    return _d_menu_component.render(items=items, **attrs)


