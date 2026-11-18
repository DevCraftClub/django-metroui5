"""
MetroUI Pagination Component
"""

from ..html import render_tag


def render_pagination(current_page, total_pages, **attrs):
	"""
	Renders MetroUI pagination component.

	Args:
		current_page: Current page number
		total_pages: Total number of pages
		**attrs: Additional HTML attributes
	Example:
		render_pagination('Text', ['One'])

	Empty or invalid:
		`render_pagination('Text', ['One'])` raises TypeError: '>' not supported between instances of 'str' and 'int'. An empty call raises TypeError: '>' not supported between instances of 'str' and 'int'.

	"""
	default_attrs = {
		"class": "pagination",
		"data-role": "pagination"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	pagination_items = []

	# Previous button
	if current_page > 1:
		pagination_items.append(render_tag("li", {}, 
			render_tag("a", {"href": f"?page={current_page-1}"}, "&laquo;")))
	else:
		pagination_items.append(render_tag("li", {"class": "disabled"}, 
			render_tag("span", {}, "&laquo;")))

	# Page numbers
	for page in range(1, total_pages + 1):
		if page == current_page:
			pagination_items.append(render_tag("li", {"class": "active"}, 
				render_tag("span", {}, str(page))))
		else:
			pagination_items.append(render_tag("li", {}, 
				render_tag("a", {"href": f"?page={page}"}, str(page))))

	# Next button
	if current_page < total_pages:
		pagination_items.append(render_tag("li", {}, 
			render_tag("a", {"href": f"?page={current_page+1}"}, "&raquo;")))
	else:
		pagination_items.append(render_tag("li", {"class": "disabled"}, 
			render_tag("span", {}, "&raquo;")))

	return render_tag("ul", attrs=final_attrs, content="".join(pagination_items))
