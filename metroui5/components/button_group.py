"""
MetroUI Button Group Component
"""

from .base import ComplexComponent
from ..html import render_tag


class ButtonGroupComponent(ComplexComponent):
	"""
	MetroUI Button Group Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/button-group/>`_.
	
	You can also reference specific sections:
	- `Basic Button Group <https://v5.metroui.org.ua/components/button-group/#basic-button-group>`_
	- `Single Selection Mode <https://v5.metroui.org.ua/components/button-group/#single-selection-mode-default>`_
	- `Multiple Selection Mode <https://v5.metroui.org.ua/components/button-group/#multiple-selection-mode>`_
	- `Required Button Selection <https://v5.metroui.org.ua/components/button-group/#required-button-selection>`_
	- `Custom Target Elements <https://v5.metroui.org.ua/components/button-group/#custom-target-elements>`_
	- `Custom Active Class <https://v5.metroui.org.ua/components/button-group/#custom-active-class>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/button-group/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/button-group/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/button-group/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/button-group/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="button_group",
			base_css_class="button-group",
			component_params=[
				'targets', 'cls_active', 'required_button', 'mode', 
				'onButtonClick', 'onButtonGroupCreate', 'cls_button_group'
			]
		)
	
	def render(self, buttons, mode="one", targets="button", cls_active="", 
			   required_button=False, **attrs):
		"""
		Renders MetroUI button group component with grouped buttons.
		
		Args:
			buttons: List of button configurations (dicts with 'text', 'active', 'disabled' keys or strings)
			mode: Selection mode ("one" for single selection, "multi" for multiple selection)
			targets: Selector for elements that should behave as buttons in the group
			cls_active: Additional CSS class to apply to active buttons
			required_button: Whether at least one button must be active
			**attrs: Additional HTML attributes including:
				onButtonClick (str): Event handler triggered when a button is clicked
				onButtonGroupCreate (str): Event handler triggered when the button group is created
				cls_button_group (str): Additional CSS class for the button group container
		
		Returns:
			str: Rendered HTML div element with button group functionality
			
		References:
			.. _MetroUI Button Group: https://v5.metroui.org.ua/components/button-group/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add data-role attribute
		base_attrs["data-role"] = "button-group"
		
		# Add button group-specific data attributes
		base_attrs["data-mode"] = mode
		base_attrs["data-targets"] = targets
		
		if cls_active:
			base_attrs["data-cls-active"] = cls_active
		
		if required_button:
			base_attrs["data-required-button"] = "true"
		
		# Add callback data attributes
		if component_attrs.get('onButtonClick'):
			base_attrs["data-on-button-click"] = component_attrs['onButtonClick']
		
		if component_attrs.get('onButtonGroupCreate'):
			base_attrs["data-on-button-group-create"] = component_attrs['onButtonGroupCreate']
		
		# Build button elements
		button_elements = []
		for button in buttons:
			if isinstance(button, dict):
				text = button.get('text', '')
				active = button.get('active', False)
				disabled = button.get('disabled', False)
				button_attrs = button.get('attrs', {})
				
				# Build button classes
				button_classes = []
				if active:
					button_classes.append("active")
				if cls_active and active:
					button_classes.append(cls_active)
				
				# Build button attributes
				button_attrs_dict = {
					"class": " ".join(button_classes) if button_classes else None,
					**button_attrs
				}
				
				# Remove None values
				button_attrs_dict = {k: v for k, v in button_attrs_dict.items() if v is not None}
				
				if disabled:
					button_attrs_dict["disabled"] = "disabled"
				
				button_elements.append(render_tag("button", button_attrs_dict, text))
			else:
				# Simple string button
				button_elements.append(render_tag("button", {}, str(button)))
		
		# Combine buttons
		content = "".join(button_elements)
		
		return render_tag("div", attrs=base_attrs, content=content)


# Create component instance
_button_group_component = ButtonGroupComponent()


def render_button_group(buttons, mode="one", targets="button", cls_active="", 
						required_button=False, **attrs):
	"""
	Renders MetroUI button group component with grouped buttons.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/button-group/>`_.
	
	You can also reference specific sections:
	- `Basic Button Group <https://v5.metroui.org.ua/components/button-group/#basic-button-group>`_
	- `Single Selection Mode <https://v5.metroui.org.ua/components/button-group/#single-selection-mode-default>`_
	- `Multiple Selection Mode <https://v5.metroui.org.ua/components/button-group/#multiple-selection-mode>`_
	- `Required Button Selection <https://v5.metroui.org.ua/components/button-group/#required-button-selection>`_
	- `Custom Target Elements <https://v5.metroui.org.ua/components/button-group/#custom-target-elements>`_
	- `Custom Active Class <https://v5.metroui.org.ua/components/button-group/#custom-active-class>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/button-group/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/button-group/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/button-group/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/button-group/#styling-with-css-variables>`_
	
	Args:
		buttons: List of button configurations (dicts with 'text', 'active', 'disabled' keys or strings)
		mode: Selection mode ("one" for single selection, "multi" for multiple selection)
		targets: Selector for elements that should behave as buttons in the group
		cls_active: Additional CSS class to apply to active buttons
		required_button: Whether at least one button must be active
		**attrs: Additional HTML attributes including:
			onButtonClick (str): Event handler triggered when a button is clicked
			onButtonGroupCreate (str): Event handler triggered when the button group is created
			cls_button_group (str): Additional CSS class for the button group container
		
	Returns:
		str: Rendered HTML div element with button group functionality
		
	References:
		.. _MetroUI Button Group: https://v5.metroui.org.ua/components/button-group/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_button_group(['One'])

	Empty or invalid:
		`render_button_group(['One'])` returns `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="button"><button>One</button></div>`. An empty call returns `<div class="button-group" id="button_group-component" data-role="button-group" data-mode="one" data-targets="[]"></div>`.

	"""
	return _button_group_component.render(buttons, mode, targets, cls_active, 
										 required_button, **attrs)
