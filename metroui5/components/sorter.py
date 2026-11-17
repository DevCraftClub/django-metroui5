"""Компонент Metro sorter."""

from .base import SimpleComponent


class SorterComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="sorter",
			base_css_class=None,
			tag_name="ul",
			component_params=[
				"sorter_deferred",
				"thousand_separator",
				"decimal_separator",
				"sort_target",
				"sort_source",
				"sort_dir",
				"sort_start",
				"save_initial",
				"on_sort_start",
				"on_sort_stop",
				"on_sort_item_switch",
				"on_sorter_create",
			],
			data_attr_mapping={},
			default_data_attrs={"data-role": "sorter"},
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


_sorter_component = SorterComponent()


def render_sorter(content="", **attrs):
	"""
	Возвращает ul для sorter.
	Example:
		render_sorter()

	Empty or invalid:
		`render_sorter()` returns `<ul data-role="sorter"></ul>`.

	"""
	return _sorter_component.render(content, **attrs)
