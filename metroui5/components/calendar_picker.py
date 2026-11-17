"""
MetroUI Calendar Picker Component
"""

from .base import SimpleComponent


class CalendarPickerComponent(SimpleComponent):
	"""
	MetroUI Calendar Picker Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/calendar-picker/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/calendar-picker/#usage>`_
	- `Advanced Configurations <https://v5.metroui.org.ua/components/calendar-picker/#advanced-configurations>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/calendar-picker/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/calendar-picker/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/calendar-picker/#events>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="calendar_picker",
			base_css_class="",
			tag_name="input",
			component_params=[
				'label', 'value', 'calendar_picker_deferred', 'null_value', 'use_now', 'prepend',
				'dialog_mode', 'dialog_point', 'dialog_overlay', 'overlay_color', 'overlay_alpha',
				'size', 'format', 'input_format', 'clear_button', 'calendar_button_icon', 'clear_button_icon',
				'prev_month_icon', 'next_month_icon', 'prev_year_icon', 'next_year_icon',
				'copy_inline_styles', 'open_mode', 'wide', 'wide_point', 'show_time', 'outside',
				'week_start', 'events', 'initial_time', 'initial_hours', 'initial_minutes',
				'header_format', 'show_week_number', 'ripple', 'ripple_color', 'special',
				'exclude', 'min_date', 'max_date', 'years_before', 'years_after',
				'cls_calendar', 'cls_calendar_header', 'cls_calendar_content', 'cls_calendar_months',
				'cls_calendar_years', 'cls_calendar_time', 'cls_time', 'cls_time_hours',
				'cls_time_minutes', 'cls_time_button', 'cls_time_button_plus', 'cls_time_button_minus',
				'cls_today', 'cls_selected', 'cls_excluded', 'cls_overlay', 'cls_picker',
				'cls_input', 'cls_prepend', 'cls_label', 'on_day_click', 'on_calendar_picker_create',
				'on_calendar_show', 'on_calendar_hide', 'on_change', 'on_picker_change',
				'on_month_change', 'on_year_change'
			],
			data_attr_mapping={
				'label': 'data-label',
				'value': 'value',
				'calendar_picker_deferred': 'data-calendar-picker-deferred',
				'null_value': 'data-null-value',
				'use_now': 'data-use-now',
				'prepend': 'data-prepend',
				'dialog_mode': 'data-dialog-mode',
				'dialog_point': 'data-dialog-point',
				'dialog_overlay': 'data-dialog-overlay',
				'overlay_color': 'data-overlay-color',
				'overlay_alpha': 'data-overlay-alpha',
				'size': 'data-size',
				'format': 'data-format',
				'input_format': 'data-input-format',
				'clear_button': 'data-clear-button',
				'calendar_button_icon': 'data-calendar-button-icon',
				'clear_button_icon': 'data-clear-button-icon',
				'prev_month_icon': 'data-prev-month-icon',
				'next_month_icon': 'data-next-month-icon',
				'prev_year_icon': 'data-prev-year-icon',
				'next_year_icon': 'data-next-year-icon',
				'copy_inline_styles': 'data-copy-inline-styles',
				'open_mode': 'data-open-mode',
				'wide': 'data-wide',
				'wide_point': 'data-wide-point',
				'show_time': 'data-show-time',
				'outside': 'data-outside',
				'week_start': 'data-week-start',
				'events': 'data-events',
				'initial_time': 'data-initial-time',
				'initial_hours': 'data-initial-hours',
				'initial_minutes': 'data-initial-minutes',
				'header_format': 'data-header-format',
				'show_week_number': 'data-show-week-number',
				'ripple': 'data-ripple',
				'ripple_color': 'data-ripple-color',
				'special': 'data-special',
				'exclude': 'data-exclude',
				'min_date': 'data-min-date',
				'max_date': 'data-max-date',
				'years_before': 'data-years-before',
				'years_after': 'data-years-after'
			},
			default_data_attrs={"data-role": "calendar-picker", "type": "text"}
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI calendar picker component.
		
		Args:
			**attrs: HTML attributes including:
				label (str): Label text displayed above the input
				value (str): Initial date value
				calendar_picker_deferred (number): Deferred initialization delay
				null_value (bool): Allow null/empty values
				use_now (bool): Use current date as default
				prepend (str): HTML content to prepend to input
				dialog_mode (bool): Force dialog mode
				dialog_point (number): Screen width breakpoint for dialog mode
				dialog_overlay (bool): Show overlay in dialog mode
				overlay_color (str): Overlay background color
				overlay_alpha (number): Overlay transparency
				size (str): Input width
				format (str): Display date format
				input_format (str): Input parsing format
				clear_button (bool): Show clear button
				calendar_button_icon (str): Calendar button icon
				clear_button_icon (str): Clear button icon
				prev_month_icon (str): Previous month icon
				next_month_icon (str): Next month icon
				prev_year_icon (str): Previous year icon
				next_year_icon (str): Next year icon
				copy_inline_styles (bool): Copy inline styles to container
				open_mode (str): Calendar open direction ("auto", "up", "down")
				wide (bool): Use wide calendar layout
				wide_point (number): Screen width for wide layout
				show_time (bool): Enable time selection
				outside (bool): Show dates outside current month
				week_start (number): First day of week (0=Sunday, 1=Monday)
				events (array): Calendar events
				initial_time (str): Initial time value (HH:MM)
				initial_hours (number): Initial hours
				initial_minutes (number): Initial minutes
				header_format (str): Calendar header format
				show_week_number (bool): Show week numbers
				ripple (bool): Enable ripple effect
				ripple_color (str): Ripple effect color
				special (array): Special dates array
				exclude (array): Excluded dates array
				min_date (str): Minimum selectable date
				max_date (str): Maximum selectable date
				years_before (number): Years before current year
				years_after (number): Years after current year
				cls_calendar (str): Calendar container classes
				cls_calendar_header (str): Calendar header classes
				cls_calendar_content (str): Calendar content classes
				cls_calendar_months (str): Month view classes
				cls_calendar_years (str): Year view classes
				cls_calendar_time (str): Time picker classes
				cls_time (str): Time container classes
				cls_time_hours (str): Hours input classes
				cls_time_minutes (str): Minutes input classes
				cls_time_button (str): Time button classes
				cls_time_button_plus (str): Plus button classes
				cls_time_button_minus (str): Minus button classes
				cls_today (str): Today date classes
				cls_selected (str): Selected date classes
				cls_excluded (str): Excluded date classes
				cls_overlay (str): Overlay classes
				cls_picker (str): Picker container classes
				cls_input (str): Input field classes
				cls_prepend (str): Prepend content classes
				cls_label (str): Label classes
				on_day_click (str): Callback function triggered when a day is clicked
				on_calendar_picker_create (str): Callback function triggered when the calendar picker is created
				on_calendar_show (str): Callback function triggered when the calendar popup is shown
				on_calendar_hide (str): Callback function triggered when the calendar popup is hidden
				on_change (str): Callback function triggered when the selected date changes
				on_picker_change (str): Callback function triggered when the picker value changes
				on_month_change (str): Callback function triggered when the calendar month changes
				on_year_change (str): Callback function triggered when the calendar year changes
		
		Returns:
			str: Rendered HTML input element with calendar picker functionality
			
		References:
			.. _MetroUI Calendar Picker: https://v5.metroui.org.ua/components/calendar-picker/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Add calendar picker-specific data attributes
		if component_attrs.get('on_day_click'):
			data_attrs["data-on-day-click"] = component_attrs['on_day_click']
		
		if component_attrs.get('on_calendar_picker_create'):
			data_attrs["data-on-calendar-picker-create"] = component_attrs['on_calendar_picker_create']
		
		if component_attrs.get('on_calendar_show'):
			data_attrs["data-on-calendar-show"] = component_attrs['on_calendar_show']
		
		if component_attrs.get('on_calendar_hide'):
			data_attrs["data-on-calendar-hide"] = component_attrs['on_calendar_hide']
		
		if component_attrs.get('on_change'):
			data_attrs["data-on-change"] = component_attrs['on_change']
		
		if component_attrs.get('on_picker_change'):
			data_attrs["data-on-picker-change"] = component_attrs['on_picker_change']
		
		if component_attrs.get('on_month_change'):
			data_attrs["data-on-month-change"] = component_attrs['on_month_change']
		
		if component_attrs.get('on_year_change'):
			data_attrs["data-on-year-change"] = component_attrs['on_year_change']
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes) if css_classes else None,
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		# Remove None values
		final_attrs = {k: v for k, v in final_attrs.items() if v is not None}
		
		return self.render_component(self.tag_name, final_attrs, content="")


# Create component instance
_calendar_picker_component = CalendarPickerComponent()


def render_calendar_picker(**attrs):
	"""
	Renders MetroUI calendar picker component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/calendar-picker/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/calendar-picker/#usage>`_
	- `Advanced Configurations <https://v5.metroui.org.ua/components/calendar-picker/#advanced-configurations>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/calendar-picker/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/calendar-picker/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/calendar-picker/#events>`_
	
	Args:
		**attrs: HTML attributes including:
			label (str): Label text displayed above the input
			value (str): Initial date value
			calendar_picker_deferred (number): Deferred initialization delay
			null_value (bool): Allow null/empty values
			use_now (bool): Use current date as default
			prepend (str): HTML content to prepend to input
			dialog_mode (bool): Force dialog mode
			dialog_point (number): Screen width breakpoint for dialog mode
			dialog_overlay (bool): Show overlay in dialog mode
			overlay_color (str): Overlay background color
			overlay_alpha (number): Overlay transparency
			size (str): Input width
			format (str): Display date format
			input_format (str): Input parsing format
			clear_button (bool): Show clear button
			calendar_button_icon (str): Calendar button icon
			clear_button_icon (str): Clear button icon
			prev_month_icon (str): Previous month icon
			next_month_icon (str): Next month icon
			prev_year_icon (str): Previous year icon
			next_year_icon (str): Next year icon
			copy_inline_styles (bool): Copy inline styles to container
			open_mode (str): Calendar open direction ("auto", "up", "down")
			wide (bool): Use wide calendar layout
			wide_point (number): Screen width for wide layout
			show_time (bool): Enable time selection
			outside (bool): Show dates outside current month
			week_start (number): First day of week (0=Sunday, 1=Monday)
			events (array): Calendar events
			initial_time (str): Initial time value (HH:MM)
			initial_hours (number): Initial hours
			initial_minutes (number): Initial minutes
			header_format (str): Calendar header format
			show_week_number (bool): Show week numbers
			ripple (bool): Enable ripple effect
			ripple_color (str): Ripple effect color
			special (array): Special dates array
			exclude (array): Excluded dates array
			min_date (str): Minimum selectable date
			max_date (str): Maximum selectable date
			years_before (number): Years before current year
			years_after (number): Years after current year
			cls_calendar (str): Calendar container classes
			cls_calendar_header (str): Calendar header classes
			cls_calendar_content (str): Calendar content classes
			cls_calendar_months (str): Month view classes
			cls_calendar_years (str): Year view classes
			cls_calendar_time (str): Time picker classes
			cls_time (str): Time container classes
			cls_time_hours (str): Hours input classes
			cls_time_minutes (str): Minutes input classes
			cls_time_button (str): Time button classes
			cls_time_button_plus (str): Plus button classes
			cls_time_button_minus (str): Minus button classes
			cls_today (str): Today date classes
			cls_selected (str): Selected date classes
			cls_excluded (str): Excluded date classes
			cls_overlay (str): Overlay classes
			cls_picker (str): Picker container classes
			cls_input (str): Input field classes
			cls_prepend (str): Prepend content classes
			cls_label (str): Label classes
			on_day_click (str): Callback function triggered when a day is clicked
			on_calendar_picker_create (str): Callback function triggered when the calendar picker is created
			on_calendar_show (str): Callback function triggered when the calendar popup is shown
			on_calendar_hide (str): Callback function triggered when the calendar popup is hidden
			on_change (str): Callback function triggered when the selected date changes
			on_picker_change (str): Callback function triggered when the picker value changes
			on_month_change (str): Callback function triggered when the calendar month changes
			on_year_change (str): Callback function triggered when the calendar year changes
	
	Returns:
		str: Rendered HTML input element with calendar picker functionality
		
	References:
		.. _MetroUI Calendar Picker: https://v5.metroui.org.ua/components/calendar-picker/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_calendar_picker()

	Empty or invalid:
		`render_calendar_picker()` returns `<input class="" data-role="calendar-picker" type="text"></input>`.

	"""
	return _calendar_picker_component.render(**attrs)
