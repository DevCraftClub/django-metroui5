"""
MetroUI Panel Component
"""

from ..html import render_tag


def render_panel(title=None, content=None, **attrs):
	"""
	Renders MetroUI panel component.

	Args:
		title: Panel title
		content: Panel content
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "panel",
		"data-role": "panel"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	panel_parts = []

	if title:
		panel_parts.append(render_tag("div", {"class": "panel-header"}, title))

	if content:
		panel_parts.append(render_tag("div", {"class": "panel-content"}, content))

	if not panel_parts:
		panel_parts.append(render_tag("div", {"class": "panel-content"}, ""))

	return render_tag("div", attrs=final_attrs, content="".join(panel_parts))
