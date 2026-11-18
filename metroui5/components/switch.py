"""Компонент Metro switch."""

from .base import SimpleComponent


class SwitchComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="switch",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"switch_deferred",
				"material",
				"prepend",
				"append",
				"style_switch",
				"style_check",
				"style_caption",
				"onoff",
				"on",
				"off",
			],
			data_attr_mapping={
				"style_switch": "data-cls-switch",
				"style_check": "data-cls-check",
				"style_caption": "data-cls-caption",
			},
			default_data_attrs={"data-role": "switch", "type": "checkbox"},
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


_switch_component = SwitchComponent()


def render_switch(**attrs):
	"""
	Возвращает input для switch.
	Example:
		render_switch()

	Empty or invalid:
		`render_switch()` returns `<input data-role="switch" type="checkbox">`.

	"""
	return _switch_component.render(**attrs)
