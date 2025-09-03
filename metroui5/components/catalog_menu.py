"""
MetroUI Catalog Menu Component
"""

from .base import ComplexComponent
from ..html import render_tag


class CatalogMenuComponent(ComplexComponent):
	"""
	MetroUI Catalog Menu Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/catalog-menu/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/catalog-menu/#basic-usage>`_
	- `Programmatic Initialization <https://v5.metroui.org.ua/components/catalog-menu/#programmatic-initialization>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/catalog-menu/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/catalog-menu/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/catalog-menu/#events>`_
	- `Global Configuration <https://v5.metroui.org.ua/components/catalog-menu/#global-configuration>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/catalog-menu/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/catalog-menu/#available-css-classes>`_
	- `HTML Structure <https://v5.metroui.org.ua/components/catalog-menu/#html-structure>`_
	- `Features <https://v5.metroui.org.ua/components/catalog-menu/#features>`_
	- `Best Practices <https://v5.metroui.org.ua/components/catalog-menu/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="catalog_menu",
			base_css_class="catalog-menu",
			component_params=[
				'onCatalogCreate', 'cls_catalog_menu', 'cls_catalog_list', 'cls_catalog_item',
				'cls_catalog_item_content', 'cls_icon', 'toggle'
			]
		)
	
	def render(self, items=None, **attrs):
		"""
		Renders MetroUI catalog menu component with expandable content areas.

		Args:
			items: List of catalog menu items (dicts with 'text', 'href', 'icon', 'content')
			**attrs: Additional HTML attributes including:
				onCatalogCreate (str): Callback function when catalog menu is created
				cls_catalog_menu (str): Additional CSS class for catalog menu container
				cls_catalog_list (str): Additional CSS class for catalog list
				cls_catalog_item (str): Additional CSS class for catalog items
				cls_catalog_item_content (str): Additional CSS class for catalog item content
				cls_icon (str): Additional CSS class for icons
				toggle (str): CSS selector for toggle button
		
		Returns:
			str: Rendered HTML nav element with catalog menu functionality
			
		References:
			.. _MetroUI Catalog Menu: https://v5.metroui.org.ua/components/catalog-menu/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add catalog menu-specific data attributes
		base_attrs["data-role"] = "catalog-menu"
		
		# Add toggle selector if specified
		if component_attrs.get('toggle'):
			base_attrs["data-toggle"] = component_attrs['toggle']
		
		# Build catalog menu content
		menu_content = ""
		if items:
			# Handle items parameter - could be a list or JSON string
			items_list = items
			if isinstance(items, str) and items.startswith('[') and items.endswith(']'):
				# Try to parse JSON string
				try:
					import json
					items_list = json.loads(items)
				except (json.JSONDecodeError, ValueError):
					# If JSON parsing fails, treat as single item
					items_list = [items]
			elif not isinstance(items, list):
				# If not a list, treat as single item
				items_list = [items]
			
			# Build list attributes
			list_attrs = {"class": "catalog-list"}
			
			# Add catalog list CSS class if specified
			if component_attrs.get('cls_catalog_list'):
				list_attrs["class"] += f" {component_attrs['cls_catalog_list']}"
			
			# Build list items
			item_elements = []
			for item in items_list:
				item_attrs = {"class": "catalog-item"}
				
				# Add catalog item CSS class if specified
				if component_attrs.get('cls_catalog_item'):
					item_attrs["class"] += f" {component_attrs['cls_catalog_item']}"
				
				# Handle item content
				if isinstance(item, dict):
					# Complex item with multiple elements
					item_content = ""
					
					# Build anchor element
					anchor_attrs = {"href": item.get('href', '#')}
					anchor_content = ""
					
					# Add icon if specified
					if item.get('icon'):
						icon_content = item['icon']
						if icon_content.startswith('mif-'):
							# Metro icon
							icon_attrs = {"class": f"icon {icon_content}"}
							anchor_content += render_tag("span", icon_attrs, "")
						else:
							# Image icon
							icon_attrs = {"class": "icon", "src": icon_content, "alt": item.get('alt', ''), "loading": "lazy"}
							anchor_content += render_tag("img", icon_attrs, "")
					
					# Add text
					if item.get('text'):
						anchor_content += item['text']
					
					item_content += render_tag("a", anchor_attrs, anchor_content)
					
					# Add content area if specified
					if item.get('content'):
						content_attrs = {"class": "catalog-item-content"}
						
						# Add catalog item content CSS class if specified
						if component_attrs.get('cls_catalog_item_content'):
							content_attrs["class"] += f" {component_attrs['cls_catalog_item_content']}"
						
						item_content += render_tag("div", content_attrs, item['content'])
					
					item_elements.append(render_tag("li", item_attrs, item_content))
				else:
					# Simple item text
					item_elements.append(render_tag("li", item_attrs, str(item)))
			
			menu_content = render_tag("ul", list_attrs, "".join(item_elements))
		
		return self.render_component("nav", base_attrs, content=menu_content)


# Create component instance
_catalog_menu_component = CatalogMenuComponent()


def render_catalog_menu(items=None, **attrs):
	"""
	Renders MetroUI catalog menu component with expandable content areas.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/catalog-menu/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/catalog-menu/#basic-usage>`_
	- `Programmatic Initialization <https://v5.metroui.org.ua/components/catalog-menu/#programmatic-initialization>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/catalog-menu/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/catalog-menu/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/catalog-menu/#events>`_
	- `Global Configuration <https://v5.metroui.org.ua/components/catalog-menu/#global-configuration>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/catalog-menu/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/catalog-menu/#available-css-classes>`_
	- `HTML Structure <https://v5.metroui.org.ua/components/catalog-menu/#html-structure>`_
	- `Features <https://v5.metroui.org.ua/components/catalog-menu/#features>`_
	- `Best Practices <https://v5.metroui.org.ua/components/catalog-menu/#best-practices>`_

	Args:
		items: List of catalog menu items (dicts with 'text', 'href', 'icon', 'content')
		**attrs: Additional HTML attributes including:
			onCatalogCreate (str): Callback function when catalog menu is created
			cls_catalog_menu (str): Additional CSS class for catalog menu container
			cls_catalog_list (str): Additional CSS class for catalog list
			cls_catalog_item (str): Additional CSS class for catalog items
			cls_catalog_item_content (str): Additional CSS class for catalog item content
			cls_icon (str): Additional CSS class for icons
			toggle (str): CSS selector for toggle button
		
		Returns:
			str: Rendered HTML nav element with catalog menu functionality
			
		References:
			.. _MetroUI Catalog Menu: https://v5.metroui.org.ua/components/catalog-menu/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _catalog_menu_component.render(items, **attrs)
