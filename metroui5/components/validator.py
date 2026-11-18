"""Компонент Metro validator."""

from .base import SimpleComponent


class ValidatorComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="validator",
			base_css_class=None,
			tag_name="form",
			component_params=[
				"validator_deferred",
				"submit_timeout",
				"interactive_check",
				"clear_invalid",
				"required_mode",
				"use_required_class",
				"on_before_submit",
				"on_submit",
				"on_error",
				"on_validate",
				"on_error_form",
				"on_validate_form",
				"on_validator_create",
			],
			data_attr_mapping={},
			default_data_attrs={"data-role": "validator"},
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


_validator_component = ValidatorComponent()


def render_validator(content="", **attrs):
	"""
	Возвращает form для validator.
	Example:
		render_validator()

	Empty or invalid:
		`render_validator()` returns `<form data-role="validator"></form>`.

	"""
	return _validator_component.render(content, **attrs)
