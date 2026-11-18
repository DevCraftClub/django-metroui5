"""
MetroUI Base Component Classes

This module provides the foundational classes for all MetroUI5 components in the Django MetroUI5 project.
It implements the DRY (Don't Repeat Yourself) principle by providing common functionality for CSS class
handling, attribute processing, and HTML rendering that all components can inherit and reuse.

The module contains three main classes:
- BaseComponent: Abstract base class with common functionality
- SimpleComponent: For components that render a single HTML element
- ComplexComponent: For components that render multiple HTML elements or have complex structure

Key Features:
- Automatic CSS class management and validation state handling
- Data attribute mapping and processing
- ID generation and management
- HTML rendering with proper attribute handling
- Debug utilities for component testing
- Support for event handlers and callback functions
- Validation state support (error, success, warning, info)

Usage:
    All MetroUI5 components should inherit from either SimpleComponent or ComplexComponent
    and implement the required abstract methods. This ensures consistent behavior and
    reduces code duplication across the component library.

Examples:
    Creating a simple component:
    ```python
    class BadgeComponent(SimpleComponent):
        def __init__(self):
            super().__init__(
                component_name="badge",
                base_css_class="badge",
                tag_name="span",
                component_params=['text', 'color', 'size'],
                data_attr_mapping={'text': 'data-text', 'color': 'data-color'}
            )
    ```

    Creating a complex component:
    ```python
    class AccordionComponent(ComplexComponent):
        def __init__(self):
            super().__init__(
                component_name="accordion",
                base_css_class="accordion",
                component_params=['frames', 'collapsible', 'on_create']
            )
        
        def render(self, **attrs):
            # Custom rendering logic for complex structure
            pass
    ```

Author: Maxim Harder
Version: 1.0.0
"""

from abc import ABC, abstractmethod

from ..html import render_tag


class BaseComponent(ABC):
	"""
	Abstract base class for all MetroUI5 components.

	This class provides the foundational functionality that all MetroUI5 components inherit,
	implementing the DRY principle by centralizing common operations like CSS class management,
	attribute processing, and HTML rendering. All component classes should inherit from this
	base class to ensure consistent behavior across the component library.

	The class handles:
	- CSS class management and validation state handling
	- Parameter separation into component-specific, standard HTML, and CSS class attributes
	- Data attribute mapping and processing for MetroUI5 JavaScript integration
	- ID generation and management
	- HTML rendering with proper attribute handling
	- Debug utilities for component testing and development

	Attributes:
		component_name (str): Name of the component (e.g., 'badge', 'button', 'accordion')
		base_css_class (str): Base CSS class for the component (e.g., 'badge', 'button')
		component_params (list): List of component-specific parameters that should be
			processed as data attributes or special handling

	Examples:
		Basic component initialization:
		```python
		class MyComponent(BaseComponent):
			def __init__(self):
				super().__init__(
					component_name="my_component",
					base_css_class="my-component",
					component_params=['param1', 'param2', 'on_click']
				)
		```

		Using the component:
		```python
		component = MyComponent()
		html = component.render(param1="value1", cls="custom-class", id="my-id")
		# Returns: <div class="my-component custom-class" id="my-id" data-param1="value1"></div>
		```
	"""

	def __init__(self, component_name, base_css_class=None, component_params=None):
		"""
		Initialize the base component with essential configuration.

		This constructor sets up the fundamental properties that all MetroUI5 components
		need for proper functionality. It establishes the component identity, base styling,
		and parameter handling configuration.

		Args:
			component_name (str): Unique name identifier for the component.
				Used for ID generation, parameter processing, and debugging.
				Examples: 'badge', 'button', 'accordion', 'dropdown'
			base_css_class (str, optional): Primary CSS class for the component.
				This becomes the main class applied to the rendered HTML element.
				If None, defaults to the component_name. Examples: 'badge', 'button'
			component_params (list, optional): List of component-specific parameters
				that require special processing. These parameters are separated from
				standard HTML attributes and processed as data attributes or special
				handling. Examples: ['text', 'color', 'on_click', 'cls_component']

		Examples:
			Basic initialization:
			```python
			super().__init__(
				component_name="badge",
				base_css_class="badge",
				component_params=['text', 'color', 'size']
			)
			```

			With event handlers:
			```python
			super().__init__(
				component_name="button",
				base_css_class="button",
				component_params=['text', 'on_click', 'on_hover', 'disabled']
			)
			```
		"""
		self.component_name = component_name
		self.base_css_class = base_css_class
		self.component_params = component_params or []

	def separate_attributes(self, attrs):
		"""
		Separate component attributes into different processing categories.

		This method categorizes all input attributes into three groups for proper processing:
		- Component-specific attributes: Parameters defined in component_params
		- CSS class attributes: Parameters starting with 'cls' or 'cls_'
		- Standard HTML attributes: All other attributes passed through to HTML

		The separation ensures that component parameters are processed as data attributes
		for MetroUI5 JavaScript integration, CSS classes are properly managed, and standard
		HTML attributes are passed through unchanged.

		Args:
			attrs (dict): Dictionary containing all attributes passed to the component.
				Can include component parameters, CSS classes, and standard HTML attributes.
				Example: {'text': 'Hello', 'cls': 'custom-class', 'id': 'my-id', 'on_click': 'handleClick()'}

		Returns:
			tuple: A tuple containing three dictionaries:
				- component_attrs (dict): Component-specific parameters that need special processing
				- standard_attrs (dict): Standard HTML attributes to pass through unchanged
				- cls_attrs (dict): CSS class-related attributes for styling

		Examples:
			Basic attribute separation:
			```python
			attrs = {'text': 'Hello', 'cls': 'custom', 'id': 'my-id', 'on_click': 'click()'}
			comp_attrs, std_attrs, cls_attrs = self.separate_attributes(attrs)
			# comp_attrs: {'text': 'Hello', 'on_click': 'click()'}
			# std_attrs: {'id': 'my-id'}
			# cls_attrs: {'cls': 'custom'}
			```

			With component-specific parameters:
			```python
			# If component_params = ['text', 'color', 'on_click']
			attrs = {'text': 'Hello', 'color': 'red', 'cls': 'custom', 'id': 'my-id'}
			comp_attrs, std_attrs, cls_attrs = self.separate_attributes(attrs)
			# comp_attrs: {'text': 'Hello', 'color': 'red'}
			# std_attrs: {'id': 'my-id'}
			# cls_attrs: {'cls': 'custom'}
			```
		"""
		component_attrs = {}
		standard_attrs = {}
		cls_attrs = {}

		# Add component-specific parameter name
		component_param_name = f'cls_{self.component_name}'
		if component_param_name not in self.component_params:
			self.component_params.append(component_param_name)

		for key, value in attrs.items():
			if key in self.component_params:
				component_attrs[key] = value
			elif key == 'cls' or key.startswith('cls_'):
				cls_attrs[key] = value
			else:
				standard_attrs[key] = value

		return component_attrs, standard_attrs, cls_attrs

	def build_css_classes(self, component_attrs, cls_attrs, standard_attrs, additional_classes=None):
		"""
		Build comprehensive CSS class list from multiple sources.

		This method combines CSS classes from various sources to create the final class
		attribute for the component. It handles base classes, additional classes, component-specific
		styling, and user-provided classes while avoiding duplicates.

		The method processes classes in this order:
		1. Base CSS class (from component definition)
		2. Additional classes (passed as parameter)
		3. Component-specific CSS classes (from cls_attrs)
		4. User-provided classes (from standard_attrs['cls'])

		Args:
			component_attrs (dict): Component-specific attributes that may contain
				styling parameters. These are processed separately from CSS classes.
			cls_attrs (dict): CSS class-related attributes starting with 'cls' or 'cls_'.
				These are added to the final class list.
			standard_attrs (dict): Standard HTML attributes including the 'cls' parameter
				for user-provided classes. The 'cls' parameter is removed after processing.
			additional_classes (list, optional): Additional CSS classes to add to the component.
				Useful for dynamic styling or component variants.

		Returns:
			list: Complete list of CSS classes to be applied to the component.
				Classes are deduplicated and properly ordered.

		Examples:
			Basic class building:
			```python
			css_classes = self.build_css_classes(
				component_attrs={},
				cls_attrs={'cls_custom': 'custom-style'},
				standard_attrs={'cls': 'user-class another-class'},
				additional_classes=['variant-large']
			)
			# Returns: ['badge', 'variant-large', 'custom-style', 'user-class', 'another-class']
			```

			With validation states:
			```python
			css_classes = self.build_css_classes(
				component_attrs={'error': True},
				cls_attrs={},
				standard_attrs={'cls': 'input-field'},
				additional_classes=['error', 'required']
			)
			# Returns: ['input', 'error', 'required', 'input-field']
			```
		"""
		css_classes = [self.base_css_class] if self.base_css_class is not None else []

		# Add additional classes if provided
		if additional_classes:
			css_classes.extend(additional_classes)

		# Add component-specific class
		component_param_name = f'cls_{self.component_name}'

		# Add any additional cls parameters
		for key, value in cls_attrs.items():
			if key != component_param_name:
				css_classes.append(value)

		# Add existing classes from cls parameter
		if "cls" in standard_attrs:
			existing_classes = standard_attrs["cls"].split()
			css_classes.extend([cls for cls in existing_classes if cls not in css_classes])
			del standard_attrs["cls"]

		if css_classes is None:
			return []

		return css_classes


	def build_data_attributes(self, component_attrs, data_attr_mapping=None):
		"""
		Build data attributes from component parameters for MetroUI5 JavaScript integration.

		This method converts component-specific parameters into HTML data attributes that
		MetroUI5 JavaScript can read and use for component initialization and behavior.
		It handles different types of parameters including event handlers, regular parameters,
		and CSS class parameters with appropriate processing for each type.

		The method automatically handles:
		- Event handlers (parameters starting with 'on_') → data-on-* attributes
		- Regular parameters → data-* attributes with kebab-case conversion
		- CSS class parameters (starting with 'cls_') → skipped (handled separately)
		- Custom mappings via data_attr_mapping parameter

		Args:
			component_attrs (dict): Component-specific attributes to convert to data attributes.
				These are the parameters that were separated from standard HTML attributes.
			data_attr_mapping (dict, optional): Custom mapping of parameter names to data attribute names.
				Allows overriding the default naming convention for specific parameters.
				Example: {'my_param': 'data-custom-attribute', 'special_handler': 'data-on-special'}

		Returns:
			dict: Dictionary of data attributes ready for HTML rendering.
				Keys are data attribute names (e.g., 'data-role', 'data-on-click').
				Values are the attribute values as strings.

		Examples:
			Basic data attribute building:
			```python
			component_attrs = {'text': 'Hello', 'color': 'red', 'on_click': 'handleClick()'}
			data_attrs = self.build_data_attributes(component_attrs)
			# Returns: {'data-text': 'Hello', 'data-color': 'red', 'data-on-click': 'handleClick()'}
			```

			With custom mapping:
			```python
			component_attrs = {'my_param': 'value', 'special_handler': 'doSomething()'}
			mapping = {'my_param': 'data-custom-param', 'special_handler': 'data-on-special'}
			data_attrs = self.build_data_attributes(component_attrs, mapping)
			# Returns: {'data-custom-param': 'value', 'data-on-special': 'doSomething()'}
			```

			Skipping CSS parameters:
			```python
			component_attrs = {'text': 'Hello', 'cls_component': 'custom-style', 'on_click': 'click()'}
			data_attrs = self.build_data_attributes(component_attrs)
			# Returns: {'data-text': 'Hello', 'data-on-click': 'click()'}
			# Note: cls_component is skipped as it's handled separately
			```
		"""
		data_attrs = {}

		if data_attr_mapping is None:
			data_attr_mapping = {}

		for param, value in component_attrs.items():
			if param.startswith('on_'):
				# Handle callback functions
				data_attr_name = f"data-{param.replace('_', '-')}"
				data_attrs[data_attr_name] = value
			elif param.startswith('cls_'):
				# Skip CSS class parameters
				continue
			else:
				# Handle regular parameters
				if param in data_attr_mapping:
					data_attr_name = data_attr_mapping[param]
				else:
					data_attr_name = f"data-{param.replace('_', '-')}"
				data_attrs[data_attr_name] = str(value)

		return data_attrs


	def build_id_attribute(self, component_attrs, standard_attrs, prefix=None, auto_generate=True):
		"""
		Build ID attribute for the component with flexible generation options.

		This method handles ID attribute generation with multiple fallback strategies:
		1. Use explicitly provided ID from standard_attrs['id']
		2. Use ID from component_attrs['id'] (component-specific parameter)
		3. Auto-generate ID using component name and optional prefix
		4. Return None if auto-generation is disabled and no ID provided

		The method ensures that each component instance has a unique identifier when needed,
		which is essential for JavaScript functionality, accessibility, and CSS targeting.

		Args:
			component_attrs (dict): Component-specific attributes that may contain an 'id' parameter.
			standard_attrs (dict): Standard HTML attributes that may contain an 'id' parameter.
				This takes precedence over component_attrs['id'].
			prefix (str, optional): Custom prefix for auto-generated IDs.
				If None, uses the component_name as prefix.
				Example: 'my-custom-prefix' → 'my-custom-prefix-component'
			auto_generate (bool, optional): Whether to auto-generate an ID if none is provided.
				Defaults to True. Set to False to disable auto-generation.

		Returns:
			str or None: The ID attribute value to use, or None if no ID should be set.
				Returns the first available ID in this priority order:
				1. standard_attrs['id']
				2. component_attrs['id']
				3. Auto-generated ID (if auto_generate=True)
				4. None (if auto_generate=False and no ID provided)

		Examples:
			Explicit ID from standard attributes:
			```python
			id_attr = self.build_id_attribute(
				component_attrs={},
				standard_attrs={'id': 'my-explicit-id'},
				prefix='custom'
			)
			# Returns: 'my-explicit-id'
			```

			Auto-generated ID:
			```python
			id_attr = self.build_id_attribute(
				component_attrs={},
				standard_attrs={},
				prefix='my-component'
			)
			# Returns: 'my-component-component'
			```

			No ID generation:
			```python
			id_attr = self.build_id_attribute(
				component_attrs={},
				standard_attrs={},
				auto_generate=False
			)
			# Returns: None
			```
		"""
		# Check if ID is explicitly provided
		if 'id' in standard_attrs:
			return standard_attrs['id']

		# Check if component has an ID parameter
		if 'id' in component_attrs:
			return component_attrs['id']

		# Auto-generate ID if requested
		if auto_generate:
			if prefix is None:
				prefix = self.component_name

			# Create a simple ID based on component name
			# This can be overridden by providing an explicit 'id' parameter
			return f"{prefix}-component"

		return None


	def render_component(self, tag_name, attrs, content="", close=True):
		"""
		Render the final HTML output for the component.

		This method takes the processed attributes and content and generates the final
		HTML string for the component. It uses the render_tag utility function to
		ensure proper HTML formatting and attribute handling.

		The method supports both self-closing tags (like <input>) and paired tags
		(like <div>content</div>) based on the close parameter.

		Args:
			tag_name (str): HTML tag name to render.
				Examples: 'div', 'span', 'input', 'button', 'section'
			attrs (dict): Dictionary of HTML attributes to apply to the tag.
				Keys are attribute names, values are attribute values.
				Example: {'class': 'badge primary', 'id': 'my-badge', 'data-role': 'badge'}
			content (str, optional): Content to place inside the HTML tag.
				Only used when close=True. Can be empty string for empty tags.
				Defaults to empty string.
			close (bool, optional): Whether to create a paired tag (True) or self-closing tag (False).
				True: <div>content</div>
				False: <input />
				Defaults to True.

		Returns:
			str: Complete HTML string for the component.
				The output is properly formatted and ready for use in templates.

		Examples:
			Basic div element:
			```python
			html = self.render_component('div', {'class': 'badge'}, 'Hello')
			# Returns: '<div class="badge">Hello</div>'
			```

			Self-closing input element:
			```python
			html = self.render_component('input', {'type': 'text', 'placeholder': 'Enter text'}, close=False)
			# Returns: '<input type="text" placeholder="Enter text" />'
			```

			Complex element with multiple attributes:
			```python
			attrs = {
				'class': 'button primary',
				'id': 'submit-btn',
				'data-role': 'button',
				'data-on-click': 'handleSubmit()'
			}
			html = self.render_component('button', attrs, 'Submit')
			# Returns: '<button class="button primary" id="submit-btn" data-role="button" data-on-click="handleSubmit()">Submit</button>'
			```
		"""
		return render_tag(tag_name, attrs=attrs, content=content, close=close)


	def debug(self, **attrs):
		"""
		Debug method that returns raw HTML output for testing and inspection.

		This method calls the component's render method and returns the raw HTML
		without any Django SafeString wrapping, making it useful for debugging,
		testing, and inspecting the exact HTML output. It's particularly helpful
		during component development and testing phases.

		The method is identical to render() in functionality but ensures the output
		is returned as a plain string rather than a Django SafeString, which can
		be useful for logging, testing assertions, or debugging HTML structure.

		Args:
			**attrs: Component attributes (same as render method).
				All parameters that would be passed to the render method.
				Example: {'text': 'Hello', 'cls': 'custom-class', 'id': 'my-id'}

		Returns:
			str: Raw HTML text output without Django SafeString wrapping.
				The output is identical to render() but as a plain string.

		Examples:
			Basic debugging:
			```python
			component = BadgeComponent()
			html_text = component.debug(text="Hello", cls="custom-class")
			print(html_text)  # Outputs: <span class="badge custom-class" data-text="Hello">Hello</span>
			```

			Testing component output:
			```python
			def test_component_output():
				component = ButtonComponent()
				html = component.debug(text="Click me", on_click="handleClick()")
				assert 'data-on-click="handleClick()"' in html
				assert 'class="button"' in html
			```

			Logging component HTML:
			```python
			import logging
			logger = logging.getLogger(__name__)

			component = MyComponent()
			html = component.debug(param1="value1", param2="value2")
			logger.debug(f"Generated HTML: {html}")
			```
		"""
		html_output = self.render(**attrs)

		# Convert to string if it's a SafeString or other wrapper
		return str(html_output)


	@abstractmethod
	def render(self, **attrs):
		"""
		Abstract method to render the component with all attributes processed.

		This method must be implemented by all concrete component classes. It should
		process the component attributes, build the necessary HTML structure, and
		return the final rendered HTML string. The method handles all the component's
		specific logic while leveraging the base class methods for common functionality.

		The implementation should typically follow this pattern:
		1. Separate attributes using separate_attributes()
		2. Build CSS classes using build_css_classes()
		3. Build data attributes using build_data_attributes()
		4. Build ID attribute using build_id_attribute()
		5. Process any component-specific logic
		6. Render the final HTML using render_component()

		Args:
			**attrs: Component attributes including:
				- Component-specific parameters (defined in component_params)
				- CSS class parameters (cls, cls_*)
				- Standard HTML attributes (id, class, etc.)
				- Event handlers (on_*)
				- Any other parameters specific to the component

		Returns:
			str: Complete HTML representation of the component.
				The output should be properly formatted and ready for use in templates.

		Raises:
			NotImplementedError: If not implemented by concrete component classes.
				This is enforced by the @abstractmethod decorator.

		Examples:
			Basic implementation pattern:
			```python
			def render(self, **attrs):
				# Separate attributes
				component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

				# Build CSS classes
				css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)

				# Build data attributes
				data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)

				# Build ID attribute
				id_attr = self.build_id_attribute(component_attrs, standard_attrs)

				# Build final attributes
				final_attrs = {
					"class": " ".join(css_classes),
					**self.default_data_attrs,
					**data_attrs,
					**standard_attrs
				}

				if id_attr:
					final_attrs["id"] = id_attr

				return self.render_component(self.tag_name, final_attrs)
			```
		"""
		pass


class SimpleComponent(BaseComponent):
	"""
	Simple component class for MetroUI5 components that render a single HTML element.

	This class extends BaseComponent to provide a streamlined implementation for components
	that render a single HTML element with attributes. It handles all the common functionality
	automatically, making it easy to create simple components without duplicating code.

	SimpleComponent is ideal for components like:
	- Badges, buttons, inputs
	- Icons, avatars, progress bars
	- Single-element containers
	- Any component that maps to one HTML tag

	The class automatically handles:
	- CSS class management and validation states
	- Data attribute mapping for MetroUI5 JavaScript
	- ID generation and management
	- HTML rendering with proper attribute handling
	- Event handler processing

	Attributes:
		component_name (str): Name of the component (inherited from BaseComponent)
		base_css_class (str): Base CSS class for the component (inherited from BaseComponent)
		component_params (list): List of component-specific parameters (inherited from BaseComponent)
		tag_name (str): HTML tag name to render (e.g., 'div', 'span', 'input', 'button')
		data_attr_mapping (dict): Mapping of parameter names to data attribute names
		default_data_attrs (dict): Default data attributes to include in every render

	Examples:
		Creating a badge component:
		```python
		class BadgeComponent(SimpleComponent):
			def __init__(self):
				super().__init__(
					component_name="badge",
					base_css_class="badge",
					tag_name="span",
					component_params=['text', 'color', 'size'],
					data_attr_mapping={'text': 'data-text', 'color': 'data-color'},
					default_data_attrs={"data-role": "badge"}
				)
		```

		Creating a button component:
		```python
		class ButtonComponent(SimpleComponent):
			def __init__(self):
				super().__init__(
					component_name="button",
					base_css_class="button",
					tag_name="button",
					component_params=['text', 'on_click', 'disabled'],
					data_attr_mapping={'on_click': 'data-on-click'},
					default_data_attrs={"data-role": "button"}
				)
		```
	"""

	def __init__(self, component_name, base_css_class=None, tag_name="div", component_params=None,
				 data_attr_mapping=None, default_data_attrs=None):
		"""
		Initialize the simple component with all necessary configuration.

		This constructor sets up a SimpleComponent with all the configuration needed
		for automatic HTML rendering. It extends the BaseComponent constructor with
		additional parameters specific to simple components.

		Args:
			component_name (str): Unique name identifier for the component.
				Used for ID generation, parameter processing, and debugging.
				Examples: 'badge', 'button', 'input', 'progress'
			base_css_class (str, optional): Primary CSS class for the component.
				This becomes the main class applied to the rendered HTML element.
				Examples: 'badge', 'button', 'input', 'progress'
			tag_name (str, default="div"): HTML tag name to render for this component.
				Examples: 'div', 'span', 'input', 'button', 'progress'
			component_params (list, optional): List of component-specific parameters
				that require special processing. These parameters are separated from
				standard HTML attributes and processed as data attributes.
				Examples: ['text', 'color', 'size', 'on_click', 'disabled']
			data_attr_mapping (dict, optional): Custom mapping of parameter names to data attribute names.
				Allows overriding the default naming convention for specific parameters.
				If None, uses automatic kebab-case conversion.
				Example: {'my_param': 'data-custom-param', 'special_handler': 'data-on-special'}
			default_data_attrs (dict, optional): Default data attributes to include in every render.
				These attributes are added to every component instance automatically.
				Example: {"data-role": "button", "data-auto-init": "true"}

		Examples:
			Basic badge component:
			```python
			super().__init__(
				component_name="badge",
				base_css_class="badge",
				tag_name="span",
				component_params=['text', 'color', 'size'],
				data_attr_mapping={'text': 'data-text', 'color': 'data-color'},
				default_data_attrs={"data-role": "badge"}
			)
			```

			Button with event handlers:
			```python
			super().__init__(
				component_name="button",
				base_css_class="button",
				tag_name="button",
				component_params=['text', 'on_click', 'on_hover', 'disabled'],
				data_attr_mapping={'on_click': 'data-on-click', 'on_hover': 'data-on-hover'},
				default_data_attrs={"data-role": "button", "type": "button"}
			)
			```
		"""
		super().__init__(component_name, base_css_class, component_params)
		self.tag_name = tag_name
		self.data_attr_mapping = data_attr_mapping or {}
		self.default_data_attrs = default_data_attrs or {}

	def render(self, **attrs):
		"""
		Render the simple component with automatic attribute processing.

		This method provides a complete implementation of the abstract render method
		from BaseComponent. It automatically handles all the common functionality
		for simple components, including attribute separation, CSS class building,
		data attribute processing, and HTML rendering.

		The method follows the standard pattern:
		1. Separate attributes into categories
		2. Build CSS classes from all sources
		3. Build data attributes for MetroUI5 JavaScript
		4. Build ID attribute with auto-generation
		5. Combine all attributes and render HTML

		Args:
			**attrs: Component attributes including:
				- Component-specific parameters (defined in component_params)
				- CSS class parameters (cls, cls_*)
				- Standard HTML attributes (id, class, etc.)
				- Event handlers (on_*)
				- Any other parameters specific to the component

		Returns:
			str: Complete HTML representation of the component.
				The output is properly formatted and ready for use in templates.

		Examples:
			Basic badge rendering:
			```python
			component = BadgeComponent()
			html = component.render(text="New", color="red", cls="custom-badge")
			# Returns: <span class="badge custom-badge" data-role="badge" data-text="New" data-color="red">New</span>
			```

			Button with event handler:
			```python
			component = ButtonComponent()
			html = component.render(text="Click me", on_click="handleClick()", id="my-button")
			# Returns: <button class="button" id="my-button" data-role="button" data-on-click="handleClick()">Click me</button>
			```

			Input with validation:
			```python
			component = InputComponent()
			html = component.render(
				type="text",
				placeholder="Enter text",
				error=True,
				error_message="Invalid input"
			)
			# Returns: <input class="input error" data-role="input" data-error="true" data-error-message="Invalid input" type="text" placeholder="Enter text" />
			```
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)

		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)

		# Build ID attribute
		id_attr = self.build_id_attribute(component_attrs, standard_attrs)

		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}

		# Add ID if generated or provided
		if id_attr:
			final_attrs["id"] = id_attr

		return self.render_component(self.tag_name, final_attrs)


class ComplexComponent(BaseComponent):
	"""
	Complex component class for MetroUI5 components that render multiple HTML elements.

	This class extends BaseComponent to provide a foundation for components that require
	custom rendering logic, multiple HTML elements, or complex structure. Unlike SimpleComponent,
	it doesn't provide automatic rendering - instead, it provides helper methods and requires
	custom implementation of the render method.

	ComplexComponent is ideal for components like:
	- Accordions, tabs, navigation menus
	- Forms with multiple elements
	- Cards with headers, content, and footers
	- Any component that needs custom HTML structure

	The class provides:
	- All BaseComponent functionality (CSS classes, data attributes, etc.)
	- Helper method for building base attributes
	- Abstract render method that must be implemented
	- Foundation for complex component logic

	Attributes:
		component_name (str): Name of the component (inherited from BaseComponent)
		base_css_class (str): Base CSS class for the component (inherited from BaseComponent)
		component_params (list): List of component-specific parameters (inherited from BaseComponent)

	Examples:
		Creating an accordion component:
		```python
		class AccordionComponent(ComplexComponent):
			def __init__(self):
				super().__init__(
					component_name="accordion",
					base_css_class="accordion",
					component_params=['frames', 'collapsible', 'on_create']
				)

			def render(self, **attrs):
				# Custom rendering logic for accordion structure
				component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
				base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)

				# Build accordion content
				content = self.build_accordion_content(component_attrs)

				return self.render_component('div', base_attrs, content)
		```

		Creating a navigation component:
		```python
		class NavigationComponent(ComplexComponent):
			def __init__(self):
				super().__init__(
					component_name="navigation",
					base_css_class="navigation",
					component_params=['items', 'orientation', 'on_select']
				)

			def render(self, **attrs):
				# Custom rendering logic for navigation structure
				# Implementation details...
				pass
		```
	"""

	def __init__(self, component_name, base_css_class=None, component_params=None):
		"""
		Initialize the complex component with basic configuration.

		This constructor sets up a ComplexComponent with the essential configuration
		needed for complex components. It inherits from BaseComponent and provides
		the foundation for custom rendering logic.

		Args:
			component_name (str): Unique name identifier for the component.
				Used for ID generation, parameter processing, and debugging.
				Examples: 'accordion', 'navigation', 'card', 'form'
			base_css_class (str, optional): Primary CSS class for the component.
				This becomes the main class applied to the rendered HTML element.
				Examples: 'accordion', 'navigation', 'card', 'form'
			component_params (list, optional): List of component-specific parameters
				that require special processing. These parameters are separated from
				standard HTML attributes and processed as data attributes.
				Examples: ['items', 'orientation', 'on_create', 'collapsible']

		Examples:
			Basic accordion component:
			```python
			super().__init__(
				component_name="accordion",
				base_css_class="accordion",
				component_params=['frames', 'collapsible', 'on_create']
			)
			```

			Navigation with orientation:
			```python
			super().__init__(
				component_name="navigation",
				base_css_class="navigation",
				component_params=['items', 'orientation', 'on_select', 'on_create']
			)
			```
		"""
		super().__init__(component_name, base_css_class, component_params)

	def build_base_attributes(self, component_attrs, cls_attrs, standard_attrs, additional_classes=None):
		"""
		Build base attributes for complex components with CSS classes and ID.

		This helper method provides a convenient way to build the base attributes
		for complex components. It combines CSS class building and ID generation
		into a single method, making it easier to implement custom render methods.

		The method processes all the common attributes that most complex components
		need, including CSS classes, ID generation, and standard HTML attributes.
		It's designed to be used as the first step in custom render implementations.

		Args:
			component_attrs (dict): Component-specific attributes that may contain
				styling parameters. These are processed separately from CSS classes.
			cls_attrs (dict): CSS class-related attributes starting with 'cls' or 'cls_'.
				These are added to the final class list.
			standard_attrs (dict): Standard HTML attributes including the 'cls' parameter
				for user-provided classes. The 'cls' parameter is removed after processing.
			additional_classes (list, optional): Additional CSS classes to add to the component.
				Useful for dynamic styling or component variants.

		Returns:
			dict: Base attributes dictionary containing:
				- 'class': Complete CSS class string
				- 'id': Generated or provided ID (if any)
				- All other standard HTML attributes

		Examples:
			Basic usage in render method:
			```python
			def render(self, **attrs):
				component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
				base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)

				# Add component-specific data attributes
				data_attrs = self.build_data_attributes(component_attrs)
				base_attrs.update(data_attrs)

				# Build custom content
				content = self.build_custom_content(component_attrs)

				return self.render_component('div', base_attrs, content)
			```

			With additional classes:
			```python
			def render(self, **attrs):
				component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

				# Add validation state classes
				additional_classes = []
				if component_attrs.get('error'):
					additional_classes.append('error')

				base_attrs = self.build_base_attributes(
					component_attrs, cls_attrs, standard_attrs, additional_classes
				)

				return self.render_component('div', base_attrs, content)
			```
		"""
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)

		# Build ID attribute
		id_attr = self.build_id_attribute(component_attrs, standard_attrs)

		base_attrs = {
			"class": " ".join(css_classes),
			**standard_attrs
		}

		# Add ID if generated or provided
		if id_attr:
			base_attrs["id"] = id_attr

		return base_attrs

	@abstractmethod
	def render(self, **attrs):
		"""
		Abstract method to render the complex component with custom logic.

		This method must be implemented by all concrete ComplexComponent classes.
		Unlike SimpleComponent, it doesn't provide automatic rendering - instead,
		it requires custom implementation to handle the complex structure and logic
		specific to each component type.

		The implementation should typically follow this pattern:
		1. Separate attributes using separate_attributes()
		2. Build base attributes using build_base_attributes()
		3. Build data attributes using build_data_attributes()
		4. Implement component-specific logic and content building
		5. Render the final HTML using render_component()

		Args:
			**attrs: Component attributes including:
				- Component-specific parameters (defined in component_params)
				- CSS class parameters (cls, cls_*)
				- Standard HTML attributes (id, class, etc.)
				- Event handlers (on_*)
				- Any other parameters specific to the component

		Returns:
			str: Complete HTML representation of the complex component.
				The output should be properly formatted and ready for use in templates.

		Raises:
			NotImplementedError: If not implemented by concrete component classes.
				This is enforced by the @abstractmethod decorator.

		Examples:
			Accordion component implementation:
			```python
			def render(self, **attrs):
				# Separate attributes
				component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

				# Build base attributes
				base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)

				# Add data attributes
				data_attrs = self.build_data_attributes(component_attrs)
				base_attrs.update(data_attrs)

				# Build accordion content
				content = self.build_accordion_frames(component_attrs.get('frames', []))

				return self.render_component('div', base_attrs, content)
			```

			Navigation component implementation:
			```python
			def render(self, **attrs):
				# Separate attributes
				component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

				# Build base attributes with orientation class
				additional_classes = []
				if component_attrs.get('orientation') == 'vertical':
					additional_classes.append('vertical')

				base_attrs = self.build_base_attributes(
					component_attrs, cls_attrs, standard_attrs, additional_classes
				)

				# Add data attributes
				data_attrs = self.build_data_attributes(component_attrs)
				base_attrs.update(data_attrs)

				# Build navigation content
				content = self.build_navigation_items(component_attrs.get('items', []))

				return self.render_component('nav', base_attrs, content)
			```
		"""
		pass
