"""
MetroUI Audio Player Component
"""

from .base import SimpleComponent


class AudioPlayerComponent(SimpleComponent):
	"""
	MetroUI Audio Player Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/audio-player/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/audio-player/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/audio-player/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/audio-player/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/audio-player/#events>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="audio_player",
			base_css_class="",
			tag_name="audio",
			component_params=[
				'show_loop', 'show_play', 'show_stop', 'show_stream', 'show_volume', 'show_info',
				'loop', 'autoplay', 'volume', 'loop_icon', 'play_icon', 'pause_icon', 'stop_icon',
				'mute_icon', 'volume_low_icon', 'volume_medium_icon', 'volume_high_icon',
				'on_play', 'on_pause', 'on_stop', 'on_end', 'on_metadata', 'on_time', 'on_audio_create',
				'cls_audio_player'
			],
			data_attr_mapping={
				'show_loop': 'data-show-loop',
				'show_play': 'data-show-play',
				'show_stop': 'data-show-stop',
				'show_stream': 'data-show-stream',
				'show_volume': 'data-show-volume',
				'show_info': 'data-show-info',
				'loop': 'data-loop',
				'autoplay': 'data-autoplay',
				'volume': 'data-volume',
				'loop_icon': 'data-loop-icon',
				'play_icon': 'data-play-icon',
				'pause_icon': 'data-pause-icon',
				'stop_icon': 'data-stop-icon',
				'mute_icon': 'data-mute-icon',
				'volume_low_icon': 'data-volume-low-icon',
				'volume_medium_icon': 'data-volume-medium-icon',
				'volume_high_icon': 'data-volume-high-icon'
			},
			default_data_attrs={"data-role": "audio-player"}
		)
	
	def render(self, src="", **attrs):
		"""
		Renders MetroUI audio player component.
		
		Args:
			src: Path to the audio file
			**attrs: Additional HTML attributes including:
				show_loop (bool): Show or hide loop control
				show_play (bool): Show or hide play control
				show_stop (bool): Show or hide stop control
				show_stream (bool): Show or hide stream control
				show_volume (bool): Show or hide volume control
				show_info (bool): Show or hide info display
				loop (bool): Enable looping audio
				autoplay (bool): Start playback automatically
				volume (float): Initial volume (0.0 to 1.0)
				loop_icon (str): Custom icon for loop control
				play_icon (str): Custom icon for play control
				pause_icon (str): Custom icon for pause control
				stop_icon (str): Custom icon for stop control
				mute_icon (str): Custom icon for mute control
				volume_low_icon (str): Custom icon for low volume
				volume_medium_icon (str): Custom icon for medium volume
				volume_high_icon (str): Custom icon for high volume
				on_play (str): Callback function triggered when playback starts
				on_pause (str): Callback function triggered when playback is paused
				on_stop (str): Callback function triggered when playback stops
				on_end (str): Callback function triggered when playback ends
				on_metadata (str): Callback function triggered when metadata is loaded
				on_time (str): Callback function triggered during playback to update current time
				on_audio_create (str): Callback function triggered when audio player is created
				cls_audio_player (str): Additional CSS class for the audio player container
			
		Returns:
			str: Rendered HTML audio element with audio player functionality
			
		References:
			.. _MetroUI Audio Player: https://v5.metroui.org.ua/components/audio-player/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Add audio source
		if src:
			data_attrs["data-src"] = src
		
		# Add audio player-specific data attributes
		if component_attrs.get('on_play'):
			data_attrs["data-on-play"] = component_attrs['on_play']
		
		if component_attrs.get('on_pause'):
			data_attrs["data-on-pause"] = component_attrs['on_pause']
		
		if component_attrs.get('on_stop'):
			data_attrs["data-on-stop"] = component_attrs['on_stop']
		
		if component_attrs.get('on_end'):
			data_attrs["data-on-end"] = component_attrs['on_end']
		
		if component_attrs.get('on_metadata'):
			data_attrs["data-on-metadata"] = component_attrs['on_metadata']
		
		if component_attrs.get('on_time'):
			data_attrs["data-on-time"] = component_attrs['on_time']
		
		if component_attrs.get('on_audio_create'):
			data_attrs["data-on-audio-create"] = component_attrs['on_audio_create']
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes) if css_classes else None,
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		# Remove None values
		final_attrs = {k: v for k, v in final_attrs.items() if v is not None}
		
		return self.render_component(self.tag_name, final_attrs, content="")


# Create component instance
_audio_player_component = AudioPlayerComponent()


def render_audio_player(src="", **attrs):
	"""
	Renders MetroUI audio player component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/audio-player/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/audio-player/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/audio-player/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/audio-player/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/audio-player/#events>`_
	
	Args:
		src: Path to the audio file
		**attrs: Additional HTML attributes including:
			show_loop (bool): Show or hide loop control
			show_play (bool): Show or hide play control
			show_stop (bool): Show or hide stop control
			show_stream (bool): Show or hide stream control
			show_volume (bool): Show or hide volume control
			show_info (bool): Show or hide info display
			loop (bool): Enable looping audio
			autoplay (bool): Start playback automatically
			volume (float): Initial volume (0.0 to 1.0)
			loop_icon (str): Custom icon for loop control
			play_icon (str): Custom icon for play control
			pause_icon (str): Custom icon for pause control
			stop_icon (str): Custom icon for stop control
			mute_icon (str): Custom icon for mute control
			volume_low_icon (str): Custom icon for low volume
			volume_medium_icon (str): Custom icon for medium volume
			volume_high_icon (str): Custom icon for high volume
			on_play (str): Callback function triggered when playback starts
			on_pause (str): Callback function triggered when playback is paused
			on_stop (str): Callback function triggered when playback stops
			on_end (str): Callback function triggered when playback ends
			on_metadata (str): Callback function triggered when metadata is loaded
			on_time (str): Callback function triggered during playback to update current time
			on_audio_create (str): Callback function triggered when audio player is created
			cls_audio_player (str): Additional CSS class for the audio player container
		
	Returns:
		str: Rendered HTML audio element with audio player functionality
		
	References:
		.. _MetroUI Audio Player: https://v5.metroui.org.ua/components/audio-player/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _audio_player_component.render(src, **attrs)
