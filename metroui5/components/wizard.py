"""Компонент Metro wizard."""

from .base import SimpleComponent


class WizardComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="wizard",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"start",
				"finish",
				"icon_help",
				"icon_prev",
				"icon_next",
				"icon_finish",
				"button_mode",
				"button_outline",
				"duration",
				"style_wizard",
				"style_actions",
				"style_help",
				"style_prev",
				"style_next",
				"style_finish",
			],
			data_attr_mapping={
				"style_wizard": "data-cls-wizard",
				"style_actions": "data-cls-actions",
				"style_help": "data-cls-help",
				"style_prev": "data-cls-prev",
				"style_next": "data-cls-next",
				"style_finish": "data-cls-finish",
			},
			default_data_attrs={"data-role": "wizard"},
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


_wizard = WizardComponent()


def render_wizard(content="", **attrs):
	"""Возвращает разметку с data-role=\"wizard\"."""
	return _wizard.render(content=content, **attrs)
