"""Компонент Metro wizard-classic."""

from .base import SimpleComponent


class WizardClassicComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="wizard-classic",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"buttons",
				"start_page",
				"height",
				"label_next",
				"label_prev",
				"label_help",
				"label_finish",
				"label_cancel",
				"icon_next",
				"icon_prev",
				"icon_help",
				"icon_finish",
				"icon_cancel",
				"style_wizard",
				"style_page",
				"style_actions",
				"style_action_help",
				"style_action_prev",
				"style_action_next",
				"style_action_finish",
				"style_action_cancel",
			],
			data_attr_mapping={
				"style_wizard": "data-cls-wizard",
				"style_page": "data-cls-page",
				"style_actions": "data-cls-actions",
				"style_action_help": "data-cls-action-help",
				"style_action_prev": "data-cls-action-prev",
				"style_action_next": "data-cls-action-next",
				"style_action_finish": "data-cls-action-finish",
				"style_action_cancel": "data-cls-action-cancel",
			},
			default_data_attrs={"data-role": "wizard-classic"},
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


_wizard_classic_component = WizardClassicComponent()


def render_wizard_classic(content="", **attrs):
	"""Возвращает div для wizard-classic."""
	return _wizard_classic_component.render(content, **attrs)
