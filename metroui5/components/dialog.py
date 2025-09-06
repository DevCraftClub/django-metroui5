"""
MetroUI Dialog Component

A dialog is a modal window that appears in front of app content to provide critical information or ask for a decision.
"""

import json
from .base import ComplexComponent


class DialogComponent(ComplexComponent):
    """
    MetroUI Dialog component.
    
    A dialog is a modal window that appears in front of app content to provide critical information or ask for a decision.
    """
    
    def __init__(self):
        super().__init__(
            component_name="dialog",
            base_css_class="dialog",
            component_params=[
                # Basic parameters
                'dialog_deferred', 'close_button', 'leave_overlay_on_close', 'to_top', 'to_bottom',
                
                # Content parameters
                'custom_buttons', 'actions_align', 'default_actions', 'default_action_buttons',
                
                # Overlay parameters
                'overlay', 'overlay_color', 'overlay_alpha', 'overlay_click_close',
                
                # Size parameters
                'width', 'height',
                
                # Behavior parameters
                'close_action', 'auto_hide', 'remove_on_close', 'show',
                
                # Styling parameters
                'cls_dialog', 'cls_title', 'cls_content', 'cls_action', 'cls_default_action', 'cls_overlay',
                
                # Event handlers
                'on_ok', 'on_cancel', 'on_help', 'on_show', 'on_hide', 'on_open', 'on_close', 'on_dialog_create'
            ]
        )
    
    def render(self, title="", content="", **attrs):
        """
        Renders MetroUI dialog component with comprehensive features.

        Args:
            title: Dialog title (string)
            content: Dialog content (string)
            **attrs: Additional HTML attributes including:
                # Basic Parameters
                - dialog_deferred: Delay before dialog initialization in milliseconds (number, default: 0)
                - close_button: Show close button in top-right corner (boolean, default: false)
                - leave_overlay_on_close: Keep overlay when dialog is closed (boolean, default: false)
                - to_top: Position dialog at top of screen (boolean, default: false)
                - to_bottom: Position dialog at bottom of screen (boolean, default: false)
                
                # Content Parameters
                - custom_buttons: Array of custom button objects (array)
                - actions_align: Alignment of action buttons - "left", "center", "right" (string, default: "right")
                - default_actions: Show default action buttons (boolean, default: true)
                - default_action_buttons: Comma-separated list of default buttons - "ok,cancel,help" (string, default: "ok,cancel,help")
                
                # Overlay Parameters
                - overlay: Show overlay behind dialog (boolean, default: true)
                - overlay_color: Color of the overlay (string, default: "#000000")
                - overlay_alpha: Opacity of the overlay (number, default: 0.5)
                - overlay_click_close: Close dialog when clicking on overlay (boolean, default: false)
                
                # Size Parameters
                - width: Width of the dialog (string, default: "auto")
                - height: Height of the dialog (string, default: "auto")
                
                # Behavior Parameters
                - close_action: Enable close action for elements with class js-dialog-close (boolean, default: true)
                - auto_hide: Auto hide dialog after specified milliseconds (number, default: 0, 0 = disabled)
                - remove_on_close: Remove dialog element from DOM when closed (boolean, default: false)
                - show: Show dialog immediately after initialization (boolean, default: false)
                
                # Styling Parameters
                - cls_dialog: Additional CSS class for dialog element (string)
                - cls_title: Additional CSS class for title element (string)
                - cls_content: Additional CSS class for content element (string)
                - cls_action: Additional CSS class for actions element (string)
                - cls_default_action: Additional CSS class for default action buttons (string)
                - cls_overlay: Additional CSS class for overlay element (string)
                
                # Event Handlers
                - on_ok: Callback when OK button is clicked (string)
                - on_cancel: Callback when Cancel button is clicked (string)
                - on_help: Callback when Help button is clicked (string)
                - on_show: Callback when dialog is shown (string)
                - on_hide: Callback when dialog is hidden (string)
                - on_open: Callback when dialog is opened (string)
                - on_close: Callback when dialog is closed (string)
                - on_dialog_create: Callback when dialog is created (string)
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Build base attributes
        base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
        
        # Add data-role
        base_attrs["data-role"] = "dialog"
        
        # Add MetroUI-specific data attributes
        data_attrs = {}
        
        if component_attrs.get('dialog_deferred'):
            data_attrs["data-dialog-deferred"] = str(component_attrs['dialog_deferred'])
        
        if component_attrs.get('close_button'):
            data_attrs["data-close-button"] = "true"
        
        if component_attrs.get('leave_overlay_on_close'):
            data_attrs["data-leave-overlay-on-close"] = "true"
        
        if component_attrs.get('to_top'):
            data_attrs["data-to-top"] = "true"
        
        if component_attrs.get('to_bottom'):
            data_attrs["data-to-bottom"] = "true"
        
        if component_attrs.get('custom_buttons'):
            if isinstance(component_attrs['custom_buttons'], (list, dict)):
                data_attrs["data-custom-buttons"] = json.dumps(component_attrs['custom_buttons'])
            else:
                data_attrs["data-custom-buttons"] = component_attrs['custom_buttons']
        
        if component_attrs.get('actions_align'):
            data_attrs["data-actions-align"] = component_attrs['actions_align']
        
        if component_attrs.get('default_actions') is not None:
            data_attrs["data-default-actions"] = "true" if component_attrs['default_actions'] else "false"
        
        if component_attrs.get('default_action_buttons'):
            data_attrs["data-default-action-buttons"] = component_attrs['default_action_buttons']
        
        if component_attrs.get('overlay') is not None:
            data_attrs["data-overlay"] = "true" if component_attrs['overlay'] else "false"
        
        if component_attrs.get('overlay_color'):
            data_attrs["data-overlay-color"] = component_attrs['overlay_color']
        
        if component_attrs.get('overlay_alpha'):
            data_attrs["data-overlay-alpha"] = str(component_attrs['overlay_alpha'])
        
        if component_attrs.get('overlay_click_close'):
            data_attrs["data-overlay-click-close"] = "true"
        
        if component_attrs.get('width'):
            data_attrs["data-width"] = component_attrs['width']
        
        if component_attrs.get('height'):
            data_attrs["data-height"] = component_attrs['height']
        
        if component_attrs.get('close_action') is not None:
            data_attrs["data-close-action"] = "true" if component_attrs['close_action'] else "false"
        
        if component_attrs.get('auto_hide'):
            data_attrs["data-auto-hide"] = str(component_attrs['auto_hide'])
        
        if component_attrs.get('remove_on_close'):
            data_attrs["data-remove-on-close"] = "true"
        
        if component_attrs.get('show'):
            data_attrs["data-show"] = "true"
        
        # Add styling parameters
        if component_attrs.get('cls_dialog'):
            data_attrs["data-cls-dialog"] = component_attrs['cls_dialog']
        
        if component_attrs.get('cls_title'):
            data_attrs["data-cls-title"] = component_attrs['cls_title']
        
        if component_attrs.get('cls_content'):
            data_attrs["data-cls-content"] = component_attrs['cls_content']
        
        if component_attrs.get('cls_action'):
            data_attrs["data-cls-action"] = component_attrs['cls_action']
        
        if component_attrs.get('cls_default_action'):
            data_attrs["data-cls-default-action"] = component_attrs['cls_default_action']
        
        if component_attrs.get('cls_overlay'):
            data_attrs["data-cls-overlay"] = component_attrs['cls_overlay']
        
        # Add event handlers
        if component_attrs.get('on_ok'):
            data_attrs["data-on-ok"] = component_attrs['on_ok']
        
        if component_attrs.get('on_cancel'):
            data_attrs["data-on-cancel"] = component_attrs['on_cancel']
        
        if component_attrs.get('on_help'):
            data_attrs["data-on-help"] = component_attrs['on_help']
        
        if component_attrs.get('on_show'):
            data_attrs["data-on-show"] = component_attrs['on_show']
        
        if component_attrs.get('on_hide'):
            data_attrs["data-on-hide"] = component_attrs['on_hide']
        
        if component_attrs.get('on_open'):
            data_attrs["data-on-open"] = component_attrs['on_open']
        
        if component_attrs.get('on_close'):
            data_attrs["data-on-close"] = component_attrs['on_close']
        
        if component_attrs.get('on_dialog_create'):
            data_attrs["data-on-dialog-create"] = component_attrs['on_dialog_create']
        
        # Merge all attributes
        final_attrs = {**base_attrs, **data_attrs}
        
        # Build dialog content
        dialog_content = ""
        
        # Add close button if enabled
        if component_attrs.get('close_button'):
            dialog_content += '<button class="closer js-dialog-close">&times;</button>'
        
        # Add title if provided
        if title:
            title_class = "dialog-title"
            if component_attrs.get('cls_title'):
                title_class += f" {component_attrs['cls_title']}"
            dialog_content += f'<div class="{title_class}">{title}</div>'
        
        # Add content if provided
        if content:
            content_class = "dialog-content"
            if component_attrs.get('cls_content'):
                content_class += f" {component_attrs['cls_content']}"
            dialog_content += f'<div class="{content_class}">{content}</div>'
        
        # Add actions section
        actions_class = "dialog-actions"
        if component_attrs.get('actions_align'):
            if component_attrs['actions_align'] == 'left':
                actions_class += " text-left"
            elif component_attrs['actions_align'] == 'center':
                actions_class += " text-center"
            elif component_attrs['actions_align'] == 'right':
                actions_class += " text-right"
        
        if component_attrs.get('cls_action'):
            actions_class += f" {component_attrs['cls_action']}"
        
        # Add default action buttons if enabled
        if component_attrs.get('default_actions', True):
            action_buttons = component_attrs.get('default_action_buttons', 'ok,cancel,help').split(',')
            buttons_html = ""
            
            for button in action_buttons:
                button = button.strip()
                if button == 'ok':
                    button_class = "button js-dialog-close"
                    if component_attrs.get('cls_default_action'):
                        button_class += f" {component_attrs['cls_default_action']}"
                    buttons_html += f'<button class="{button_class}" data-action="ok">OK</button>'
                elif button == 'cancel':
                    button_class = "button js-dialog-close"
                    if component_attrs.get('cls_default_action'):
                        button_class += f" {component_attrs['cls_default_action']}"
                    buttons_html += f'<button class="{button_class}" data-action="cancel">Cancel</button>'
                elif button == 'help':
                    button_class = "button js-dialog-close"
                    if component_attrs.get('cls_default_action'):
                        button_class += f" {component_attrs['cls_default_action']}"
                    buttons_html += f'<button class="{button_class}" data-action="help">Help</button>'
            
            if buttons_html:
                dialog_content += f'<div class="{actions_class}">{buttons_html}</div>'
        
        # Add custom buttons if provided
        if component_attrs.get('custom_buttons'):
            custom_buttons_html = ""
            custom_buttons = component_attrs['custom_buttons']
            
            if isinstance(custom_buttons, list):
                for button in custom_buttons:
                    if isinstance(button, dict):
                        button_text = button.get('text', 'Button')
                        button_class = button.get('cls', 'button')
                        button_onclick = button.get('onclick', '')
                        
                        onclick_attr = f' onclick="{button_onclick}"' if button_onclick else ''
                        custom_buttons_html += f'<button class="{button_class}"{onclick_attr}>{button_text}</button>'
            
            if custom_buttons_html:
                # If we already have default actions, append to them, otherwise create new actions div
                if component_attrs.get('default_actions', True):
                    # Find the existing actions div and append custom buttons
                    dialog_content = dialog_content.replace('</div>', f'{custom_buttons_html}</div>', 1)
                else:
                    dialog_content += f'<div class="{actions_class}">{custom_buttons_html}</div>'
        
        return self.render_component("div", final_attrs, dialog_content)


# Create component instance
_dialog_component = DialogComponent()


def render_dialog(title="", content="", **attrs):
    """
    Renders MetroUI dialog component using the base component class.
    
    Args:
        title: Dialog title (string)
        content: Dialog content (string)
        **attrs: Component attributes (see DialogComponent.render for details)
    """
    return _dialog_component.render(title, content, **attrs)


def render_dialog_create(**options):
    """
    Renders JavaScript code to create a dialog dynamically using Metro.dialog.create().
    
    Args:
        **options: Dialog creation options matching Metro.dialog.create() parameters
        
    Returns:
        str: JavaScript code to create the dialog
    """
    js_options = {}
    
    # Map Python parameters to JavaScript options
    param_mapping = {
        'title': 'title',
        'content': 'content',
        'close_button': 'closeButton',
        'default_actions': 'defaultActions',
        'default_action_buttons': 'defaultActionButtons',
        'custom_buttons': 'customButtons',
        'actions_align': 'actionsAlign',
        'overlay': 'overlay',
        'overlay_color': 'overlayColor',
        'overlay_alpha': 'overlayAlpha',
        'overlay_click_close': 'overlayClickClose',
        'width': 'width',
        'height': 'height',
        'close_action': 'closeAction',
        'auto_hide': 'autoHide',
        'remove_on_close': 'removeOnClose',
        'show': 'show',
        'to_top': 'toTop',
        'to_bottom': 'toBottom',
        'leave_overlay_on_close': 'leaveOverlayOnClose'
    }
    
    for py_param, js_param in param_mapping.items():
        if py_param in options:
            js_options[js_param] = options[py_param]
    
    # Convert to JavaScript object
    js_object = json.dumps(js_options, indent=2)
    
    return f"Metro.dialog.create({js_object});"
