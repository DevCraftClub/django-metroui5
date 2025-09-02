"""
MetroUI Breadcrumb Component
"""

from .base import ComplexComponent
from ..html import render_tag


class BreadcrumbComponent(ComplexComponent):
	"""
	MetroUI Breadcrumb Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/breadcrumbs/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/breadcrumbs/#usage>`_
	- `Additional Configurations <https://v5.metroui.org.ua/components/breadcrumbs/#additional-configurations>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/breadcrumbs/#available-css-classes>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/breadcrumbs/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="breadcrumb",
			base_css_class="breadcrumbs",
			component_params=['arrow', 'cls_breadcrumb']
		)
	
	def render(self, items, **attrs):
		"""
		Renders MetroUI breadcrumb component with navigation hierarchy.
		
		Args:
			items: List of breadcrumb items (dicts with 'text', 'href', 'icon' keys or strings)
			**attrs: Additional HTML attributes including:
				arrow (bool): Use arrow style breadcrumbs with automatic counters
				cls_breadcrumb (str): Additional CSS class for the breadcrumb container
		
		Returns:
			str: Rendered HTML ul element with breadcrumb functionality
			
		References:
			.. _MetroUI Breadcrumbs: https://v5.metroui.org.ua/components/breadcrumbs/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build additional classes based on parameters
		additional_classes = []
		if component_attrs.get('arrow'):
			additional_classes.append("arrow")
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Build breadcrumb items
		breadcrumb_items = []
		for i, item in enumerate(items):
			is_last = i == len(items) - 1
			
			if isinstance(item, dict):
				text = item.get('text', '')
				href = item.get('href', '#')
				icon = item.get('icon', '')
				divider = item.get('divider', '')
				
				# Build item content
				item_content = ""
				if icon:
					item_content += render_tag("span", {"class": f"icon {icon}"})
				if text:
					if icon:
						item_content += text
					else:
						item_content = text
				
				# Build item attributes
				item_attrs = {}
				if divider:
					item_attrs["data-divider"] = divider
				
				if is_last:
					# Last item (active)
					item_attrs["class"] = "active"
					if href and href != '#':
						breadcrumb_items.append(render_tag("li", item_attrs, render_tag("a", {"href": href}, item_content)))
					else:
						breadcrumb_items.append(render_tag("li", item_attrs, item_content))
				else:
					# Regular item with link
					breadcrumb_items.append(render_tag("li", item_attrs, render_tag("a", {"href": href}, item_content)))
			else:
				# Simple string item
				item_attrs = {}
				if is_last:
					item_attrs["class"] = "active"
					breadcrumb_items.append(render_tag("li", item_attrs, str(item)))
				else:
					breadcrumb_items.append(render_tag("li", item_attrs, render_tag("a", {"href": "#"}, str(item))))

		return render_tag("ul", attrs=base_attrs, content="".join(breadcrumb_items))


# Create component instance
_breadcrumb_component = BreadcrumbComponent()


def render_breadcrumb(items, **attrs):
	"""
	Renders MetroUI breadcrumb component with navigation hierarchy.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/breadcrumbs/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/breadcrumbs/#usage>`_
	- `Additional Configurations <https://v5.metroui.org.ua/components/breadcrumbs/#additional-configurations>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/breadcrumbs/#available-css-classes>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/breadcrumbs/#styling-with-css-variables>`_
	
	Args:
		items: List of breadcrumb items (dicts with 'text', 'href', 'icon' keys or strings)
		**attrs: Additional HTML attributes including:
			arrow (bool): Use arrow style breadcrumbs with automatic counters
			cls_breadcrumb (str): Additional CSS class for the breadcrumb container
		
	Returns:
		str: Rendered HTML ul element with breadcrumb functionality
		
	References:
		.. _MetroUI Breadcrumbs: https://v5.metroui.org.ua/components/breadcrumbs/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _breadcrumb_component.render(items, **attrs)
