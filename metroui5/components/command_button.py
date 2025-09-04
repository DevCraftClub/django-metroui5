"""
MetroUI Command Button Component

This module provides the Command Button component for MetroUI 5.
The Command Button component is a styled button that includes an icon and a caption
with optional description text. It's designed to provide a more visually prominent
button option with additional information.

References:
    - `MetroUI Command Button <https://v5.metroui.org.ua/components/command-button/>`_
    - `MetroUI Documentation <https://v5.metroui.org.ua/>`_
"""

from .base import ComplexComponent


class CommandButtonComponent(ComplexComponent):
	"""
	MetroUI Command Button component for styled buttons with icons and captions.
	
	The Command Button component is a styled button that includes an icon and a caption
	with optional description text. It's designed to provide a more visually prominent
	button option with additional information.
	
	Features:
	- Icon and caption display
	- Optional description text
	- Multiple color variations
	- Icon positioning (left/right)
	- Outline and shadow effects
	- Integration with ripple effects
	- Customizable styling with CSS variables
	
	References:
		- `MetroUI Command Button <https://v5.metroui.org.ua/components/command-button/>`_
		- `Dependencies <https://v5.metroui.org.ua/components/command-button/#dependencies>`_
		- `Usage <https://v5.metroui.org.ua/components/command-button/#usage>`_
		- `Structure <https://v5.metroui.org.ua/components/command-button/#structure>`_
		- `Integration <https://v5.metroui.org.ua/components/command-button/#integration-with-other-components>`_
		- `Styling <https://v5.metroui.org.ua/components/command-button/#styling-with-css-variables>`_
		- `CSS Classes <https://v5.metroui.org.ua/components/command-button/#available-css-classes>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="command-button",
			base_css_class="command-button",
			component_params=[
				'icon', 'caption', 'description', 'iconRight', 'outline', 'shadow',
				'primary', 'secondary', 'success', 'alert', 'warning', 'info',
				'dark', 'light', 'yellow', 'shift', 'ripple', 'rippleColor',
				'onClick', 'disabled', 'type'
			]
		)
	
	def render(self, icon="", caption="", description="", **attrs):
		"""
		Renders MetroUI command button component for styled buttons with icons and captions.

		Args:
			icon (str): Icon class or content for the button
			caption (str): Main caption text for the button
			description (str): Optional description text (displayed as small text)
			**attrs: HTML attributes including:
				iconRight (bool): Whether to place the icon on the right side
				outline (bool): Whether to create an outlined version
				shadow (bool): Whether to add a shadow effect
				shift (bool): Whether to add a shift effect when clicked
				primary (bool): Whether to apply primary color styling
				secondary (bool): Whether to apply secondary color styling
				success (bool): Whether to apply success color styling
				alert (bool): Whether to apply alert color styling
				warning (bool): Whether to apply warning color styling
				info (bool): Whether to apply info color styling
				dark (bool): Whether to apply dark color styling
				light (bool): Whether to apply light color styling
				yellow (bool): Whether to apply yellow color styling
				ripple (bool): Whether to add ripple effect
				rippleColor (str): Color for the ripple effect
				onClick (str): JavaScript click handler
				disabled (bool): Whether the button is disabled
				type (str): Button type (button, submit, reset)
				cls (str): Additional CSS classes
				id (str): ID attribute for the button element
				name (str): Name attribute for form submission
				value (str): Value attribute for form submission
		
		Returns:
			str: Rendered HTML button element with command button styling
			
		References:
			- `MetroUI Command Button <https://v5.metroui.org.ua/components/command-button/>`_
			- `Basic Usage <https://v5.metroui.org.ua/components/command-button/#basic-usage>`_
			- `Additional Configurations <https://v5.metroui.org.ua/components/command-button/#additional-configurations>`_
			- `Structure <https://v5.metroui.org.ua/components/command-button/#structure>`_
			- `Integration <https://v5.metroui.org.ua/components/command-button/#integration-with-other-components>`_
			- `Styling <https://v5.metroui.org.ua/components/command-button/#styling-with-css-variables>`_
			- `CSS Classes <https://v5.metroui.org.ua/components/command-button/#available-css-classes>`_

		Examples:
			Basic command button:
			.. code-block:: python
				render_command_button(icon="mif-share", caption="Share", description="Share this content")

			Command button with icon on right:
			.. code-block:: python
				render_command_button(
					icon="mif-share", 
					caption="Share", 
					description="Share this content",
					iconRight=True
				)

			Outlined command button:
			.. code-block:: python
				render_command_button(
					icon="mif-share", 
					caption="Share", 
					description="Share this content",
					outline=True
				)

			Colored command button with ripple:
			.. code-block:: python
				render_command_button(
					icon="mif-alarm", 
					caption="Alarm", 
					description="Important notification",
					alert=True,
					ripple=True,
					rippleColor="gray"
				)
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add command button-specific classes
		css_classes = [self.base_css_class]
		
		# Add modifier classes
		if component_attrs.get('iconRight'):
			css_classes.append('icon-right')
		
		if component_attrs.get('outline'):
			css_classes.append('outline')
		
		if component_attrs.get('shadow'):
			css_classes.append('shadow')
		
		if component_attrs.get('shift'):
			css_classes.append('shift')
		
		# Add color classes
		color_classes = ['primary', 'secondary', 'success', 'alert', 'warning', 'info', 'dark', 'light', 'yellow']
		for color_class in color_classes:
			if component_attrs.get(color_class):
				css_classes.append(color_class)
		
		# Update class attribute
		base_attrs['class'] = ' '.join(css_classes)
		
		# Add button-specific attributes
		if component_attrs.get('type'):
			base_attrs['type'] = component_attrs['type']
		elif 'type' not in standard_attrs:
			base_attrs['type'] = 'button'
		
		if component_attrs.get('disabled'):
			base_attrs['disabled'] = True
		
		if component_attrs.get('onClick'):
			base_attrs['onclick'] = component_attrs['onClick']
		
		# Add ripple effect if specified
		if component_attrs.get('ripple'):
			base_attrs['data-role'] = 'ripple'
			if component_attrs.get('rippleColor'):
				base_attrs['data-ripple-color'] = component_attrs['rippleColor']
		
		# Build content
		content_parts = []
		
		# Add icon
		if icon:
			icon_class = f"icon {icon}" if not icon.startswith('mif-') else f"icon {icon}"
			content_parts.append(f'<span class="{icon_class}"></span>')
		
		# Add caption
		if caption or description:
			caption_content = caption
			if description:
				caption_content += f'<small>{description}</small>'
			content_parts.append(f'<span class="caption">{caption_content}</span>')
		
		content = ''.join(content_parts)
		
		return self.render_component("button", base_attrs, content=content)


# Create component instance
_command_button_component = CommandButtonComponent()


def render_command_button(icon="", caption="", description="", **attrs):
	"""
	Renders MetroUI command button component for styled buttons with icons and captions.

	The Command Button component is a styled button that includes an icon and a caption
	with optional description text. It's designed to provide a more visually prominent
	button option with additional information.

	Args:
		icon (str): Icon class or content for the button
		caption (str): Main caption text for the button
		description (str): Optional description text (displayed as small text)
		**attrs: HTML attributes including:
			iconRight (bool): Whether to place the icon on the right side
			outline (bool): Whether to create an outlined version
			shadow (bool): Whether to add a shadow effect
			shift (bool): Whether to add a shift effect when clicked
			primary (bool): Whether to apply primary color styling
			secondary (bool): Whether to apply secondary color styling
			success (bool): Whether to apply success color styling
			alert (bool): Whether to apply alert color styling
			warning (bool): Whether to apply warning color styling
			info (bool): Whether to apply info color styling
			dark (bool): Whether to apply dark color styling
			light (bool): Whether to apply light color styling
			yellow (bool): Whether to apply yellow color styling
			ripple (bool): Whether to add ripple effect
			rippleColor (str): Color for the ripple effect
			onClick (str): JavaScript click handler
			disabled (bool): Whether the button is disabled
			type (str): Button type (button, submit, reset)
			cls (str): Additional CSS classes
			id (str): ID attribute for the button element
			name (str): Name attribute for form submission
			value (str): Value attribute for form submission
		
		Returns:
			str: Rendered HTML button element with command button styling
			
		References:
			- `MetroUI Command Button <https://v5.metroui.org.ua/components/command-button/>`_
			- `Basic Usage <https://v5.metroui.org.ua/components/command-button/#basic-usage>`_
			- `Additional Configurations <https://v5.metroui.org.ua/components/command-button/#additional-configurations>`_
			- `Structure <https://v5.metroui.org.ua/components/command-button/#structure>`_
			- `Integration <https://v5.metroui.org.ua/components/command-button/#integration-with-other-components>`_
			- `Styling <https://v5.metroui.org.ua/components/command-button/#styling-with-css-variables>`_
			- `CSS Classes <https://v5.metroui.org.ua/components/command-button/#available-css-classes>`_

		Examples:
			Basic command button:
			.. code-block:: python
				render_command_button(icon="mif-share", caption="Share", description="Share this content")

			Command button with icon on right:
			.. code-block:: python
				render_command_button(
					icon="mif-share", 
					caption="Share", 
					description="Share this content",
					iconRight=True
				)

			Outlined command button:
			.. code-block:: python
				render_command_button(
					icon="mif-share", 
					caption="Share", 
					description="Share this content",
					outline=True
				)

			Colored command button with ripple:
			.. code-block:: python
				render_command_button(
					icon="mif-alarm", 
					caption="Alarm", 
					description="Important notification",
					alert=True,
					ripple=True,
					rippleColor="gray"
				)
	"""
	return _command_button_component.render(icon=icon, caption=caption, description=description, **attrs)
