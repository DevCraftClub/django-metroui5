"""Компонент Metro master."""

from .base import SimpleComponent


class MasterComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="master",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"master_deferred",
				"effect",
				"effect_func",
				"duration",
				"control_prev",
				"control_next",
				"control_title",
				"background_image",
				"style_master",
				"style_controls",
				"style_control_prev",
				"style_control_next",
				"style_control_title",
				"style_pages",
				"style_page",
				"on_before_page",
				"on_before_next",
				"on_before_prev",
				"on_next_page",
				"on_prev_page",
				"on_master_create",
			],
			data_attr_mapping={
				"style_master": "data-cls-master",
				"style_controls": "data-cls-controls",
				"style_control_prev": "data-cls-control-prev",
				"style_control_next": "data-cls-control-next",
				"style_control_title": "data-cls-control-title",
				"style_pages": "data-cls-pages",
				"style_page": "data-cls-page",
			},
			default_data_attrs={"data-role": "master"},
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


_master_component = MasterComponent()


def render_master(content="", **attrs):
	"""
	Возвращает div для master.
	Example:
		render_master()

	Empty or invalid:
		`render_master()` returns `<div data-role="master"></div>`.

	"""
	return _master_component.render(content, **attrs)
