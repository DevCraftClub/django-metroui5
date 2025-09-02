"""
MetroUI Dialog Component
"""

from ..html import render_tag


def render_dialog(title, content, **attrs):
	"""
	Renders MetroUI dialog component.

	Args:
		title: Dialog title
		content: Dialog content
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "dialog",
		"data-role": "dialog"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	dialog_content = f"<div class='dialog-title'>{title}</div>"
	dialog_content += f"<div class='dialog-content'>{content}</div>"

	return render_tag("div", attrs=final_attrs, content=dialog_content)
