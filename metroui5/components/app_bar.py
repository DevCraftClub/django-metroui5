"""
MetroUI App Bar Component
"""

from .base import ComplexComponent
from ..html import render_tag


class AppBarComponent(ComplexComponent):
	"""
	MetroUI App Bar Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/app-bar/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/app-bar/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/app-bar/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/app-bar/#api-methods>`_
	- `Responsive Behavior <https://v5.metroui.org.ua/components/app-bar/#responsive-behavior>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="app_bar",
			base_css_class="app-bar",
			component_params=[
				'appbar_deferred', 'expand', 'expand_point', 'duration', 'check_hamburger_color',
				'on_menu_open', 'on_menu_close', 'on_before_menu_open', 'on_before_menu_close',
				'on_menu_collapse', 'on_menu_expand', 'on_app_bar_create',
				'cls_app_bar', 'cls_brand', 'cls_menu', 'cls_menu_item'
			]
		)
	
	def render(self, brand=None, menu_items=None, static_items=None, **attrs):
		"""
		Renders MetroUI app bar component.
		
		Args:
			brand: Brand information (dict with 'text', 'href', 'icon' keys)
			menu_items: List of menu items (list of dicts with 'text', 'href', 'icon' keys)
			static_items: List of static items for the right side (list of dicts)
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
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add data-role attribute
		base_attrs["data-role"] = "appbar"
		
		# Add app bar-specific data attributes
		if component_attrs.get('appbar_deferred'):
			base_attrs["data-appbar-deferred"] = str(component_attrs['appbar_deferred'])
		
		if component_attrs.get('expand') is not None:
			base_attrs["data-expand"] = "true" if component_attrs['expand'] else "false"
		
		if component_attrs.get('expand_point'):
			base_attrs["data-expand-point"] = component_attrs['expand_point']
		
		if component_attrs.get('duration'):
			base_attrs["data-duration"] = str(component_attrs['duration'])
		
		if component_attrs.get('check_hamburger_color') is not None:
			base_attrs["data-check-hamburger-color"] = "true" if component_attrs['check_hamburger_color'] else "false"
		
		# Add callback functions
		if component_attrs.get('on_menu_open'):
			base_attrs["data-on-menu-open"] = component_attrs['on_menu_open']
		
		if component_attrs.get('on_menu_close'):
			base_attrs["data-on-menu-close"] = component_attrs['on_menu_close']
		
		if component_attrs.get('on_before_menu_open'):
			base_attrs["data-on-before-menu-open"] = component_attrs['on_before_menu_open']
		
		if component_attrs.get('on_before_menu_close'):
			base_attrs["data-on-before-menu-close"] = component_attrs['on_before_menu_close']
		
		if component_attrs.get('on_menu_collapse'):
			base_attrs["data-on-menu-collapse"] = component_attrs['on_menu_collapse']
		
		if component_attrs.get('on_menu_expand'):
			base_attrs["data-on-menu-expand"] = component_attrs['on_menu_expand']
		
		if component_attrs.get('on_app_bar_create'):
			base_attrs["data-on-app-bar-create"] = component_attrs['on_app_bar_create']
		
		# Build app bar content
		app_bar_content = ""
		
		# Add brand element (static item on the left)
		if brand:
			brand_classes = ["app-bar-item-static", "no-hover"]
			if component_attrs.get('cls_brand'):
				brand_classes.append(component_attrs['cls_brand'])
			
			brand_content = ""
			if brand.get('icon'):
				if isinstance(brand['icon'], str) and brand['icon'].startswith('<'):
					# HTML content
					brand_content += brand["icon"]
				else:
					# Icon class
					brand_content += f'<span class="{brand["icon"]}"></span>'
			
			if brand.get('text'):
				brand_content += f'<span class="caption">{brand["text"]}</span>'
			
			app_bar_content += render_tag("div", {"class": " ".join(brand_classes)}, brand_content)
		
		# Add menu items
		if menu_items:
			menu_classes = ["app-bar-menu"]
			if component_attrs.get('cls_menu'):
				menu_classes.append(component_attrs['cls_menu'])
			
			menu_list_items = []
			for item in menu_items:
				# Check if item has dropdown
				if item.get('dropdown'):
					# Create dropdown menu item
					item_content = ""
					if item.get('icon'):
						item_content += f'<span class="icon"><span class="{item["icon"]}"></span></span>'
					if item.get('text'):
						item_content += item['text']
					
					# Create dropdown menu
					dropdown_items = []
					for dropdown_item in item['dropdown']:
						dropdown_item_content = ""
						if dropdown_item.get('icon'):
							dropdown_item_content += f'<span class="icon"><span class="{dropdown_item["icon"]}"></span></span>'
						if dropdown_item.get('text'):
							dropdown_item_content += dropdown_item['text']
						
						dropdown_item_attrs = {"href": dropdown_item.get('href', '#')}
						dropdown_items.append(render_tag("li", {}, render_tag("a", dropdown_item_attrs, dropdown_item_content)))
					
					dropdown_menu = render_tag("ul", {"class": "d-menu", "data-role": "dropdown"}, "".join(dropdown_items))
					menu_list_items.append(render_tag("li", {}, render_tag("a", {"href": item.get('href', '#'), "class": "dropdown-caret"}, item_content) + dropdown_menu))
				else:
					# Regular menu item
					item_content = ""
					if item.get('icon'):
						item_content += f'<span class="icon"><span class="{item["icon"]}"></span></span>'
					if item.get('text'):
						item_content += item['text']
					
					item_attrs = {"href": item.get('href', '#')}
					menu_list_items.append(render_tag("li", {}, render_tag("a", item_attrs, item_content)))
			
			app_bar_content += render_tag("ul", {"class": " ".join(menu_classes)}, "".join(menu_list_items))
		
		# Add static items (right side)
		if static_items:
			for static_item in static_items:
				static_classes = ["app-bar-item-static"]
				if static_item.get('no_hover'):
					static_classes.append("no-hover")
				if static_item.get('ml_auto'):
					static_classes.append("ml-auto")
				if static_item.get('cls'):
					static_classes.append(static_item['cls'])
				
				static_content = static_item.get('content', '')
				app_bar_content += render_tag("div", {"class": " ".join(static_classes)}, static_content)
		
		return render_tag("nav", attrs=base_attrs, content=app_bar_content)


# Create component instance
_app_bar_component = AppBarComponent()


def render_app_bar(brand=None, menu_items=None, static_items=None, **attrs):
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
	return _app_bar_component.render(brand, menu_items, static_items, **attrs)
