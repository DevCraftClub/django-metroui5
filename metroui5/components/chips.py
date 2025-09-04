"""
MetroUI Chips Component
"""

from .base import SimpleComponent


class ChipsComponent(SimpleComponent):
	"""
	MetroUI Chips Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/chips/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/chips/#basic-usage>`_
	- `With Icon <https://v5.metroui.org.ua/components/chips/#with-icon>`_
	- `With Action (Close Button) <https://v5.metroui.org.ua/components/chips/#with-action-close-button>`_
	- `Pill-shaped Chip <https://v5.metroui.org.ua/components/chips/#pill-shaped-chip>`_
	- `Colored Chips <https://v5.metroui.org.ua/components/chips/#colored-chips>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/chips/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/chips/#available-css-classes>`_
	- `Structure <https://v5.metroui.org.ua/components/chips/#structure>`_
	- `Notes <https://v5.metroui.org.ua/components/chips/#notes>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="chips",
			base_css_class="chip",
			tag_name="div",
			component_params=[
				'label', 'icon', 'action', 'pill', 'color', 'soft', 'readonly', 'disabled'
			]
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI chips component for compact elements that represent an input, attribute, or action.

		Args:
			**attrs: HTML attributes including:
				label (str): Text label for the chip (required)
				icon (str): Icon class or HTML for the chip icon
				action (bool): Whether to show the close/action button
				pill (bool): Whether to make the chip pill-shaped
				color (str): Color variant (red, blue, green, etc.)
				soft (bool): Whether to use soft color variant
				readonly (bool): Whether the chip is readonly (hides action button)
				disabled (bool): Whether the chip is disabled (hides action button)
				cls (str): Additional CSS classes
				id (str): ID attribute for the chip
		
		Returns:
			str: Rendered HTML div element with chip structure
			
		References:
			.. _MetroUI Chips: https://v5.metroui.org.ua/components/chips/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base CSS classes
		css_classes = ['chip']
		
		# Add modifier classes
		if component_attrs.get('pill'):
			css_classes.append('pill-chip')
		
		if component_attrs.get('readonly'):
			css_classes.append('readonly')
		
		if component_attrs.get('disabled'):
			css_classes.append('disabled')
		
		# Add color classes
		if component_attrs.get('color'):
			color = component_attrs['color']
			if component_attrs.get('soft'):
				css_classes.append(f'soft-{color}')
			else:
				css_classes.append(color)
		
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
		
		# Build chip content
		content_parts = []
		
		# Add icon if specified
		if component_attrs.get('icon'):
			icon_html = component_attrs['icon']
			# If it's just a class name, wrap it in a span
			if not icon_html.startswith('<'):
				icon_html = f'<span class="{icon_html}"></span>'
			content_parts.append(f'<div class="icon">{icon_html}</div>')
		
		# Add label (required)
		label = component_attrs.get('label', 'Chip')
		content_parts.append(f'<div class="label">{label}</div>')
		
		# Add action button if specified and not readonly/disabled
		if component_attrs.get('action') and not component_attrs.get('readonly') and not component_attrs.get('disabled'):
			content_parts.append('<div class="action"></div>')
		
		# Join content parts
		content = ''.join(content_parts)
		
		# Render the div element
		from ..html import render_tag
		return render_tag("div", final_attrs, content=content)


# Create component instance
_chips_component = ChipsComponent()


def render_chips(**attrs):
	"""
	Renders MetroUI chips component for compact elements that represent an input, attribute, or action.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/chips/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/chips/#basic-usage>`_
	- `With Icon <https://v5.metroui.org.ua/components/chips/#with-icon>`_
	- `With Action (Close Button) <https://v5.metroui.org.ua/components/chips/#with-action-close-button>`_
	- `Pill-shaped Chip <https://v5.metroui.org.ua/components/chips/#pill-shaped-chip>`_
	- `Colored Chips <https://v5.metroui.org.ua/components/chips/#colored-chips>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/chips/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/chips/#available-css-classes>`_
	- `Structure <https://v5.metroui.org.ua/components/chips/#structure>`_
	- `Notes <https://v5.metroui.org.ua/components/chips/#notes>`_

	Args:
		**attrs: HTML attributes including:
			label (str): Text label for the chip (required)
			icon (str): Icon class or HTML for the chip icon
			action (bool): Whether to show the close/action button
			pill (bool): Whether to make the chip pill-shaped
			color (str): Color variant (red, blue, green, etc.)
			soft (bool): Whether to use soft color variant
			readonly (bool): Whether the chip is readonly (hides action button)
			disabled (bool): Whether the chip is disabled (hides action button)
			cls (str): Additional CSS classes
			id (str): ID attribute for the chip
		
		Returns:
			str: Rendered HTML div element with chip structure
			
		References:
			.. _MetroUI Chips: https://v5.metroui.org.ua/components/chips/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _chips_component.render(**attrs)
