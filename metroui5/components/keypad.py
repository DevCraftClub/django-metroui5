"""Компонент Metro keypad."""

from .base import SimpleComponent


class KeypadComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="keypad",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"keypad_deferred",
				"label",
				"key_size",
				"keys",
				"except_keys",
				"key_separator",
				"trim_separator",
				"key_delimiter",
				"copy_inline_styles",
				"target",
				"key_length",
				"shuffle",
				"shuffle_count",
				"service_buttons",
				"show_value",
				"open",
				"use_element_size_for_keys",
				"open_mode",
				"style_keypad",
				"style_input",
				"style_keys",
				"style_key",
				"style_service_key",
				"style_backspace",
				"style_clear",
				"style_label",
			],
			data_attr_mapping={
				"style_keypad": "data-cls-keypad",
				"style_input": "data-cls-input",
				"style_keys": "data-cls-keys",
				"style_key": "data-cls-key",
				"style_service_key": "data-cls-service-key",
				"style_backspace": "data-cls-backspace",
				"style_clear": "data-cls-clear",
				"style_label": "data-cls-label",
			},
			default_data_attrs={"data-role": "keypad"},
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


_keypad = KeypadComponent()


def render_keypad(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"keypad\".
	Example:
		render_keypad()

	Empty or invalid:
		`render_keypad()` returns `<input data-role="keypad">`.

	"""
	return _keypad.render(content=content, **attrs)
