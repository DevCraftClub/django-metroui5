"""
MetroUI Adblock Detection Component
"""

from ..html import render_tag


def render_adblock_detection(**attrs):
	"""
	Renders MetroUI adblock detection component.

	Link: https://v5.metroui.org.ua/components/adblock/

	Args:
		**attrs: Additional HTML attributes including:
			# Adblock Detection Parameters
			- adblock_deferred: Deferred initialization time in milliseconds (number)
			- check_interval: Interval in milliseconds to check for ad blockers (number)
			- fire_once: Whether to fire the alert event only once (boolean/number)
			- check_stop: Number of checks before stopping even if no ad blocker is detected (number)
			- localhost: Whether to check for ad blockers on localhost (boolean)
			- on_alert: Callback function triggered when an ad blocker is detected (string)
			- on_fishing_start: Callback function triggered when the detection starts (string)
			- on_fishing_done: Callback function triggered when the detection is done (string)
			- cls_adblock: Additional CSS class for the adblock detection container (string)
	"""
	# Extract adblock-specific attributes
	adblock_attrs = {}
	standard_attrs = {}
	
	# Adblock-specific parameters
	adblock_params = [
		'adblock_deferred', 'check_interval', 'fire_once', 'check_stop', 'localhost',
		'on_alert', 'on_fishing_start', 'on_fishing_done', 'cls_adblock'
	]
	
	# Separate adblock attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in adblock_params:
			adblock_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "adblock"
	}
	
	# Add adblock-specific data attributes
	if adblock_attrs.get('adblock_deferred'):
		default_attrs["data-adblock-deferred"] = str(adblock_attrs['adblock_deferred'])
	
	if adblock_attrs.get('check_interval'):
		default_attrs["data-check-interval"] = str(adblock_attrs['check_interval'])
	
	if adblock_attrs.get('fire_once') is not None:
		if isinstance(adblock_attrs['fire_once'], bool):
			default_attrs["data-fire-once"] = "true" if adblock_attrs['fire_once'] else "false"
		else:
			default_attrs["data-fire-once"] = str(adblock_attrs['fire_once'])
	
	if adblock_attrs.get('check_stop'):
		default_attrs["data-check-stop"] = str(adblock_attrs['check_stop'])
	
	if adblock_attrs.get('localhost') is not None:
		default_attrs["data-localhost"] = "true" if adblock_attrs['localhost'] else "false"
	
	if adblock_attrs.get('on_alert'):
		default_attrs["data-on-alert"] = adblock_attrs['on_alert']
	
	if adblock_attrs.get('on_fishing_start'):
		default_attrs["data-on-fishing-start"] = adblock_attrs['on_fishing_start']
	
	if adblock_attrs.get('on_fishing_done'):
		default_attrs["data-on-fishing-done"] = adblock_attrs['on_fishing_done']
	
	# Build CSS classes
	css_classes = ["adblock-detection"]
	
	if adblock_attrs.get('cls_adblock'):
		css_classes.append(adblock_attrs['cls_adblock'])
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
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
	
	return render_tag("div", attrs=final_attrs, content=adblock_content)
