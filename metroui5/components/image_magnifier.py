"""Компонент Metro image-magnifier."""

from .base import SimpleComponent


class ImageMagnifierComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="image-magnifier",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"image_magnifier_deferred",
				"width",
				"height",
				"lens_size",
				"lens_type",
				"magnifier_zoom",
				"magnifier_mode",
				"magnifier_zoom_element",
				"style_magnifier",
				"style_lens",
				"style_zoom",
				"on_magnifier_move",
				"on_image_magnifier_create",
			],
			data_attr_mapping={
				"style_magnifier": "data-cls-magnifier",
				"style_lens": "data-cls-lens",
				"style_zoom": "data-cls-zoom",
			},
			default_data_attrs={"data-role": "image-magnifier"},
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


_image_magnifier_component = ImageMagnifierComponent()


def render_image_magnifier(content="", **attrs):
	"""
	Возвращает div для image-magnifier.
	Example:
		render_image_magnifier()

	Empty or invalid:
		`render_image_magnifier()` returns `<div data-role="image-magnifier"></div>`.

	"""
	return _image_magnifier_component.render(content, **attrs)
