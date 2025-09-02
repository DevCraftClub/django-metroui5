"""
MetroUI Alert Component
"""

from ..css import merge_css_classes
from ..html import render_tag


def render_alert(content, alert_type="info", dismissible=False, **attrs):
	"""
	Renders MetroUI alert component.

	Args:
		content: Alert content
		alert_type: Alert type (info, success, warning, danger, error)
		dismissible: Whether alert can be dismissed
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": f"alert alert-{alert_type}",
		"role": "alert"
	}

	if dismissible:
		default_attrs["class"] = merge_css_classes(default_attrs["class"], "alert-dismissible")

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	if dismissible:
		close_button = render_tag(
			"button",
			{
				"type": "button",
				"class": "button button-mini",
				"data-role": "close",
				"aria-label": "Close"
			},
			"&times;"
		)
		content = f"{content}{close_button}"

	return render_tag("div", attrs=final_attrs, content=content)
