"""
MetroUI Button Component
"""

from ..css import merge_css_classes
from ..html import render_tag


def render_button(content, button_type="default", size=None, outline=False, **attrs):
	"""
	Renders MetroUI button component.

	Args:
		content: Button text
		button_type: Button type (default, primary, secondary, success, danger, warning, info)
		size: Button size (sm, lg)
		outline: Outline style
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"type": "button",
		"class": "button"
	}

	if button_type != "default":
		if outline:
			default_attrs["class"] = merge_css_classes(default_attrs["class"], f"outline-{button_type}")
		else:
			default_attrs["class"] = merge_css_classes(default_attrs["class"], button_type)

	if size:
		default_attrs["class"] = merge_css_classes(default_attrs["class"], f"button-{size}")

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("button", attrs=final_attrs, content=content)
