"""
MetroUI Audio Button Component
"""

from ..html import render_tag


def render_audio_button(content="", **attrs):
	"""
	Renders MetroUI audio button component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/audio-button/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/audio-button/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/audio-button/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/audio-button/#api-methods>`_
	
	Args:
		content: Button content/text
		**attrs: Additional HTML attributes including:
			audio_volume (float): Volume level for the audio (0.0 to 1.0)
			audio_src (str): Path to the audio file
			on_audio_start (str): Callback function triggered when audio starts playing
			on_audio_end (str): Callback function triggered when audio finishes playing
			on_audio_button_create (str): Callback function triggered when audio button is created
			cls_audio_button (str): Additional CSS class for the audio button
		
	Returns:
		str: Rendered HTML button element with audio functionality
		
	References:
		.. _MetroUI Audio Button: https://v5.metroui.org.ua/components/audio-button/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	# Extract audio button-specific attributes
	audio_button_attrs = {}
	standard_attrs = {}
	
	# Audio button-specific parameters
	audio_button_params = [
		'audio_volume', 'audio_src', 'on_audio_start', 'on_audio_end',
		'on_audio_button_create', 'cls_audio_button'
	]
	
	# Separate audio button attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in audio_button_params:
			audio_button_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "audio-button"
	}
	
	# Add audio button-specific data attributes
	if audio_button_attrs.get('audio_src'):
		default_attrs["data-audio-src"] = audio_button_attrs['audio_src']
	
	if audio_button_attrs.get('audio_volume') is not None:
		default_attrs["data-audio-volume"] = str(audio_button_attrs['audio_volume'])
	
	# Add callback functions
	if audio_button_attrs.get('on_audio_start'):
		default_attrs["data-on-audio-start"] = audio_button_attrs['on_audio_start']
	
	if audio_button_attrs.get('on_audio_end'):
		default_attrs["data-on-audio-end"] = audio_button_attrs['on_audio_end']
	
	if audio_button_attrs.get('on_audio_button_create'):
		default_attrs["data-on-audio-button-create"] = audio_button_attrs['on_audio_button_create']
	
	# Build CSS classes
	css_classes = ["button"]
	
	if audio_button_attrs.get('cls_audio_button'):
		css_classes.append(audio_button_attrs['cls_audio_button'])
	
	# Add default button class if not already present
	if "class" in standard_attrs:
		existing_classes = standard_attrs["class"].split()
		css_classes.extend([cls for cls in existing_classes if cls not in css_classes])
		del standard_attrs["class"]
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("button", attrs=final_attrs, content=content)
