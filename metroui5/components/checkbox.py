"""
MetroUI Checkbox Component
"""

from .base import SimpleComponent


class CheckboxComponent(SimpleComponent):
	"""
	MetroUI Checkbox Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/checkbox/>`_.
	
	You can also reference specific sections:
	- `Dependencies <https://v5.metroui.org.ua/components/checkbox/#dependencies>`_
	- `Basic Usage <https://v5.metroui.org.ua/components/checkbox/#basic-usage>`_
	- `Checkbox Caption <https://v5.metroui.org.ua/components/checkbox/#checkbox-caption>`_
	- `Checked State <https://v5.metroui.org.ua/components/checkbox/#checked-state>`_
	- `Disabled State <https://v5.metroui.org.ua/components/checkbox/#disabled-state>`_
	- `Three-State Checkbox <https://v5.metroui.org.ua/components/checkbox/#three-state-checkbox>`_
	- `With Prepend and Append <https://v5.metroui.org.ua/components/checkbox/#with-prepend-and-append>`_
	- `With Custom Classes <https://v5.metroui.org.ua/components/checkbox/#with-custom-classes>`_
	- `Custom Styling with CSS Variables <https://v5.metroui.org.ua/components/checkbox/#custom-styling-with-css-variables>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/checkbox/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/checkbox/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/checkbox/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/checkbox/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/checkbox/#available-css-classes>`_
	- `Accessibility <https://v5.metroui.org.ua/components/checkbox/#accessibility>`_
	- `Best Practices <https://v5.metroui.org.ua/components/checkbox/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="checkbox",
			base_css_class="",
			tag_name="input",
			component_params=[
				'checkboxDeferred', 'state', 'threeState', 'prepend', 'append', 'caption',
				'clsCheckbox', 'clsCaption', 'clsPrepend', 'clsAppend', 'onCheckboxCreate'
			],
			data_attr_mapping={
				'threeState': 'data-three-state',
				'clsCheckbox': 'data-cls-checkbox',
				'clsCaption': 'data-cls-caption',
				'clsPrepend': 'data-cls-prepend',
				'clsAppend': 'data-cls-append',
				'checkboxDeferred': 'data-checkbox-deferred',
				'onCheckboxCreate': 'data-on-checkbox-create'
			}
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI checkbox component for customizable checkbox input.

		Args:
			**attrs: HTML attributes including:
				checkboxDeferred (int): Delay for initialization in milliseconds
				state (int/str): Initial state (-1/unchecked, 0/indeterminate, 1/checked)
				threeState (bool): Whether the checkbox supports three states
				prepend (str): Content to prepend to the checkbox
				append (str): Content to append to the checkbox
				caption (str): Caption for the checkbox (alternative to append)
				clsCheckbox (str): Additional CSS class for the checkbox container
				clsCaption (str): Additional CSS class for the caption
				clsPrepend (str): Additional CSS class for prepended content
				clsAppend (str): Additional CSS class for appended content
				onCheckboxCreate (str): Callback function when checkbox is created
				checked (bool): Whether the checkbox is checked
				disabled (bool): Whether the checkbox is disabled
				name (str): Name attribute for the checkbox
				value (str): Value attribute for the checkbox
				id (str): ID attribute for the checkbox
		
		Returns:
			str: Rendered HTML input element with checkbox functionality
			
		References:
			.. _MetroUI Checkbox: https://v5.metroui.org.ua/components/checkbox/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Build ID attribute
		id_attr = self.build_id_attribute(component_attrs, standard_attrs)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		# Add ID if generated or provided
		if id_attr:
			final_attrs["id"] = id_attr
		
		# Set input type
		final_attrs["type"] = "checkbox"
		
		# Add checkbox-specific data attributes
		final_attrs["data-role"] = "checkbox"
		
		# Add configuration parameters
		if component_attrs.get('state') is not None:
			final_attrs["data-state"] = str(component_attrs['state'])
		
		if component_attrs.get('prepend'):
			final_attrs["data-prepend"] = component_attrs['prepend']
		
		if component_attrs.get('append'):
			final_attrs["data-append"] = component_attrs['append']
		
		if component_attrs.get('caption'):
			final_attrs["data-caption"] = component_attrs['caption']
		
		# Handle checked state
		if standard_attrs.get('checked') or component_attrs.get('checked'):
			final_attrs["checked"] = "checked"
		
		# Handle disabled state
		if standard_attrs.get('disabled') or component_attrs.get('disabled'):
			final_attrs["disabled"] = "disabled"
		
		# Render the input element
		from ..html import render_tag
		return render_tag("input", final_attrs, content="", close=False)


# Create component instance
_checkbox_component = CheckboxComponent()


def render_checkbox(**attrs):
	"""
	Renders MetroUI checkbox component for customizable checkbox input.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/checkbox/>`_.
	
	You can also reference specific sections:
	- `Dependencies <https://v5.metroui.org.ua/components/checkbox/#dependencies>`_
	- `Basic Usage <https://v5.metroui.org.ua/components/checkbox/#basic-usage>`_
	- `Checkbox Caption <https://v5.metroui.org.ua/components/checkbox/#checkbox-caption>`_
	- `Checked State <https://v5.metroui.org.ua/components/checkbox/#checked-state>`_
	- `Disabled State <https://v5.metroui.org.ua/components/checkbox/#disabled-state>`_
	- `Three-State Checkbox <https://v5.metroui.org.ua/components/checkbox/#three-state-checkbox>`_
	- `With Prepend and Append <https://v5.metroui.org.ua/components/checkbox/#with-prepend-and-append>`_
	- `With Custom Classes <https://v5.metroui.org.ua/components/checkbox/#with-custom-classes>`_
	- `Custom Styling with CSS Variables <https://v5.metroui.org.ua/components/checkbox/#custom-styling-with-css-variables>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/checkbox/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/checkbox/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/checkbox/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/checkbox/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/checkbox/#available-css-classes>`_
	- `Accessibility <https://v5.metroui.org.ua/components/checkbox/#accessibility>`_
	- `Best Practices <https://v5.metroui.org.ua/components/checkbox/#best-practices>`_

	Args:
		**attrs: HTML attributes including:
			checkboxDeferred (int): Delay for initialization in milliseconds
			state (int/str): Initial state (-1/unchecked, 0/indeterminate, 1/checked)
			threeState (bool): Whether the checkbox supports three states
			prepend (str): Content to prepend to the checkbox
			append (str): Content to append to the checkbox
			caption (str): Caption for the checkbox (alternative to append)
			clsCheckbox (str): Additional CSS class for the checkbox container
			clsCaption (str): Additional CSS class for the caption
			clsPrepend (str): Additional CSS class for prepended content
			clsAppend (str): Additional CSS class for appended content
			onCheckboxCreate (str): Callback function when checkbox is created
			checked (bool): Whether the checkbox is checked
			disabled (bool): Whether the checkbox is disabled
			name (str): Name attribute for the checkbox
			value (str): Value attribute for the checkbox
			id (str): ID attribute for the checkbox
		
		Returns:
			str: Rendered HTML input element with checkbox functionality
			
		References:
			.. _MetroUI Checkbox: https://v5.metroui.org.ua/components/checkbox/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_checkbox()

	Empty or invalid:
		`render_checkbox()` returns `<input class="" id="checkbox-component" type="checkbox" data-role="checkbox">`.

	"""
	return _checkbox_component.render(**attrs)
