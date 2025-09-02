"""
MetroUI Dropdown Component
"""

from ..html import render_tag


def render_dropdown(items, button_text="Dropdown", **attrs):
	"""
	Renders MetroUI dropdown component.

	Args:
		items: List of dropdown items
		button_text: Button text
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "dropdown",
		"data-role": "dropdown"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	button = render_tag("button", {"class": "button dropdown-toggle"}, button_text)
	
	menu_items = []
	for item in items:
		if isinstance(item, dict):
			text = item.get('text', '')
			href = item.get('href', '#')
			menu_items.append(render_tag("li", {}, render_tag("a", {"href": href}, text)))
		else:
			menu_items.append(render_tag("li", {}, render_tag("a", {"href": "#"}, str(item))))
	
	menu = render_tag("ul", {"class": "dropdown-menu"}, "".join(menu_items))
	
	return render_tag("div", attrs=final_attrs, content=button + menu)
