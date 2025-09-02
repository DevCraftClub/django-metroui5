"""
MetroUI Menu Component
"""

from ..html import render_tag


def render_menu(items, **attrs):
	"""
	Renders MetroUI menu component.

	Args:
		items: List of menu items
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "menu",
		"data-role": "menu"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	menu_items = []
	for item in items:
		if isinstance(item, dict):
			text = item.get('text', '')
			href = item.get('href', '#')
			icon = item.get('icon', '')
			content = f"<span class='{icon}'></span> {text}" if icon else text
			menu_items.append(render_tag("li", {}, render_tag("a", {"href": href}, content)))
		else:
			menu_items.append(render_tag("li", {}, render_tag("a", {"href": "#"}, str(item))))

	return render_tag("ul", attrs=final_attrs, content="".join(menu_items))
