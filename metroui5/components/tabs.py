"""
MetroUI Tabs Component
"""

from ..html import render_tag


def render_tabs(tabs, **attrs):
	"""
	Renders MetroUI tabs component.

	Args:
		tabs: List of tab dictionaries with 'title' and 'content' keys
		**attrs: Additional HTML attributes
	"""
	list_attrs = {"data-role": "tabs", **attrs}

	tab_headers = []
	tab_contents = []

	for i, tab in enumerate(tabs):
		title = tab.get('title', f'Tab {i+1}')
		content = tab.get('content', '')
		active = tab.get('active', False)
		item_attrs = {"class": "active"} if active else {}
		tab_headers.append(render_tag(
			"li", item_attrs, render_tag("a", {"href": f"#tab-{i}"}, title)
		))
		tab_contents.append(render_tag("div", {"id": f"tab-{i}"}, content))

	headers_list = render_tag("ul", list_attrs, "".join(tab_headers))
	contents_div = render_tag("div", {"class": "tabs-targets"}, "".join(tab_contents))
	return headers_list + contents_div
