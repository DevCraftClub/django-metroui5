"""
MetroUI Chart Card Component
"""

from .base import SimpleComponent
from ..html import render_tag


class ChartCardComponent(SimpleComponent):
	"""
	MetroUI Chart Card Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/chart-card/>`_.
	
	You can also reference specific sections:
	- `Usage <https://v5.metroui.org.ua/components/chart-card/#usage>`_
	- `Structure <https://v5.metroui.org.ua/components/chart-card/#structure>`_
	- `Content Elements <https://v5.metroui.org.ua/components/chart-card/#content-elements>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/chart-card/#styling-with-css-variables>`_
	- `Additional Information <https://v5.metroui.org.ua/components/chart-card/#additional-information>`_
	- `Best Practices <https://v5.metroui.org.ua/components/chart-card/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="chart_card",
			base_css_class="chart-card",
			tag_name="div",
			component_params=[
				'value', 'title', 'subtitle', 'chart_content', 'cls_content', 'cls_chart'
			]
		)
	
	def render(self, value=None, title=None, subtitle=None, chart_content=None, **attrs):
		"""
		Renders MetroUI chart card component for displaying charts alongside content.

		Args:
			value: Large, bold text for displaying the primary metric (28px)
			title: Medium-sized text for the card's title (16px)
			subtitle: Smaller text for additional information (12px)
			chart_content: HTML content for the chart or visualization element
			**attrs: Additional HTML attributes including:
				cls_content (str): Additional CSS class(es) for the content section
				cls_chart (str): Additional CSS class(es) for the chart section
		
		Returns:
			str: Rendered HTML div element with chart card structure
			
		References:
			.. _MetroUI Chart Card: https://v5.metroui.org.ua/components/chart-card/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Build ID attribute
		id_attr = self.build_id_attribute(component_attrs, standard_attrs)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		if id_attr:
			final_attrs["id"] = id_attr
		
		# Build content section
		content_attrs = {"class": "content"}
		if component_attrs.get('cls_content'):
			content_attrs["class"] += f" {component_attrs['cls_content']}"
		
		content_elements = []
		
		# Add value if provided
		if value:
			content_elements.append(render_tag("div", {"class": "value"}, str(value)))
		
		# Add title if provided
		if title:
			content_elements.append(render_tag("div", {"class": "title"}, str(title)))
		
		# Add subtitle if provided
		if subtitle:
			content_elements.append(render_tag("div", {"class": "subtitle"}, str(subtitle)))
		
		content_section = render_tag("div", content_attrs, "".join(content_elements))
		
		# Build chart section
		chart_attrs = {"class": "chart"}
		if component_attrs.get('cls_chart'):
			chart_attrs["class"] += f" {component_attrs['cls_chart']}"
		
		chart_section = render_tag("div", chart_attrs, chart_content or "")
		
		# Combine content and chart sections
		card_content = content_section + chart_section
		
		return render_tag(self.tag_name, final_attrs, card_content)


# Create component instance
_chart_card_component = ChartCardComponent()


def render_chart_card(value=None, title=None, subtitle=None, chart_content=None, **attrs):
	"""
	Renders MetroUI chart card component for displaying charts alongside content.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/chart-card/>`_.
	
	You can also reference specific sections:
	- `Usage <https://v5.metroui.org.ua/components/chart-card/#usage>`_
	- `Structure <https://v5.metroui.org.ua/components/chart-card/#structure>`_
	- `Content Elements <https://v5.metroui.org.ua/components/chart-card/#content-elements>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/chart-card/#styling-with-css-variables>`_
	- `Additional Information <https://v5.metroui.org.ua/components/chart-card/#additional-information>`_
	- `Best Practices <https://v5.metroui.org.ua/components/chart-card/#best-practices>`_

	Args:
		value: Large, bold text for displaying the primary metric (28px)
		title: Medium-sized text for the card's title (16px)
		subtitle: Smaller text for additional information (12px)
		chart_content: HTML content for the chart or visualization element
		**attrs: Additional HTML attributes including:
			cls_content (str): Additional CSS class(es) for the content section
			cls_chart (str): Additional CSS class(es) for the chart section
		
		Returns:
			str: Rendered HTML div element with chart card structure
			
		References:
			.. _MetroUI Chart Card: https://v5.metroui.org.ua/components/chart-card/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _chart_card_component.render(value, title, subtitle, chart_content, **attrs)
