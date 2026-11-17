"""Компонент Metro info-box."""

from .base import SimpleComponent


class InfoBoxComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="info-box",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"infobox_deferred",
				"type",
				"width",
				"height",
				"overlay",
				"overlay_color",
				"overlay_alpha",
				"overlay_click_close",
				"auto_hide",
				"remove_on_close",
				"close_button",
				"style_box",
				"style_box_content",
				"style_overlay",
			],
			data_attr_mapping={
				"style_box": "data-cls-box",
				"style_box_content": "data-cls-box-content",
				"style_overlay": "data-cls-overlay",
			},
			default_data_attrs={"data-role": "info-box"},
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


_info_box_component = InfoBoxComponent()


def render_info_box(content="", **attrs):
	"""Возвращает div для info-box."""
	return _info_box_component.render(content, **attrs)
