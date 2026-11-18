"""Компонент Metro marquee."""

from .base import SimpleComponent


class MarqueeComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="marquee",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"items",
				"loop",
				"height",
				"width",
				"duration",
				"direction",
				"ease",
				"mode",
				"accent_pause",
				"first_pause",
				"stop_on_hover",
				"split_by",
				"style_marquee",
				"style_marquee_item",
			],
			data_attr_mapping={
				"style_marquee": "data-cls-marquee",
				"style_marquee_item": "data-cls-marquee-item",
			},
			default_data_attrs={"data-role": "marquee"},
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


_marquee = MarqueeComponent()


def render_marquee(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"marquee\".
	Example:
		render_marquee()

	Empty or invalid:
		`render_marquee()` returns `<div data-role="marquee"></div>`.

	"""
	return _marquee.render(content=content, **attrs)
