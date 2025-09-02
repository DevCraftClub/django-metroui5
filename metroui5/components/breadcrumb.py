"""
MetroUI Breadcrumb Component
"""

from .base import ComplexComponent
from ..html import render_tag


class BreadcrumbComponent(ComplexComponent):
	"""
	MetroUI Breadcrumb Component
	"""
	
	def __init__(self):
		super().__init__(
			component_name="breadcrumb",
			base_css_class="breadcrumb",
			component_params=['cls_breadcrumb']
		)
	
	def render(self, items, **attrs):
		"""
		Renders MetroUI breadcrumb component.

		Args:
			items: List of breadcrumb items
			**attrs: Additional HTML attributes including:
				cls_breadcrumb (str): Additional CSS class for the breadcrumb container
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add data-role attribute
		base_attrs["data-role"] = "breadcrumb"
		
		# Build breadcrumb items
		breadcrumb_items = []
		for i, item in enumerate(items):
			if isinstance(item, dict):
				text = item.get('text', '')
				href = item.get('href', '#')
				if i == len(items) - 1:  # Last item
					breadcrumb_items.append(render_tag("li", {"class": "active"}, text))
				else:
					breadcrumb_items.append(render_tag("li", {}, render_tag("a", {"href": href}, text)))
			else:
				if i == len(items) - 1:  # Last item
					breadcrumb_items.append(render_tag("li", {"class": "active"}, str(item)))
				else:
					breadcrumb_items.append(render_tag("li", {}, render_tag("a", {"href": "#"}, str(item))))

		return render_tag("ul", attrs=base_attrs, content="".join(breadcrumb_items))


# Create component instance
_breadcrumb_component = BreadcrumbComponent()


def render_breadcrumb(items, **attrs):
	"""
	Renders MetroUI breadcrumb component.

	Args:
		items: List of breadcrumb items
		**attrs: Additional HTML attributes including:
			cls_breadcrumb (str): Additional CSS class for the breadcrumb container
	"""
	return _breadcrumb_component.render(items, **attrs)
