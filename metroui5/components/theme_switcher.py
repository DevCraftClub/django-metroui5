"""Компонент Metro theme-switcher."""

from .base import SimpleComponent


class ThemeSwitcherComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="theme_switcher",
			base_css_class=None,
			tag_name="input",
			component_params=[
				"state",
				"target",
				"save_state",
				"save_state_key",
				"style_dark",
				"dark_symbol",
				"light_symbol",
				"mode",
			],
			data_attr_mapping={
				"style_dark": "data-cls-dark",
			},
			default_data_attrs={"data-role": "theme-switcher"},
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
		return self.render_component(self.tag_name, final_attrs, content=content, close=False)


_theme_switcher = ThemeSwitcherComponent()


def render_theme_switcher(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"theme-switcher\".
	Example:
		render_theme_switcher()

	Empty or invalid:
		`render_theme_switcher()` returns `<input data-role="theme-switcher">`.

	"""
	return _theme_switcher.render(content=content, **attrs)
