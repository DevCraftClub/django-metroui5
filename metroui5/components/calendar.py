"""
MetroUI Calendar Component
"""

from ..html import render_tag


def render_calendar(**attrs):
	"""
	Renders MetroUI calendar component.

	Args:
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "calendar",
		"data-role": "calendar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("div", attrs=final_attrs, content="")
