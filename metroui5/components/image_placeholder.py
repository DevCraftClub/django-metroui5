"""Компонент Metro image-placeholder."""

from .base import SimpleComponent


class ImagePlaceholderComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="image_placeholder",
			base_css_class=None,
			tag_name="img",
			component_params=[
				"size",
				"width",
				"height",
				"color",
				"text_color",
				"font",
				"text",
				"show_text",
			],
			default_data_attrs={"data-role": "image-placeholder"},
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
		return self.render_component(self.tag_name, final_attrs, content=content, close=False)


_image_placeholder = ImagePlaceholderComponent()


def render_image_placeholder(content="", **attrs):
	"""Возвращает разметку с data-role=\"image-placeholder\"."""
	return _image_placeholder.render(content=content, **attrs)
