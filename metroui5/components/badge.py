"""
MetroUI Badge Component
"""

from ..html import render_tag


def render_badge(content, badge_type="default", **attrs):
	"""
	Renders MetroUI badge component.

	Args:
		content: Badge content
		badge_type: Badge type (default, primary, secondary, success, danger, warning, info)
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": f"badge badge-{badge_type}"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("span", attrs=final_attrs, content=content)
