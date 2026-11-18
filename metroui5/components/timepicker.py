"""Компонент Metro timepicker."""

from .base import SimpleComponent


class TimepickerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="timepicker",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"label",
				"timepicker_deferred",
				"hours_step",
				"minutes_step",
				"seconds_step",
				"value",
				"distance",
				"hours",
				"minutes",
				"seconds",
				"show_labels",
				"scroll_speed",
				"copy_inline_styles",
				"open_mode",
				"style_picker",
				"style_part",
				"style_hours",
				"style_minutes",
				"style_seconds",
				"style_label",
				"style_button",
				"style_ok_button",
				"style_cancel_button",
				"ok_button_icon",
				"cancel_button_icon",
			],
			data_attr_mapping={
				"style_picker": "data-cls-picker",
				"style_part": "data-cls-part",
				"style_hours": "data-cls-hours",
				"style_minutes": "data-cls-minutes",
				"style_seconds": "data-cls-seconds",
				"style_label": "data-cls-label",
				"style_button": "data-cls-button",
				"style_ok_button": "data-cls-ok-button",
				"style_cancel_button": "data-cls-cancel-button",
			},
			default_data_attrs={"data-role": "time-picker"},
		)

	def render(self, **attrs):
		cleaned = {}
		for key, value in attrs.items():
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
		id_attr = self.build_id_attribute(
			component_attrs, standard_attrs, auto_generate=False
		)
		if id_attr:
			final_attrs["id"] = id_attr
		return self.render_component(self.tag_name, final_attrs, close=False)


_timepicker_component = TimepickerComponent()


def render_timepicker(**attrs):
	"""
	Возвращает input для timepicker.
	Example:
		render_timepicker()

	Empty or invalid:
		`render_timepicker()` returns `<input data-role="time-picker">`.

	"""
	return _timepicker_component.render(**attrs)
