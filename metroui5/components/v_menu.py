"""Компонент Metro v-menu."""

from .base import SimpleComponent


class VMenuComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="v-menu",
			base_css_class="v-menu",
			tag_name="ul",
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


_v_menu_component = VMenuComponent()


def render_v_menu(content="", **attrs):
	"""
	Возвращает ul для v-menu.
	Example:
		render_v_menu()

	Empty or invalid:
		`render_v_menu()` returns `<ul class="v-menu"></ul>`.

	"""
	return _v_menu_component.render(content, **attrs)
