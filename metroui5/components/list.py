"""
MetroUI List Component
"""

from ..html import render_tag


def render_list(items, list_type="ul", **attrs):
	"""
	Renders MetroUI list component.

	Args:
		items: List of items
		list_type: List type (ul, ol)
		**attrs: Additional HTML attributes
	Example:
		render_list([{'text': 'One', 'href': '/one'}])

	Empty or invalid:
		`render_list([{'text': 'One', 'href': '/one'}])` returns `<ul class="list" data-role="list"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="list" data-role="list"></ul>`.

	"""
	default_attrs = {
		"class": "list",
		"data-role": "list"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	list_items = []
	for item in items:
		if isinstance(item, dict):
			text = item.get('text', '')
			href = item.get('href', '#')
			list_items.append(render_tag("li", {}, render_tag("a", {"href": href}, text)))
		else:
			list_items.append(render_tag("li", {}, str(item)))

	return render_tag(list_type, attrs=final_attrs, content="".join(list_items))
