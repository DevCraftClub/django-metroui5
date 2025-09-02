"""
MetroUI Analog Clock Component
"""

from ..html import render_tag


def render_analog_clock(**attrs):
	"""
	Renders MetroUI analog clock component.

	Link: https://v5.metroui.org.ua/components/analog-clock/

	Args:
		**attrs: Additional HTML attributes including:
			# Analog Clock Parameters
			- icon: Custom icon to display on the clock (HTML content) (string)
			- show_numbers: Whether to show numbers on the clock face instead of dashes (boolean)
			- show_moon: Whether to show the current moon phase (boolean)
			- show_day: Whether to show the day and month display (boolean)
			- show_digital_clock: Whether to show the digital clock (boolean)
			- time_format: Time format (12 or 24 hour) (number)
			- on_analog_clock_create: Callback function triggered when the clock is created (string)
			- cls_analog_clock: Additional CSS class for the analog clock container (string)
			- size: Size modifier (xs, sm, md, lg, xl) (string)
	"""
	# Extract analog clock-specific attributes
	clock_attrs = {}
	standard_attrs = {}
	
	# Analog clock-specific parameters
	clock_params = [
		'icon', 'show_numbers', 'show_moon', 'show_day', 'show_digital_clock',
		'time_format', 'on_analog_clock_create', 'cls_analog_clock', 'size'
	]
	
	# Separate analog clock attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in clock_params:
			clock_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "analog-clock"
	}
	
	# Add analog clock-specific data attributes
	if clock_attrs.get('icon'):
		default_attrs["data-icon"] = clock_attrs['icon']
	
	if clock_attrs.get('show_numbers') is not None:
		default_attrs["data-show-numbers"] = "true" if clock_attrs['show_numbers'] else "false"
	
	if clock_attrs.get('show_moon') is not None:
		default_attrs["data-show-moon"] = "true" if clock_attrs['show_moon'] else "false"
	
	if clock_attrs.get('show_day') is not None:
		default_attrs["data-show-day"] = "true" if clock_attrs['show_day'] else "false"
	
	if clock_attrs.get('show_digital_clock') is not None:
		default_attrs["data-show-digital-clock"] = "true" if clock_attrs['show_digital_clock'] else "false"
	
	if clock_attrs.get('time_format'):
		default_attrs["data-time-format"] = str(clock_attrs['time_format'])
	
	if clock_attrs.get('on_analog_clock_create'):
		default_attrs["data-on-analog-clock-create"] = clock_attrs['on_analog_clock_create']
	
	# Build CSS classes
	css_classes = ["analog-clock"]
	
	# Add size modifier if specified
	if clock_attrs.get('size'):
		size_class = f"size-{clock_attrs['size']}"
		css_classes.append(size_class)
	
	# Add show-numbers class if numbers are enabled
	if clock_attrs.get('show_numbers'):
		css_classes.append("show-numbers")
	
	# Add custom CSS class if specified
	if clock_attrs.get('cls_analog_clock'):
		css_classes.append(clock_attrs['cls_analog_clock'])
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("div", attrs=final_attrs, content="")
