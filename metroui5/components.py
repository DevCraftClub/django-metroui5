"""
MetroUI components for Django.
"""

from .css import merge_css_classes
from .html import render_tag


def render_alert(content, alert_type="info", dismissible=False, **attrs):
	"""
	Renders MetroUI alert component.

	Args:
		content: Alert content
		alert_type: Alert type (info, success, warning, danger, error)
		dismissible: Whether alert can be dismissed
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": f"alert alert-{alert_type}",
		"role": "alert"
	}

	if dismissible:
		default_attrs["class"] = merge_css_classes(default_attrs["class"], "alert-dismissible")

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	if dismissible:
		close_button = render_tag(
			"button",
			{
				"type": "button",
				"class": "button button-mini",
				"data-role": "close",
				"aria-label": "Close"
			},
			"&times;"
		)
		content = f"{content}{close_button}"

	return render_tag("div", attrs=final_attrs, content=content)


def render_button(content, button_type="default", size=None, outline=False, **attrs):
	"""
	Renders MetroUI button component.

	Args:
		content: Button text
		button_type: Button type (default, primary, secondary, success, danger, warning, info)
		size: Button size (sm, lg)
		outline: Outline style
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"type": "button",
		"class": "button"
	}

	if button_type != "default":
		if outline:
			default_attrs["class"] = merge_css_classes(default_attrs["class"], f"outline-{button_type}")
		else:
			default_attrs["class"] = merge_css_classes(default_attrs["class"], button_type)

	if size:
		default_attrs["class"] = merge_css_classes(default_attrs["class"], f"button-{size}")

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("button", attrs=final_attrs, content=content)


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


def render_card(header=None, content=None, footer=None, **attrs):
	"""
	Renders MetroUI card component.

	Args:
		header: Card header
		content: Card content
		footer: Card footer
		**attrs: Additional HTML attributes
	"""
	default_attrs = {"class": "card"}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	card_parts = []

	if header:
		card_parts.append(render_tag("div", {"class": "card-header"}, header))

	if content:
		card_parts.append(render_tag("div", {"class": "card-content"}, content))

	if footer:
		card_parts.append(render_tag("div", {"class": "card-footer"}, footer))

	if not card_parts:
		card_parts.append(render_tag("div", {"class": "card-content"}, ""))

	return render_tag("div", attrs=final_attrs, content="".join(card_parts))


def render_progress(value, max_value=100, color="blue", size="default", **attrs):
	"""
	Renders MetroUI progress bar component.

	Args:
		value: Current value
		max_value: Maximum value
		color: Progress bar color
		size: Size (mini, small, large)
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": f"progress progress-{color}",
		"data-role": "progress",
		"data-value": str(value),
		"data-max": str(max_value)
	}

	if size != "default":
		default_attrs["class"] = merge_css_classes(default_attrs["class"], f"progress-{size}")

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("div", attrs=final_attrs, content="")


def render_accordion(items, **attrs):
	"""
	Renders MetroUI accordion component.

	Args:
		items: List of dictionaries with 'title' and 'content' keys
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "accordion",
		"data-role": "accordion"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	accordion_items = []
	for i, item in enumerate(items):
		item_html = render_tag(
			"div",
			{"class": "accordion-frame"},
			render_tag("a", {"class": "accordion-title", "href": "#"}, item.get('title', '')) +
			render_tag("div", {"class": "accordion-content"}, item.get('content', ''))
		)
		accordion_items.append(item_html)

	return render_tag("div", attrs=final_attrs, content="".join(accordion_items))


def render_calendar(**attrs):
	"""
	Renders MetroUI calendar component.

	Args:
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "calendar",
		"data-role": "calendar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("div", attrs=final_attrs, content="")


def render_dialog(title, content, **attrs):
	"""
	Renders MetroUI dialog component.

	Args:
		title: Dialog title
		content: Dialog content
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "dialog",
		"data-role": "dialog"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	dialog_content = render_tag("div", {"class": "dialog-title"}, title) + \
					 render_tag("div", {"class": "dialog-content"}, content)

	return render_tag("div", attrs=final_attrs, content=dialog_content)


def render_dropdown(items, button_text="Dropdown", **attrs):
	"""
	Renders MetroUI dropdown component.

	Args:
		items: List of dropdown items
		button_text: Button text
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "dropdown",
		"data-role": "dropdown"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	button = render_tag("button", {"class": "button dropdown-toggle"}, button_text)

	dropdown_items = []
	for item in items:
		if isinstance(item, dict):
			item_html = render_tag("a", {"href": item.get('url', '#')}, item.get('text', ''))
		else:
			item_html = render_tag("a", {"href": "#"}, str(item))
		dropdown_items.append(render_tag("li", {}, item_html))

	dropdown_menu = render_tag("ul", {"class": "dropdown-menu"}, "".join(dropdown_items))

	return render_tag("div", attrs=final_attrs, content=button + dropdown_menu)


def render_input(input_type="text", placeholder="", **attrs):
	"""
	Renders MetroUI input component.

	Args:
		input_type: Input field type
		placeholder: Placeholder text
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"type": input_type,
		"class": "input",
		"data-role": "input"
	}

	if placeholder:
		default_attrs["placeholder"] = placeholder

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("input", attrs=final_attrs, close=False)


def render_list(items, list_type="ul", **attrs):
	"""
	Renders MetroUI list component.

	Args:
		items: List of items
		list_type: List type (ul, ol)
		**attrs: Additional HTML attributes
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
			item_html = render_tag("a", {"href": item.get('url', '#')}, item.get('text', ''))
		else:
			item_html = str(item)
		list_items.append(render_tag("li", {}, item_html))

	return render_tag(list_type, attrs=final_attrs, content="".join(list_items))


def render_menu(items, **attrs):
	"""
	Renders MetroUI menu component.

	Args:
		items: List of menu items
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "menu",
		"data-role": "menu"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	menu_items = []
	for item in items:
		if isinstance(item, dict):
			item_html = render_tag("a", {"href": item.get('url', '#')}, item.get('text', ''))
		else:
			item_html = render_tag("a", {"href": "#"}, str(item))
		menu_items.append(render_tag("li", {}, item_html))

	return render_tag("ul", attrs=final_attrs, content="".join(menu_items))


def render_navigation(items, **attrs):
	"""
	Renders MetroUI navigation component.

	Args:
		items: List of navigation items
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "navigation",
		"data-role": "navigation"
	}

	final_attrs = {**default_attrs, **attrs}

	nav_items = []
	for item in items:
		if isinstance(item, dict):
			item_html = render_tag("a", {"href": item.get('url', '#')}, item.get('text', ''))
		else:
			item_html = render_tag("a", {"href": "#"}, str(item))
		nav_items.append(render_tag("li", {}, item_html))

	return render_tag("nav", attrs=final_attrs, content=render_tag("ul", {}, "".join(nav_items)))


def render_panel(title=None, content=None, **attrs):
	"""
	Renders MetroUI panel component.

	Args:
		title: Panel title
		content: Panel content
		**attrs: Дополнительные HTML атрибуты
	"""
	default_attrs = {"class": "panel"}

	final_attrs = {**default_attrs, **attrs}

	panel_parts = []

	if title:
		panel_parts.append(render_tag("div", {"class": "panel-header"}, title))

	if content:
		panel_parts.append(render_tag("div", {"class": "panel-content"}, content))

	if not panel_parts:
		panel_parts.append(render_tag("div", {"class": "panel-content"}, ""))

	return render_tag("div", attrs=final_attrs, content="".join(panel_parts))


def render_sidebar(items, **attrs):
	"""
	Renders MetroUI sidebar component.

	Args:
		items: List of sidebar items
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "sidebar",
		"data-role": "sidebar"
	}

	final_attrs = {**default_attrs, **attrs}

	sidebar_items = []
	for item in items:
		if isinstance(item, dict):
			item_html = render_tag("a", {"href": item.get('url', '#')}, item.get('text', ''))
		else:
			item_html = render_tag("a", {"href": "#"}, str(item))
		sidebar_items.append(render_tag("li", {}, item_html))

	return render_tag("div", attrs=final_attrs, content=render_tag("ul", {}, "".join(sidebar_items)))


def render_table(headers, rows, **attrs):
	"""
	Renders MetroUI table component.

	Args:
		headers: List of table headers
		rows: List of rows (each row is a list of cells)
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "table",
		"data-role": "table"
	}

	final_attrs = {**default_attrs, **attrs}

	# Headers
	header_cells = [render_tag("th", {}, str(header)) for header in headers]
	header_row = render_tag("tr", {}, "".join(header_cells))

	# Rows
	table_rows = []
	for row in rows:
		cells = [render_tag("td", {}, str(cell)) for cell in row]
		table_rows.append(render_tag("tr", {}, "".join(cells)))

	table_body = "".join(table_rows)

	return render_tag("table", attrs=final_attrs, content=header_row + table_body)


def render_tabs(tabs, **attrs):
	"""
	Renders MetroUI tabs component.

	Args:
		tabs: List of dictionaries with 'title' and 'content' keys
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "tabs",
		"data-role": "tabs"
	}

	final_attrs = {**default_attrs, **attrs}

	# Tab navigation
	tab_nav = []
	tab_content = []

	for i, tab in enumerate(tabs):
		is_active = "active" if i == 0 else ""
		tab_nav.append(render_tag("a", {"class": f"tab {is_active}", "href": f"#tab-{i}"}, tab.get('title', '')))
		tab_content.append(
			render_tag("div", {"class": f"tab-content {is_active}", "id": f"tab-{i}"}, tab.get('content', '')))

	nav = render_tag("div", {"class": "tab-nav"}, "".join(tab_nav))
	content = render_tag("div", {"class": "tab-content-wrapper"}, "".join(tab_content))

	return render_tag("div", attrs=final_attrs, content=nav + content)


def render_toolbar(items, **attrs):
	"""
	Renders MetroUI toolbar component.

	Args:
		items: List of toolbar items
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "toolbar",
		"data-role": "toolbar"
	}

	final_attrs = {**default_attrs, **attrs}

	toolbar_items = []
	for item in items:
		if isinstance(item, dict):
			if item.get('type') == 'button':
				item_html = render_button(item.get('text', ''), **item.get('button_attrs', {}))
			else:
				item_html = render_tag("a", {"href": item.get('url', '#')}, item.get('text', ''))
		else:
			item_html = str(item)
		toolbar_items.append(render_tag("div", {"class": "toolbar-item"}, item_html))

	return render_tag("div", attrs=final_attrs, content="".join(toolbar_items))


def render_modal(title, content, **attrs):
	"""
	Renders MetroUI modal component.

	Args:
		title: Modal title
		content: Modal content
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "modal",
		"data-role": "modal"
	}

	final_attrs = {**default_attrs, **attrs}

	modal_header = render_tag("div", {"class": "modal-header"}, title)
	modal_body = render_tag("div", {"class": "modal-body"}, content)
	modal_footer = render_tag("div", {"class": "modal-footer"},
							  render_button("Close", button_type="secondary", **{"data-role": "close"}))

	modal_content = modal_header + modal_body + modal_footer

	return render_tag("div", attrs=final_attrs, content=modal_content)


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

	final_attrs = {**default_attrs, **attrs}

	breadcrumb_items = []
	for i, item in enumerate(items):
		if isinstance(item, dict):
			item_html = render_tag("a", {"href": item.get('url', '#')}, item.get('text', ''))
		else:
			item_html = str(item)

		if i < len(items) - 1:
			item_html += render_tag("span", {"class": "separator"}, "/")

		breadcrumb_items.append(render_tag("li", {}, item_html))

	return render_tag("nav", attrs=final_attrs, content=render_tag("ul", {}, "".join(breadcrumb_items)))


def render_pagination(current_page, total_pages, **attrs):
	"""
	Renders MetroUI pagination component.

	Args:
		current_page: Current page
		total_pages: Total number of pages
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "pagination",
		"data-role": "pagination"
	}

	final_attrs = {**default_attrs, **attrs}

	pagination_items = []

	# Previous button
	if current_page > 1:
		prev_item = render_tag("a", {"href": f"?page={current_page - 1}"}, "&laquo;")
		pagination_items.append(render_tag("li", {}, prev_item))

	# Page numbers
	for page in range(1, total_pages + 1):
		if page == current_page:
			page_item = render_tag("span", {"class": "current"}, str(page))
		else:
			page_item = render_tag("a", {"href": f"?page={page}"}, str(page))
		pagination_items.append(render_tag("li", {}, page_item))

	# Next button
	if current_page < total_pages:
		next_item = render_tag("a", {"href": f"?page={current_page + 1}"}, "&raquo;")
		pagination_items.append(render_tag("li", {}, next_item))

	return render_tag("nav", attrs=final_attrs, content=render_tag("ul", {}, "".join(pagination_items)))


def render_badge(content, badge_type="default", **attrs):
	"""
	Renders MetroUI badge component.

	Args:
		content: Badge content
		badge_type: Badge type (default, primary, secondary, success, danger, warning, info)
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": f"badge badge-{badge_type}"
	}

	final_attrs = {**default_attrs, **attrs}

	return render_tag("span", attrs=final_attrs, content=content)


def render_avatar(image_url, **attrs):
	"""
	Renders MetroUI avatar component.

	Args:
		image_url: Image URL
		**attrs: Additional HTML attributes
	"""
	avatar_attrs = {
		"classes": ["avatar"],
		"data-attr": {},
		"html-attr": {}
	}

	tag = None

	def filter_avatar_attrs(attrs, avatar_attrs):
		attrs_to_remove = []

		# Process avatar_class attributes
		for key, value in attrs.items():
			if key == "avatar_class":
				classes = value.split(",")
				for cls in classes:
					cls = cls.strip()
					if cls:
						avatar_attrs['classes'].append(cls)
				attrs_to_remove.append(key)

		# Process avatar_data_attr_* attributes
		for key, value in attrs.items():
			if key.startswith("avatar_data_attr_"):
				data_key = key[len("avatar_data_attr_"):]
				avatar_attrs['data-attr'][data_key] = value
				attrs_to_remove.append(key)

		# Process avatar_html_attr_* attributes
		for key, value in attrs.items():
			if key.startswith("avatar_html_attr_"):
				html_key = key[len("avatar_html_attr_"):]
				avatar_attrs['html-attr'][html_key] = value
				attrs_to_remove.append(key)

		# Remove processed attributes
		for key in attrs_to_remove:
			attrs.pop(key, None)

		return attrs, avatar_attrs

	# Filter attributes
	attrs, avatar_attrs = filter_avatar_attrs(attrs, avatar_attrs)

	if image_url == '':
		image_url = None

	if image_url is None and attrs.get("icon_name"):
		icon = attrs.get("icon_name", "person")
		try:
			attrs.pop("icon_name")
		except:
			pass
		tag = render_icon_avatar(icon, **attrs)
	elif image_url is None and attrs.get("initials"):
		tag = render_initials_avatar(attrs.get("initials"), **attrs)
	else:
		tag = render_image_avatar(image_url, **attrs)

	# Build data attributes string
	data_attrs_str = ""
	for key, value in avatar_attrs['data-attr'].items():
		data_attrs_str += f' data-{key}="{value}"'

	# Build HTML attributes string
	html_attrs_str = ""
	for key, value in avatar_attrs['html-attr'].items():
		html_attrs_str += f' {key}="{value}"'

	return f"""
		<div class="{' '.join(avatar_attrs['classes'])}"{data_attrs_str}{html_attrs_str}>
			{tag}
		</div>
	"""


def render_initials_avatar(name, **attr):
	"""
	Renders MetroUI initials avatar component.

	Args:
		name: Full name to generate initials from
		**attr: Additional attributes including:
			- size: Avatar size (small, medium, large, xlarge)
			- bg_color: Background color (default: auto-generated from name)
			- text_color: Text color (default: white)
			- font_size: Font size in pixels (default: auto-calculated)
			- font_weight: Font weight (default: bold)
			- shape: Avatar shape (circle, square, rounded)
			- max_initials: Maximum number of initials to show (default: 2)
			- output_format: Image format (png, jpg, webp) - default: png
			- save_path: Custom save path for generated image
	"""
	import hashlib
	import re
	import os
	from django.conf import settings
	from PIL import Image, ImageDraw, ImageFont
	import io
	import base64

	# Default settings
	settings_config = {
		"size": attr.get("size", "medium"),
		"bg_color": attr.get("bg_color"),
		"text_color": attr.get("text_color", "white"),
		"font_size": attr.get("font_size"),
		"font_weight": attr.get("font_weight", "bold"),
		"shape": attr.get("shape", "circle"),
		"max_initials": attr.get("max_initials", 2),
		"output_format": attr.get("output_format", "png"),
		"save_path": attr.get("save_path")
	}

	# Generate initials from name
	def generate_initials(full_name, max_count=2):
		"""Extract initials from full name"""
		if not full_name:
			return "?"

		# Split name and clean up
		name_parts = re.split(r'[\s\-_]+', full_name.strip())
		name_parts = [part for part in name_parts if part]

		if not name_parts:
			return "?"

		# Extract initials
		initials = []
		for part in name_parts:
			if part and len(initials) < max_count:
				initials.append(part[0].upper())

		return ''.join(initials)

	# Generate background color from name
	def generate_bg_color(full_name):
		"""Generate consistent background color from name"""
		if not full_name:
			return "#6c757d"

		# Create hash from name
		name_hash = hashlib.md5(full_name.lower().encode()).hexdigest()

		# Predefined color palette for avatars
		colors = [
			"#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6",
			"#1abc9c", "#e67e22", "#34495e", "#16a085", "#27ae60",
			"#2980b9", "#8e44ad", "#f1c40f", "#e74c3c", "#95a5a6",
			"#d35400", "#c0392b", "#7f8c8d", "#2c3e50", "#f8f9fa"
		]

		# Use hash to select color
		color_index = int(name_hash[:8], 16) % len(colors)
		return colors[color_index]

	# Convert color to RGB
	def color_to_rgb(color):
		"""Convert hex color or color name to RGB tuple"""
		# Handle hex colors
		if color.startswith('#'):
			hex_color = color.lstrip('#')
			return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

		# Handle common color names
		color_map = {
			'white': (255, 255, 255),
			'black': (0, 0, 0),
			'red': (255, 0, 0),
			'green': (0, 255, 0),
			'blue': (0, 0, 255),
			'yellow': (255, 255, 0),
			'cyan': (0, 255, 255),
			'magenta': (255, 0, 255),
			'gray': (128, 128, 128),
			'grey': (128, 128, 128),
			'orange': (255, 165, 0),
			'purple': (128, 0, 128),
			'brown': (165, 42, 42),
			'pink': (255, 192, 203),
			'lime': (0, 255, 0),
			'navy': (0, 0, 128),
			'teal': (0, 128, 128),
			'olive': (128, 128, 0),
			'maroon': (128, 0, 0),
			'silver': (192, 192, 192),
			'gold': (255, 215, 0)
		}

		return color_map.get(color.lower(), (255, 255, 255))  # Default to white

	# Get size dimensions
	def get_size_dimensions(size):
		"""Get width and height for given size"""
		size_map = {
			"small": 32,
			"medium": 48,
			"large": 64,
			"xlarge": 96
		}
		return size_map.get(size, 48)

	# Get font size based on avatar size
	def get_font_size(avatar_size, text_length):
		"""Calculate appropriate font size"""
		if settings_config["font_size"]:
			return settings_config["font_size"]

		# Base font size calculation
		base_size = avatar_size * 0.4

		# Adjust for text length
		if text_length > 2:
			base_size *= 0.8
		elif text_length == 1:
			base_size *= 1.2

		return int(base_size)

	# Generate the image
	def generate_avatar_image(initials, dimensions, bg_color, text_color, font_size, shape):
		"""Generate avatar image using PIL"""
		# Create image with RGBA support for transparency
		img = Image.new('RGBA', (dimensions, dimensions), (0, 0, 0, 0))
		draw = ImageDraw.Draw(img)

		# Convert colors
		bg_rgb = color_to_rgb(bg_color)
		text_rgb = color_to_rgb(text_color)

		# Create background
		if shape == "circle":
			# Draw circle background
			draw.ellipse([0, 0, dimensions-1, dimensions-1], fill=bg_rgb)
		elif shape == "rounded":
			# Draw rounded rectangle
			radius = dimensions // 8
			draw.rounded_rectangle([0, 0, dimensions-1, dimensions-1], radius=radius, fill=bg_rgb)
		else:  # square
			draw.rectangle([0, 0, dimensions-1, dimensions-1], fill=bg_rgb)

		# Try to load Geologica font first, then fallback to system fonts
		font = None

		# Try to load Geologica from various possible locations
		geologica_paths = [
			# Common system font directories
			"/System/Library/Fonts/Geologica.ttf",  # macOS
			"/usr/share/fonts/truetype/google/Geologica.ttf",  # Linux
			"/usr/local/share/fonts/Geologica.ttf",  # Linux
			"~/.fonts/Geologica.ttf",  # User fonts
			# Project-specific font directory
			os.path.join(os.path.dirname(__file__), "static", "fonts", "Geologica.ttf"),
			# Example project fonts
			os.path.join(os.path.dirname(__file__), "..", "example", "static", "fonts", "Geologica.ttf"),
		]

		for font_path in geologica_paths:
			try:
				expanded_path = os.path.expanduser(font_path)
				if os.path.exists(expanded_path):
					# Load Geologica variable font - it will use the default weight
					font = ImageFont.truetype(expanded_path, font_size)
					break
			except:
				continue

		# If Geologica not found, try system fonts as fallback
		if font is None:
			try:
				# Try to use a system font - prefer bold fonts for better centering
				font = ImageFont.truetype("/System/Library/Fonts/Arial Bold.ttf", font_size)
			except:
				try:
					# Try alternative bold system fonts
					font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
				except:
					try:
						# Try Linux fonts
						font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
					except:
						try:
							# Try macOS fonts
							font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
						except:
							# Fallback to default font
							font = ImageFont.load_default()

		# Calculate text position (center)
		bbox = draw.textbbox((0, 0), initials, font=font)
		text_width = bbox[2] - bbox[0]
		text_height = bbox[3] - bbox[1]

		# Center the text both horizontally and vertically
		x = (dimensions - text_width) // 2
		y = (dimensions - text_height) // 2

		# Adjust for font baseline - PIL draws text from the top-left of the text baseline
		# We need to account for the font's ascent and descent
		font_ascent = font.getmetrics()[0]  # Get font ascent
		y = (dimensions - text_height) // 2 - font_ascent // 4

		# Ensure text stays within bounds
		x = max(0, min(x, dimensions - text_width))
		y = max(0, min(y, dimensions - text_height))

		# Draw text
		draw.text((x, y), initials, fill=text_rgb, font=font)

		return img

	# Generate initials
	initials = generate_initials(name, settings_config["max_initials"])

	# Get dimensions
	dimensions = get_size_dimensions(settings_config["size"])

	# Generate background color if not provided
	bg_color = settings_config["bg_color"] or generate_bg_color(name)

	# Calculate font size
	font_size = get_font_size(dimensions, len(initials))

	# Generate the image
	img = generate_avatar_image(
		initials, dimensions, bg_color,
		settings_config["text_color"], font_size,
		settings_config["shape"]
	)

	# Handle output
	if settings_config["save_path"]:
		# Save to custom path
		img_path = settings_config["save_path"]
		os.makedirs(os.path.dirname(img_path), exist_ok=True)
		img.save(img_path, format=settings_config["output_format"].upper())
		return render_image_avatar(img_path, alt=f"Avatar for {name}", **attr)
	else:
		# Generate responsive avatar with all sizes
		try:
			import os
			os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django.conf.global_settings')
			from django.conf import settings

			# Generate all sizes automatically
			all_sizes = ["small", "medium", "large", "xlarge"]
			initials_str = generate_initials(name, settings_config["max_initials"])
			generated_images = {}

			for size in all_sizes:
				# Get dimensions for this size
				size_dimensions = get_size_dimensions(size)
				size_font_size = get_font_size(size_dimensions, len(initials))

				# Generate image for this size
				size_img = generate_avatar_image(
					initials, size_dimensions, bg_color,
					settings_config["text_color"], size_font_size,
					settings_config["shape"]
				)

				# Create filename and path
				filename = f"{size}.{settings_config['output_format']}"
				size_dir = os.path.join(settings.MEDIA_ROOT, "avatars", "initials", initials_str)
				size_path = os.path.join(size_dir, filename)

				# Ensure directory exists
				os.makedirs(size_dir, exist_ok=True)

				# Save image
				size_img.save(size_path, format=settings_config["output_format"].upper())

				# Store media URL
				media_url = f"{settings.MEDIA_URL}avatars/initials/{initials_str}/{filename}"
				generated_images[size] = media_url

			# Return responsive figure element
			return render_responsive_avatar(generated_images, name, **attr)

		except Exception:
			# Fallback to base64 when Django settings are not available (e.g., in tests)
			buffer = io.BytesIO()
			img.save(buffer, format=settings_config["output_format"].upper())
			img_data = base64.b64encode(buffer.getvalue()).decode()
			data_url = f"data:image/{settings_config['output_format']};base64,{img_data}"
			return render_image_avatar(data_url, alt=f"Avatar for {name}", **attr)


def render_icon_avatar(icon_name, **icon_attrs):
	icon_classes = [
		f"mif-{icon_name}"
	]
	if icon_attrs.get("size"):
		try:
			size = int(icon_attrs.get("size"))
			if size >= 1 and size <= 10:
				icon_classes.append(f"mif-{size}x")
		except:
			pass

	if icon_attrs.get("text_color"):
		icon_classes.append(f"fg-{icon_attrs.get('text_color')}")

	if icon_attrs.get("bg_color"):
		icon_classes.append(f"bg-{icon_attrs.get('bg_color')}")

	return render_tag("span", {"class": " ".join(icon_classes)})


def render_image_avatar(image_url, **attrs):
	img_attrs = {"src": image_url, **attrs}
	return render_tag("img", attrs=img_attrs, close=False)


def render_responsive_avatar(generated_images, name, **attrs):
	"""Render a responsive avatar figure with picture elements for different sizes"""
	# Extract common attributes
	common_attrs = {k: v for k, v in attrs.items() if k not in ['class', 'style']}

	# Create figure element
	figure_attrs = {"class": "avatar-figure"}
	if 'class' in attrs:
		figure_attrs["class"] += f" {attrs['class']}"
	if 'style' in attrs:
		figure_attrs["style"] = attrs['style']

	# Create picture element with source sets for different sizes
	picture_content = ""

	# Add source elements for different sizes
	sizes_mapping = {
		"small": "(max-width: 480px) 48px",
		"medium": "(max-width: 768px) 64px",
		"large": "(max-width: 1024px) 96px",
		"xlarge": "(min-width: 1025px) 128px"
	}

	for size, media_query in sizes_mapping.items():
		if size in generated_images:
			source_attrs = {
				"media": media_query,
				"srcset": generated_images[size]
			}
			picture_content += render_tag("source", attrs=source_attrs, close=False)

	# Add img element as fallback (using medium size)
	fallback_img = generated_images.get(attrs.get("size"), generated_images.get("large", list(generated_images.values())[0]))
	img_attrs = {
		"src": fallback_img,
		"alt": f"Avatar for {name}",
		"class": "avatar-img",
		**common_attrs
	}
	picture_content += render_tag("img", attrs=img_attrs, close=False)

	# Create figure with picture inside
	figure_content = render_tag("picture", content=picture_content)
	return render_tag("figure", attrs=figure_attrs, content=figure_content)


def render_rating(value, max_value=5, **attrs):
	"""
	Renders MetroUI rating component.

	Args:
		value: Current rating
		max_value: Maximum rating
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "rating",
		"data-role": "rating",
		"data-value": str(value),
		"data-max": str(max_value)
	}

	final_attrs = {**default_attrs, **attrs}

	stars = ""
	for i in range(1, max_value + 1):
		star_class = "star" if i <= value else "star-empty"
		stars += render_tag("span", {"class": star_class}, "★")

	return render_tag("div", attrs=final_attrs, content=stars)
