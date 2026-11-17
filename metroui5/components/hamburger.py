"""Компонент Metro hamburger."""

from .base import SimpleComponent


class HamburgerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="hamburger",
			base_css_class="hamburger",
			tag_name="button",
			component_params=[],
			data_attr_mapping={},
			default_data_attrs={},
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


_hamburger_component = HamburgerComponent()


def render_hamburger(content="", **attrs):
	"""
	Возвращает button для hamburger.
	Example:
		render_hamburger()

	Empty or invalid:
		`render_hamburger()` returns `<button class="hamburger"></button>`.

	"""
	return _hamburger_component.render(content, **attrs)
