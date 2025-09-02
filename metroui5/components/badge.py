"""
MetroUI Badge Component
"""

from ..html import render_tag


def render_badge(content, corner=False, corner_outside=False, **attrs):
	"""
	Renders MetroUI badge component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/badges/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/badges/#usage>`_
	- `CSS Variables <https://v5.metroui.org.ua/components/badges/#css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/badges/#available-css-classes>`_
	
	Args:
		content: Badge content/text
		corner: Position the badge in the top-right corner of a relative-positioned parent
		corner_outside: Position the badge outside the parent element in the top-right corner
		**attrs: Additional HTML attributes including:
			cls_badge (str): Additional CSS class for the badge
		
	Returns:
		str: Rendered HTML span element with badge functionality
		
	References:
		.. _MetroUI Badges: https://v5.metroui.org.ua/components/badges/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	# Extract badge-specific attributes
	badge_attrs = {}
	standard_attrs = {}
	
	# Badge-specific parameters
	badge_params = ['cls_badge']
	
	# Separate badge attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in badge_params:
			badge_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build CSS classes
	css_classes = ["badge"]
	
	if corner:
		css_classes.append("corner")
	
	if corner_outside:
		css_classes.append("corner-outside")
	
	if badge_attrs.get('cls_badge'):
		css_classes.append(badge_attrs['cls_badge'])
	
	# Add existing classes if present
	if "class" in standard_attrs:
		existing_classes = standard_attrs["class"].split()
		css_classes.extend([cls for cls in existing_classes if cls not in css_classes])
		del standard_attrs["class"]
	
	# Build base attributes
	default_attrs = {
		"class": " ".join(css_classes)
	}
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("span", attrs=final_attrs, content=content)
