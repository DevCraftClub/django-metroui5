"""
MetroUI Progress Component
"""

from ..css import merge_css_classes
from ..html import render_tag


def render_progress(value, max_value=100, color="blue", size="default", **attrs):
	"""
	Renders MetroUI progress bar component.

	Args:
		value: Current value
		max_value: Maximum value
		color: Progress bar color
		size: Size (mini, small, large)
		**attrs: Additional HTML attributes
	Example:
		render_progress(0)

	Empty or invalid:
		`render_progress(0)` returns `<div class="progress progress-blue" data-role="progress" data-value="0" data-max="100"></div>`. An empty call returns `<div class="progress progress-blue progress-0" data-role="progress" data-value="0" data-max="0"></div>`.

	"""
	default_attrs = {
		"class": f"progress progress-{color}",
		"data-role": "progress",
		"data-value": str(value),
		"data-max": str(max_value)
	}

	if size != "default":
		default_attrs["class"] = merge_css_classes(default_attrs["class"], f"progress-{size}")
	if size == "small":
		default_attrs["data-small"] = "true"

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("div", attrs=final_attrs, content="")
