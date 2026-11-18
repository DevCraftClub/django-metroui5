"""
MetroUI Clock Component
"""

from .base import SimpleComponent


class ClockComponent(SimpleComponent):
	"""
	MetroUI Clock Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/clock/>`_.
	
	You can also reference specific sections:
	- `Dependencies <https://v5.metroui.org.ua/components/clock/#dependencies>`_
	- `Basic Usage <https://v5.metroui.org.ua/components/clock/#basic-usage>`_
	- `Display Modes <https://v5.metroui.org.ua/components/clock/#display-modes>`_
	- `Custom Formats <https://v5.metroui.org.ua/components/clock/#custom-formats>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/clock/#plugin-parameters>`_
	- `Events <https://v5.metroui.org.ua/components/clock/#events>`_
	- `API Methods <https://v5.metroui.org.ua/components/clock/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/clock/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/clock/#available-css-classes>`_
	- `Best Practices <https://v5.metroui.org.ua/components/clock/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="clock",
			base_css_class="clock",
			tag_name="div",
			component_params=[
				'clockDeferred', 'show', 'showTime', 'showDate', 'dateFormat', 'timeFormat',
				'divider', 'twoLines', 'onTick', 'onSecond', 'onClockCreate'
			],
			data_attr_mapping={
				'clockDeferred': 'data-clock-deferred',
				'showTime': 'data-show-time',
				'showDate': 'data-show-date',
				'dateFormat': 'data-date-format',
				'timeFormat': 'data-time-format',
				'twoLines': 'data-two-lines',
				'onTick': 'data-on-tick',
				'onSecond': 'data-on-second',
				'onClockCreate': 'data-on-clock-create'
			}
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI clock component for displaying current date and time with automatic updates.

		Args:
			**attrs: HTML attributes including:
				clockDeferred (int): Delay before initialization in milliseconds
				show (str): Display mode - 'row' (horizontal) or 'column' (vertical)
				showTime (bool): Whether to display the time
				showDate (bool): Whether to display the date
				dateFormat (str): Format for displaying the date (default: 'DD.MM.YYYY')
				timeFormat (str): Format for displaying the time (default: 'HH:mm')
				divider (str): HTML content to use as divider between date and time
				twoLines (bool): Whether to display date and time on separate lines
				onTick (str): Callback function triggered every 500ms when clock updates
				onSecond (str): Callback function triggered every second
				onClockCreate (str): Callback function when clock component is created
				cls (str): Additional CSS classes
				id (str): ID attribute for the clock
		
		Returns:
			str: Rendered HTML div element with clock functionality
			
		References:
			.. _MetroUI Clock: https://v5.metroui.org.ua/components/clock/
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
		
		# Add clock-specific data attributes
		final_attrs["data-role"] = "clock"
		
		# Add display mode
		show_mode = component_attrs.get('show', 'row')
		if show_mode == 'column':
			css_classes.append('show-column')
			final_attrs["class"] = " ".join(css_classes)
		
		# Add divider if specified
		if component_attrs.get('divider'):
			final_attrs["data-divider"] = component_attrs['divider']
		
		# Render the div element
		from ..html import render_tag
		return render_tag("div", final_attrs, content="")


# Create component instance
_clock_component = ClockComponent()


def render_clock(**attrs):
	"""
	Renders MetroUI clock component for displaying current date and time with automatic updates.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/clock/>`_.
	
	You can also reference specific sections:
	- `Dependencies <https://v5.metroui.org.ua/components/clock/#dependencies>`_
	- `Basic Usage <https://v5.metroui.org.ua/components/clock/#basic-usage>`_
	- `Display Modes <https://v5.metroui.org.ua/components/clock/#display-modes>`_
	- `Custom Formats <https://v5.metroui.org.ua/components/clock/#custom-formats>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/clock/#plugin-parameters>`_
	- `Events <https://v5.metroui.org.ua/components/clock/#events>`_
	- `API Methods <https://v5.metroui.org.ua/components/clock/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/clock/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/clock/#available-css-classes>`_
	- `Best Practices <https://v5.metroui.org.ua/components/clock/#best-practices>`_

	Args:
		**attrs: HTML attributes including:
			clockDeferred (int): Delay before initialization in milliseconds
			show (str): Display mode - 'row' (horizontal) or 'column' (vertical)
			showTime (bool): Whether to display the time
			showDate (bool): Whether to display the date
			dateFormat (str): Format for displaying the date (default: 'DD.MM.YYYY')
			timeFormat (str): Format for displaying the time (default: 'HH:mm')
			divider (str): HTML content to use as divider between date and time
			twoLines (bool): Whether to display date and time on separate lines
			onTick (str): Callback function triggered every 500ms when clock updates
			onSecond (str): Callback function triggered every second
			onClockCreate (str): Callback function when clock component is created
			cls (str): Additional CSS classes
			id (str): ID attribute for the clock
		
		Returns:
			str: Rendered HTML div element with clock functionality
			
		References:
			.. _MetroUI Clock: https://v5.metroui.org.ua/components/clock/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_clock()

	Empty or invalid:
		`render_clock()` returns `<div class="clock" id="clock-component" data-role="clock"></div>`.

	"""
	return _clock_component.render(**attrs)
