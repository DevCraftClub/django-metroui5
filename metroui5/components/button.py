"""
MetroUI Button Component
"""

from .base import SimpleComponent


class ButtonComponent(SimpleComponent):
	"""
	MetroUI Button Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/button/>`_.
	
	You can also reference specific sections:
	- `Basic Buttons <https://v5.metroui.org.ua/components/button/#basic-buttons>`_
	- `Button Variants <https://v5.metroui.org.ua/components/button/#button-variants>`_
	- `Button Sizes <https://v5.metroui.org.ua/components/button/#button-sizes>`_
	- `Button Shapes <https://v5.metroui.org.ua/components/button/#button-shapes>`_
	- `Button States <https://v5.metroui.org.ua/components/button/#button-states>`_
	- `Button Effects <https://v5.metroui.org.ua/components/button/#button-effects>`_
	- `Color Variants <https://v5.metroui.org.ua/components/button/#color-variants>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/button/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/button/#available-css-classes>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="button",
			base_css_class="button",
			tag_name="button",
			component_params=[
				'variant', 'size', 'shape', 'color', 'outline', 'flat', 'link', 
				'shadow', 'shift', 'loading', 'disabled', 'icon', 'icon_position',
				'cls_button'
			]
		)
	
	def render(self, content="", variant="default", size="default", shape=None, color=None, 
			   outline=False, flat=False, link=False, shadow=False, shift=False, 
			   loading=False, disabled=False, icon=None, icon_position="left", **attrs):
		"""
		Renders MetroUI button component with comprehensive styling options.

		Args:
			content: Button text content
			variant: Button variant (default, flat-button, outline, link)
			size: Button size (mini, small, medium, default, large)
			shape: Button shape (pill-button, square, cycle)
			color: Button color (primary, secondary, success, warning, alert, info, or custom color)
			outline: Apply outline style (transparent background with colored border)
			flat: Apply flat style (transparent background and border)
			link: Apply link style (looks like a link)
			shadow: Apply shadow effect
			shift: Apply shift effect (moves when clicked)
			loading: Show loading state with spinner
			disabled: Disable the button
			icon: Icon class (e.g., 'mif-home', 'mif-plus')
			icon_position: Icon position ('left' or 'right')
			**attrs: Additional HTML attributes including:
				cls_button (str): Additional CSS class for the button
		
		Returns:
			str: Rendered HTML button element
			
		References:
			.. _MetroUI Button: https://v5.metroui.org.ua/components/button/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Старый вызов передаёт button_type и size="lg"/"sm".
		button_type = attrs.pop("button_type", None)
		if button_type and button_type != "default" and color in (None, "default"):
			color = button_type
		size = {"sm": "small", "lg": "large"}.get(size, size)

		# Build additional classes based on parameters
		additional_classes = []
		
		# Variant classes
		if variant == "flat-button":
			additional_classes.append("flat-button")
		elif variant == "outline":
			additional_classes.append("outline")
		elif variant == "link":
			additional_classes.append("link")
		
		# Size classes
		if size in ["mini", "small", "medium", "large"]:
			additional_classes.append(size)
		
		# Shape classes
		if shape == "pill-button":
			additional_classes.append("pill-button")
		elif shape == "square":
			additional_classes.append("square")
		elif shape == "cycle":
			additional_classes.append("cycle")
		
		# Color classes. Контур в документации — отдельный класс outline.
		if outline:
			additional_classes.append("outline")
		if color and color not in ["default"]:
			additional_classes.append(color)
		
		# Effect classes
		if shadow:
			additional_classes.append("shadow")
		if shift:
			additional_classes.append("shift")
		
		# State classes
		if loading:
			additional_classes.append("loading")
		if disabled:
			additional_classes.append("disabled")
		
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Build button content
		button_content = ""
		
		if loading:
			# Loading state with spinner
			button_content = f'<span class="loader"><span class="mif-spinner"></span></span><span class="caption">{content}</span>'
		elif icon:
			# Icon and text content
			icon_html = f'<span class="icon {icon}"></span>'
			if icon_position == "right":
				button_content = f'{content}{icon_html}'
			else:
				button_content = f'{icon_html}{content}'
		else:
			# Plain text content
			button_content = content
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			"type": "button",
			**standard_attrs
		}
		
		# Add disabled attribute if needed
		if disabled:
			final_attrs["disabled"] = "disabled"
		
		return self.render_component(self.tag_name, final_attrs, content=button_content)


# Create component instance
_button_component = ButtonComponent()


def render_button(content="", variant="default", size="default", shape=None, color=None, 
				  outline=False, flat=False, link=False, shadow=False, shift=False, 
				  loading=False, disabled=False, icon=None, icon_position="left", **attrs):
	"""
	Renders MetroUI button component with comprehensive styling options.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/button/>`_.
	
	You can also reference specific sections:
	- `Basic Buttons <https://v5.metroui.org.ua/components/button/#basic-buttons>`_
	- `Button Variants <https://v5.metroui.org.ua/components/button/#button-variants>`_
	- `Button Sizes <https://v5.metroui.org.ua/components/button/#button-sizes>`_
	- `Button Shapes <https://v5.metroui.org.ua/components/button/#button-shapes>`_
	- `Button States <https://v5.metroui.org.ua/components/button/#button-states>`_
	- `Button Effects <https://v5.metroui.org.ua/components/button/#button-effects>`_
	- `Color Variants <https://v5.metroui.org.ua/components/button/#color-variants>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/button/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/button/#available-css-classes>`_

	Args:
		content: Button text content
		variant: Button variant (default, flat-button, outline, link)
		size: Button size (mini, small, medium, default, large)
		shape: Button shape (pill-button, square, cycle)
		color: Button color (primary, secondary, success, warning, alert, info, or custom color)
		outline: Apply outline style (transparent background with colored border)
		flat: Apply flat style (transparent background and border)
		link: Apply link style (looks like a link)
		shadow: Apply shadow effect
		shift: Apply shift effect (moves when clicked)
		loading: Show loading state with spinner
		disabled: Disable the button
		icon: Icon class (e.g., 'mif-home', 'mif-plus')
		icon_position: Icon position ('left' or 'right')
		**attrs: Additional HTML attributes including:
			cls_button (str): Additional CSS class for the button
		
	Returns:
		str: Rendered HTML button element
		
	References:
		.. _MetroUI Button: https://v5.metroui.org.ua/components/button/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_button()

	Empty or invalid:
		`render_button()` returns `<button class="button" type="button"></button>`.

	"""
	return _button_component.render(content, variant, size, shape, color, outline, flat, 
								   link, shadow, shift, loading, disabled, icon, icon_position, **attrs)
