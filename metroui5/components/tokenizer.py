"""Компонент Metro tokenizer."""

from .base import SimpleComponent


class TokenizerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="tokenizer",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"text_to_tokenize",
				"space_symbol",
				"space_class",
				"token_class",
				"splitter",
				"token_element",
				"use_token_symbol",
				"use_token_index",
				"style_tokenizer",
				"style_token",
				"style_token_odd",
				"style_token_even",
				"prepend",
				"append",
			],
			data_attr_mapping={
				"style_tokenizer": "data-cls-tokenizer",
				"style_token": "data-cls-token",
				"style_token_odd": "data-cls-token-odd",
				"style_token_even": "data-cls-token-even",
			},
			default_data_attrs={"data-role": "tokenizer"},
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


_tokenizer = TokenizerComponent()


def render_tokenizer(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"tokenizer\".
	Example:
		render_tokenizer()

	Empty or invalid:
		`render_tokenizer()` returns `<div data-role="tokenizer"></div>`.

	"""
	return _tokenizer.render(content=content, **attrs)
