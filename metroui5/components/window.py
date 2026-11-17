"""Компонент Metro window."""

from .base import SimpleComponent


class WindowComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="window",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"window_deferred",
				"hidden",
				"width",
				"height",
				"btn_close",
				"btn_min",
				"btn_max",
				"draggable",
				"drag_element",
				"drag_area",
				"shadow",
				"icon",
				"title",
				"attr_content",
				"resizable",
				"overlay",
				"overlay_color",
				"overlay_alpha",
				"modal",
				"position",
				"check_embed",
				"top",
				"left",
				"place",
				"close_action",
				"custom_buttons",
				"status",
				"can_close",
				"can_maximize",
				"can_minimize",
				"style_custom_button",
				"style_caption",
				"style_content",
				"style_window",
				"min_width",
				"min_height",
				"max_width",
				"max_height",
			],
			data_attr_mapping={
				"attr_content": "data-content",
				"style_custom_button": "data-cls-custom-button",
				"style_caption": "data-cls-caption",
				"style_content": "data-cls-content",
				"style_window": "data-cls-window",
			},
			default_data_attrs={"data-role": "window"},
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


_window = WindowComponent()


def render_window(content="", **attrs):
	"""Возвращает разметку с data-role=\"window\"."""
	return _window.render(content=content, **attrs)
