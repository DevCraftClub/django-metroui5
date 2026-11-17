"""Компонент Metro working-tree."""

from .base import SimpleComponent


class WorkingTreeComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="working_tree",
			base_css_class=None,
			tag_name="ul",
			component_params=[
				"on_state_change",
				"on_working_tree_create",
			],
			default_data_attrs={"data-role": "working-tree"},
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


_working_tree = WorkingTreeComponent()


def render_working_tree(content="", **attrs):
	"""
	Возвращает разметку с data-role=\"working-tree\".
	Example:
		render_working_tree()

	Empty or invalid:
		`render_working_tree()` returns `<ul data-role="working-tree"></ul>`.

	"""
	return _working_tree.render(content=content, **attrs)
