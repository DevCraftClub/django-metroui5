"""
MetroUI App Bar Component
"""

from ..html import render_tag


def render_app_bar(brand=None, menu_items=None, **attrs):
	"""
	Renders MetroUI app bar component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/app-bar/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/app-bar/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/app-bar/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/app-bar/#api-methods>`_
	- `Responsive Behavior <https://v5.metroui.org.ua/components/app-bar/#responsive-behavior>`_
	
	Args:
		brand: Brand information (dict with 'text', 'href', 'icon' keys)
		menu_items: List of menu items (list of dicts with 'text', 'href', 'icon' keys)
		**attrs: Additional HTML attributes including:
			appbar_deferred (int): Deferred initialization time in milliseconds
			expand (bool): If true, the app bar will always be expanded
			expand_point (str): Media query string at which the app bar will expand
			duration (int): Animation duration for menu open/close in milliseconds
			check_hamburger_color (bool): If true, hamburger color will be set dependent on app-bar background color
			on_menu_open (str): Callback function triggered when menu is opened
			on_menu_close (str): Callback function triggered when menu is closed
			on_before_menu_open (str): Callback function triggered before menu is opened
			on_before_menu_close (str): Callback function triggered before menu is closed
			on_menu_collapse (str): Callback function triggered when menu is collapsed
			on_menu_expand (str): Callback function triggered when menu is expanded
			on_app_bar_create (str): Callback function triggered when app bar is created
			cls_app_bar (str): Additional CSS class for the app bar container
			cls_brand (str): Additional CSS class for the brand element
			cls_menu (str): Additional CSS class for the menu container
			cls_menu_item (str): Additional CSS class for menu items
		
	Returns:
		str: Rendered HTML nav element with app bar functionality
		
	References:
		.. _MetroUI App Bar: https://v5.metroui.org.ua/components/app-bar/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	# Extract app bar-specific attributes
	appbar_attrs = {}
	standard_attrs = {}
	
	# App bar-specific parameters
	appbar_params = [
		'appbar_deferred', 'expand', 'expand_point', 'duration', 'check_hamburger_color',
		'on_menu_open', 'on_menu_close', 'on_before_menu_open', 'on_before_menu_close',
		'on_menu_collapse', 'on_menu_expand', 'on_app_bar_create',
		'cls_app_bar', 'cls_brand', 'cls_menu', 'cls_menu_item'
	]
	
	# Separate app bar attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in appbar_params:
			appbar_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "app-bar"
	}
	
	# Add app bar-specific data attributes
	if appbar_attrs.get('appbar_deferred'):
		default_attrs["data-appbar-deferred"] = str(appbar_attrs['appbar_deferred'])
	
	if appbar_attrs.get('expand') is not None:
		default_attrs["data-expand"] = "true" if appbar_attrs['expand'] else "false"
	
	if appbar_attrs.get('expand_point'):
		default_attrs["data-expand-point"] = appbar_attrs['expand_point']
	
	if appbar_attrs.get('duration'):
		default_attrs["data-duration"] = str(appbar_attrs['duration'])
	
	if appbar_attrs.get('check_hamburger_color') is not None:
		default_attrs["data-check-hamburger-color"] = "true" if appbar_attrs['check_hamburger_color'] else "false"
	
	# Add callback functions
	if appbar_attrs.get('on_menu_open'):
		default_attrs["data-on-menu-open"] = appbar_attrs['on_menu_open']
	
	if appbar_attrs.get('on_menu_close'):
		default_attrs["data-on-menu-close"] = appbar_attrs['on_menu_close']
	
	if appbar_attrs.get('on_before_menu_open'):
		default_attrs["data-on-before-menu-open"] = appbar_attrs['on_before_menu_open']
	
	if appbar_attrs.get('on_before_menu_close'):
		default_attrs["data-on-before-menu-close"] = appbar_attrs['on_before_menu_close']
	
	if appbar_attrs.get('on_menu_collapse'):
		default_attrs["data-on-menu-collapse"] = appbar_attrs['on_menu_collapse']
	
	if appbar_attrs.get('on_menu_expand'):
		default_attrs["data-on-menu-expand"] = appbar_attrs['on_menu_expand']
	
	if appbar_attrs.get('on_app_bar_create'):
		default_attrs["data-on-app-bar-create"] = appbar_attrs['on_app_bar_create']
	
	# Build CSS classes
	css_classes = ["app-bar"]
	
	if appbar_attrs.get('cls_app_bar'):
		css_classes.append(appbar_attrs['cls_app_bar'])
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	# Build app bar content
	app_bar_content = ""
	
	# Add brand element
	if brand:
		brand_classes = ["brand"]
		if appbar_attrs.get('cls_brand'):
			brand_classes.append(appbar_attrs['cls_brand'])
		
		brand_attrs = {"class": " ".join(brand_classes)}
		if brand.get('href'):
			brand_attrs["href"] = brand['href']
		
		brand_content = ""
		if brand.get('icon'):
			if isinstance(brand['icon'], str) and brand['icon'].startswith('<'):
				# HTML content
				brand_content += f'<span class="icon">{brand["icon"]}</span>'
			else:
				# Icon class
				brand_content += f'<span class="icon"><span class="{brand["icon"]}"></span></span>'
		
		if brand.get('text'):
			brand_content += f'<span class="caption">{brand["text"]}</span>'
		
		app_bar_content += render_tag("a", brand_attrs, brand_content)
	
	# Add menu items
	if menu_items:
		menu_classes = ["app-bar-menu"]
		if appbar_attrs.get('cls_menu'):
			menu_classes.append(appbar_attrs['cls_menu'])
		
		menu_list_items = []
		for item in menu_items:
			item_classes = ["app-bar-item"]
			if appbar_attrs.get('cls_menu_item'):
				item_classes.append(appbar_attrs['cls_menu_item'])
			
			item_attrs = {"class": " ".join(item_classes)}
			if item.get('href'):
				item_attrs["href"] = item['href']
			
			item_content = ""
			if item.get('icon'):
				item_content += f'<span class="icon"><span class="{item["icon"]}"></span></span>'
			if item.get('text'):
				item_content += item['text']
			
			menu_list_items.append(render_tag("li", {}, render_tag("a", item_attrs, item_content)))
		
		app_bar_content += render_tag("ul", {"class": " ".join(menu_classes)}, "".join(menu_list_items))
	
	return render_tag("nav", attrs=final_attrs, content=app_bar_content)
