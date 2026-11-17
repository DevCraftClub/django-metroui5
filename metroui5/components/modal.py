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
	Example:
		render_modal('Text', 'Text')

	Empty or invalid:
		`render_modal('Text', 'Text')` returns `<div class="modal" data-role="modal"><div class='modal-title'>Text</div><div class='modal-content'>Text</div></div>`. An empty call returns `<div class="modal" data-role="modal"><div class='modal-title'></div><div class='modal-content'></div></div>`.

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
