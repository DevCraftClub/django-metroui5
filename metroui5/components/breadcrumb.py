"""
MetroUI Breadcrumb Component
"""

from ..html import render_tag


def render_breadcrumb(items, **attrs):
	"""
	Renders MetroUI breadcrumb component.

	Args:
		items: List of breadcrumb items
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "breadcrumb",
		"data-role": "breadcrumb"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	breadcrumb_items = []
	for i, item in enumerate(items):
		if isinstance(item, dict):
			text = item.get('text', '')
			href = item.get('href', '#')
			if i == len(items) - 1:  # Last item
				breadcrumb_items.append(render_tag("li", {"class": "active"}, text))
			else:
				breadcrumb_items.append(render_tag("li", {}, render_tag("a", {"href": href}, text)))
		else:
			if i == len(items) - 1:  # Last item
				breadcrumb_items.append(render_tag("li", {"class": "active"}, str(item)))
			else:
				breadcrumb_items.append(render_tag("li", {}, render_tag("a", {"href": "#"}, str(item))))

	return render_tag("ul", attrs=final_attrs, content="".join(breadcrumb_items))
