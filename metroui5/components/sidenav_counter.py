"""Компонент Metro sidenav-counter."""

from .base import SimpleComponent


class SidenavCounterComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="sidenav_counter",
			base_css_class=None,
			tag_name="ul",
			component_params=[
				"compacted",
				"toggle",
				"expand_point",
				"on_menu_item_click",
				"on_collapse",
				"on_expand",
				"on_sidenav_create",
			],
			default_data_attrs={"data-role": "sidenav-counter"},
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


_sidenav_counter = SidenavCounterComponent()


def render_sidenav_counter(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"sidenav-counter\".
	Example:
		render_sidenav_counter()

	Empty or invalid:
		`render_sidenav_counter()` returns `<ul data-role="sidenav-counter"></ul>`.

	"""
	return _sidenav_counter.render(content=content, **attrs)
