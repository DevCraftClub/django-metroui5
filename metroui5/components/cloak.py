"""
MetroUI Cloak Component
"""

from .base import SimpleComponent


class CloakComponent(SimpleComponent):
	"""
	MetroUI Cloak Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/cloak/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/cloak/#basic-usage>`_
	- `Revealing Cloaked Elements <https://v5.metroui.org.ua/components/cloak/#revealing-cloaked-elements>`_
	- `Hiding Visible Elements <https://v5.metroui.org.ua/components/cloak/#hiding-visible-elements>`_
	- `Features <https://v5.metroui.org.ua/components/cloak/#features>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/cloak/#available-css-classes>`_
	- `Common Use Cases <https://v5.metroui.org.ua/components/cloak/#common-use-cases>`_
	- `Loading Indicators <https://v5.metroui.org.ua/components/cloak/#loading-indicators>`_
	- `Progressive Enhancement <https://v5.metroui.org.ua/components/cloak/#progressive-enhancement>`_
	- `Animation Details <https://v5.metroui.org.ua/components/cloak/#animation-details>`_
	- `CSS Implementation <https://v5.metroui.org.ua/components/cloak/#css-implementation>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="cloak",
			base_css_class="cloak",
			tag_name="div",
			component_params=[
				'reveal', 'hide', 'duration', 'delay'
			]
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI cloak component for hiding elements initially and revealing them with smooth fade-in animation.

		Args:
			**attrs: HTML attributes including:
				reveal (bool): Whether to add remove-cloak class for fade-in animation
				hide (bool): Whether to add add-cloak class for fade-out animation
				duration (str): Custom animation duration (e.g., '2s', '500ms')
				delay (str): Animation delay (e.g., '1s', '200ms')
				cls (str): Additional CSS classes
				id (str): ID attribute for the element
				content (str): Content to be cloaked
		
		Returns:
			str: Rendered HTML div element with cloak functionality
			
		References:
			.. _MetroUI Cloak: https://v5.metroui.org.ua/components/cloak/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base CSS classes
		css_classes = ['cloak']
		
		# Add reveal class if specified
		if component_attrs.get('reveal'):
			css_classes.append('remove-cloak')
		
		# Add hide class if specified
		if component_attrs.get('hide'):
			css_classes.append('add-cloak')
		
		# Add custom CSS classes
		if cls_attrs:
			css_classes.extend(cls_attrs)
		
		# Add standard CSS classes
		if standard_attrs.get('class'):
			css_classes.append(standard_attrs['class'])
		
		# Build ID attribute
		id_attr = self.build_id_attribute(component_attrs, standard_attrs)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**{k: v for k, v in standard_attrs.items() if k != 'class'}
		}
		
		# Add ID if generated or provided
		if id_attr:
			final_attrs["id"] = id_attr
		
		# Add custom animation properties if specified
		style_parts = []
		if component_attrs.get('duration'):
			style_parts.append(f'animation-duration: {component_attrs["duration"]}')
		if component_attrs.get('delay'):
			style_parts.append(f'animation-delay: {component_attrs["delay"]}')
		
		if style_parts:
			final_attrs["style"] = "; ".join(style_parts)
		
		# Get content from component_attrs or standard_attrs
		content = component_attrs.get('content', '') or standard_attrs.get('content', '')
		
		# Remove content from final_attrs to avoid it being rendered as an attribute
		if 'content' in final_attrs:
			del final_attrs['content']
		
		# Render the div element
		from ..html import render_tag
		return render_tag("div", final_attrs, content=content)


# Create component instance
_cloak_component = CloakComponent()


def render_cloak(**attrs):
	"""
	Renders MetroUI cloak component for hiding elements initially and revealing them with smooth fade-in animation.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/cloak/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/cloak/#basic-usage>`_
	- `Revealing Cloaked Elements <https://v5.metroui.org.ua/components/cloak/#revealing-cloaked-elements>`_
	- `Hiding Visible Elements <https://v5.metroui.org.ua/components/cloak/#hiding-visible-elements>`_
	- `Features <https://v5.metroui.org.ua/components/cloak/#features>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/cloak/#available-css-classes>`_
	- `Common Use Cases <https://v5.metroui.org.ua/components/cloak/#common-use-cases>`_
	- `Loading Indicators <https://v5.metroui.org.ua/components/cloak/#loading-indicators>`_
	- `Progressive Enhancement <https://v5.metroui.org.ua/components/cloak/#progressive-enhancement>`_
	- `Animation Details <https://v5.metroui.org.ua/components/cloak/#animation-details>`_
	- `CSS Implementation <https://v5.metroui.org.ua/components/cloak/#css-implementation>`_

	Args:
		**attrs: HTML attributes including:
			reveal (bool): Whether to add remove-cloak class for fade-in animation
			hide (bool): Whether to add add-cloak class for fade-out animation
			duration (str): Custom animation duration (e.g., '2s', '500ms')
			delay (str): Animation delay (e.g., '1s', '200ms')
			cls (str): Additional CSS classes
			id (str): ID attribute for the element
			content (str): Content to be cloaked
		
		Returns:
			str: Rendered HTML div element with cloak functionality
			
		References:
			.. _MetroUI Cloak: https://v5.metroui.org.ua/components/cloak/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _cloak_component.render(**attrs)
