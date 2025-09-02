"""
MetroUI Button Component
"""

from .base import SimpleComponent


class ButtonComponent(SimpleComponent):
	"""
	MetroUI Button Component
	"""
	
	def __init__(self):
		super().__init__(
			component_name="button",
			base_css_class="button",
			tag_name="button",
			component_params=['button_type', 'size', 'outline', 'cls_button']
		)
	
	def render(self, content, button_type="default", size=None, outline=False, **attrs):
		"""
		Renders MetroUI button component.

		Args:
			content: Button text
			button_type: Button type (default, primary, secondary, success, danger, warning, info)
			size: Button size (sm, lg)
			outline: Outline style
			**attrs: Additional HTML attributes including:
				cls_button (str): Additional CSS class for the button
		"""
		# Build additional classes based on parameters
		additional_classes = []
		
		if button_type != "default":
			if outline:
				additional_classes.append(f"outline-{button_type}")
			else:
				additional_classes.append(button_type)
		
		if size:
			additional_classes.append(f"button-{size}")
		
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			"type": "button",
			**standard_attrs
		}
		
		return self.render_component(self.tag_name, final_attrs, content=content)


# Create component instance
_button_component = ButtonComponent()


def render_button(content, button_type="default", size=None, outline=False, **attrs):
	"""
	Renders MetroUI button component.

	Args:
		content: Button text
		button_type: Button type (default, primary, secondary, success, danger, warning, info)
		size: Button size (sm, lg)
		outline: Outline style
		**attrs: Additional HTML attributes including:
			cls_button (str): Additional CSS class for the button
	"""
	return _button_component.render(content, button_type, size, outline, **attrs)
