"""
MetroUI Tile Component
"""

from ..html import render_tag


def render_tile(title, content=None, size="medium", color="blue", icon=None, **attrs):
	"""
	Renders MetroUI tile component.

	Args:
		title: Tile title
		content: Additional content
		size: Tile size (small, medium, large, wide, tall)
		color: Tile color
		icon: MetroUI icon
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": f"tile tile-{size} tile-{color}",
		"data-role": "tile"
	}

	if icon:
		default_attrs["data-icon"] = icon

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	tile_content = f"<h3 class='tile-title'>{title}</h3>"

	if content:
		tile_content += f"<small>{content}</small>"

	return render_tag("div", attrs=final_attrs, content=tile_content)
