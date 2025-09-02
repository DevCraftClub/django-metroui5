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
	default_attrs = {
		"class": "tabs",
		"data-role": "tabs"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	tab_headers = []
	tab_contents = []

	for i, tab in enumerate(tabs):
		title = tab.get('title', f'Tab {i+1}')
		content = tab.get('content', '')
		active = tab.get('active', False)

		# Build tab header
		header_classes = ["tab"]
		if active:
			header_classes.append("active")
		
		tab_headers.append(render_tag("li", {"class": " ".join(header_classes)}, 
			render_tag("a", {"href": f"#tab-{i}"}, title)))

		# Build tab content
		content_classes = ["tab-content"]
		if active:
			content_classes.append("active")
		
		tab_contents.append(render_tag("div", {
			"class": " ".join(content_classes),
			"id": f"tab-{i}"
		}, content))

	# Combine headers and contents
	headers_list = render_tag("ul", {"class": "tab-headers"}, "".join(tab_headers))
	contents_div = render_tag("div", {"class": "tab-contents"}, "".join(tab_contents))

	return render_tag("div", attrs=final_attrs, content=headers_list + contents_div)
