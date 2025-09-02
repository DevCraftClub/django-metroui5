"""
MetroUI Audio Player Component
"""

from ..html import render_tag


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
	# Extract audio player-specific attributes
	audio_player_attrs = {}
	standard_attrs = {}
	
	# Audio player-specific parameters
	audio_player_params = [
		'show_loop', 'show_play', 'show_stop', 'show_stream', 'show_volume', 'show_info',
		'loop', 'autoplay', 'volume', 'loop_icon', 'play_icon', 'pause_icon', 'stop_icon',
		'mute_icon', 'volume_low_icon', 'volume_medium_icon', 'volume_high_icon',
		'on_play', 'on_pause', 'on_stop', 'on_end', 'on_metadata', 'on_time', 'on_audio_create',
		'cls_audio_player'
	]
	
	# Separate audio player attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in audio_player_params:
			audio_player_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "audio-player"
	}
	
	# Add audio source
	if src:
		default_attrs["data-src"] = src
	
	# Add audio player-specific data attributes
	if audio_player_attrs.get('show_loop') is not None:
		default_attrs["data-show-loop"] = "true" if audio_player_attrs['show_loop'] else "false"
	
	if audio_player_attrs.get('show_play') is not None:
		default_attrs["data-show-play"] = "true" if audio_player_attrs['show_play'] else "false"
	
	if audio_player_attrs.get('show_stop') is not None:
		default_attrs["data-show-stop"] = "true" if audio_player_attrs['show_stop'] else "false"
	
	if audio_player_attrs.get('show_stream') is not None:
		default_attrs["data-show-stream"] = "true" if audio_player_attrs['show_stream'] else "false"
	
	if audio_player_attrs.get('show_volume') is not None:
		default_attrs["data-show-volume"] = "true" if audio_player_attrs['show_volume'] else "false"
	
	if audio_player_attrs.get('show_info') is not None:
		default_attrs["data-show-info"] = "true" if audio_player_attrs['show_info'] else "false"
	
	if audio_player_attrs.get('loop') is not None:
		default_attrs["data-loop"] = "true" if audio_player_attrs['loop'] else "false"
	
	if audio_player_attrs.get('autoplay') is not None:
		default_attrs["data-autoplay"] = "true" if audio_player_attrs['autoplay'] else "false"
	
	if audio_player_attrs.get('volume') is not None:
		default_attrs["data-volume"] = str(audio_player_attrs['volume'])
	
	# Add custom icons
	if audio_player_attrs.get('loop_icon'):
		default_attrs["data-loop-icon"] = audio_player_attrs['loop_icon']
	
	if audio_player_attrs.get('play_icon'):
		default_attrs["data-play-icon"] = audio_player_attrs['play_icon']
	
	if audio_player_attrs.get('pause_icon'):
		default_attrs["data-pause-icon"] = audio_player_attrs['pause_icon']
	
	if audio_player_attrs.get('stop_icon'):
		default_attrs["data-stop-icon"] = audio_player_attrs['stop_icon']
	
	if audio_player_attrs.get('mute_icon'):
		default_attrs["data-mute-icon"] = audio_player_attrs['mute_icon']
	
	if audio_player_attrs.get('volume_low_icon'):
		default_attrs["data-volume-low-icon"] = audio_player_attrs['volume_low_icon']
	
	if audio_player_attrs.get('volume_medium_icon'):
		default_attrs["data-volume-medium-icon"] = audio_player_attrs['volume_medium_icon']
	
	if audio_player_attrs.get('volume_high_icon'):
		default_attrs["data-volume-high-icon"] = audio_player_attrs['volume_high_icon']
	
	# Add callback functions
	if audio_player_attrs.get('on_play'):
		default_attrs["data-on-play"] = audio_player_attrs['on_play']
	
	if audio_player_attrs.get('on_pause'):
		default_attrs["data-on-pause"] = audio_player_attrs['on_pause']
	
	if audio_player_attrs.get('on_stop'):
		default_attrs["data-on-stop"] = audio_player_attrs['on_stop']
	
	if audio_player_attrs.get('on_end'):
		default_attrs["data-on-end"] = audio_player_attrs['on_end']
	
	if audio_player_attrs.get('on_metadata'):
		default_attrs["data-on-metadata"] = audio_player_attrs['on_metadata']
	
	if audio_player_attrs.get('on_time'):
		default_attrs["data-on-time"] = audio_player_attrs['on_time']
	
	if audio_player_attrs.get('on_audio_create'):
		default_attrs["data-on-audio-create"] = audio_player_attrs['on_audio_create']
	
	# Build CSS classes
	css_classes = []
	
	if audio_player_attrs.get('cls_audio_player'):
		css_classes.append(audio_player_attrs['cls_audio_player'])
	
	# Add light theme class if specified
	if "class" in standard_attrs and "light" in standard_attrs["class"]:
		css_classes.append("light")
		del standard_attrs["class"]
	elif "class" in standard_attrs:
		css_classes.extend(standard_attrs["class"].split())
		del standard_attrs["class"]
	
	if css_classes:
		default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("audio", attrs=final_attrs, content="")
