"""
MetroUI Activity Component
"""

from .base import SimpleComponent


class ActivityComponent(SimpleComponent):
	"""
	MetroUI Activity Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/activity/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/activity/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/activity/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/activity/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/activity/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="activity",
			base_css_class="activity",
			tag_name="div",
			component_params=[
				'activityDeferred', 'type', 'style', 'size', 'radius', 
				'onActivityCreate', 'cls_activity'
			],
			data_attr_mapping={
				'activityDeferred': 'data-activity-deferred',
				'type': 'data-type',
				'style': 'data-style',
				'size': 'data-size',
				'radius': 'data-radius'
			},
			default_data_attrs={"data-role": "activity"}
		)
	
	def render(self, **attrs):
		"""
		Renders MetroUI activity component with animated loading indicators.
		
		Args:
			**attrs: Additional HTML attributes including:
				activityDeferred (int): Deferred initialization time in milliseconds
				type (str): Type of activity indicator - Options: "ring", "metro", "square", "cycle", "simple", "atom", "bars"
				style (str): Style of the activity indicator - Options: "", "dark", "color"
				size (int): Size of the activity indicator in pixels
				radius (int): Radius for the "simple" type activity indicator
				onActivityCreate (str): Callback function triggered when the activity indicator is created
				cls_activity (str): Additional CSS class for the activity container
			
		Returns:
			str: Rendered HTML div element with activity indicator functionality
			
		References:
			.. _MetroUI Activity: https://v5.metroui.org.ua/components/activity/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
		
		# Build data attributes
		data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
		
		# Add activity-specific data attributes
		if component_attrs.get('onActivityCreate'):
			data_attrs["data-on-activity-create"] = component_attrs['onActivityCreate']
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			**self.default_data_attrs,
			**data_attrs,
			**standard_attrs
		}
		
		return self.render_component(self.tag_name, final_attrs, close=True)


# Create component instance
_activity_component = ActivityComponent()


def render_activity(**attrs):
	"""
	Renders MetroUI activity component with animated loading indicators.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/activity/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/activity/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/activity/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/activity/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/activity/#styling-with-css-variables>`_
	
	Args:
		**attrs: Additional HTML attributes including:
			activityDeferred (int): Deferred initialization time in milliseconds
			type (str): Type of activity indicator - Options: "ring", "metro", "square", "cycle", "simple", "atom", "bars"
			style (str): Style of the activity indicator - Options: "", "dark", "color"
			size (int): Size of the activity indicator in pixels
			radius (int): Radius for the "simple" type activity indicator
			onActivityCreate (str): Callback function triggered when the activity indicator is created
			cls_activity (str): Additional CSS class for the activity container
		
	Returns:
		str: Rendered HTML div element with activity indicator functionality
		
	References:
		.. _MetroUI Activity: https://v5.metroui.org.ua/components/activity/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _activity_component.render(**attrs)
