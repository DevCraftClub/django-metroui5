"""Компонент Metro linked-block."""

from .base import SimpleComponent


class LinkedBlockComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="linked_block",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"width",
				"height",
				"min_width",
				"min_height",
				"max_width",
				"max_height",
				"attr_content",
				"show_add_buttons",
				"add_buttons",
				"resize_hotkey",
				"drag_hotkey",
				"connection_type",
				"connection_style",
				"one_point",
				"can_drag",
				"can_resize",
				"on_add_point",
				"on_remove_point",
				"on_start_connection",
				"on_cancel_connection",
				"on_connect",
				"on_disconnect",
				"on_drag_start",
				"on_drag_move",
				"on_drag_end",
				"on_resize",
				"on_linked_block_create",
			],
			data_attr_mapping={
				"attr_content": "data-content",
			},
			default_data_attrs={"data-role": "linked-block"},
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


_linked_block = LinkedBlockComponent()


def render_linked_block(content="", **attrs):
	"""Возвращает разметку с data-role=\"linked-block\"."""
	return _linked_block.render(content=content, **attrs)
