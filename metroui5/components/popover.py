"""Компонент Metro popover."""

from .base import SimpleComponent


class PopoverComponent(SimpleComponent):
	def __init__(self):
		super().__init__(
			component_name="popover",
			base_css_class=None,
			tag_name="button",
			component_params=[
				"popover_deferred",
				"popover_text",
				"popover_hide",
				"popover_timeout",
				"popover_offset",
				"popover_trigger",
				"popover_position",
				"hide_on_leave",
				"close_button",
				"style_popover",
				"style_popover_content",
			],
			data_attr_mapping={
				"style_popover": "data-cls-popover",
				"style_popover_content": "data-cls-popover-content",
			},
			default_data_attrs={"data-role": "popover"},
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


_popover = PopoverComponent()


def render_popover(content="", **attrs):
	"""Возвращает разметку с data-role=\"popover\"."""
	return _popover.render(content=content, **attrs)
