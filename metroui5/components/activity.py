"""
MetroUI Activity Component
"""

from ..html import render_tag


def render_activity(**attrs):
	"""
	Renders MetroUI activity component with animated loading indicators.

	References:
		Documentation: https://v5.metroui.org.ua/components/activity/

	Args:
		**attrs: Additional HTML attributes including:
			# Activity Parameters
			- activity_deferred: Deferred initialization time in milliseconds (number)
			- type: Type of activity indicator (string) - Options: "ring", "metro", "square", "cycle", "simple", "atom", "bars"
			- style: Style of the activity indicator (string) - Options: "", "dark", "color"
			- size: Size of the activity indicator in pixels (number)
			- radius: Radius for the "simple" type activity indicator (number)
			- on_activity_create: Callback function triggered when the activity indicator is created (string)
			- cls_activity: Additional CSS class for the activity container (string)
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
