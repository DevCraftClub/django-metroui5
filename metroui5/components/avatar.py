"""
MetroUI Avatar Components
"""

import base64
import hashlib
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

from ..html import render_tag

_AVATAR_SIZES = {"small": 48, "medium": 64, "large": 96, "xlarge": 128}
_AVATAR_FORMATS = {"png": "PNG", "jpg": "JPEG", "jpeg": "JPEG", "webp": "WEBP"}


def render_avatar(image_url, **attrs):
	"""
	Renders MetroUI avatar component.

	Args:
		image_url: Image URL
		**attrs: Additional HTML attributes
	Example:
		render_avatar('Text')

	Empty or invalid:
		`render_avatar('Text')` returns `<img class="avatar" data-role="avatar" src="Text" alt="Avatar">`. An empty call returns `<img class="avatar" data-role="avatar" src="" alt="Avatar">`.

	"""
	default_attrs = {
		"class": "avatar",
		"data-role": "avatar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("img", attrs={**final_attrs, "src": image_url, "alt": "Avatar"}, close=False)


def _avatar_initials(name, max_initials):
	words = [word for word in (name or "").replace("-", " ").split() if word]
	letters = "".join(word[0] for word in words)
	try:
		limit = int(max_initials)
	except (TypeError, ValueError):
		limit = 2
	return letters[: max(0, limit)].upper()


def _avatar_color(name, bg_color):
	if bg_color:
		return bg_color
	digest = hashlib.md5((name or "").encode("utf-8")).hexdigest()
	return f"#{digest[:6]}"


def _avatar_image(initials, bg, fg, px, shape, font_size):
	img = Image.new("RGBA", (px, px), (0, 0, 0, 0))
	draw = ImageDraw.Draw(img)
	box = (0, 0, px - 1, px - 1)
	if shape == "circle":
		draw.ellipse(box, fill=bg)
	elif shape == "rounded":
		draw.rounded_rectangle(box, radius=max(4, px // 6), fill=bg)
	else:
		draw.rectangle(box, fill=bg)
	if initials:
		font = ImageFont.load_default(font_size or max(12, px // 2))
		bbox = draw.textbbox((0, 0), initials, font=font)
		width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
		draw.text(
			((px - width) / 2 - bbox[0], (px - height) / 2 - bbox[1]),
			initials,
			fill=fg or "white",
			font=font,
		)
	return img


def render_initials_avatar(name, **attrs):
	"""
	Renders an initials avatar as an image.

	Args:
		name: Name to generate initials from
<<<<<<< ours
		**attrs: Additional HTML attributes. size, shape, bg_color, text_color,
			max_initials, save_path and output_format control the picture.
||||||| ancestor
		**attrs: Additional HTML attributes
=======
		**attrs: Additional HTML attributes. size, shape, bg_color, text_color,
			max_initials, save_path and output_format control the picture.
	Example:
		render_initials_avatar('John Doe')

	Empty or invalid:
		`render_initials_avatar(None)` returns an img with empty initials.
>>>>>>> theirs
	"""
<<<<<<< ours
	label = "" if name is None else str(name)
	max_initials = attrs.pop("max_initials", 2)
	size = attrs.pop("size", "medium")
	shape = attrs.pop("shape", "square")
	bg_color = attrs.pop("bg_color", None)
	text_color = attrs.pop("text_color", "white")
	save_path = attrs.pop("save_path", None)
	output_format = attrs.pop("output_format", "png")
	font_size = attrs.pop("font_size", None)
	attrs.pop("font_weight", None)

	px = _AVATAR_SIZES.get(size, _AVATAR_SIZES["medium"])
	try:
		font_px = int(font_size) if font_size else max(12, px // 2)
	except (TypeError, ValueError):
		font_px = max(12, px // 2)
	img = _avatar_image(
		_avatar_initials(label, max_initials),
		_avatar_color(label, bg_color),
		text_color,
		px,
		shape,
		font_px,
	)
	buffer = BytesIO()
	img.save(buffer, format="PNG")
	src = "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")
	if save_path:
		file_format = _AVATAR_FORMATS.get(str(output_format).lower(), "PNG")
		stored = img.convert("RGB") if file_format == "JPEG" else img
		stored.save(save_path, format=file_format)

	final_attrs = {
||||||| ancestor
	# This is a simplified version - the full implementation would be much larger
	default_attrs = {
=======
	label = "" if name is None else str(name)
	max_initials = attrs.pop("max_initials", 2)
	size = attrs.pop("size", "medium")
	shape = attrs.pop("shape", "square")
	bg_color = attrs.pop("bg_color", None)
	text_color = attrs.pop("text_color", "white")
	save_path = attrs.pop("save_path", None)
	output_format = attrs.pop("output_format", "png")
	font_size = attrs.pop("font_size", None)
	attrs.pop("font_weight", None)  # ponytail: встроенный шрифт Pillow без насыщенности

	px = _AVATAR_SIZES.get(size, _AVATAR_SIZES["medium"])
	try:
		font_px = int(font_size) if font_size else max(12, px // 2)
	except (TypeError, ValueError):
		font_px = max(12, px // 2)
	img = _avatar_image(
		_avatar_initials(label, max_initials),
		_avatar_color(label, bg_color),
		text_color,
		px,
		shape,
		font_px,
	)
	buffer = BytesIO()
	img.save(buffer, format="PNG")
	src = "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")
	if save_path:
		file_format = _AVATAR_FORMATS.get(str(output_format).lower(), "PNG")
		stored = img.convert("RGB") if file_format == "JPEG" else img
		stored.save(save_path, format=file_format)

	final_attrs = {
>>>>>>> theirs
		"class": "avatar initials-avatar",
		"src": src,
		"alt": f"Avatar for {label}",
	}
	final_attrs.update(attrs)
	return render_tag("img", attrs=final_attrs, close=False)


def render_icon_avatar(icon_name, **attrs):
	"""
	Renders icon avatar component.

	Args:
		icon_name: Icon class name
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "avatar icon-avatar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	icon_content = render_tag("span", {"class": icon_name}, "")
	return render_tag("div", attrs=final_attrs, content=icon_content)


def render_image_avatar(image_url, **attrs):
	"""
	Renders image avatar component.

	Args:
		image_url: Image URL
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "avatar image-avatar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("img", attrs={**final_attrs, "src": image_url, "alt": "Avatar"}, close=False)


def render_responsive_avatar(generated_images, name, **attrs):
	"""
	Renders responsive avatar component.

	Args:
		generated_images: Dictionary of generated image URLs by size
		name: Name for alt text
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "avatar responsive-avatar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	# Create picture element with multiple sources
	sources = []
	for size, url in generated_images.items():
		sources.append(f'<source media="(max-width: {size}px)" srcset="{url}">')
	
	img_tag = f'<img src="{generated_images.get("medium", "")}" alt="{name}" class="avatar-img">'
	picture_content = f'<picture>{"".join(sources)}{img_tag}</picture>'
	
	return render_tag("figure", attrs=final_attrs, content=picture_content)
