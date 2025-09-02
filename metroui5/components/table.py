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
