"""
MetroUI Table Component
"""

from ..html import render_tag


def render_table(headers, rows, **attrs):
	"""
	Renders MetroUI table component.

	Args:
		headers: List of header texts
		rows: List of rows (each row is a list of cells)
		**attrs: Additional HTML attributes
	Example:
		render_table(['Name'], [['One']])

	Empty or invalid:
		`render_table(['Name'], [['One']])` returns `<table class="table" data-role="table"><tr><th>Name</th></tr><tr><td>One</td></tr></table>`. An empty call returns `<table class="table" data-role="table"><tr></tr></table>`.

	"""
	default_attrs = {
		"class": "table",
		"data-role": "table"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	# Build header row
	header_cells = []
	for header in headers:
		header_cells.append(render_tag("th", {}, str(header)))
	header_row = render_tag("tr", {}, "".join(header_cells))

	# Build data rows
	data_rows = []
	for row in rows:
		row_cells = []
		for cell in row:
			row_cells.append(render_tag("td", {}, str(cell)))
		data_rows.append(render_tag("tr", {}, "".join(row_cells)))

	# Combine all rows
	all_rows = header_row + "".join(data_rows)

	return render_tag("table", attrs=final_attrs, content=all_rows)
