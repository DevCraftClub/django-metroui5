"""
MetroUI Calendar Component
"""

from .base import SimpleComponent
from ..html import render_tag


class CalendarComponent(SimpleComponent):
	"""
	MetroUI Calendar Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/calendar/>`_.
	
	You can also reference specific sections:
	- `Basic Calendar <https://v5.metroui.org.ua/components/calendar/#basic-calendar>`_
	- `Calendar Modes <https://v5.metroui.org.ua/components/calendar/#calendar-modes>`_
	- `Calendar with Time Selection <https://v5.metroui.org.ua/components/calendar/#calendar-with-time-selection>`_
	- `Calendar with Date Constraints <https://v5.metroui.org.ua/components/calendar/#calendar-with-date-constraints>`_
	- `Calendar with Events <https://v5.metroui.org.ua/components/calendar/#calendar-with-events>`_
	- `Calendar with Multiple Date Selection <https://v5.metroui.org.ua/components/calendar/#calendar-with-multiple-date-selection>`_
	- `Plugin Options <https://v5.metroui.org.ua/components/calendar/#plugin-options>`_
	- `API Methods <https://v5.metroui.org.ua/components/calendar/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/calendar/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/calendar/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="calendar",
			base_css_class="calendar",
			tag_name="div",
			component_params=[
				'week_start', 'static', 'readonly', 'show_ghost', 'events', 'show_time', 
				'initial_time', 'compact', 'wide', 'picker_mode', 'day_border', 'ripple', 
				'ripple_color', 'exclude', 'preset', 'min_date', 'max_date', 'week_day_click', 
				'week_number_click', 'multi_select', 'special', 'format', 'input_format',
				'onCancel', 'onToday', 'onClear', 'onDone', 'onDayClick', 'onDrawDay', 
				'onDrawMonth', 'onDrawYear', 'onWeekDayClick', 'onWeekNumberClick', 
				'onMonthChange', 'onYearChange', 'onTimeChange', 'onHoursChange', 
				'onMinutesChange', 'onCalendarCreate', 'cls_calendar'
			]
		)
	
	def render(self, show=None, **attrs):
		"""
		Renders MetroUI calendar component with comprehensive date management features.

		Args:
			show: Date to show in calendar (string or object)
			**attrs: Additional HTML attributes including:
				week_start (int): First day of week (0 for Sunday, 1 for Monday, etc.)
				static (bool): If true, calendar becomes non-interactive
				readonly (bool): If true, calendar is read-only
				show_ghost (bool): If true, shows ghost days from previous/next months
				events (str/list): Array or comma-separated string of dates with events
				show_time (bool): If true, enables time selection
				initial_time (str): Initial time in "HH:MM" format
				compact (bool): If true, shows compact calendar
				wide (bool): If true, shows wide calendar
				picker_mode (bool): If true, enables picker mode for date selection
				day_border (bool): If true, shows day borders
				ripple (bool): If true, enables ripple effect
				ripple_color (str): Color for ripple effect
				exclude (str/list): Array or comma-separated string of dates to exclude
				preset (str/list): Array or comma-separated string of preset selected dates
				min_date (str): Minimum selectable date
				max_date (str): Maximum selectable date
				week_day_click (bool): If true, enables clicking on week days
				week_number_click (bool): If true, enables clicking on week numbers
				multi_select (bool): If true, enables multiple date selection
				special (str/list): Array or comma-separated string of special dates
				format (str): Format for date output
				input_format (str): Format for date input
				onCancel (str): Callback when cancel button is clicked
				onToday (str): Callback when today button is clicked
				onClear (str): Callback when clear button is clicked
				onDone (str): Callback when done button is clicked
				onDayClick (str): Callback when a day is clicked
				onDrawDay (str): Callback when a day is drawn
				onDrawMonth (str): Callback when a month is drawn
				onDrawYear (str): Callback when a year is drawn
				onWeekDayClick (str): Callback when a week day is clicked
				onWeekNumberClick (str): Callback when a week number is clicked
				onMonthChange (str): Callback when month is changed
				onYearChange (str): Callback when year is changed
				onTimeChange (str): Callback when time is changed
				onHoursChange (str): Callback when hours are changed
				onMinutesChange (str): Callback when minutes are changed
				onCalendarCreate (str): Callback when calendar is created
				cls_calendar (str): Additional CSS class for the calendar container
		
		Returns:
			str: Rendered HTML div element with calendar functionality
			
		References:
			.. _MetroUI Calendar: https://v5.metroui.org.ua/components/calendar/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs)
		
		# Add calendar-specific data attributes
		data_attrs["data-role"] = "calendar"
		
		# Add show date if provided
		if show:
			data_attrs["data-show"] = str(show)
		
		# Add calendar-specific data attributes
		if component_attrs.get('week_start') is not None:
			data_attrs["data-week-start"] = str(component_attrs['week_start'])
		
		if component_attrs.get('static'):
			data_attrs["data-static"] = "true"
		
		if component_attrs.get('readonly'):
			data_attrs["data-readonly"] = "true"
		
		if component_attrs.get('show_ghost'):
			data_attrs["data-show-ghost"] = "true"
		
		if component_attrs.get('events'):
			events = component_attrs['events']
			if isinstance(events, list):
				events = ",".join(events)
			data_attrs["data-events"] = events
		
		if component_attrs.get('show_time'):
			data_attrs["data-show-time"] = "true"
		
		if component_attrs.get('initial_time'):
			data_attrs["data-initial-time"] = component_attrs['initial_time']
		
		if component_attrs.get('compact'):
			data_attrs["data-compact"] = "true"
		
		if component_attrs.get('wide'):
			data_attrs["data-wide"] = "true"
		
		if component_attrs.get('picker_mode'):
			data_attrs["data-picker-mode"] = "true"
		
		if component_attrs.get('day_border'):
			data_attrs["data-day-border"] = "true"
		
		if component_attrs.get('ripple'):
			data_attrs["data-ripple"] = "true"
		
		if component_attrs.get('ripple_color'):
			data_attrs["data-ripple-color"] = component_attrs['ripple_color']
		
		if component_attrs.get('exclude'):
			exclude = component_attrs['exclude']
			if isinstance(exclude, list):
				exclude = ",".join(exclude)
			data_attrs["data-exclude"] = exclude
		
		if component_attrs.get('preset'):
			preset = component_attrs['preset']
			if isinstance(preset, list):
				preset = ",".join(preset)
			data_attrs["data-preset"] = preset
		
		if component_attrs.get('min_date'):
			data_attrs["data-min-date"] = component_attrs['min_date']
		
		if component_attrs.get('max_date'):
			data_attrs["data-max-date"] = component_attrs['max_date']
		
		if component_attrs.get('week_day_click'):
			data_attrs["data-week-day-click"] = "true"
		
		if component_attrs.get('week_number_click'):
			data_attrs["data-week-number-click"] = "true"
		
		if component_attrs.get('multi_select'):
			data_attrs["data-multi-select"] = "true"
		
		if component_attrs.get('special'):
			special = component_attrs['special']
			if isinstance(special, list):
				special = ",".join(special)
			data_attrs["data-special"] = special
		
		if component_attrs.get('format'):
			data_attrs["data-format"] = component_attrs['format']
		
		if component_attrs.get('input_format'):
			data_attrs["data-input-format"] = component_attrs['input_format']
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**data_attrs,
			**standard_attrs
		}
		
		return self.render_component(self.tag_name, final_attrs, content="")


# Create component instance
_calendar_component = CalendarComponent()


def render_calendar(show=None, **attrs):
	"""
	Renders MetroUI calendar component with comprehensive date management features.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/calendar/>`_.
	
	You can also reference specific sections:
	- `Basic Calendar <https://v5.metroui.org.ua/components/calendar/#basic-calendar>`_
	- `Calendar Modes <https://v5.metroui.org.ua/components/calendar/#calendar-modes>`_
	- `Calendar with Time Selection <https://v5.metroui.org.ua/components/calendar/#calendar-with-time-selection>`_
	- `Calendar with Date Constraints <https://v5.metroui.org.ua/components/calendar/#calendar-with-date-constraints>`_
	- `Calendar with Events <https://v5.metroui.org.ua/components/calendar/#calendar-with-events>`_
	- `Calendar with Multiple Date Selection <https://v5.metroui.org.ua/components/calendar/#calendar-with-multiple-date-selection>`_
	- `Plugin Options <https://v5.metroui.org.ua/components/calendar/#plugin-options>`_
	- `API Methods <https://v5.metroui.org.ua/components/calendar/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/calendar/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/calendar/#styling-with-css-variables>`_

	Args:
		show: Date to show in calendar (string or object)
		**attrs: Additional HTML attributes including:
			week_start (int): First day of week (0 for Sunday, 1 for Monday, etc.)
			static (bool): If true, calendar becomes non-interactive
			readonly (bool): If true, calendar is read-only
			show_ghost (bool): If true, shows ghost days from previous/next months
			events (str/list): Array or comma-separated string of dates with events
			show_time (bool): If true, enables time selection
			initial_time (str): Initial time in "HH:MM" format
			compact (bool): If true, shows compact calendar
			wide (bool): If true, shows wide calendar
			picker_mode (bool): If true, enables picker mode for date selection
			day_border (bool): If true, shows day borders
			ripple (bool): If true, enables ripple effect
			ripple_color (str): Color for ripple effect
			exclude (str/list): Array or comma-separated string of dates to exclude
			preset (str/list): Array or comma-separated string of preset selected dates
			min_date (str): Minimum selectable date
			max_date (str): Maximum selectable date
			week_day_click (bool): If true, enables clicking on week days
			week_number_click (bool): If true, enables clicking on week numbers
			multi_select (bool): If true, enables multiple date selection
			special (str/list): Array or comma-separated string of special dates
			format (str): Format for date output
			input_format (str): Format for date input
			onCancel (str): Callback when cancel button is clicked
			onToday (str): Callback when today button is clicked
			onClear (str): Callback when clear button is clicked
			onDone (str): Callback when done button is clicked
			onDayClick (str): Callback when a day is clicked
			onDrawDay (str): Callback when a day is drawn
			onDrawMonth (str): Callback when a month is drawn
			onDrawYear (str): Callback when a year is drawn
			onWeekDayClick (str): Callback when a week day is clicked
			onWeekNumberClick (str): Callback when a week number is clicked
			onMonthChange (str): Callback when month is changed
			onYearChange (str): Callback when year is changed
			onTimeChange (str): Callback when time is changed
			onHoursChange (str): Callback when hours are changed
			onMinutesChange (str): Callback when minutes are changed
			onCalendarCreate (str): Callback when calendar is created
			cls_calendar (str): Additional CSS class for the calendar container
		
		Returns:
			str: Rendered HTML div element with calendar functionality
			
		References:
			.. _MetroUI Calendar: https://v5.metroui.org.ua/components/calendar/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _calendar_component.render(show, **attrs)