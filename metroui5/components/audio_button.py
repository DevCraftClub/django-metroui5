"""
MetroUI Audio Button Component
"""

from .base import SimpleComponent


class AudioButtonComponent(SimpleComponent):
	"""
	MetroUI Audio Button Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/audio-button/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/audio-button/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/audio-button/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/audio-button/#api-methods>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="audio_button",
			base_css_class="button",
			tag_name="button",
			component_params=[
				'audio_volume', 'audio_src', 'on_audio_start', 'on_audio_end',
				'on_audio_button_create', 'cls_audio_button'
			],
			data_attr_mapping={
				'audio_src': 'data-audio-src',
				'audio_volume': 'data-audio-volume'
			},
			default_data_attrs={"data-role": "audio-button"}
		)
	
	def render(self, content="", **attrs):
		"""
		Renders MetroUI audio button component.
		
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
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Add audio button-specific data attributes
		if component_attrs.get('on_audio_start'):
			data_attrs["data-on-audio-start"] = component_attrs['on_audio_start']
		
		if component_attrs.get('on_audio_end'):
			data_attrs["data-on-audio-end"] = component_attrs['on_audio_end']
		
		if component_attrs.get('on_audio_button_create'):
			data_attrs["data-on-audio-button-create"] = component_attrs['on_audio_button_create']
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		return self.render_component(self.tag_name, final_attrs, content=content)


# Create component instance
_audio_button_component = AudioButtonComponent()


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
	return _audio_button_component.render(content, **attrs)
