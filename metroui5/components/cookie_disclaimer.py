"""Компонент Metro cookie-disclaimer."""

from .base import SimpleComponent


class CookieDisclaimerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="cookie-disclaimer",
			base_css_class="cookie-disclaimer",
			tag_name="div",
			component_params=[
				"name",
				"template_url",
				"title",
				"message",
				"duration",
				"style_container",
				"style_message",
				"style_buttons",
				"style_accept_button",
				"style_cancel_button",
				"custom_buttons",
				"on_accept",
				"on_decline",
			],
			data_attr_mapping={
				"style_container": "data-cls-container",
				"style_message": "data-cls-message",
				"style_buttons": "data-cls-buttons",
				"style_accept_button": "data-cls-accept-button",
				"style_cancel_button": "data-cls-cancel-button",
			},
			default_data_attrs={},
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


_cookie_disclaimer_component = CookieDisclaimerComponent()


def render_cookie_disclaimer(content="", **attrs):
	"""Возвращает div для cookie-disclaimer."""
	return _cookie_disclaimer_component.render(content, **attrs)
