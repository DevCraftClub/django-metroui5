"""
MetroUI Bulls Component
"""

from .base import SimpleComponent
from ..html import render_tag


class BullsComponent(SimpleComponent):
	"""
	MetroUI Bulls Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/bulls/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/bulls/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/bulls/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/bulls/#api-methods>`_
	- `Bull Types <https://v5.metroui.org.ua/components/bulls/#bull-types>`_
	- `Events <https://v5.metroui.org.ua/components/bulls/#events>`_
	- `Styling <https://v5.metroui.org.ua/components/bulls/#styling>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="bulls",
			base_css_class="bull",
			tag_name="div",
			component_params=['type', 'size', 'onBullCreate', 'onBullChange', 'cls_bull']
		)
	
	def render(self, bull_type="success", size=16, **attrs):
		"""
		Renders MetroUI bulls component with status indicator SVG icons.
		
		Args:
			bull_type: Type of bull icon. Possible values: "success", "fail", "pending", "warning", "bulb-on", "bulb-off", "star", "badge", "chat", "tree", "checkmark", "cancel", "rocket", "default"
			size: Size of the bull icon in pixels (default: 16)
			**attrs: Additional HTML attributes including:
				onBullCreate (str): Callback function triggered when the bull is created
				onBullChange (str): Callback function triggered when the bull type is changed
				cls_bull (str): Additional CSS class for the bull container
		
		Returns:
			str: Rendered HTML div element with bull functionality
			
		References:
			.. _MetroUI Bulls: https://v5.metroui.org.ua/components/bulls/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs)
		
		# Add bull-specific data attributes
		data_attrs["data-role"] = "bull"
		data_attrs["data-type"] = bull_type
		data_attrs["data-size"] = str(size)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**data_attrs,
			**standard_attrs
		}
		
		return self.render_component(self.tag_name, final_attrs, content="")


# Create component instance
_bulls_component = BullsComponent()


def render_bulls(bull_type="success", size=16, **attrs):
	"""
	Renders MetroUI bulls component with status indicator SVG icons.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/bulls/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/bulls/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/bulls/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/bulls/#api-methods>`_
	- `Bull Types <https://v5.metroui.org.ua/components/bulls/#bull-types>`_
	- `Events <https://v5.metroui.org.ua/components/bulls/#events>`_
	- `Styling <https://v5.metroui.org.ua/components/bulls/#styling>`_
	
	Args:
		bull_type: Type of bull icon. Possible values: "success", "fail", "pending", "warning", "bulb-on", "bulb-off", "star", "badge", "chat", "tree", "checkmark", "cancel", "rocket", "default"
		size: Size of the bull icon in pixels (default: 16)
		**attrs: Additional HTML attributes including:
			onBullCreate (str): Callback function triggered when the bull is created
			onBullChange (str): Callback function triggered when the bull type is changed
			cls_bull (str): Additional CSS class for the bull container
		
	Returns:
		str: Rendered HTML div element with bull functionality
		
	References:
		.. _MetroUI Bulls: https://v5.metroui.org.ua/components/bulls/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _bulls_component.render(bull_type, size, **attrs)
