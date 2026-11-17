"""Компонент Metro toggle-button."""

from .base import SimpleComponent


class ToggleButtonComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="toggle-button",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"on_change",
				"on_button_click",
				"on_toggle_button_create",
			],
			data_attr_mapping={},
			default_data_attrs={"data-role": "toggle-button"},
		)

	def render(self, content="", **attrs):
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
		return self.render_component(self.tag_name, final_attrs, content, close=True)


_toggle_button_component = ToggleButtonComponent()


def render_toggle_button(content="", **attrs):
	"""
	Возвращает div для toggle-button.
	Example:
		render_toggle_button()

	Empty or invalid:
		`render_toggle_button()` returns `<div data-role="toggle-button"></div>`.

	"""
	return _toggle_button_component.render(content, **attrs)
