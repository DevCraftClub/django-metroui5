"""Компонент Metro radio."""

from .base import SimpleComponent


class RadioComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="radio",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"radio_deferred",
				"prepend",
				"append",
				"caption",
				"style_radio",
				"style_caption",
				"style_prepend",
				"style_append",
				"on_radio_create",
			],
			data_attr_mapping={
				"style_radio": "data-cls-radio",
				"style_caption": "data-cls-caption",
				"style_prepend": "data-cls-prepend",
				"style_append": "data-cls-append",
			},
			default_data_attrs={"data-role": "radio", "type": "radio"},
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


_radio_component = RadioComponent()


def render_radio(**attrs):
	"""Возвращает input для radio."""
	return _radio_component.render(**attrs)
