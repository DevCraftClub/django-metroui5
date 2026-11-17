"""Компонент Metro video-player."""

from .base import SimpleComponent


class VideoPlayerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="video_player",
			base_css_class=None,
			tag_name="video",
			component_params=[
				"video_deferred",
				"src",
				"poster",
				"logo",
				"logo_height",
				"logo_width",
				"logo_target",
				"volume",
				"loop",
				"autoplay",
				"full_screen_mode",
				"aspect_ratio",
				"controls_hide",
				"show_loop",
				"show_play",
				"show_stop",
				"show_mute",
				"show_full",
				"show_stream",
				"show_volume",
				"show_info",
				"loop_icon",
				"stop_icon",
				"play_icon",
				"pause_icon",
				"mute_icon",
				"volume_low_icon",
				"volume_medium_icon",
				"volume_high_icon",
				"screen_more_icon",
				"screen_less_icon",
			],
			default_data_attrs={"data-role": "video-player"},
		)

	def render(self, content="", **attrs):
		cleaned = {}
		for key, value in attrs.items():
			if value is None:
				continue
			if isinstance(value, bool):
				cleaned[key] = "true" if value else "false"
			else:
				cleaned[key] = value
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(cleaned)
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		final_attrs = {
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs,
		}
		if css_classes:
			final_attrs["class"] = " ".join(css_classes)
		id_attr = self.build_id_attribute(component_attrs, standard_attrs, auto_generate=False)
		if id_attr:
			final_attrs["id"] = id_attr
		return self.render_component(self.tag_name, final_attrs, content=content, close=True)


_video_player = VideoPlayerComponent()


def render_video_player(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"video-player\".
	Example:
		render_video_player()

	Empty or invalid:
		`render_video_player()` returns `<video data-role="video-player"></video>`.

	"""
	return _video_player.render(content=content, **attrs)
