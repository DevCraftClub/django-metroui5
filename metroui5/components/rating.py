"""
MetroUI Rating Component
"""

from ..html import render_tag


def render_rating(value, max_value=5, **attrs):
	"""
	Renders MetroUI rating component.

	Args:
		value: Current rating value
		max_value: Maximum rating value
		**attrs: Additional HTML attributes
	Example:
		render_rating(0)

	Empty or invalid:
		`render_rating(0)` returns `<input class="rating" data-role="rating" data-value="0" data-stars="5">`. An empty call returns `<input class="rating" data-role="rating" data-value="0" data-stars="0">`.

	"""
	default_attrs = {
		"class": "rating",
		"data-role": "rating",
		"data-value": str(value),
		"data-stars": str(max_value),
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("input", attrs=final_attrs, close=False)
