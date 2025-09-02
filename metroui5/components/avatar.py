"""
MetroUI Avatar Components
"""

from ..html import render_tag


def render_avatar(image_url, **attrs):
	"""
	Renders MetroUI avatar component.

	Args:
		image_url: Image URL
		**attrs: Additional HTML attributes
	"""
	default_attrs = {
		"class": "avatar",
		"data-role": "avatar"
	}

	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}

	return render_tag("img", attrs={**final_attrs, "src": image_url, "alt": "Avatar"}, close=False)


def render_initials_avatar(name, **attrs):
	"""
	Renders initials avatar component (simplified version).
	
	Args:
		name: Name to generate initials from
		**attrs: Additional HTML attributes
	"""
	# This is a simplified version - the full implementation would be much larger
	default_attrs = {
		"class": "avatar initials-avatar",
		"data-name": name
	}
	
	# Merge with custom attributes
	final_attrs = {**default_attrs, **attrs}
	
	return render_tag("div", attrs=final_attrs, content=name[:2].upper())


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
