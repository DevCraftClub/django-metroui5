"""Компонент Metro image-grid."""

from .base import SimpleComponent


class ImageGridComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="image-grid",
			base_css_class="image-grid",
			tag_name="div",
			component_params=[
				"use_background",
				"background_size",
				"background_position",
				"style_image_grid",
				"style_image_grid_item",
				"style_image_grid_image",
			],
			data_attr_mapping={
				"style_image_grid": "data-cls-image-grid",
				"style_image_grid_item": "data-cls-image-grid-item",
				"style_image_grid_image": "data-cls-image-grid-image",
			},
			default_data_attrs={"data-role": "image-grid"},
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


_image_grid_component = ImageGridComponent()


def render_image_grid(content="", **attrs):
	"""Возвращает div для image-grid."""
	return _image_grid_component.render(content, **attrs)
