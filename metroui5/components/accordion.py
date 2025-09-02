"""
MetroUI Accordion Component
"""

from ..html import render_tag


def render_accordion(items, **attrs):
	"""
	Renders MetroUI accordion component with advanced features.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/accordion/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/accordion/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/accordion/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/accordion/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/accordion/#styling-with-css-variables>`_
	
	Args:
		items: List of dictionaries with 'title', 'content', and optional 'active' keys
		**attrs: Additional HTML attributes including:
			accordion_deferred (int): Deferred initialization time in milliseconds
			show_marker (bool): Show/hide marker (arrow) in the heading
			material (bool): Use material design style
			duration (int): Animation duration for expanding/collapsing
			one_frame (bool): Allow only one frame to be open at a time
			show_active (bool): Show active frames on initialization
			cls_frame (str): Additional CSS class for frames
			cls_heading (str): Additional CSS class for headings
			cls_content (str): Additional CSS class for content
			cls_accordion (str): Additional CSS class for the accordion container
			cls_active_frame (str): Additional CSS class for active frames
			cls_active_frame_heading (str): Additional CSS class for active frame headings
			cls_active_frame_content (str): Additional CSS class for active frame content
		
	Returns:
		str: Rendered HTML div element with accordion functionality
		
	References:
		.. _MetroUI Accordion: https://v5.metroui.org.ua/components/accordion/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	# Extract accordion-specific attributes
	accordion_attrs = {}
	standard_attrs = {}
	
	# Accordion-specific parameters
	accordion_params = [
		'accordion_deferred', 'show_marker', 'material', 'duration', 'one_frame',
		'show_active', 'cls_frame', 'cls_heading', 'cls_content', 'cls_accordion',
		'cls_active_frame', 'cls_active_frame_heading', 'cls_active_frame_content'
	]
	
	# Separate accordion attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in accordion_params:
			accordion_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "accordion"
	}
	
	# Add accordion-specific data attributes
	if accordion_attrs.get('accordion_deferred'):
		default_attrs["data-accordion-deferred"] = str(accordion_attrs['accordion_deferred'])
	
	if accordion_attrs.get('show_marker') is not None:
		default_attrs["data-show-marker"] = "true" if accordion_attrs['show_marker'] else "false"
	
	if accordion_attrs.get('material'):
		default_attrs["data-material"] = "true"
	
	if accordion_attrs.get('duration'):
		default_attrs["data-duration"] = str(accordion_attrs['duration'])
	
	if accordion_attrs.get('one_frame') is not None:
		default_attrs["data-one-frame"] = "true" if accordion_attrs['one_frame'] else "false"
	
	if accordion_attrs.get('show_active') is not None:
		default_attrs["data-show-active"] = "true" if accordion_attrs['show_active'] else "false"
	
	# Build CSS classes
	css_classes = ["accordion"]
	
	if accordion_attrs.get('material'):
		css_classes.append("material")
	
	if accordion_attrs.get('cls_accordion'):
		css_classes.append(accordion_attrs['cls_accordion'])
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	# Generate accordion frames
	accordion_items = []
	for i, item in enumerate(items):
		# Determine if this frame should be active
		is_active = item.get('active', False)
		
		# Build frame classes
		frame_classes = ["frame"]
		if is_active:
			frame_classes.append("active")
		if accordion_attrs.get('cls_frame'):
			frame_classes.append(accordion_attrs['cls_frame'])
		if is_active and accordion_attrs.get('cls_active_frame'):
			frame_classes.append(accordion_attrs['cls_active_frame'])
		
		# Build heading classes
		heading_classes = ["heading"]
		if accordion_attrs.get('cls_heading'):
			heading_classes.append(accordion_attrs['cls_heading'])
		if is_active and accordion_attrs.get('cls_active_frame_heading'):
			heading_classes.append(accordion_attrs['cls_active_frame_heading'])
		
		# Build content classes
		content_classes = ["content"]
		if accordion_attrs.get('cls_content'):
			content_classes.append(accordion_attrs['cls_content'])
		if is_active and accordion_attrs.get('cls_active_frame_content'):
			content_classes.append(accordion_attrs['cls_active_frame_content'])
		
		# Create frame HTML
		frame_html = render_tag(
			"div",
			{"class": " ".join(frame_classes)},
			render_tag("div", {"class": " ".join(heading_classes)}, item.get('title', '')) +
			render_tag("div", {"class": " ".join(content_classes)}, item.get('content', ''))
		)
		accordion_items.append(frame_html)
	
	return render_tag("div", attrs=final_attrs, content="".join(accordion_items))
