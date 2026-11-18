"""
MetroUI Box Component
"""

from .base import ComplexComponent
from ..html import render_tag


class BoxComponent(ComplexComponent):
	"""
	MetroUI Box Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/box/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/box/#usage>`_
	- `Additional Configurations <https://v5.metroui.org.ua/components/box/#additional-configurations>`_
	- `CSS Variables <https://v5.metroui.org.ua/components/box/#css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/box/#available-css-classes>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="box",
			base_css_class="box",
			component_params=['cls_box']
		)
	
	def render(self, content="", title=None, secondary_title=None, **attrs):
		"""
		Renders MetroUI box component with optional title and secondary title.
		
		Args:
			content: Main content of the box
			title: Primary title for the box (optional)
			secondary_title: Secondary title for the box (optional)
			**attrs: Additional HTML attributes including:
				cls_box (str): Additional CSS class for the box container
		
		Returns:
			str: Rendered HTML div element with box functionality
			
		References:
			.. _MetroUI Box: https://v5.metroui.org.ua/components/box/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Build box content
		box_content = ""
		
		# Add primary title if provided
		if title:
			box_content += render_tag("div", {"class": "box-title"}, title)
		
		# Add main content
		if content:
			box_content += content
		
		# Add secondary title if provided
		if secondary_title:
			box_content += render_tag("div", {"class": "box-title-secondary"}, secondary_title)
		
		return render_tag("div", attrs=base_attrs, content=box_content)


# Create component instance
_box_component = BoxComponent()


def render_box(content="", title=None, secondary_title=None, **attrs):
	"""
	Renders MetroUI box component with optional title and secondary title.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/box/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/box/#usage>`_
	- `Additional Configurations <https://v5.metroui.org.ua/components/box/#additional-configurations>`_
	- `CSS Variables <https://v5.metroui.org.ua/components/box/#css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/box/#available-css-classes>`_
	
	Args:
		content: Main content of the box
		title: Primary title for the box (optional)
		secondary_title: Secondary title for the box (optional)
		**attrs: Additional HTML attributes including:
			cls_box (str): Additional CSS class for the box container
		
	Returns:
		str: Rendered HTML div element with box functionality
		
	References:
			.. _MetroUI Box: https://v5.metroui.org.ua/components/box/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_box()

	Empty or invalid:
		`render_box()` returns `<div class="box" id="box-component"></div>`.

	"""
	return _box_component.render(content, title, secondary_title, **attrs)
