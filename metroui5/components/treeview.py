"""Компонент Metro treeview."""

from .base import SimpleComponent


class TreeviewComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="treeview",
			base_css_class=None,
			tag_name="ul",
			component_params=[
				"treeview_deferred",
				"show_child_count",
				"duration",
				"hide_actions_on_leave",
				"recheck_timeout",
				"leaves",
				"on_node_click",
				"on_node_dbl_click",
				"on_node_delete",
				"on_node_insert",
				"on_node_clean",
				"on_check_click",
				"on_radio_click",
				"on_expand_node",
				"on_collapse_node",
				"on_tree_view_create",
			],
			data_attr_mapping={},
			default_data_attrs={"data-role": "treeview"},
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


_treeview_component = TreeviewComponent()


def render_treeview(content="", **attrs):
	"""Возвращает ul для treeview."""
	return _treeview_component.render(content, **attrs)
