"""
MetroUI Container Component

This module provides the Container component for MetroUI 5.
The Container component provides responsive layout containers that help center
and horizontally pad your content. It's a fundamental building block for creating
responsive layouts in Metro UI.

References:
    - `MetroUI Container <https://v5.metroui.org.ua/components/container/>`_
    - `MetroUI Documentation <https://v5.metroui.org.ua/>`_
"""

from .base import ComplexComponent


class ContainerComponent(ComplexComponent):
	"""
	MetroUI Container component for responsive layout containers.
	
	The Container component provides responsive layout containers that help center
	and horizontally pad your content. It's a fundamental building block for creating
	responsive layouts in Metro UI.
	
	Features:
	- Responsive containers that adapt to different screen sizes
	- Fluid container option for full-width layouts
	- Fixed-width container options for specific breakpoints
	- Container query support for component-level responsiveness
	- Consistent padding on left and right sides (12px by default)
	- Automatic centering with margin: 0 auto
	- Relative positioning, allowing absolute positioning of child elements
	
	References:
		- `MetroUI Container <https://v5.metroui.org.ua/components/container/>`_
		- `Dependencies <https://v5.metroui.org.ua/components/container/#dependencies>`_
		- `Usage <https://v5.metroui.org.ua/components/container/#usage>`_
		- `Styling <https://v5.metroui.org.ua/components/container/#styling-with-css-variables>`_
		- `CSS Classes <https://v5.metroui.org.ua/components/container/#available-css-classes>`_
		- `Responsive Behavior <https://v5.metroui.org.ua/components/container/#responsive-behavior>`_
		- `Container Queries <https://v5.metroui.org.ua/components/container/#container-queries>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="container",
			base_css_class="container",
			component_params=[
				'fluid', 'max', 'query', 'responsive', 'xs', 'sm', 'md', 'lg', 'xl', 'xxl',
				'semantic', 'tag'
			]
		)
	
	def render(self, content="", **attrs):
		"""
		Renders MetroUI container component for responsive layout containers.

		Args:
			content (str): Content to be placed inside the container
			**attrs: HTML attributes including:
				fluid (bool): Whether to create a fluid container (full-width)
				max (bool): Whether to create a maximum width container (100%)
				query (bool): Whether to enable container query support
				responsive (bool): Whether to enable responsive container queries
				xs (bool): Whether to use xs breakpoint max-width
				sm (bool): Whether to use sm breakpoint max-width
				md (bool): Whether to use md breakpoint max-width
				lg (bool): Whether to use lg breakpoint max-width
				xl (bool): Whether to use xl breakpoint max-width
				xxl (bool): Whether to use xxl breakpoint max-width
				semantic (bool): Whether to use semantic HTML element
				tag (str): HTML tag to use (div, section, header, footer, aside, main, article)
				cls (str): Additional CSS classes
				id (str): ID attribute for the container element
		
		Returns:
			str: Rendered HTML container element with responsive styling
			
		References:
			- `MetroUI Container <https://v5.metroui.org.ua/components/container/>`_
			- `Basic Usage <https://v5.metroui.org.ua/components/container/#basic-usage>`_
			- `Additional Configurations <https://v5.metroui.org.ua/components/container/#additional-configurations>`_
			- `Styling <https://v5.metroui.org.ua/components/container/#styling-with-css-variables>`_
			- `CSS Classes <https://v5.metroui.org.ua/components/container/#available-css-classes>`_
			- `Responsive Behavior <https://v5.metroui.org.ua/components/container/#responsive-behavior>`_
			- `Container Queries <https://v5.metroui.org.ua/components/container/#container-queries>`_

		Examples:
			Basic container:
			.. code-block:: python
				render_container(content="<p>Your content here</p>")

			Fluid container:
			.. code-block:: python
				render_container(content="<p>Full-width content</p>", fluid=True)

			Fixed-width container:
			.. code-block:: python
				render_container(content="<p>Medium width content</p>", md=True)

			Container with queries:
			.. code-block:: python
				render_container(content="<p>Responsive content</p>", query=True)

			Semantic container:
			.. code-block:: python
				render_container(content="<h1>Header content</h1>", semantic=True, tag="header")
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Determine container type and CSS class
		css_classes = []
		
		# Check for specific container types
		if component_attrs.get('fluid'):
			css_classes.append('container-fluid')
		elif component_attrs.get('max'):
			css_classes.append('container-max')
		elif component_attrs.get('query'):
			css_classes.append('container-query')
		elif component_attrs.get('responsive'):
			css_classes.append('responsive-container')
		elif component_attrs.get('xs'):
			css_classes.append('container-xs')
		elif component_attrs.get('sm'):
			css_classes.append('container-sm')
		elif component_attrs.get('md'):
			css_classes.append('container-md')
		elif component_attrs.get('lg'):
			css_classes.append('container-lg')
		elif component_attrs.get('xl'):
			css_classes.append('container-xl')
		elif component_attrs.get('xxl'):
			css_classes.append('container-xxl')
		else:
			# Default container
			css_classes.append(self.base_css_class)
		
		# Update class attribute
		base_attrs['class'] = ' '.join(css_classes)
		
		# Determine HTML tag
		tag = 'div'
		if component_attrs.get('semantic') or component_attrs.get('tag'):
			tag = component_attrs.get('tag', 'div')
			# Validate semantic tag
			valid_semantic_tags = ['div', 'section', 'header', 'footer', 'aside', 'main', 'article']
			if tag not in valid_semantic_tags:
				tag = 'div'
		
		return self.render_component(tag, base_attrs, content=content)


# Create component instance
_container_component = ContainerComponent()


def render_container(content="", **attrs):
	"""
	Renders MetroUI container component for responsive layout containers.

	The Container component provides responsive layout containers that help center
	and horizontally pad your content. It's a fundamental building block for creating
	responsive layouts in Metro UI.

	Args:
		content (str): Content to be placed inside the container
		**attrs: HTML attributes including:
			fluid (bool): Whether to create a fluid container (full-width)
			max (bool): Whether to create a maximum width container (100%)
			query (bool): Whether to enable container query support
			responsive (bool): Whether to enable responsive container queries
			xs (bool): Whether to use xs breakpoint max-width
			sm (bool): Whether to use sm breakpoint max-width
			md (bool): Whether to use md breakpoint max-width
			lg (bool): Whether to use lg breakpoint max-width
			xl (bool): Whether to use xl breakpoint max-width
			xxl (bool): Whether to use xxl breakpoint max-width
			semantic (bool): Whether to use semantic HTML element
			tag (str): HTML tag to use (div, section, header, footer, aside, main, article)
			cls (str): Additional CSS classes
			id (str): ID attribute for the container element
		
		Returns:
			str: Rendered HTML container element with responsive styling
			
		References:
			- `MetroUI Container <https://v5.metroui.org.ua/components/container/>`_
			- `Basic Usage <https://v5.metroui.org.ua/components/container/#basic-usage>`_
			- `Additional Configurations <https://v5.metroui.org.ua/components/container/#additional-configurations>`_
			- `Styling <https://v5.metroui.org.ua/components/container/#styling-with-css-variables>`_
			- `CSS Classes <https://v5.metroui.org.ua/components/container/#available-css-classes>`_
			- `Responsive Behavior <https://v5.metroui.org.ua/components/container/#responsive-behavior>`_
			- `Container Queries <https://v5.metroui.org.ua/components/container/#container-queries>`_

		Examples:
			Basic container:
			.. code-block:: python
				render_container(content="<p>Your content here</p>")

			Fluid container:
			.. code-block:: python
				render_container(content="<p>Full-width content</p>", fluid=True)

			Fixed-width container:
			.. code-block:: python
				render_container(content="<p>Medium width content</p>", md=True)

			Container with queries:
			.. code-block:: python
				render_container(content="<p>Responsive content</p>", query=True)

			Semantic container:
			.. code-block:: python
				render_container(content="<h1>Header content</h1>", semantic=True, tag="header")
	Example:
		render_container()

	Empty or invalid:
		`render_container()` returns `<div class="container" id="container-component"></div>`.

	"""
	return _container_component.render(content=content, **attrs)
