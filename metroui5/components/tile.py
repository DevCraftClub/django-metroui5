"""
MetroUI Tile Component
"""

from django.utils.html import escape

from .base import SimpleComponent


class TileComponent(SimpleComponent):
	"""
	MetroUI Tile Component
	"""
	
	def __init__(self):
		super().__init__(
			component_name="tile",
			base_css_class="tile",
			tag_name="div",
			component_params=['title', 'content', 'size', 'color', 'icon', 'cls_tile'],
			data_attr_mapping={'icon': 'data-icon'},
			default_data_attrs={"data-role": "tile"}
		)
	
	def render(self, title, content=None, size="medium", color="blue", icon=None, **attrs):
		"""
		Renders MetroUI tile component.

		Args:
			title: Tile title
			content: Additional content
			size: Tile size (small, medium, large, wide, tall)
			color: Tile color
			icon: MetroUI icon
			**attrs: Additional HTML attributes including:
				cls_tile (str): Additional CSS class for the tile
		"""
		# Build additional classes based on parameters
		additional_classes = [f"tile-{size}", f"tile-{color}"]
		
		# Separate attributes. icon — именованный аргумент, в attrs его нет.
		merged = dict(attrs)
		safe_icon = escape(icon) if icon else None
		if safe_icon:
			merged["icon"] = safe_icon
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(merged)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		# Build tile content
		icon_html = ""
		if safe_icon:
			icon_class = safe_icon if str(safe_icon).startswith("mif-") else f"mif-{safe_icon}"
			icon_html = f"<span class='{icon_class} icon'></span>"
		tile_content = icon_html + f"<h3 class='tile-title'>{title}</h3>"
		if content:
			tile_content += f"<small>{content}</small>"
		
		return self.render_component(self.tag_name, final_attrs, content=tile_content)


# Create component instance
_tile_component = TileComponent()


def render_tile(title, content=None, size="medium", color="blue", icon=None, **attrs):
	"""
	Renders MetroUI tile component.

	Args:
		title: Tile title
		content: Additional content
		size: Tile size (small, medium, large, wide, tall)
		color: Tile color
		icon: MetroUI icon
		**attrs: Additional HTML attributes including:
			cls_tile (str): Additional CSS class for the tile
	"""
	return _tile_component.render(title, content, size, color, icon, **attrs)
