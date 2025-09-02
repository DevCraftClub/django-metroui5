"""
MetroUI Bar3d Component
"""

from ..html import render_tag


def render_bar3d(**attrs):
	"""
	Renders MetroUI bar3d component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/bar3d/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/bar3d/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/bar3d/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/bar3d/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/bar3d/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/bar3d/#styling-with-css-variables>`_
	
	Args:
		**attrs: Additional HTML attributes including:
			height (int): The height of the bar (default: 200)
			bar_color (str): The color of the growing bar (default: "#22ec1a")
			value_color (str): The color of the displayed value text (default: "#191919")
			total (int): The total value (maximum) (default: 100)
			value (int): The current value to display (default: 60)
			value_suffix (str): A suffix to append to the displayed value (e.g., "%")
			animation_duration (int): The duration of the animation in milliseconds (default: 300)
			on_bar3d_create (str): Callback function triggered when the component is created
			cls_bar3d (str): Additional CSS class for the bar3d container
		
	Returns:
		str: Rendered HTML div element with bar3d functionality
		
	References:
		.. _MetroUI Bar3d: https://v5.metroui.org.ua/components/bar3d/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	# Extract bar3d-specific attributes
	bar3d_attrs = {}
	standard_attrs = {}
	
	# Bar3d-specific parameters
	bar3d_params = [
		'height', 'bar_color', 'value_color', 'total', 'value', 'value_suffix',
		'animation_duration', 'on_bar3d_create', 'cls_bar3d'
	]
	
	# Separate bar3d attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in bar3d_params:
			bar3d_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "bar3d"
	}
	
	# Add bar3d-specific data attributes
	for param in ['height', 'bar_color', 'value_color', 'total', 'value', 'value_suffix', 'animation_duration']:
		if bar3d_attrs.get(param) is not None:
			# Convert parameter names to data attributes
			data_attr = param.replace('_', '-')
			default_attrs[f"data-{data_attr}"] = str(bar3d_attrs[param])
	
	# Add callback functions
	if bar3d_attrs.get('on_bar3d_create'):
		default_attrs["data-on-bar3d-create"] = bar3d_attrs['on_bar3d_create']
	
	# Build CSS classes
	css_classes = []
	if standard_attrs.get('class'):
		css_classes.append(standard_attrs.pop('class'))  # Remove 'class' from standard_attrs to avoid duplication
	
	if bar3d_attrs.get('cls_bar3d'):
		css_classes.append(bar3d_attrs['cls_bar3d'])
	
	if css_classes:
		default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("div", attrs=final_attrs, content="")
