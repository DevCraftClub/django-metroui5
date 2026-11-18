"""Компонент Metro viewport-check."""

from .base import SimpleComponent


class ViewportCheckComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="viewport_check",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"on_viewport",
				"on_viewport_enter",
				"on_viewport_leave",
				"on_viewport_check_create",
			],
			default_data_attrs={"data-role": "viewport-check"},
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


_viewport_check = ViewportCheckComponent()


def render_viewport_check(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"viewport-check\".
	Example:
		render_viewport_check()

	Empty or invalid:
		`render_viewport_check()` returns `<div data-role="viewport-check"></div>`.

	"""
	return _viewport_check.render(content=content, **attrs)
