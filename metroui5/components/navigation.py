"""
MetroUI Navigation Component
"""

from ..html import render_tag


def render_navigation(items, **attrs):
	"""
	Renders MetroUI navigation component.

	Args:
		items: List of navigation items
		**attrs: Additional HTML attributes
	Example:
		render_navigation([{'text': 'One', 'href': '/one'}])

	Empty or invalid:
		`render_navigation([{'text': 'One', 'href': '/one'}])` returns `<ul class="navigation" data-role="navigation"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="navigation" data-role="navigation"></ul>`.

	"""
	default_attrs = {
		"class": "navigation",
		"data-role": "navigation"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	nav_items = []
	for item in items:
		if isinstance(item, dict):
			text = item.get('text', '')
			href = item.get('href', '#')
			icon = item.get('icon', '')
			content = f"<span class='{icon}'></span> {text}" if icon else text
			nav_items.append(render_tag("li", {}, render_tag("a", {"href": href}, content)))
		else:
			nav_items.append(render_tag("li", {}, render_tag("a", {"href": "#"}, str(item))))

	return render_tag("ul", attrs=final_attrs, content="".join(nav_items))
