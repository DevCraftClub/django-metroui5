"""Компонент Metro countdown."""

from .base import SimpleComponent


class CountdownComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="countdown",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"countdown_deferred",
				"stop_on_blur",
				"animate",
				"ease",
				"duration",
				"input_format",
				"days",
				"hours",
				"minutes",
				"seconds",
				"date",
				"start",
				"font_size",
				"style_countdown",
				"style_part",
				"style_zero",
				"style_alarm",
				"style_days",
				"style_hours",
				"style_minutes",
				"style_seconds",
				"on_alarm",
				"on_tick",
				"on_zero",
				"on_blink",
				"on_countdown_create",
			],
			data_attr_mapping={
				"style_countdown": "data-cls-countdown",
				"style_part": "data-cls-part",
				"style_zero": "data-cls-zero",
				"style_alarm": "data-cls-alarm",
				"style_days": "data-cls-days",
				"style_hours": "data-cls-hours",
				"style_minutes": "data-cls-minutes",
				"style_seconds": "data-cls-seconds",
			},
			default_data_attrs={"data-role": "countdown"},
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


_countdown = CountdownComponent()


def render_countdown(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"countdown\".
	Example:
		render_countdown()

	Empty or invalid:
		`render_countdown()` returns `<div data-role="countdown"></div>`.

	"""
	return _countdown.render(content=content, **attrs)
