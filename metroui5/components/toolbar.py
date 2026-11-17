"""
MetroUI Toolbar Component
"""

from ..html import render_tag


def render_toolbar(items, **attrs):
	"""
	Renders MetroUI toolbar component.

	Args:
		items: List of toolbar items
		**attrs: Additional HTML attributes
	Example:
		render_toolbar([{'text': 'One', 'href': '/one'}])

	Empty or invalid:
		`render_toolbar([{'text': 'One', 'href': '/one'}])` returns `<ul class="toolbar" data-role="toolbar"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="toolbar" data-role="toolbar"></ul>`.

	"""
	default_attrs = {
		"class": "toolbar",
		"data-role": "toolbar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	toolbar_items = []
	for item in items:
		if isinstance(item, dict):
			text = item.get('text', '')
			href = item.get('href', '#')
			icon = item.get('icon', '')
			content = f"<span class='{icon}'></span> {text}" if icon else text
			toolbar_items.append(render_tag("li", {}, render_tag("a", {"href": href}, content)))
		else:
			toolbar_items.append(render_tag("li", {}, render_tag("a", {"href": "#"}, str(item))))

	return render_tag("ul", attrs=final_attrs, content="".join(toolbar_items))
