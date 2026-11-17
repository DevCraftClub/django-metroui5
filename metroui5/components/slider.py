"""Компонент Metro slider."""

from .base import SimpleComponent


class SliderComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="slider",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"min",
				"max",
				"accuracy",
				"value",
				"buffer",
				"round_value",
				"show_min_max",
				"min_max_position",
				"hint",
				"hint_always",
				"hint_position",
				"hint_mask",
				"vertical",
				"target",
				"return_type",
				"size",
				"label",
				"hide_button",
				"style_slider",
				"style_backside",
				"style_complete",
				"style_buffer",
				"style_marker",
				"style_hint",
				"style_min_max",
				"style_min",
				"style_max",
			],
			data_attr_mapping={
				"style_slider": "data-cls-slider",
				"style_backside": "data-cls-backside",
				"style_complete": "data-cls-complete",
				"style_buffer": "data-cls-buffer",
				"style_marker": "data-cls-marker",
				"style_hint": "data-cls-hint",
				"style_min_max": "data-cls-min-max",
				"style_min": "data-cls-min",
				"style_max": "data-cls-max",
			},
			default_data_attrs={"data-role": "slider"},
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
		return self.render_component(self.tag_name, final_attrs, content=content, close=False)


_slider = SliderComponent()


def render_slider(content="", **attrs):
	"""Возвращает разметку с data-role=\"slider\"."""
	return _slider.render(content=content, **attrs)
