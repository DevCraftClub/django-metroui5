"""
MetroUI Action Button Component
"""

from .base import ComplexComponent
from ..html import render_tag


class ActionButtonComponent(ComplexComponent):
	"""
	MetroUI Action Button Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/action-button/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/action-button/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/action-button/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/action-button/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/action-button/#styling-with-css-variables>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="action_button",
			base_css_class="action-button",
			component_params=[
				'rotate', 'main_href', 'main_title', 'main_onclick', 'cls_action_button',
				'cls_main_action', 'cls_actions', 'cls_sub_action', 'onClick', 'onActionClick',
				'onActionButtonCreate'
			]
		)
	
	def render(self, actions, main_icon="mif-plus", **attrs):
		"""
		Renders MetroUI action button component with expandable sub-actions.
		
		Args:
			actions: List of dictionaries with 'icon', 'href', 'title', and optional 'onclick' keys
			main_icon: Icon class for the main action button
			**attrs: Additional HTML attributes including:
				rotate (bool): Add rotation effect to main button
				main_href (str): URL for main button
				main_title (str): Title/tooltip for main button
				main_onclick (str): JavaScript onclick handler for main button
				cls_action_button (str): Additional CSS class for action button container
				cls_main_action (str): Additional CSS class for main action button
				cls_actions (str): Additional CSS class for actions container
				cls_sub_action (str): Additional CSS class for sub-action items
				onClick (str): Callback function triggered when the main button is clicked
				onActionClick (str): Callback function triggered when a sub-action is clicked
				onActionButtonCreate (str): Callback function triggered when the action button is created
			
		Returns:
			str: Rendered HTML div element with action button functionality
			
		References:
			.. _MetroUI Action Button: https://v5.metroui.org.ua/components/action-button/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add data-role attribute
		base_attrs["data-role"] = "action-button"
		
		# Add action button-specific data attributes
		if component_attrs.get('onClick'):
			base_attrs["data-on-click"] = component_attrs['onClick']
		
		if component_attrs.get('onActionClick'):
			base_attrs["data-on-action-click"] = component_attrs['onActionClick']
		
		if component_attrs.get('onActionButtonCreate'):
			base_attrs["data-on-action-button-create"] = component_attrs['onActionButtonCreate']
		
		# Build main action button
		main_button_classes = ["main-action"]
		if component_attrs.get('rotate'):
			main_button_classes.append("rotate")
		if component_attrs.get('cls_main_action'):
			main_button_classes.append(component_attrs['cls_main_action'])
		
		main_button_attrs = {"class": " ".join(main_button_classes)}
		
		if component_attrs.get('main_href'):
			main_button_attrs["href"] = component_attrs['main_href']
		
		if component_attrs.get('main_title'):
			main_button_attrs["title"] = component_attrs['main_title']
		
		if component_attrs.get('main_onclick'):
			main_button_attrs["onclick"] = component_attrs['main_onclick']
		
		main_button = render_tag(
			"button",
			main_button_attrs,
			render_tag("span", {"class": "icon"}, render_tag("span", {"class": main_icon}))
		)
		
		# Build sub-actions
		actions_classes = ["actions"]
		if component_attrs.get('cls_actions'):
			actions_classes.append(component_attrs['cls_actions'])
		
		sub_actions = []
		for action in actions:
			sub_action_classes = ["sub-action"]
			if component_attrs.get('cls_sub_action'):
				sub_action_classes.append(component_attrs['cls_sub_action'])
			
			action_attrs_dict = {"class": " ".join(sub_action_classes)}
			
			if action.get('href'):
				action_attrs_dict["href"] = action['href']
			
			if action.get('title'):
				action_attrs_dict["title"] = action['title']
			
			if action.get('onclick'):
				action_attrs_dict["onclick"] = action['onclick']
			
			action_icon = action.get('icon', 'mif-circle')
			action_content = render_tag("span", {"class": action_icon})
			
			sub_action = render_tag("li", {}, render_tag("a", action_attrs_dict, action_content))
			sub_actions.append(sub_action)
		
		actions_list = render_tag("ul", {"class": " ".join(actions_classes)}, "".join(sub_actions))
		
		# Combine main button and actions
		content = main_button + actions_list
		
		return render_tag("div", attrs=base_attrs, content=content)


# Create component instance
_action_button_component = ActionButtonComponent()


def render_action_button(actions, main_icon="mif-plus", **attrs):
	"""
	Renders MetroUI action button component with expandable sub-actions.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/action-button/>`_.
	
	You can also reference specific sections:
	- `Basic Usage <https://v5.metroui.org.ua/components/action-button/#usage>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/action-button/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/action-button/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/action-button/#styling-with-css-variables>`_
	
	Args:
		actions: List of dictionaries with 'icon', 'href', 'title', and optional 'onclick' keys
		main_icon: Icon class for the main action button
		**attrs: Additional HTML attributes including:
			rotate (bool): Add rotation effect to main button
			main_href (str): URL for main button
			main_title (str): Title/tooltip for main button
			main_onclick (str): JavaScript onclick handler for main button
			cls_action_button (str): Additional CSS class for action button container
			cls_main_action (str): Additional CSS class for main action button
			cls_actions (str): Additional CSS class for actions container
			cls_sub_action (str): Additional CSS class for sub-action items
			onClick (str): Callback function triggered when the main button is clicked
			onActionClick (str): Callback function triggered when a sub-action is clicked
			onActionButtonCreate (str): Callback function triggered when the action button is created
		
	Returns:
		str: Rendered HTML div element with action button functionality
		
	References:
		.. _MetroUI Action Button: https://v5.metroui.org.ua/components/action-button/
		.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _action_button_component.render(actions, main_icon, **attrs)
