"""Компонент Metro resizable."""

from .base import SimpleComponent


class ResizableComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="resizable",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"resizable_deferred",
				"can_resize",
				"resize_element",
				"min_width",
				"min_height",
				"max_width",
				"max_height",
				"preserve_ratio",
			],
			default_data_attrs={"data-role": "resizable"},
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


_resizable = ResizableComponent()


def render_resizable(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"resizable\".
	Example:
		render_resizable()

	Empty or invalid:
		`render_resizable()` returns `<div data-role="resizable"></div>`.

	"""
	return _resizable.render(content=content, **attrs)
