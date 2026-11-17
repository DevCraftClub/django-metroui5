"""Компонент Metro stepper."""

from .base import SimpleComponent


class StepperComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="stepper",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"stepper_deferred",
				"view",
				"steps",
				"step",
				"step_click",
				"style_stepper",
				"style_step",
				"style_complete",
				"style_current",
			],
			data_attr_mapping={
				"style_stepper": "data-cls-stepper",
				"style_step": "data-cls-step",
				"style_complete": "data-cls-complete",
				"style_current": "data-cls-current",
			},
			default_data_attrs={"data-role": "stepper"},
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


_stepper = StepperComponent()


def render_stepper(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"stepper\".
	Example:
		render_stepper()

	Empty or invalid:
		`render_stepper()` returns `<div data-role="stepper"></div>`.

	"""
	return _stepper.render(content=content, **attrs)
