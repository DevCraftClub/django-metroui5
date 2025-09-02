"""
MetroUI Card Component
"""

from ..html import render_tag


def render_card(header=None, content=None, footer=None, **attrs):
	"""
	Renders MetroUI card component.

	Args:
		header: Card header
		content: Card content
		footer: Card footer
		**attrs: Additional HTML attributes
	"""
	default_attrs = {"class": "card"}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	card_parts = []

	if header:
		card_parts.append(render_tag("div", {"class": "card-header"}, header))

	if content:
		card_parts.append(render_tag("div", {"class": "card-content"}, content))

	if footer:
		card_parts.append(render_tag("div", {"class": "card-footer"}, footer))

	if not card_parts:
		card_parts.append(render_tag("div", {"class": "card-content"}, ""))

	return render_tag("div", attrs=final_attrs, content="".join(card_parts))
