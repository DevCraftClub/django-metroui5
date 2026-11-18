"""Компонент Metro tag-input."""

from .base import SimpleComponent


class TagInputComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="tag_input",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"autocomplete",
				"autocomplete_unique",
				"autocomplete_url",
				"autocomplete_url_method",
				"autocomplete_url_key",
				"autocomplete_divider",
				"autocomplete_list_height",
				"label",
				"size",
				"tag_input_deferred",
				"static",
				"clear_button",
				"clear_button_icon",
				"random_color",
				"max_tags",
				"tag_separator",
				"tag_trigger",
				"backspace",
				"style_component",
				"style_input",
				"style_clear_button",
				"style_tag",
				"style_tag_title",
				"style_tag_action",
				"style_label",
			],
			data_attr_mapping={
				"style_component": "data-cls-component",
				"style_input": "data-cls-input",
				"style_clear_button": "data-cls-clear-button",
				"style_tag": "data-cls-tag",
				"style_tag_title": "data-cls-tag-title",
				"style_tag_action": "data-cls-tag-action",
				"style_label": "data-cls-label",
			},
			default_data_attrs={"data-role": "tag-input"},
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


_tag_input = TagInputComponent()


def render_tag_input(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"tag-input\".
	Example:
		render_tag_input()

	Empty or invalid:
		`render_tag_input()` returns `<input data-role="tag-input">`.

	"""
	return _tag_input.render(content=content, **attrs)
