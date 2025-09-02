"""
MetroUI Adblock Detection Component
"""

from .base import ComplexComponent
from ..html import render_tag


class AdblockComponent(ComplexComponent):
	"""
	MetroUI Adblock Detection Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/adblock/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/adblock/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/adblock/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/adblock/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/adblock/#events>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="adblock",
			base_css_class="adblock-detection",
			component_params=[
				'adblock_deferred', 'check_interval', 'fire_once', 'check_stop', 'localhost',
				'on_alert', 'on_fishing_start', 'on_fishing_done', 'cls_adblock'
			]
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI adblock detection component.
		
		Args:
			**attrs: Additional HTML attributes including:
				adblock_deferred (int): Deferred initialization time in milliseconds
				check_interval (int): Interval in milliseconds to check for ad blockers
				fire_once (bool|int): Whether to fire the alert event only once (boolean) or a specific number of times (number)
				check_stop (int): Number of checks before stopping even if no ad blocker is detected
				localhost (bool): Whether to check for ad blockers on localhost
				on_alert (str): Callback function triggered when an ad blocker is detected
				on_fishing_start (str): Callback function triggered when the detection starts
				on_fishing_done (str): Callback function triggered when the detection is done
				cls_adblock (str): Additional CSS class for the adblock detection container
			
		Returns:
			str: Rendered HTML div element with adblock detection functionality
			
		References:
			.. _MetroUI Adblock Detection: https://v5.metroui.org.ua/components/adblock/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add data-role attribute
		base_attrs["data-role"] = "adblock"
		
		# Add adblock-specific data attributes
		if component_attrs.get('adblock_deferred'):
			base_attrs["data-adblock-deferred"] = str(component_attrs['adblock_deferred'])
		
		if component_attrs.get('check_interval'):
			base_attrs["data-check-interval"] = str(component_attrs['check_interval'])
		
		if component_attrs.get('fire_once') is not None:
			if isinstance(component_attrs['fire_once'], bool):
				base_attrs["data-fire-once"] = "true" if component_attrs['fire_once'] else "false"
			else:
				base_attrs["data-fire-once"] = str(component_attrs['fire_once'])
		
		if component_attrs.get('check_stop'):
			base_attrs["data-check-stop"] = str(component_attrs['check_stop'])
		
		if component_attrs.get('localhost') is not None:
			base_attrs["data-localhost"] = "true" if component_attrs['localhost'] else "false"
		
		if component_attrs.get('on_alert'):
			base_attrs["data-on-alert"] = component_attrs['on_alert']
		
		if component_attrs.get('on_fishing_start'):
			base_attrs["data-on-fishing-start"] = component_attrs['on_fishing_start']
		
		if component_attrs.get('on_fishing_done'):
			base_attrs["data-on-fishing-done"] = component_attrs['on_fishing_done']
		
		# Create the adblock detection element
		# This creates a hidden element that ad blockers typically target
		adblock_content = """
			<!-- Hidden element to detect ad blockers -->
			<div class="adsbox" style="position: absolute; left: -10000px; top: -10000px; width: 1px; height: 1px; overflow: hidden;">
				<div class="advertisement"></div>
				<div class="ads"></div>
				<div class="ad-banner"></div>
				<div class="advertisement-banner"></div>
				<div class="google-ads"></div>
				<div class="adsense"></div>
			</div>
		"""
		
		return render_tag("div", attrs=base_attrs, content=adblock_content)


# Create component instance
_adblock_component = AdblockComponent()


def render_adblock_detection(**attrs):
	"""
	Renders MetroUI adblock detection component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/adblock/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/adblock/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/adblock/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/adblock/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/adblock/#events>`_
	
	Args:
		**attrs: Additional HTML attributes including:
			adblock_deferred (int): Deferred initialization time in milliseconds
			check_interval (int): Interval in milliseconds to check for ad blockers
			fire_once (bool|int): Whether to fire the alert event only once (boolean) or a specific number of times (number)
			check_stop (int): Number of checks before stopping even if no ad blocker is detected
			localhost (bool): Whether to check for ad blockers on localhost
			on_alert (str): Callback function triggered when an ad blocker is detected
			on_fishing_start (str): Callback function triggered when the detection starts
			on_fishing_done (str): Callback function triggered when the detection is done
			cls_adblock (str): Additional CSS class for the adblock detection container
		
	Returns:
		str: Rendered HTML div element with adblock detection functionality
		
	References:
		.. _MetroUI Adblock Detection: https://v5.metroui.org.ua/components/adblock/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _adblock_component.render(**attrs)
