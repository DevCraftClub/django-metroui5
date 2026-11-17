"""Поле с шагом: число и кнопки плюс и минус."""

from .base import SimpleComponent


class SpinnerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="spinner",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"spinner_deferred",
				"label",
				"step",
				"plus_icon",
				"minus_icon",
				"buttons_position",
				"default_value",
				"min_value",
				"max_value",
				"fixed",
				"repeat_threshold",
				"hide_cursor",
				"spinner_class",
				"spinner_input_class",
				"spinner_button_class",
				"spinner_button_plus_class",
				"spinner_button_minus_class",
				"label_class",
			],
			data_attr_mapping={
				"spinner_class": "data-cls-spinner",
				"spinner_input_class": "data-cls-spinner-input",
				"spinner_button_class": "data-cls-spinner-button",
				"spinner_button_plus_class": "data-cls-spinner-button-plus",
				"spinner_button_minus_class": "data-cls-spinner-button-minus",
				"label_class": "data-cls-label",
			},
			default_data_attrs={"data-role": "spinner"},
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


_spinner_component = SpinnerComponent()


def render_spinner(**attrs):
	"""Возвращает input с data-role=\"spinner\" и переданными параметрами."""
	return _spinner_component.render(**attrs)
