"""
MetroUI Analog Clock Component
"""

from .base import SimpleComponent


class AnalogClockComponent(SimpleComponent):
	"""
	MetroUI Analog Clock Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/analog-clock/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/analog-clock/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/analog-clock/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/analog-clock/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/analog-clock/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="analog_clock",
			base_css_class="analog-clock",
			tag_name="div",
			component_params=[
				'icon', 'show_numbers', 'show_moon', 'show_day', 'show_digital_clock',
				'time_format', 'on_analog_clock_create', 'cls_analog_clock', 'size'
			],
			data_attr_mapping={
				'icon': 'data-icon',
				'show_numbers': 'data-show-numbers',
				'show_moon': 'data-show-moon',
				'show_day': 'data-show-day',
				'show_digital_clock': 'data-show-digital-clock',
				'time_format': 'data-time-format'
			},
			default_data_attrs={"data-role": "analog-clock"}
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI analog clock component.
		
		Args:
			**attrs: Additional HTML attributes including:
				icon (str): Custom icon to display on the clock (HTML content)
				show_numbers (bool): Whether to show numbers on the clock face instead of dashes
				show_moon (bool): Whether to show the current moon phase
				show_day (bool): Whether to show the day and month display
				show_digital_clock (bool): Whether to show the digital clock
				time_format (int): Time format (12 or 24 hour)
				on_analog_clock_create (str): Callback function triggered when the clock is created
				cls_analog_clock (str): Additional CSS class for the analog clock container
				size (str): Size modifier (xs, sm, md, lg, xl)
			
		Returns:
			str: Rendered HTML div element with analog clock functionality
			
		References:
			.. _MetroUI Analog Clock: https://v5.metroui.org.ua/components/analog-clock/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build additional classes based on parameters
		additional_classes = []
		
		# Add size modifier if specified
		if component_attrs.get('size'):
			additional_classes.append(f"size-{component_attrs['size']}")
		
		# Add show-numbers class if numbers are enabled
		if component_attrs.get('show_numbers'):
			additional_classes.append("show-numbers")
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Add analog clock-specific data attributes
		if component_attrs.get('on_analog_clock_create'):
			data_attrs["data-on-analog-clock-create"] = component_attrs['on_analog_clock_create']
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		return self.render_component(self.tag_name, final_attrs, content="")


# Create component instance
_analog_clock_component = AnalogClockComponent()


def render_analog_clock(**attrs):
	"""
	Renders MetroUI analog clock component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/analog-clock/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/analog-clock/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/analog-clock/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/analog-clock/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/analog-clock/#styling-with-css-variables>`_
	
	Args:
		**attrs: Additional HTML attributes including:
			icon (str): Custom icon to display on the clock (HTML content)
			show_numbers (bool): Whether to show numbers on the clock face instead of dashes
			show_moon (bool): Whether to show the current moon phase
			show_day (bool): Whether to show the day and month display
			show_digital_clock (bool): Whether to show the digital clock
			time_format (int): Time format (12 or 24 hour)
			on_analog_clock_create (str): Callback function triggered when the clock is created
			cls_analog_clock (str): Additional CSS class for the analog clock container
			size (str): Size modifier (xs, sm, md, lg, xl)
		
	Returns:
		str: Rendered HTML div element with analog clock functionality
		
	References:
		.. _MetroUI Analog Clock: https://v5.metroui.org.ua/components/analog-clock/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_analog_clock()

	Empty or invalid:
		`render_analog_clock()` returns `<div class="analog-clock" data-role="analog-clock"></div>`.

	"""
	return _analog_clock_component.render(**attrs)
