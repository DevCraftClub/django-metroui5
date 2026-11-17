"""Компонент Metro ribbon-menu."""

from .base import SimpleComponent


class RibbonMenuComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="ribbon-menu",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"ribbon_menu_deferred",
				"on_static",
				"on_before_tab",
				"on_tab",
				"on_ribbon_menu_create",
			],
			data_attr_mapping={},
			default_data_attrs={"data-role": "ribbon-menu"},
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


_ribbon_menu_component = RibbonMenuComponent()


def render_ribbon_menu(content="", **attrs):
	"""
	Возвращает div для ribbon-menu.
	Example:
		render_ribbon_menu()

	Empty or invalid:
		`render_ribbon_menu()` returns `<div data-role="ribbon-menu"></div>`.

	"""
	return _ribbon_menu_component.render(content, **attrs)
