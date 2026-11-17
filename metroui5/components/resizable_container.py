"""Компонент Metro resizable-container."""

from .base import SimpleComponent


class ResizableContainerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="resizable_container",
			base_css_class=None,
			tag_name="div",
			default_data_attrs={"data-role": "resizable-container"},
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


_resizable_container = ResizableContainerComponent()


def render_resizable_container(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"resizable-container\".
	Example:
		render_resizable_container()

	Empty or invalid:
		`render_resizable_container()` returns `<div data-role="resizable-container"></div>`.

	"""
	return _resizable_container.render(content=content, **attrs)
