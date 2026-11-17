"""Компонент Metro lightbox."""

from .base import SimpleComponent


class LightboxComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="lightbox",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"loop",
				"source",
				"icon_close",
				"icon_prev",
				"icon_next",
				"style_next",
				"style_prev",
				"style_close",
				"style_image",
				"style_image_container",
				"style_image_wrapper",
				"style_lightbox",
				"on_draw_image",
				"on_lightbox_create",
			],
			data_attr_mapping={
				"style_next": "data-cls-next",
				"style_prev": "data-cls-prev",
				"style_close": "data-cls-close",
				"style_image": "data-cls-image",
				"style_image_container": "data-cls-image-container",
				"style_image_wrapper": "data-cls-image-wrapper",
				"style_lightbox": "data-cls-lightbox",
			},
			default_data_attrs={"data-role": "lightbox"},
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


_lightbox_component = LightboxComponent()


def render_lightbox(content="", **attrs):
	"""Возвращает div для lightbox."""
	return _lightbox_component.render(content, **attrs)
