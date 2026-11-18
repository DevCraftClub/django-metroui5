"""
MetroUI Accordion Component
"""

from .base import ComplexComponent
from ..html import render_tag


class AccordionComponent(ComplexComponent):
	"""
	MetroUI Accordion Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/accordion/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/accordion/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/accordion/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/accordion/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/accordion/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="accordion",
			base_css_class="accordion",
			component_params=[
				'accordion_deferred', 'show_marker', 'material', 'duration', 'one_frame',
				'show_active', 'cls_frame', 'cls_heading', 'cls_content', 'cls_accordion',
				'cls_active_frame', 'cls_active_frame_heading', 'cls_active_frame_content'
			]
		)
	
	def render(self, items, **attrs):
		"""
		Renders MetroUI accordion component with advanced features.
		
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
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build additional classes based on parameters
		additional_classes = []
		if component_attrs.get('material'):
			additional_classes.append("material")
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Add data-role attribute
		base_attrs["data-role"] = "accordion"
		
		# Add accordion-specific data attributes
		if component_attrs.get('accordion_deferred'):
			base_attrs["data-accordion-deferred"] = str(component_attrs['accordion_deferred'])
		
		if component_attrs.get('show_marker') is not None:
			base_attrs["data-show-marker"] = "true" if component_attrs['show_marker'] else "false"
		
		if component_attrs.get('material'):
			base_attrs["data-material"] = "true"
		
		if component_attrs.get('duration'):
			base_attrs["data-duration"] = str(component_attrs['duration'])
		
		if component_attrs.get('one_frame') is not None:
			base_attrs["data-one-frame"] = "true" if component_attrs['one_frame'] else "false"
		
		if component_attrs.get('show_active') is not None:
			base_attrs["data-show-active"] = "true" if component_attrs['show_active'] else "false"
		
		# Generate accordion frames
		accordion_items = []
		for i, item in enumerate(items):
			# Determine if this frame should be active
			is_active = item.get('active', False)
			
			# Build frame classes
			frame_classes = ["frame"]
			if is_active:
				frame_classes.append("active")
			if component_attrs.get('cls_frame'):
				frame_classes.append(component_attrs['cls_frame'])
			if is_active and component_attrs.get('cls_active_frame'):
				frame_classes.append(component_attrs['cls_active_frame'])
			
			# Build heading classes
			heading_classes = ["heading"]
			if component_attrs.get('cls_heading'):
				heading_classes.append(component_attrs['cls_heading'])
			if is_active and component_attrs.get('cls_active_frame_heading'):
				heading_classes.append(component_attrs['cls_active_frame_heading'])
			
			# Build content classes
			content_classes = ["content"]
			if component_attrs.get('cls_content'):
				content_classes.append(component_attrs['cls_content'])
			if is_active and component_attrs.get('cls_active_frame_content'):
				content_classes.append(component_attrs['cls_active_frame_content'])
			
			# Create frame HTML
			frame_html = render_tag(
				"div",
				{"class": " ".join(frame_classes)},
				render_tag("div", {"class": " ".join(heading_classes)}, item.get('title', '')) +
				render_tag("div", {"class": " ".join(content_classes)}, item.get('content', ''))
			)
			accordion_items.append(frame_html)
		
		return render_tag("div", attrs=base_attrs, content="".join(accordion_items))


# Create component instance
_accordion_component = AccordionComponent()


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

	Example:
		render_accordion([{"title": "One", "content": "Text"}])

	Empty or invalid:
		render_accordion([]) returns
		`<div class="accordion" id="accordion-component" data-role="accordion"></div>`.
		None raises TypeError. The function does not catch it.

	References:
		.. _MetroUI Accordion: https://v5.metroui.org.ua/components/accordion/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _accordion_component.render(items, **attrs)
