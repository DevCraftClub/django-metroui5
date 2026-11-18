"""Компонент Metro textarea."""

from .base import SimpleComponent


class TextareaComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="textarea",
			base_css_class=None,
			tag_name="textarea",
			component_params=[
				"label",
				"textarea_deferred",
				"chars_counter",
				"chars_counter_template",
				"default_value",
				"prepend",
				"append",
				"clear_button",
				"clear_button_icon",
				"auto_size",
				"max_height",
				"style_prepend",
				"style_append",
				"style_component",
				"style_textarea",
				"style_label",
			],
			data_attr_mapping={
				"style_prepend": "data-cls-prepend",
				"style_append": "data-cls-append",
				"style_component": "data-cls-component",
				"style_textarea": "data-cls-textarea",
				"style_label": "data-cls-label",
			},
			default_data_attrs={"data-role": "textarea"},
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


_textarea = TextareaComponent()


def render_textarea(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"textarea\".
	Example:
		render_textarea()

	Empty or invalid:
		`render_textarea()` returns `<textarea data-role="textarea"></textarea>`.

	"""
	return _textarea.render(content=content, **attrs)
