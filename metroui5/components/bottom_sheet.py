"""Нижняя панель из примера Metro."""

from .base import SimpleComponent


class BottomSheetComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="bottom-sheet",
			base_css_class="bottom-sheet",
			tag_name="ul",
			component_params=[],
			data_attr_mapping={},
			default_data_attrs={"data-role": "bottomsheet"},
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


_bottom_sheet_component = BottomSheetComponent()


def render_bottom_sheet(content="", **attrs):
	"""Возвращает список с data-role bottomsheet."""
	return _bottom_sheet_component.render(content, **attrs)
