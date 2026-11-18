"""Компонент Metro hover-box."""

from .base import SimpleComponent


class HoverBoxComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="hover_box",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"on_hover_box_create",
			],
			default_data_attrs={"data-role": "hover-box"},
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


_hover_box = HoverBoxComponent()


def render_hover_box(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"hover-box\".
	Example:
		render_hover_box()

	Empty or invalid:
		`render_hover_box()` returns `<div data-role="hover-box"></div>`.

	"""
	return _hover_box.render(content=content, **attrs)
