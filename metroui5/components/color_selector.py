"""
MetroUI Color Selector Component

This module provides the Color Selector component for MetroUI 5.
The Color Selector is a comprehensive color picking component that allows users to select colors
in various formats (HEX, RGB, RGBA, HSL, HSLA, HSV, CMYK). It provides a visual interface with
color maps, hue and alpha sliders, and predefined color swatches.

References:
    - `MetroUI Color Selector <https://v5.metroui.org.ua/components/color-selector/>`_
    - `MetroUI Documentation <https://v5.metroui.org.ua/>`_
"""

from .base import ComplexComponent


class ColorSelectorComponent(ComplexComponent):
	"""
	MetroUI Color Selector component for comprehensive color selection.
	
	The Color Selector is a comprehensive color picking component that allows users to select colors
	in various formats (HEX, RGB, RGBA, HSL, HSLA, HSV, CMYK). It provides a visual interface with
	color maps, hue and alpha sliders, and predefined color swatches.
	
	Features:
	- Visual color selection interface with color maps
	- Hue and alpha channel sliders
	- Predefined color swatches
	- User-defined color swatches
	- Multiple color format support (HEX, RGB, RGBA, HSL, HSLA, HSV, CMYK)
	- Controller input integration
	- Programmatic value setting
	- Event handling for color selection
	- Customizable styling and behavior
	
	References:
		- `MetroUI Color Selector <https://v5.metroui.org.ua/components/color-selector/>`_
		- `Dependencies <https://v5.metroui.org.ua/components/color-selector/#dependencies>`_
		- `Usage <https://v5.metroui.org.ua/components/color-selector/#usage>`_
		- `Plugin Parameters <https://v5.metroui.org.ua/components/color-selector/#plugin-parameters>`_
		- `API Methods <https://v5.metroui.org.ua/components/color-selector/#api-methods>`_
		- `Events <https://v5.metroui.org.ua/components/color-selector/#events>`_
		- `Styling <https://v5.metroui.org.ua/components/color-selector/#styling-with-css-variables>`_
		- `CSS Classes <https://v5.metroui.org.ua/components/color-selector/#available-css-classes>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="color-selector",
			base_css_class="",
			component_params=[
				'defaultSwatches', 'userColors', 'returnValueType', 'returnAsString',
				'showValues', 'showAsString', 'showUserColors', 'controller',
				'addUserColorTitle', 'userColorsTitle', 'hslMode', 'showAlphaChannel',
				'inputThreshold', 'initColor', 'readonlyInput', 'clsSelector',
				'clsSwatches', 'clsSwatch', 'clsValue', 'clsLabel', 'clsInput',
				'clsUserColorButton', 'clsUserColors', 'clsUserColorsTitle', 'clsUserColor',
				'onSelectColor', 'onColorSelectorCreate'
			]
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI color selector component for comprehensive color selection.

		Args:
			**attrs: HTML attributes including:
				defaultSwatches (str): Comma-separated list of default color swatches
				userColors (str): Comma-separated list of user-defined colors
				returnValueType (str): Format of the returned color value (hex, rgb, rgba, hsl, hsla, hsv, cmyk)
				returnAsString (bool): If true, returns color as a string; if false, returns a color object
				showValues (str): Comma-separated list of color formats to display
				showAsString (str): Comma-separated list of color formats to display as strings
				showUserColors (bool): If true, shows the user colors section
				controller (str): Selector for an input element to be used as a controller
				addUserColorTitle (str): Title for the "Add User Color" button
				userColorsTitle (str): Title for the user colors section
				hslMode (str): Mode for HSL values display ("percent" or numeric)
				showAlphaChannel (bool): If true, shows the alpha channel slider
				inputThreshold (int): Debounce threshold for input changes in milliseconds
				initColor (str): Initial color value
				readonlyInput (bool): If true, makes color value inputs readonly
				clsSelector (str): Additional CSS class for the selector element
				clsSwatches (str): Additional CSS class for the swatches container
				clsSwatch (str): Additional CSS class for individual swatches
				clsValue (str): Additional CSS class for color value elements
				clsLabel (str): Additional CSS class for labels
				clsInput (str): Additional CSS class for input elements
				clsUserColorButton (str): Additional CSS class for the user color button
				clsUserColors (str): Additional CSS class for the user colors container
				clsUserColorsTitle (str): Additional CSS class for the user colors title
				clsUserColor (str): Additional CSS class for user color elements
				onSelectColor (str): Callback function when a color is selected
				onColorSelectorCreate (str): Callback function when the color selector is created
				cls (str): Additional CSS classes
				id (str): ID attribute for the color selector element
		
		Returns:
			str: Rendered HTML div element with color selector functionality
			
		References:
			- `MetroUI Color Selector <https://v5.metroui.org.ua/components/color-selector/>`_
			- `Basic Usage <https://v5.metroui.org.ua/components/color-selector/#basic-usage>`_
			- `Additional Configurations <https://v5.metroui.org.ua/components/color-selector/#additional-configurations>`_
			- `With Controller Input <https://v5.metroui.org.ua/components/color-selector/#with-controller-input>`_
			- `Setting Values Programmatically <https://v5.metroui.org.ua/components/color-selector/#setting-values-programmatically>`_
			- `Plugin Parameters <https://v5.metroui.org.ua/components/color-selector/#plugin-parameters>`_
			- `API Methods <https://v5.metroui.org.ua/components/color-selector/#api-methods>`_
			- `Events <https://v5.metroui.org.ua/components/color-selector/#events>`_
			- `Styling <https://v5.metroui.org.ua/components/color-selector/#styling-with-css-variables>`_
			- `CSS Classes <https://v5.metroui.org.ua/components/color-selector/#available-css-classes>`_

		Examples:
			Basic color selector:
			.. code-block:: python
				render_color_selector()

			Color selector with alpha channel and custom swatches:
			.. code-block:: python
				render_color_selector(
					showAlphaChannel=True,
					defaultSwatches="#FF0000,#00FF00,#0000FF",
					returnValueType="rgba"
				)

			Color selector with controller input:
			.. code-block:: python
				render_color_selector(
					controller="#color-controller",
					initColor="#9c27b0"
				)

			Color selector with events:
			.. code-block:: python
				render_color_selector(
					id="my-color-selector",
					onSelectColor="handleColorSelect()",
					onColorSelectorCreate="onColorSelectorCreate()"
				)
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add color selector-specific data attributes
		base_attrs["data-role"] = "color-selector"
		
		# Add configuration parameters
		if component_attrs.get('defaultSwatches'):
			base_attrs["data-default-swatches"] = component_attrs['defaultSwatches']
		
		if component_attrs.get('userColors'):
			base_attrs["data-user-colors"] = component_attrs['userColors']
		
		if component_attrs.get('returnValueType'):
			base_attrs["data-return-value-type"] = component_attrs['returnValueType']
		
		if component_attrs.get('returnAsString') is not None:
			base_attrs["data-return-as-string"] = str(component_attrs['returnAsString']).lower()
		
		if component_attrs.get('showValues'):
			base_attrs["data-show-values"] = component_attrs['showValues']
		
		if component_attrs.get('showAsString'):
			base_attrs["data-show-as-string"] = component_attrs['showAsString']
		
		if component_attrs.get('showUserColors') is not None:
			base_attrs["data-show-user-colors"] = str(component_attrs['showUserColors']).lower()
		
		if component_attrs.get('controller'):
			base_attrs["data-controller"] = component_attrs['controller']
		
		if component_attrs.get('addUserColorTitle'):
			base_attrs["data-add-user-color-title"] = component_attrs['addUserColorTitle']
		
		if component_attrs.get('userColorsTitle'):
			base_attrs["data-user-colors-title"] = component_attrs['userColorsTitle']
		
		if component_attrs.get('hslMode'):
			base_attrs["data-hsl-mode"] = component_attrs['hslMode']
		
		if component_attrs.get('showAlphaChannel') is not None:
			base_attrs["data-show-alpha-channel"] = str(component_attrs['showAlphaChannel']).lower()
		
		if component_attrs.get('inputThreshold'):
			base_attrs["data-input-threshold"] = str(component_attrs['inputThreshold'])
		
		if component_attrs.get('initColor'):
			base_attrs["data-init-color"] = component_attrs['initColor']
		
		if component_attrs.get('readonlyInput') is not None:
			base_attrs["data-readonly-input"] = str(component_attrs['readonlyInput']).lower()
		
		# Add CSS class parameters
		if component_attrs.get('clsSelector'):
			base_attrs["data-cls-selector"] = component_attrs['clsSelector']
		
		if component_attrs.get('clsSwatches'):
			base_attrs["data-cls-swatches"] = component_attrs['clsSwatches']
		
		if component_attrs.get('clsSwatch'):
			base_attrs["data-cls-swatch"] = component_attrs['clsSwatch']
		
		if component_attrs.get('clsValue'):
			base_attrs["data-cls-value"] = component_attrs['clsValue']
		
		if component_attrs.get('clsLabel'):
			base_attrs["data-cls-label"] = component_attrs['clsLabel']
		
		if component_attrs.get('clsInput'):
			base_attrs["data-cls-input"] = component_attrs['clsInput']
		
		if component_attrs.get('clsUserColorButton'):
			base_attrs["data-cls-user-color-button"] = component_attrs['clsUserColorButton']
		
		if component_attrs.get('clsUserColors'):
			base_attrs["data-cls-user-colors"] = component_attrs['clsUserColors']
		
		if component_attrs.get('clsUserColorsTitle'):
			base_attrs["data-cls-user-colors-title"] = component_attrs['clsUserColorsTitle']
		
		if component_attrs.get('clsUserColor'):
			base_attrs["data-cls-user-color"] = component_attrs['clsUserColor']
		
		# Add callback functions if specified
		if component_attrs.get('onSelectColor'):
			base_attrs["data-on-select-color"] = component_attrs['onSelectColor']
		
		if component_attrs.get('onColorSelectorCreate'):
			base_attrs["data-on-color-selector-create"] = component_attrs['onColorSelectorCreate']
		
		return self.render_component("div", base_attrs)


# Create component instance
_color_selector_component = ColorSelectorComponent()


def render_color_selector(**attrs):
	"""
	Renders MetroUI color selector component for comprehensive color selection.

	The Color Selector is a comprehensive color picking component that allows users to select colors
	in various formats (HEX, RGB, RGBA, HSL, HSLA, HSV, CMYK). It provides a visual interface with
	color maps, hue and alpha sliders, and predefined color swatches.

	Args:
		**attrs: HTML attributes including:
			defaultSwatches (str): Comma-separated list of default color swatches
			userColors (str): Comma-separated list of user-defined colors
			returnValueType (str): Format of the returned color value (hex, rgb, rgba, hsl, hsla, hsv, cmyk)
			returnAsString (bool): If true, returns color as a string; if false, returns a color object
			showValues (str): Comma-separated list of color formats to display
			showAsString (str): Comma-separated list of color formats to display as strings
			showUserColors (bool): If true, shows the user colors section
			controller (str): Selector for an input element to be used as a controller
			addUserColorTitle (str): Title for the "Add User Color" button
			userColorsTitle (str): Title for the user colors section
			hslMode (str): Mode for HSL values display ("percent" or numeric)
			showAlphaChannel (bool): If true, shows the alpha channel slider
			inputThreshold (int): Debounce threshold for input changes in milliseconds
			initColor (str): Initial color value
			readonlyInput (bool): If true, makes color value inputs readonly
			clsSelector (str): Additional CSS class for the selector element
			clsSwatches (str): Additional CSS class for the swatches container
			clsSwatch (str): Additional CSS class for individual swatches
			clsValue (str): Additional CSS class for color value elements
			clsLabel (str): Additional CSS class for labels
			clsInput (str): Additional CSS class for input elements
			clsUserColorButton (str): Additional CSS class for the user color button
			clsUserColors (str): Additional CSS class for the user colors container
			clsUserColorsTitle (str): Additional CSS class for the user colors title
			clsUserColor (str): Additional CSS class for user color elements
			onSelectColor (str): Callback function when a color is selected
			onColorSelectorCreate (str): Callback function when the color selector is created
			cls (str): Additional CSS classes
			id (str): ID attribute for the color selector element
		
		Returns:
			str: Rendered HTML div element with color selector functionality
			
		References:
			- `MetroUI Color Selector <https://v5.metroui.org.ua/components/color-selector/>`_
			- `Basic Usage <https://v5.metroui.org.ua/components/color-selector/#basic-usage>`_
			- `Additional Configurations <https://v5.metroui.org.ua/components/color-selector/#additional-configurations>`_
			- `With Controller Input <https://v5.metroui.org.ua/components/color-selector/#with-controller-input>`_
			- `Setting Values Programmatically <https://v5.metroui.org.ua/components/color-selector/#setting-values-programmatically>`_
			- `Plugin Parameters <https://v5.metroui.org.ua/components/color-selector/#plugin-parameters>`_
			- `API Methods <https://v5.metroui.org.ua/components/color-selector/#api-methods>`_
			- `Events <https://v5.metroui.org.ua/components/color-selector/#events>`_
			- `Styling <https://v5.metroui.org.ua/components/color-selector/#styling-with-css-variables>`_
			- `CSS Classes <https://v5.metroui.org.ua/components/color-selector/#available-css-classes>`_

		Examples:
			Basic color selector:
			.. code-block:: python
				render_color_selector()

			Color selector with alpha channel and custom swatches:
			.. code-block:: python
				render_color_selector(
					showAlphaChannel=True,
					defaultSwatches="#FF0000,#00FF00,#0000FF",
					returnValueType="rgba"
				)

			Color selector with controller input:
			.. code-block:: python
				render_color_selector(
					controller="#color-controller",
					initColor="#9c27b0"
				)

			Color selector with events:
			.. code-block:: python
				render_color_selector(
					id="my-color-selector",
					onSelectColor="handleColorSelect()",
					onColorSelectorCreate="onColorSelectorCreate()"
				)
	Example:
		render_color_selector()

	Empty or invalid:
		`render_color_selector()` returns `<div class="" id="color-selector-component" data-role="color-selector"></div>`.

	"""
	return _color_selector_component.render(**attrs)
