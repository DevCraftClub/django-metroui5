"""Компонент Metro streamer."""

from .base import SimpleComponent


class StreamerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="streamer",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"streamer_deferred",
				"wheel",
				"wheel_step",
				"duration",
				"default_closed_icon",
				"default_open_icon",
				"change_uri",
				"encode_link",
				"closed",
				"chrome_notice",
				"start_from",
				"slide_to_start",
				"start_slide_sleep",
				"source",
				"data",
				"event_click",
				"select_global",
				"stream_select",
				"exclude_select_element",
				"exclude_click_element",
				"exclude_element",
				"exclude_select_class",
				"exclude_click_class",
				"exclude_class",
			],
			default_data_attrs={"data-role": "streamer"},
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


_streamer = StreamerComponent()


def render_streamer(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"streamer\".
	Example:
		render_streamer()

	Empty or invalid:
		`render_streamer()` returns `<div data-role="streamer"></div>`.

	"""
	return _streamer.render(content=content, **attrs)
