"""Компонент Metro remote-dataset."""

from .base import SimpleComponent


class RemoteDatasetComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="remote_dataset",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"caption",
				"url",
				"url_search",
				"method",
				"limit",
				"offset",
				"sort",
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
				"sort_rules",
				"show_service_block",
				"quick_search",
				"select_order",
				"select_count",
				"show_more",
				"show_pagination",
				"params",
				"search_control",
				"sorting_control",
				"rows_count_control",
				"search_threshold",
				"sort_label",
				"rows_label",
				"search_label",
				"page_mode",
				"style_body",
				"style_pagination",
				"style_search_block",
				"style_order_block",
				"style_rows_count_block",
				"style_service_block",
			],
			data_attr_mapping={
				"style_body": "data-cls-body",
				"style_pagination": "data-cls-pagination",
				"style_search_block": "data-cls-search-block",
				"style_order_block": "data-cls-order-block",
				"style_rows_count_block": "data-cls-rows-count-block",
				"style_service_block": "data-cls-service-block",
			},
			default_data_attrs={"data-role": "remote-dataset"},
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


_remote_dataset = RemoteDatasetComponent()


def render_remote_dataset(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"remote-dataset\".
	Example:
		render_remote_dataset()

	Empty or invalid:
		`render_remote_dataset()` returns `<div data-role="remote-dataset"></div>`.

	"""
	return _remote_dataset.render(content=content, **attrs)
