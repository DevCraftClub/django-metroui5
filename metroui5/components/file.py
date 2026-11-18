"""
MetroUI File Component

A customizable file input interface with multiple modes of operation: standard input, button, and drop zone.
Enhances the native HTML file input with better styling and additional functionality.
"""

from .base import SimpleComponent


class FileComponent(SimpleComponent):
    """
    MetroUI File component.

    Provides a customizable file input interface with multiple modes of operation:
    - Standard input mode
    - Button mode  
    - Drop zone mode

    Supports custom labels, icons, validation states, and event handlers.
    """

    def __init__(self):
        super().__init__(
            component_name="file",
            base_css_class=None,  # File component doesn't have a single base class
            tag_name="input",
            component_params=[
                # Configuration
                'file_deferred', 'label', 'mode', 'button_title', 'files_selected_title',
                'drop_title', 'drop_icon', 'clear_button_icon', 'prepend',
                # Styling
                'cls_component', 'cls_prepend', 'cls_button', 'cls_caption', 'cls_label',
                # Events
                'on_select', 'on_file_create',
                # Validation
                'error', 'error_message', 'success', 'success_message',
                # Standard input attributes
                'multiple', 'accept', 'disabled', 'required'
            ],
            data_attr_mapping={
                'file_deferred': 'data-file-deferred',
                'label': 'data-label',
                'mode': 'data-mode',
                'button_title': 'data-button-title',
                'files_selected_title': 'data-files-selected-title',
                'drop_title': 'data-drop-title',
                'drop_icon': 'data-drop-icon',
                'clear_button_icon': 'data-clear-button-icon',
                'prepend': 'data-prepend',
                'cls_component': 'data-cls-component',
                'cls_prepend': 'data-cls-prepend',
                'cls_button': 'data-cls-button',
                'cls_caption': 'data-cls-caption',
                'cls_label': 'data-cls-label',
                'on_select': 'data-on-select',
                'on_file_create': 'data-on-file-create'
            },
            default_data_attrs={
                "type": "file",
                "data-role": "file"
            }
        )

    def render(self, **attrs):
        """
        Render the file component.

        Args:
            **attrs: Component attributes including:
                # Configuration
                - file_deferred: Delay before initialization in milliseconds (number, default: 0)
                - label: Label text for the file input (string, default: "")
                - mode: Mode of operation - "input", "button", or "drop" (string, default: "input")
                - button_title: Text for the select files button (string, default: "")
                - files_selected_title: Text for displaying selected files count (string, default: "")
                - drop_title: Text for the drop zone (string, default: "")
                - drop_icon: Icon for the drop zone (string, default: "📥")
                - clear_button_icon: Icon for the clear button (string, default: "❌")
                - prepend: HTML content to prepend to the input (string, default: "")
                
                # Styling
                - cls_component: Additional CSS class for component container (string)
                - cls_prepend: Additional CSS class for prepend element (string)
                - cls_button: Additional CSS class for button (string)
                - cls_caption: Additional CSS class for caption (string)
                - cls_label: Additional CSS class for label (string)
                
                # Events
                - on_select: Callback function when files are selected (string)
                - on_file_create: Callback function when component is created (string)
                
                # Validation
                - error: Show error state (boolean)
                - error_message: Error message text (string)
                - success: Show success state (boolean)
                - success_message: Success message text (string)
                
                # Standard input attributes
                - multiple: Allow multiple file selection (boolean)
                - accept: File types to accept (string)
                - disabled: Disable the input (boolean)
                - required: Make the input required (boolean)
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

        # Build CSS classes
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)

        # Filter out None values from css_classes
        css_classes = [cls for cls in css_classes if cls is not None]

        # Add validation state classes if needed
        if component_attrs.get('error') or component_attrs.get('error_message'):
            css_classes.append("error")

        if component_attrs.get('success') or component_attrs.get('success_message'):
            css_classes.append("success")

        # Build data attributes
        data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)

        # Handle special boolean attributes
        if component_attrs.get('multiple'):
            data_attrs['multiple'] = "multiple"

        if component_attrs.get('required'):
            data_attrs['required'] = "required"

        # Handle validation states
        if component_attrs.get('error') or component_attrs.get('error_message'):
            data_attrs['data-error'] = "true"

        if component_attrs.get('success') or component_attrs.get('success_message'):
            data_attrs['data-success'] = "true"

        # Build final attributes
        final_attrs = {
            "class": " ".join(css_classes),
            **self.default_data_attrs,
            **data_attrs,
            **standard_attrs
        }

        # Add special attributes
        if component_attrs.get('accept'):
            final_attrs["accept"] = component_attrs['accept']

        if component_attrs.get('disabled'):
            final_attrs["disabled"] = "disabled"

        return self.render_component(self.tag_name, final_attrs)


# Create component instance
_file = FileComponent()


def render_file(**attrs):
    """
    Renders MetroUI file component using the base component class.

    Args:
        **attrs: Component attributes (see FileComponent.render for details)
	Example:
		render_file()

	Empty or invalid:
		`render_file()` returns `<input class="" type="file" data-role="file"></input>`.

    """
    return _file.render(**attrs)


# Utility functions for common file input patterns
def render_file_button(button_text="Choose File", **attrs):
    """
    Renders a file input in button mode.

    Args:
        button_text: Text for the button (string, default: "Choose File")
        **attrs: Additional component attributes
    """
    return _file.render(mode="button", button_title=button_text, **attrs)


def render_file_drop(drop_text="Drop file here", **attrs):
    """
    Renders a file input in drop zone mode.

    Args:
        drop_text: Text for the drop zone (string, default: "Drop file here")
        **attrs: Additional component attributes
    """
    return _file.render(mode="drop", drop_title=drop_text, **attrs)


def render_file_with_icon(icon_class="mif-folder", **attrs):
    """
    Renders a file input with an icon prepend.

    Args:
        icon_class: CSS class for the icon (string, default: "mif-folder")
        **attrs: Additional component attributes
    """
    prepend_html = f'<span class="{icon_class} mif-2x"></span>'
    return _file.render(prepend=prepend_html, **attrs)


def render_file_multiple(**attrs):
    """
    Renders a file input that accepts multiple files.

    Args:
        **attrs: Additional component attributes
    """
    return _file.render(multiple=True, **attrs)
