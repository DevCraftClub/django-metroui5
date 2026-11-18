"""
MetroUI Charms Component
"""

from .base import ComplexComponent
from ..html import render_tag


class CharmsComponent(ComplexComponent):
	"""
	MetroUI Charms Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/charms/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/charms/#basic-usage>`_
	- `Controlling Charms <https://v5.metroui.org.ua/components/charms/#controlling-charms>`_
	- `Charm Elements <https://v5.metroui.org.ua/components/charms/#charm-elements>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/charms/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/charms/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/charms/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/charms/#available-css-classes>`_
	- `Best Practices <https://v5.metroui.org.ua/components/charms/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="charms",
			base_css_class="charms",
			component_params=[
				'charmsDeferred', 'position', 'opacity', 'clsCharms', 'onCharmCreate',
				'onOpen', 'onClose', 'onToggle'
			]
		)
	
	def render(self, content=None, **attrs):
		"""
		Renders MetroUI charms component with panel that can be positioned on any side of the screen.

		Args:
			content: Content to display inside the charms panel
			**attrs: Additional HTML attributes including:
				charmsDeferred (int): Deferred initialization time in milliseconds
				position (str): Position of the charms panel ("right", "left", "top", "bottom")
				opacity (float): Opacity of the charms panel background (0-1)
				clsCharms (str): Additional CSS class(es) for the charms element
				onCharmCreate (str): Callback function triggered after charms creation
				onOpen (str): Callback function triggered when charms is opened
				onClose (str): Callback function triggered when charms is closed
				onToggle (str): Callback function triggered when charms state is toggled
		
		Returns:
			str: Rendered HTML div element with charms functionality
			
		References:
			.. _MetroUI Charms: https://v5.metroui.org.ua/components/charms/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add charms-specific data attributes
		base_attrs["data-role"] = "charms"
		
		# Add position if specified
		if component_attrs.get('position'):
			base_attrs["data-position"] = component_attrs['position']
		
		# Add opacity if specified
		if component_attrs.get('opacity'):
			base_attrs["data-opacity"] = str(component_attrs['opacity'])
		
		# Add deferred initialization if specified
		if component_attrs.get('charmsDeferred'):
			base_attrs["data-charms-deferred"] = str(component_attrs['charmsDeferred'])
		
		# Add callback functions if specified
		if component_attrs.get('onCharmCreate'):
			base_attrs["data-on-charm-create"] = component_attrs['onCharmCreate']
		
		if component_attrs.get('onOpen'):
			base_attrs["data-on-open"] = component_attrs['onOpen']
		
		if component_attrs.get('onClose'):
			base_attrs["data-on-close"] = component_attrs['onClose']
		
		if component_attrs.get('onToggle'):
			base_attrs["data-on-toggle"] = component_attrs['onToggle']
		
		# Add position-specific CSS class
		position = component_attrs.get('position', 'right')
		if position in ['top', 'bottom', 'left', 'right']:
			base_attrs["class"] += f" {position}-side"
		
		return self.render_component("div", base_attrs, content=content)


# Create component instance
_charms_component = CharmsComponent()


def render_charms(content=None, **attrs):
	"""
	Renders MetroUI charms component with panel that can be positioned on any side of the screen.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/charms/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/charms/#basic-usage>`_
	- `Controlling Charms <https://v5.metroui.org.ua/components/charms/#controlling-charms>`_
	- `Charm Elements <https://v5.metroui.org.ua/components/charms/#charm-elements>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/charms/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/charms/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/charms/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/charms/#available-css-classes>`_
	- `Best Practices <https://v5.metroui.org.ua/components/charms/#best-practices>`_

	Args:
		content: Content to display inside the charms panel
		**attrs: Additional HTML attributes including:
			charmsDeferred (int): Deferred initialization time in milliseconds
			position (str): Position of the charms panel ("right", "left", "top", "bottom")
			opacity (float): Opacity of the charms panel background (0-1)
			clsCharms (str): Additional CSS class(es) for the charms element
			onCharmCreate (str): Callback function triggered after charms creation
			onOpen (str): Callback function triggered when charms is opened
			onClose (str): Callback function triggered when charms is closed
			onToggle (str): Callback function triggered when charms state is toggled
		
		Returns:
			str: Rendered HTML div element with charms functionality
			
		References:
			.. _MetroUI Charms: https://v5.metroui.org.ua/components/charms/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_charms()

	Empty or invalid:
		`render_charms()` returns `<div class="charms right-side" id="charms-component" data-role="charms" />`. An empty call returns `<div class="charms right-side" id="charms-component" data-role="charms"></div>`.

	"""
	return _charms_component.render(content, **attrs)
