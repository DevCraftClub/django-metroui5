"""Компонент Metro page-control."""

from .base import SimpleComponent


class PageControlComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="page-control",
			base_css_class=None,
			tag_name="ul",
			component_params=[
				"append_button",
				"tabs_position",
				"custom_buttons",
				"activate_new_tab",
				"default_new_tab_title",
				"default_new_can_close",
				"default_new_tab_icon",
				"default_new_tab_image",
				"default_new_tab_position",
				"append_actions",
				"tabs_actions",
				"tab_actions",
				"ref_control",
			],
			data_attr_mapping={},
			default_data_attrs={"data-role": "page-control"},
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


_page_control_component = PageControlComponent()


def render_page_control(content="", **attrs):
	"""Возвращает ul для page-control."""
	return _page_control_component.render(content, **attrs)
