"""Компонент Metro tabs-material."""

from .base import SimpleComponent


class TabsMaterialComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="tabs-material",
			base_css_class=None,
			tag_name="ul",
			component_params=[
				"wheel_step",
				"material_tabs_deferred",
				"deep",
				"fixed_tabs",
				"duration",
				"app_bar",
				"style_component",
				"style_tabs",
				"style_tab",
				"style_tab_active",
				"style_marker",
			],
			data_attr_mapping={
				"style_component": "data-cls-component",
				"style_tabs": "data-cls-tabs",
				"style_tab": "data-cls-tab",
				"style_tab_active": "data-cls-tab-active",
				"style_marker": "data-cls-marker",
			},
			default_data_attrs={"data-role": "materialtabs"},
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


_tabs_material_component = TabsMaterialComponent()


def render_tabs_material(content="", **attrs):
	"""
	Возвращает ul для tabs-material.
	Example:
		render_tabs_material()

	Empty or invalid:
		`render_tabs_material()` returns `<ul data-role="materialtabs"></ul>`.

	"""
	return _tabs_material_component.render(content, **attrs)
