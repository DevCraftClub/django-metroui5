"""
MetroUI Activity Component
"""

from ..html import render_tag


def render_activity(**attrs):
	"""
	Renders MetroUI activity component with animated loading indicators.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/activity/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/activity/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/activity/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/activity/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/activity/#styling-with-css-variables>`_
	
	Args:
		**attrs: Additional HTML attributes including:
			activity_deferred (int): Deferred initialization time in milliseconds
			type (str): Type of activity indicator - Options: "ring", "metro", "square", "cycle", "simple", "atom", "bars"
			style (str): Style of the activity indicator - Options: "", "dark", "color"
			size (int): Size of the activity indicator in pixels
			radius (int): Radius for the "simple" type activity indicator
			on_activity_create (str): Callback function triggered when the activity indicator is created
			cls_activity (str): Additional CSS class for the activity container
		
	Returns:
		str: Rendered HTML div element with activity indicator functionality
		
	References:
		.. _MetroUI Activity: https://v5.metroui.org.ua/components/activity/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	# Extract activity-specific attributes
	activity_attrs = {}
	standard_attrs = {}
	
	# Activity-specific parameters
	activity_params = [
		'activity_deferred', 'type', 'style', 'size', 'radius', 
		'on_activity_create', 'cls_activity'
	]
	
	# Separate activity attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in activity_params:
			activity_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "activity"
	}
	
	# Add activity-specific data attributes
	if activity_attrs.get('activity_deferred'):
		default_attrs["data-activity-deferred"] = str(activity_attrs['activity_deferred'])
	
	if activity_attrs.get('type'):
		default_attrs["data-type"] = activity_attrs['type']
	
	if activity_attrs.get('style'):
		default_attrs["data-style"] = activity_attrs['style']
	
	if activity_attrs.get('size'):
		default_attrs["data-size"] = str(activity_attrs['size'])
	
	if activity_attrs.get('radius'):
		default_attrs["data-radius"] = str(activity_attrs['radius'])
	
	if activity_attrs.get('on_activity_create'):
		default_attrs["data-on-activity-create"] = activity_attrs['on_activity_create']
	
	# Build CSS classes
	css_classes = ["activity"]
	
	if activity_attrs.get('cls_activity'):
		css_classes.append(activity_attrs['cls_activity'])
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("div", attrs=final_attrs, close=False)
