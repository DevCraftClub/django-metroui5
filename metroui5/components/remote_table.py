"""Компонент Metro remote-table."""

from .base import SimpleComponent


class RemoteTableComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="remote_table",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"caption",
				"url",
				"url_search",
				"method",
				"limit",
				"offset",
				"fields",
				"sortable_fields",
				"col_size",
				"sort",
				"sort_order",
				"captions",
				"key_limit",
				"key_offset",
				"key_total",
				"key_data",
				"key_sort",
				"key_order",
				"key_search",
				"short_pagination",
				"rows",
				"rows_steps",
				"show_service_block",
				"quick_search",
				"select_order",
				"select_count",
				"show_pagination",
				"params",
				"search_control",
				"rows_count_control",
				"search_threshold",
				"rows_label",
				"search_label",
				"style_table",
				"style_row",
				"style_cell",
				"style_head",
				"style_pagination",
			],
			data_attr_mapping={
				"style_table": "data-cls-table",
				"style_row": "data-cls-row",
				"style_cell": "data-cls-cell",
				"style_head": "data-cls-head",
				"style_pagination": "data-cls-pagination",
			},
			default_data_attrs={"data-role": "remote-table"},
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


_remote_table = RemoteTableComponent()


def render_remote_table(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"remote-table\".
	Example:
		render_remote_table()

	Empty or invalid:
		`render_remote_table()` returns `<div data-role="remote-table"></div>`.

	"""
	return _remote_table.render(content=content, **attrs)
