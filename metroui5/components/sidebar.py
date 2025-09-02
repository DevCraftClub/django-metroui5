"""
MetroUI Sidebar Component
"""

from ..html import render_tag


def render_sidebar(items, **attrs):
	"""
	Renders MetroUI sidebar component.

	Args:
		items: List of sidebar items
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "sidebar",
		"data-role": "sidebar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	sidebar_items = []
	for item in items:
		if isinstance(item, dict):
			text = item.get('text', '')
			href = item.get('href', '#')
			icon = item.get('icon', '')
			content = f"<span class='{icon}'></span> {text}" if icon else text
			sidebar_items.append(render_tag("li", {}, render_tag("a", {"href": href}, content)))
		else:
			sidebar_items.append(render_tag("li", {}, render_tag("a", {"href": "#"}, str(item))))

	return render_tag("ul", attrs=final_attrs, content="".join(sidebar_items))
