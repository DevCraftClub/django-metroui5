"""
MetroUI Dropdown Component

The Dropdown component provides a flexible way to create dropdown menus and lists that can be 
toggled to show or hide content. It supports various positioning options and can be customized 
through configuration options and CSS variables.
"""

from .base import ComplexComponent


class DropdownComponent(ComplexComponent):
	"""
	MetroUI Dropdown component.

	Provides a flexible way to create dropdown menus and lists that can be toggled
	to show or hide content with various positioning options.
	"""

	def __init__(self):
		super().__init__(
			component_name="dropdown",
			base_css_class="dropdown",
			component_params=[
				# Basic parameters
				'content', 'button_text', 'toggle_element', 'items',
				# Supported configuration parameters
				'dropdown_deferred', 'no_close', 'open_mode', 'height', 'keep_open',
				# Event handlers
				'on_drop', 'on_up', 'on_dropdown_create'
				# Note: cls_* parameters are handled automatically by base class
			]
		)

	def render(self, content="", button_text="", toggle_element=None, items=None, **attrs):
		"""
		Render the dropdown component.

		Args:
			content: The HTML content to be displayed in the dropdown (string)
			button_text: Text for the dropdown toggle button (string, default: "")
			toggle_element: Custom toggle element HTML (string, default: None)
			items: List of dropdown items to auto-generate menu (list, default: None)
			**attrs: Component attributes including:
				- dropdown_deferred: Delay before dropdown appears (number, default: 0)
				- no_close: Won't close when clicking outside (boolean, default: false)
				- open_mode: How dropdown opens ("down", "up", "left", "right")
				- height: Height of dropdown (string)
				- keep_open: Prevent closing when clicking outside (boolean, adds CSS class)
				- on_drop: Triggered when dropdown is opened (string)
				- on_up: Triggered when dropdown is closed (string)
				- on_dropdown_create: Triggered when dropdown is created (string)
				- cls_dropdown: Additional CSS class for dropdown (string)
				- cls_toggle: Additional CSS class for toggle (string)
				- cls_content: Additional CSS class for content (string)
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

		# Store method parameters separately (not as component attributes)
		method_params = {
			'content': content,
			'button_text': button_text,
			'toggle_element': toggle_element,
			'items': items
		}

		# Build CSS classes including positioning classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)

		# Add keep-open CSS class if specified
		if component_attrs.get('keep_open'):
			css_classes.append('keep-open')

		# Build data attributes using base class method
		data_attr_mapping = {
			'dropdown_deferred': 'data-dropdown-deferred',
			'open_mode': 'data-open-mode',
			'height': 'data-height',
			'on_drop': 'data-on-drop',
			'on_up': 'data-on-up',
			'on_dropdown_create': 'data-on-dropdown-create'
		}

		data_attrs = self.build_data_attributes(component_attrs, data_attr_mapping)
		data_attrs["data-role"] = "dropdown"

		# Build final dropdown attributes
		dropdown_attrs = {
			"class": " ".join(css_classes),
			**data_attrs,
			**standard_attrs
		}

		# Build dropdown content
		dropdown_content = self.build_dropdown_content(method_params)

		# Build dropdown HTML
		dropdown_html = self.render_component('div', dropdown_attrs, dropdown_content)

		# Create the complete dropdown structure
		return self.build_dropdown_structure(method_params, cls_attrs, dropdown_html)

	def build_dropdown_content(self, method_params):
		"""Build the dropdown content from various sources."""
		content = method_params.get('content', '')
		items = method_params.get('items')

		# Auto-generate content from items if provided and no content
		if items and not content:
			if any(isinstance(item, dict) and 'href' in item for item in items):
				# Generate as list menu
				menu_items = []
				for item in items:
					if isinstance(item, dict):
						text = item.get('text', '')
						href = item.get('href', '#')
						item_attrs = {k: v for k, v in item.items() if k not in ['text', 'href']}

						if item_attrs:
							item_attrs_str = ' '.join([f'{k}="{v}"' for k, v in item_attrs.items()])
							menu_items.append(f'<li {item_attrs_str}><a href="{href}">{text}</a></li>')
						else:
							menu_items.append(f'<li><a href="{href}">{text}</a></li>')
					else:
						menu_items.append(f'<li><a href="#">{item}</a></li>')

				return f'<ul>{"".join(menu_items)}</ul>'
			else:
				# Generate as simple div content
				return '<div>' + '<br>'.join([str(item) for item in items]) + '</div>'

		return content

	def build_dropdown_structure(self, method_params, cls_attrs, dropdown_html):
		"""Build the complete dropdown structure with toggle element."""
		toggle_element = method_params.get('toggle_element')
		button_text = method_params.get('button_text')

		if toggle_element:
			# Use custom toggle element with nested dropdown
			if '</button>' in toggle_element:
				return toggle_element.replace('</button>', dropdown_html + '</button>')
			elif '</div>' in toggle_element:
				return toggle_element.replace('</div>', dropdown_html + '</div>')
			else:
				# Fallback: wrap in div
				container_attrs = {'class': 'dropdown-toggle'}
				return self.render_component('div', container_attrs, toggle_element + dropdown_html)
		elif button_text:
			# Create button toggle with dropdown in container (dropdown-button pattern from examples)
			button_attrs = {'class': 'button dropdown-toggle'}

			# Add toggle-specific CSS classes
			if cls_attrs.get('cls_toggle'):
				button_attrs['class'] += ' ' + cls_attrs['cls_toggle']

			button_html = self.render_component('button', button_attrs, button_text)
			container_attrs = {}

			return self.render_component('div', container_attrs, button_html + dropdown_html)
		else:
			# Create default div toggle with nested dropdown
			container_attrs = {'class': 'dropdown-toggle'}
			return self.render_component('div', container_attrs, 'Click me' + dropdown_html)


# Create component instance
_dropdown_component = DropdownComponent()


def render_dropdown(content="", button_text="", toggle_element=None, items=None, **attrs):
	"""
	Renders MetroUI dropdown using the base component class.

	Args:
		content: The HTML content to be displayed in the dropdown (string)
		button_text: Text for the dropdown toggle button (string, default: "")
		toggle_element: Custom toggle element HTML (string, default: None)
		items: List of dropdown items to auto-generate menu (list, default: None)
		**attrs: Component attributes (see DropdownComponent.render for details)

	Example:
		Basic dropdown with button:
		```python
		render_dropdown(button_text="Options", content="<div>Dropdown content</div>")
		```

		Dropdown with positioning:
		```python
		render_dropdown(
			button_text="Drop Up",
			content="<div>Content appears above</div>",
			open_mode="up"
		)
		```

		Dropdown with deferred creation:
		```python
		render_dropdown(
			button_text="Deferred",
			content="<div>Created after delay</div>",
			dropdown_deferred=3000
		)
		```

		Dropdown with keep-open behavior:
		```python
		render_dropdown(
			button_text="Keep Open",
			content="<div>Won't close automatically</div>",
			no_close=True
		)
		```
	Example:
		render_dropdown()

	Empty or invalid:
		`render_dropdown()` returns `<div class="dropdown-toggle">Click me<div class="dropdown" data-role="dropdown"></div></div>`.

	"""
	return _dropdown_component.render(
		content=content,
		button_text=button_text,
		toggle_element=toggle_element,
		items=items,
		**attrs
	)
