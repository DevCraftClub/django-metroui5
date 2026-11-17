"""
MetroUI Bar3d Component
"""

from .base import SimpleComponent


class Bar3dComponent(SimpleComponent):
	"""
	MetroUI Bar3d Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/bar3d/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/bar3d/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/bar3d/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/bar3d/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/bar3d/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/bar3d/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="bar3d",
			base_css_class="bar3d",
			tag_name="div",
			component_params=[
				'height', 'bar_color', 'value_color', 'total', 'value', 'value_suffix',
				'animation_duration', 'on_bar3d_create', 'cls_bar3d'
			],
			data_attr_mapping={
				'bar_color': 'data-bar-color',
				'value_color': 'data-value-color',
				'value_suffix': 'data-value-suffix',
				'animation_duration': 'data-animation-duration'
			},
			default_data_attrs={
				"data-role": "bar3d"
			}
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI bar3d component.
		
		Args:
			**attrs: Additional HTML attributes including:
				height (int): The height of the bar (default: 200)
				bar_color (str): The color of the growing bar (default: "#22ec1a")
				value_color (str): The color of the displayed value text (default: "#191919")
				total (int): The total value (maximum) (default: 100)
				value (int): The current value to display (default: 60)
				value_suffix (str): A suffix to append to the displayed value (e.g., "%")
				animation_duration (int): The duration of the animation in milliseconds (default: 300)
				on_bar3d_create (str): Callback function triggered when the component is created
				cls_bar3d (str): Additional CSS class for the bar3d container
			
		Returns:
			str: Rendered HTML div element with bar3d functionality
			
		References:
			.. _MetroUI Bar3d: https://v5.metroui.org.ua/components/bar3d/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		return super().render(**attrs)


# Create component instance
_bar3d_component = Bar3dComponent()


def render_bar3d(**attrs):
	"""
	Renders MetroUI bar3d component.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/bar3d/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/bar3d/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/bar3d/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/bar3d/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/bar3d/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/bar3d/#styling-with-css-variables>`_
	
	Args:
		**attrs: Additional HTML attributes including:
			height (int): The height of the bar (default: 200)
			bar_color (str): The color of the growing bar (default: "#22ec1a")
			value_color (str): The color of the displayed value text (default: "#191919")
			total (int): The total value (maximum) (default: 100)
			value (int): The current value to display (default: 60)
			value_suffix (str): A suffix to append to the displayed value (e.g., "%")
			animation_duration (int): The duration of the animation in milliseconds (default: 300)
			on_bar3d_create (str): Callback function triggered when the component is created
			cls_bar3d (str): Additional CSS class for the bar3d container
		
	Returns:
		str: Rendered HTML div element with bar3d functionality
		
	References:
		.. _MetroUI Bar3d: https://v5.metroui.org.ua/components/bar3d/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_bar3d()

	Empty or invalid:
		`render_bar3d()` returns `<div class="bar3d" data-role="bar3d" id="bar3d-component"></div>`.

	"""
	return _bar3d_component.render(**attrs)
