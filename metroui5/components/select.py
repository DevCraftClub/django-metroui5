"""Компонент Metro select."""

from .base import SimpleComponent


class SelectComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="select",
			base_css_class=None,
			tag_name="select",
			component_params=[
				"id",
				"label",
				"size",
				"select_deferred",
				"clear_button",
				"clear_button_icon",
				"use_placeholder",
				"placeholder",
				"add_empty_value",
				"empty_value",
				"duration",
				"prepend",
				"append",
				"filter_placeholder",
				"filter",
				"drop_height",
				"drop_width",
				"drop_full_size",
				"open_mode",
				"show_group_name",
				"short_tag",
				"source",
				"source_method",
				"source_type",
				"filter_source",
				"filter_threshold",
				"style_select",
				"style_select_input",
				"style_prepend",
				"style_append",
				"style_option",
				"style_option_active",
				"style_option_group",
				"style_drop_list",
				"style_drop_container",
				"style_selected_item",
				"style_selected_item_action",
				"style_label",
				"style_group_name",
				"style_filter_input",
			],
			data_attr_mapping={
				"style_select": "data-cls-select",
				"style_select_input": "data-cls-select-input",
				"style_prepend": "data-cls-prepend",
				"style_append": "data-cls-append",
				"style_option": "data-cls-option",
				"style_option_active": "data-cls-option-active",
				"style_option_group": "data-cls-option-group",
				"style_drop_list": "data-cls-drop-list",
				"style_drop_container": "data-cls-drop-container",
				"style_selected_item": "data-cls-selected-item",
				"style_selected_item_action": "data-cls-selected-item-action",
				"style_label": "data-cls-label",
				"style_group_name": "data-cls-group-name",
				"style_filter_input": "data-cls-filter-input",
			},
			default_data_attrs={"data-role": "select"},
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


_select = SelectComponent()


def render_select(content="", **attrs):
	"""Возвращает разметку с data-role=\"select\"."""
	return _select.render(content=content, **attrs)
