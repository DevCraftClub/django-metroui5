"""
MetroUI Card Component
"""

from .base import SimpleComponent
from ..html import render_tag


class CardComponent(SimpleComponent):
	"""
	MetroUI Card Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/cards/>`_.
	
	You can also reference specific sections:
	- `Basic Card <https://v5.metroui.org.ua/components/cards/#basic-card>`_
	- `Card with buttons in Header <https://v5.metroui.org.ua/components/cards/#card-with-buttons-in-header>`_
	- `Card with Image Header <https://v5.metroui.org.ua/components/cards/#card-with-image-header>`_
	- `Features <https://v5.metroui.org.ua/components/cards/#features>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/cards/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/cards/#available-css-classes>`_
	- `Special Card Types <https://v5.metroui.org.ua/components/cards/#special-card-types>`_
	- `Best Practices <https://v5.metroui.org.ua/components/cards/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="card",
			base_css_class="card",
			tag_name="div",
			component_params=[
				'flex_card', 'image_header', 'header_background', 'header_buttons',
				'header_avatar', 'header_date', 'cls_header', 'cls_content', 'cls_footer'
			]
		)
	
	def render(self, header=None, content=None, footer=None, **attrs):
		"""
		Renders MetroUI card component with flexible structure and styling options.

		Args:
			header: Card header content (string or dict with 'text', 'buttons', 'avatar', 'date')
			content: Card content
			footer: Card footer content
			**attrs: Additional HTML attributes including:
				flex_card (bool): If true, creates a flexible card that expands to fill space
				image_header (bool): If true, creates a card with image header
				header_background (str): Background image URL for header
				header_buttons (list): List of button configurations for header
				header_avatar (str): Avatar image URL for header
				header_date (str): Date text for header
				cls_header (str): Additional CSS class for header
				cls_content (str): Additional CSS class for content
				cls_footer (str): Additional CSS class for footer
		
		Returns:
			str: Rendered HTML div element with card structure
			
		References:
			.. _MetroUI Cards: https://v5.metroui.org.ua/components/cards/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Add special card type classes
		if component_attrs.get('flex_card'):
			css_classes.append('flex-card')
		
		if component_attrs.get('image_header'):
			css_classes.append('image-header')
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**standard_attrs
		}
		
		# Build card parts
		card_parts = []
		
		# Handle header
		if header or component_attrs.get('header_background'):
			header_attrs = {"class": "card-header"}
			
			# Add header CSS class if specified
			if component_attrs.get('cls_header'):
				header_attrs["class"] += f" {component_attrs['cls_header']}"
			
			# Add background image if specified
			if component_attrs.get('header_background'):
				header_attrs["style"] = f"background-image: url('{component_attrs['header_background']}')"
			
			# Handle header content
			header_content = ""
			if isinstance(header, dict):
				# Complex header with multiple elements
				header_elements = []
				
				# Add avatar if specified
				if component_attrs.get('header_avatar'):
					header_elements.append(f'<img src="{component_attrs["header_avatar"]}" class="avatar" alt="Avatar">')
				
				# Add main header text
				if header.get('text'):
					header_elements.append(header['text'])
				
				# Add date if specified
				if component_attrs.get('header_date'):
					header_elements.append(f'<span class="date">{component_attrs["header_date"]}</span>')
				
				# Add buttons if specified
				buttons = component_attrs.get('header_buttons') or header.get('buttons', [])
				if buttons:
					button_html = '<div class="buttons">'
					for button in buttons:
						if isinstance(button, dict):
							icon = button.get('icon', '')
							text = button.get('text', '')
							cls = button.get('class', 'button')
							if icon:
								button_html += f'<button class="{cls}"><span class="{icon}"></span></button>'
							else:
								button_html += f'<button class="{cls}">{text}</button>'
						else:
							button_html += f'<button class="button">{button}</button>'
					button_html += '</div>'
					header_elements.append(button_html)
				
				header_content = "".join(header_elements)
			elif header and isinstance(header, str) and header.startswith('{') and header.endswith('}'):
				# Try to parse JSON string
				try:
					import json
					header_dict = json.loads(header)
					header_elements = []
					
					# Add avatar if specified
					if component_attrs.get('header_avatar'):
						header_elements.append(f'<img src="{component_attrs["header_avatar"]}" class="avatar" alt="Avatar">')
					
					# Add main header text
					if header_dict.get('text'):
						header_elements.append(header_dict['text'])
					
					# Add date if specified
					if component_attrs.get('header_date'):
						header_elements.append(f'<span class="date">{component_attrs["header_date"]}</span>')
					
					# Add buttons if specified
					buttons = component_attrs.get('header_buttons') or header_dict.get('buttons', [])
					if buttons:
						button_html = '<div class="buttons">'
						for button in buttons:
							if isinstance(button, dict):
								icon = button.get('icon', '')
								text = button.get('text', '')
								cls = button.get('class', 'button')
								if icon:
									button_html += f'<button class="{cls}"><span class="{icon}"></span></button>'
								else:
									button_html += f'<button class="{cls}">{text}</button>'
							else:
								button_html += f'<button class="button">{button}</button>'
						button_html += '</div>'
						header_elements.append(button_html)
					
					header_content = "".join(header_elements)
				except (json.JSONDecodeError, ValueError):
					# If JSON parsing fails, treat as simple text
					header_content = str(header)
			elif header:
				# Simple header text
				header_content = str(header)
			
			card_parts.append(render_tag("div", header_attrs, header_content))
		
		# Handle content
		if content:
			content_attrs = {"class": "card-content"}
			
			# Add content CSS class if specified
			if component_attrs.get('cls_content'):
				content_attrs["class"] += f" {component_attrs['cls_content']}"
			
			card_parts.append(render_tag("div", content_attrs, content))
		
		# Handle footer
		if footer:
			footer_attrs = {"class": "card-footer"}
			
			# Add footer CSS class if specified
			if component_attrs.get('cls_footer'):
				footer_attrs["class"] += f" {component_attrs['cls_footer']}"
			
			card_parts.append(render_tag("div", footer_attrs, footer))
		
		# Ensure at least content exists
		if not card_parts:
			content_attrs = {"class": "card-content"}
			if component_attrs.get('cls_content'):
				content_attrs["class"] += f" {component_attrs['cls_content']}"
			card_parts.append(render_tag("div", content_attrs, ""))
		
		return self.render_component(self.tag_name, final_attrs, content="".join(card_parts))


# Create component instance
_card_component = CardComponent()


def render_card(header=None, content=None, footer=None, **attrs):
	"""
	Renders MetroUI card component with flexible structure and styling options.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/cards/>`_.
	
	You can also reference specific sections:
	- `Basic Card <https://v5.metroui.org.ua/components/cards/#basic-card>`_
	- `Card with buttons in Header <https://v5.metroui.org.ua/components/cards/#card-with-buttons-in-header>`_
	- `Card with Image Header <https://v5.metroui.org.ua/components/cards/#card-with-image-header>`_
	- `Features <https://v5.metroui.org.ua/components/cards/#features>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/cards/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/cards/#available-css-classes>`_
	- `Special Card Types <https://v5.metroui.org.ua/components/cards/#special-card-types>`_
	- `Best Practices <https://v5.metroui.org.ua/components/cards/#best-practices>`_

	Args:
		header: Card header content (string or dict with 'text', 'buttons', 'avatar', 'date')
		content: Card content
		footer: Card footer content
		**attrs: Additional HTML attributes including:
			flex_card (bool): If true, creates a flexible card that expands to fill space
			image_header (bool): If true, creates a card with image header
			header_background (str): Background image URL for header
			header_buttons (list): List of button configurations for header
			header_avatar (str): Avatar image URL for header
			header_date (str): Date text for header
			cls_header (str): Additional CSS class for header
			cls_content (str): Additional CSS class for content
			cls_footer (str): Additional CSS class for footer
		
		Returns:
			str: Rendered HTML div element with card structure
			
		References:
			.. _MetroUI Cards: https://v5.metroui.org.ua/components/cards/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _card_component.render(header, content, footer, **attrs)
