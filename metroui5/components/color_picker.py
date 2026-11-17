"""
MetroUI Color Picker Component

This module provides the Color Picker component for MetroUI 5.
The Color Picker component provides an interactive interface for selecting colors.
It integrates with the Color Selector component to offer a comprehensive color selection experience.

References:
    - `MetroUI Color Picker <https://v5.metroui.org.ua/components/color-picker/>`_
    - `MetroUI Documentation <https://v5.metroui.org.ua/>`_
"""

from .base import SimpleComponent


class ColorPickerComponent(SimpleComponent):
	"""
	MetroUI Color Picker component for interactive color selection.
	
	The Color Picker component provides an interactive interface for selecting colors.
	It integrates with the Color Selector component to offer a comprehensive color selection experience
	with various formats and options.
	
	Features:
	- Interactive color selection interface
	- Multiple color format support (hex, rgb, rgba, hsl, hsla, cmyk)
	- Predefined color swatches
	- Clear button functionality
	- Customizable icons and labels
	- Programmatic value setting
	- Event handling for color selection
	
	References:
		- `MetroUI Color Picker <https://v5.metroui.org.ua/components/color-picker/>`_
		- `Dependencies <https://v5.metroui.org.ua/components/color-picker/#dependencies>`_
		- `Usage <https://v5.metroui.org.ua/components/color-picker/#usage>`_
		- `Plugin Parameters <https://v5.metroui.org.ua/components/color-picker/#plugin-parameters>`_
		- `API Methods <https://v5.metroui.org.ua/components/color-picker/#api-methods>`_
		- `Events <https://v5.metroui.org.ua/components/color-picker/#events>`_
		- `Styling <https://v5.metroui.org.ua/components/color-picker/#styling-with-css-variables>`_
		- `CSS Classes <https://v5.metroui.org.ua/components/color-picker/#available-css-classes>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="color-picker",
			base_css_class="",
			tag_name="input",
			component_params=[
				'defaultSwatches', 'duration', 'prepend', 'append', 'label',
				'clearButton', 'clearButtonIcon', 'pickerButtonIcon', 'defaultValue',
				'openMode', 'resultType', 'inputThreshold', 'showValues',
				'returnValueType', 'onColorSelected', 'onColorPickerCreate'
			],
			data_attr_mapping={
				'defaultSwatches': 'data-default-swatches',
				'duration': 'data-duration',
				'prepend': 'data-prepend',
				'append': 'data-append',
				'label': 'data-label',
				'clearButton': 'data-clear-button',
				'clearButtonIcon': 'data-clear-button-icon',
				'pickerButtonIcon': 'data-picker-button-icon',
				'defaultValue': 'data-default-value',
				'openMode': 'data-open-mode',
				'resultType': 'data-result-type',
				'inputThreshold': 'data-input-threshold',
				'showValues': 'data-show-values',
				'returnValueType': 'data-return-value-type',
				'onColorSelected': 'data-on-color-selected',
				'onColorPickerCreate': 'data-on-color-picker-create'
			},
			default_data_attrs={
				'type': 'text',
				'data-role': 'color-picker'
			}
		)


# Create component instance
_color_picker_component = ColorPickerComponent()


def render_color_picker(**attrs):
	"""
	Renders MetroUI color picker component for interactive color selection.

	The Color Picker component provides an interactive interface for selecting colors.
	It integrates with the Color Selector component to offer a comprehensive color selection experience
	with various formats and options.

	Args:
		**attrs: HTML attributes including:
			defaultSwatches (str): Comma-separated list of predefined color swatches
			duration (int): Animation duration for dropdown in milliseconds
			prepend (str): Content to prepend to the color picker
			append (str): Content to append to the color picker
			label (str): Label text for the color picker
			clearButton (bool): Whether to show a clear button
			clearButtonIcon (str): Icon for the clear button
			pickerButtonIcon (str): Icon for the color picker button
			defaultValue (str): Default color value
			openMode (str): Mode for opening the color picker dropdown (auto, click, focus)
			resultType (str): Format of the color result (hex, rgb, rgba, hsl, hsla, cmyk)
			inputThreshold (int): Threshold for input in milliseconds
			showValues (str): Comma-separated list of value formats to show
			returnValueType (str): Format of the returned value
			onColorSelected (str): Callback function when a color is selected
			onColorPickerCreate (str): Callback function when the color picker is created
			cls (str): Additional CSS classes
			id (str): ID attribute for the color picker element
			name (str): Name attribute for form submission
			value (str): Initial value of the color picker
			placeholder (str): Placeholder text
			disabled (bool): Whether the color picker is disabled
			readonly (bool): Whether the color picker is readonly
			required (bool): Whether the color picker is required
	
	Returns:
		str: Rendered HTML input element with color picker functionality
		
	References:
		- `MetroUI Color Picker <https://v5.metroui.org.ua/components/color-picker/>`_
		- `Basic Usage <https://v5.metroui.org.ua/components/color-picker/#basic-usage>`_
		- `Additional Configurations <https://v5.metroui.org.ua/components/color-picker/#additional-configurations>`_
		- `Setting Value Programmatically <https://v5.metroui.org.ua/components/color-picker/#setting-value-programmatically>`_
		- `Plugin Parameters <https://v5.metroui.org.ua/components/color-picker/#plugin-parameters>`_
		- `API Methods <https://v5.metroui.org.ua/components/color-picker/#api-methods>`_
		- `Events <https://v5.metroui.org.ua/components/color-picker/#events>`_
		- `Styling <https://v5.metroui.org.ua/components/color-picker/#styling-with-css-variables>`_
		- `CSS Classes <https://v5.metroui.org.ua/components/color-picker/#available-css-classes>`_

	Examples:
		Basic color picker:
		.. code-block:: python
			render_color_picker()

		Color picker with label and clear button:
		.. code-block:: python
			render_color_picker(
				label="Select color:",
				clearButton=True,
				clearButtonIcon="❌"
			)

		Color picker with custom swatches and result type:
		.. code-block:: python
			render_color_picker(
				defaultSwatches="#FF0000,#00FF00,#0000FF,#FFFF00,#FF00FF,#00FFFF",
				resultType="rgba",
				showValues="hex,rgb,hsl"
			)

		Color picker with events:
		.. code-block:: python
			render_color_picker(
				id="my-color-picker",
				onColorSelected="onColorSelected()",
				onColorPickerCreate="onColorPickerCreate()"
			)
	Example:
		render_color_picker()

	Empty or invalid:
		`render_color_picker()` returns `<input class="" type="text" data-role="color-picker" id="color-picker-component"></input>`.

	"""
	return _color_picker_component.render(**attrs)
