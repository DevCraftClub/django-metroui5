"""
MetroUI Badge Component
"""

from .base import SimpleComponent


class BadgeComponent(SimpleComponent):
	"""
	MetroUI Badge Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/badges/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/badges/#usage>`_
	- `CSS Variables <https://v5.metroui.org.ua/components/badges/#css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/badges/#available-css-classes>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="badge",
			base_css_class="badge",
			tag_name="span",
			component_params=['cls_badge']
		)
	
	def render(self, content, corner=False, corner_outside=False, **attrs):
		"""
		Renders MetroUI badge component.
		
		Args:
			content: Badge content/text
			corner: Position the badge in the top-right corner of a relative-positioned parent
			corner_outside: Position the badge outside the parent element in the top-right corner
			**attrs: Additional HTML attributes including:
				cls_badge (str): Additional CSS class for the badge
			
		Returns:
			str: Rendered HTML span element with badge functionality
			
		References:
			.. _MetroUI Badges: https://v5.metroui.org.ua/components/badges/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Build additional classes based on parameters
		additional_classes = []
		if corner:
			additional_classes.append("corner")
		if corner_outside:
			additional_classes.append("corner-outside")
		
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**standard_attrs
		}
		
		return self.render_component(self.tag_name, final_attrs, content=content)


# Create component instance
_badge_component = BadgeComponent()


def render_badge(content, corner=False, corner_outside=False, **attrs):
	"""
	Renders MetroUI badge component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/badges/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/badges/#usage>`_
	- `CSS Variables <https://v5.metroui.org.ua/components/badges/#css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/badges/#available-css-classes>`_
	
	Args:
		content: Badge content/text
		corner: Position the badge in the top-right corner of a relative-positioned parent
		corner_outside: Position the badge outside the parent element in the top-right corner
		**attrs: Additional HTML attributes including:
			cls_badge (str): Additional CSS class for the badge
		
	Returns:
		str: Rendered HTML span element with badge functionality
		
	References:
		.. _MetroUI Badges: https://v5.metroui.org.ua/components/badges/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_badge('Text')

	Empty or invalid:
		`render_badge('Text')` returns `<span class="badge">Text</span>`. An empty call returns `<span class="badge"></span>`.

	"""
	return _badge_component.render(content, corner, corner_outside, **attrs)
