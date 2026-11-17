"""Компонент Metro listview."""

from .base import SimpleComponent


class ListviewComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="listview",
			base_css_class=None,
			tag_name="ul",
			component_params=[
				"listview_deferred",
				"selectable",
				"duration",
				"view",
				"select_current",
				"default_icon",
				"on_node_insert",
				"on_node_delete",
				"on_node_clean",
				"on_collapse_node",
				"on_expand_node",
				"on_group_node_click",
				"on_node_click",
				"on_node_dblclick",
				"on_list_view_create",
			],
			default_data_attrs={"data-role": "listview"},
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


_listview = ListviewComponent()


def render_listview(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"listview\".
	Example:
		render_listview()

	Empty or invalid:
		`render_listview()` returns `<ul data-role="listview"></ul>`.

	"""
	return _listview.render(content=content, **attrs)
