"""
MetroUI Collapse Component
"""

from .base import ComplexComponent


class CollapseComponent(ComplexComponent):
	"""
	MetroUI Collapse Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/collapse/>`_.
	
	You can also reference specific sections:
	- `Basic Collapse <https://v5.metroui.org.ua/components/collapse/#basic-collapse>`_
	- `Custom Toggle Element <https://v5.metroui.org.ua/components/collapse/#custom-toggle-element>`_
	- `Initially Collapsed <https://v5.metroui.org.ua/components/collapse/#initially-collapsed>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/collapse/#plugin-parameters>`_
	- `Event Callbacks <https://v5.metroui.org.ua/components/collapse/#event-callbacks>`_
	- `API Methods <https://v5.metroui.org.ua/components/collapse/#api-methods>`_
	- `Styling <https://v5.metroui.org.ua/components/collapse/#styling>`_
	- `Accessibility <https://v5.metroui.org.ua/components/collapse/#accessibility>`_
	- `Best Practices <https://v5.metroui.org.ua/components/collapse/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="collapse",
			base_css_class="",
			component_params=[
				'collapseDeferred', 'collapsed', 'toggleElement', 'duration',
				'onExpand', 'onCollapse', 'onCollapseCreate'
			]
		)
	
	def render(self, content="", **attrs):
		"""
		Renders MetroUI collapse component for toggling content visibility with smooth animations.

		Args:
			content (str): Content to be collapsible
			**attrs: HTML attributes including:
				collapseDeferred (int): Delay in milliseconds before collapse action starts
				collapsed (bool): Whether the element should be initially collapsed
				toggleElement (str): Selector for custom toggle element
				duration (int): Duration of collapse/expand animation in milliseconds
				onExpand (str): Callback function when element is expanded
				onCollapse (str): Callback function when element is collapsed
				onCollapseCreate (str): Callback function when collapse component is created
				cls (str): Additional CSS classes
				id (str): ID attribute for the collapse element
		
		Returns:
			str: Rendered HTML div element with collapse functionality
			
		References:
			.. _MetroUI Collapse: https://v5.metroui.org.ua/components/collapse/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add collapse-specific data attributes
		base_attrs["data-role"] = "collapse"
		
		# Add configuration parameters
		if component_attrs.get('collapseDeferred'):
			base_attrs["data-collapse-deferred"] = str(component_attrs['collapseDeferred'])
		
		if component_attrs.get('collapsed'):
			base_attrs["data-collapsed"] = str(component_attrs['collapsed']).lower()
		
		if component_attrs.get('toggleElement'):
			base_attrs["data-toggle-element"] = component_attrs['toggleElement']
		
		if component_attrs.get('duration'):
			base_attrs["data-duration"] = str(component_attrs['duration'])
		
		# Add callback functions if specified
		if component_attrs.get('onExpand'):
			base_attrs["data-on-expand"] = component_attrs['onExpand']
		
		if component_attrs.get('onCollapse'):
			base_attrs["data-on-collapse"] = component_attrs['onCollapse']
		
		if component_attrs.get('onCollapseCreate'):
			base_attrs["data-on-collapse-create"] = component_attrs['onCollapseCreate']
		
		return self.render_component("div", base_attrs, content=content)


# Create component instance
_collapse_component = CollapseComponent()


def render_collapse(content="", **attrs):
	"""
	Renders MetroUI collapse component for toggling content visibility with smooth animations.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/collapse/>`_.
	
	You can also reference specific sections:
	- `Basic Collapse <https://v5.metroui.org.ua/components/collapse/#basic-collapse>`_
	- `Custom Toggle Element <https://v5.metroui.org.ua/components/collapse/#custom-toggle-element>`_
	- `Initially Collapsed <https://v5.metroui.org.ua/components/collapse/#initially-collapsed>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/collapse/#plugin-parameters>`_
	- `Event Callbacks <https://v5.metroui.org.ua/components/collapse/#event-callbacks>`_
	- `API Methods <https://v5.metroui.org.ua/components/collapse/#api-methods>`_
	- `Styling <https://v5.metroui.org.ua/components/collapse/#styling>`_
	- `Accessibility <https://v5.metroui.org.ua/components/collapse/#accessibility>`_
	- `Best Practices <https://v5.metroui.org.ua/components/collapse/#best-practices>`_

	Args:
		content (str): Content to be collapsible
		**attrs: HTML attributes including:
			collapseDeferred (int): Delay in milliseconds before collapse action starts
			collapsed (bool): Whether the element should be initially collapsed
			toggleElement (str): Selector for custom toggle element
			duration (int): Duration of collapse/expand animation in milliseconds
			onExpand (str): Callback function when element is expanded
			onCollapse (str): Callback function when element is collapsed
			onCollapseCreate (str): Callback function when collapse component is created
			cls (str): Additional CSS classes
			id (str): ID attribute for the collapse element
		
		Returns:
			str: Rendered HTML div element with collapse functionality
			
		References:
			.. _MetroUI Collapse: https://v5.metroui.org.ua/components/collapse/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _collapse_component.render(content=content, **attrs)
