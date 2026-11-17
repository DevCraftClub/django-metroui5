"""
MetroUI Directive Component

The Directive component creates styled directive boxes for displaying notes, warnings, tips, and other informational content in your application.
"""

from .base import SimpleComponent


class DirectiveComponent(SimpleComponent):
    """
    MetroUI Directive component.
    
    Creates styled directive boxes for displaying notes, warnings, tips, and other 
    informational content in your application.
    """
    
    def __init__(self):
        super().__init__(
            component_name="directive",
            base_css_class="",
            tag_name="div",
            component_params=[
                # Basic parameters
                'directive', 'show_icon', 'title', 'style',
                # Event handlers
                'on_directive_create',
                # Styling parameters (cls_directive is handled automatically by base class)
                'cls_title', 'cls_content'
            ],
            data_attr_mapping={
                'directive': 'data-directive',
                'show_icon': 'data-show-icon',
                'title': 'data-title',
                'style': 'data-style',
                'on_directive_create': 'data-on-directive-create',
                'cls_directive': 'data-cls-directive',
                'cls_title': 'data-cls-title',
                'cls_content': 'data-cls-content'
            },
            default_data_attrs={
                "data-role": "directive"
            }
        )

    def render(self, content="", **attrs):
        """
        Render the directive component.
        
        Args:
            content: Directive content text (string)
            **attrs: Component attributes including:
                - directive: Type of directive. Options: "note", "info", "warning", "caution", "tip", "success", "important", "bug", "shit", "air", "fuck" (string, default: "note")
                - show_icon: Whether to show an icon (boolean, default: true)
                - title: Title of the directive. If set to "default", it will use the localized label for the directive type (string, default: "default")
                - style: Style of the directive. Options: 1, 2, 3 (number, default: 1)
                - on_directive_create: Event fired when directive is created (string)
                - cls_directive: Additional CSS class for directive element (string)
                - cls_title: Additional CSS class for title element (string)
                - cls_content: Additional CSS class for content element (string)
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Build CSS classes using base class method
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
        
        # Build data attributes
        data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
        
        # Handle special boolean attributes
        if component_attrs.get('show_icon') is not None:
            data_attrs['data-show-icon'] = "true" if component_attrs['show_icon'] else "false"
        
        # Build final attributes
        final_attrs = {
            **self.default_data_attrs,
            **data_attrs,
            **standard_attrs
        }
        
        # Add class attribute if we have any classes
        if css_classes:
            # Filter out empty strings and join
            filtered_classes = [cls for cls in css_classes if cls and cls.strip()]
            if filtered_classes:
                final_attrs["class"] = " ".join(filtered_classes)
        
        return self.render_component(self.tag_name, final_attrs, content)


# Create component instance
_directive_component = DirectiveComponent()


def render_directive(content="", **attrs):
    """
    Renders MetroUI directive component using the base component class.

    Args:
        content: Directive content text (string)
        **attrs: Component attributes (see DirectiveComponent.render for details)

    Example:
        Basic directive:
        ```python
        render_directive("This is a basic directive")
        ```

        Directive with type and style:
        ```python
        render_directive(
            "This is a warning directive", 
            directive="warning", 
            style=2
        )
        ```

        Directive with custom title and no icon:
        ```python
        render_directive(
            "This is a tip directive", 
            directive="tip", 
            title="Custom Tip", 
            show_icon=False
        )
        ```

        Directive with all directive types:
        ```python
        # Note (default)
        render_directive("Note content")
        
        # Info
        render_directive("Info content", directive="info")
        
        # Warning
        render_directive("Warning content", directive="warning")
        
        # Success
        render_directive("Success content", directive="success")
        
        # Tip
        render_directive("Tip content", directive="tip")
        
        # Caution
        render_directive("Caution content", directive="caution")
        
        # Important
        render_directive("Important content", directive="important")
        
        # Bug
        render_directive("Bug content", directive="bug")
        ```
	Example:
		render_directive()

	Empty or invalid:
		`render_directive()` returns `<div data-role="directive"></div>`.

    """
    return _directive_component.render(content=content, **attrs)
