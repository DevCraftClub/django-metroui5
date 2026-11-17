"""Компонент Metro package-manager."""

from .base import SimpleComponent


class PackageManagerComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="package_manager",
			base_css_class=None,
			tag_name="div",
			component_params=[
				"link",
				"deps",
				"package",
			],
			default_data_attrs={"data-role": "package-manager"},
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


_package_manager = PackageManagerComponent()


def render_package_manager(content="", **attrs):
	"""Возвращает разметку с data-role=\"package-manager\"."""
	return _package_manager.render(content=content, **attrs)
