"""Компонент Metro gauge."""

from .base import SimpleComponent


class GaugeComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="gauge",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"min",
				"max",
				"value",
				"size",
				"label_min",
				"label_max",
				"label",
				"suffix",
				"values",
				"segments",
				"start_angle",
				"range",
				"theme",
			],
			default_data_attrs={"data-role": "gauge"},
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


_gauge = GaugeComponent()


def render_gauge(content="", **attrs):
	"""Возвращает разметку с data-role=\"gauge\"."""
	return _gauge.render(content=content, **attrs)
