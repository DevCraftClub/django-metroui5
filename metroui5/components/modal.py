"""
MetroUI Modal Component
"""

from ..html import render_tag


def render_modal(title, content, **attrs):
	"""
	Renders MetroUI modal component.

	Args:
		title: Modal title
		content: Modal content
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "modal",
		"data-role": "modal"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	modal_content = f"<div class='modal-title'>{title}</div>"
	modal_content += f"<div class='modal-content'>{content}</div>"

	return render_tag("div", attrs=final_attrs, content=modal_content)
