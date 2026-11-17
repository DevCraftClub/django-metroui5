"""Компонент Metro input-mask."""

from .base import SimpleComponent


class InputMaskComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="input-mask",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"mask",
				"mask_pattern",
				"mask_placeholder",
				"mask_editable_start",
				"threshold_interval",
				"on_char",
				"on_input_mask_create",
			],
			data_attr_mapping={},
			default_data_attrs={"data-role": "input, input-mask"},
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


_input_mask_component = InputMaskComponent()


def render_input_mask(**attrs):
	"""Возвращает input для input-mask."""
	return _input_mask_component.render(**attrs)
