"""Компонент Metro hint."""

from .base import SimpleComponent


class HintComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="hint",
			base_css_class=None,
			tag_name="button",
			component_params=[
				"hint_deferred",
				"hint_hide",
				"style_hint",
				"hint_text",
				"hint_position",
				"hint_offset",
				"on_hint_show",
				"on_hint_hide",
				"on_hint_create",
			],
			data_attr_mapping={
				"style_hint": "data-cls-hint",
			},
			default_data_attrs={"data-role": "hint"},
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


_hint = HintComponent()


def render_hint(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"hint\".
	Example:
		render_hint()

	Empty or invalid:
		`render_hint()` returns `<button data-role="hint"></button>`.

	"""
	return _hint.render(content=content, **attrs)
