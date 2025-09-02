"""
MetroUI Action Button Component
"""

from ..html import render_tag


def render_action_button(actions, main_icon="mif-plus", **attrs):
	"""
	Renders MetroUI action button component with expandable sub-actions.

	Link: https://v5.metroui.org.ua/components/action-button/

	Args:
		actions: List of dictionaries with 'icon', 'href', 'title', and optional 'onclick' keys
		main_icon: Icon class for the main action button (string)
		**attrs: Additional HTML attributes including:
			# Action Button Parameters
			- rotate: Add rotation effect to main button (boolean)
			- main_href: URL for main button (string)
			- main_title: Title/tooltip for main button (string)
			- main_onclick: JavaScript onclick handler for main button (string)
			- cls_action_button: Additional CSS class for action button container (string)
			- cls_main_action: Additional CSS class for main action button (string)
			- cls_actions: Additional CSS class for actions container (string)
			- cls_sub_action: Additional CSS class for sub-action items (string)
			- onClick: Callback function triggered when the main button is clicked (string)
			- onActionClick: Callback function triggered when a sub-action is clicked (string)
			- onActionButtonCreate: Callback function triggered when the action button is created (string)
	"""
	# Extract action button-specific attributes
	action_attrs = {}
	standard_attrs = {}
	
	# Action button-specific parameters
	action_params = [
		'rotate', 'main_href', 'main_title', 'main_onclick', 'cls_action_button',
		'cls_main_action', 'cls_actions', 'cls_sub_action', 'onClick', 'onActionClick',
		'onActionButtonCreate'
	]
	
	# Separate action button attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in action_params:
			action_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"data-role": "action-button"
	}
	
	# Add action button-specific data attributes
	if action_attrs.get('onClick'):
		default_attrs["data-on-click"] = action_attrs['onClick']
	
	if action_attrs.get('onActionClick'):
		default_attrs["data-on-action-click"] = action_attrs['onActionClick']
	
	if action_attrs.get('onActionButtonCreate'):
		default_attrs["data-on-action-button-create"] = action_attrs['onActionButtonCreate']
	
	# Build CSS classes
	css_classes = ["action-button"]
	
	if action_attrs.get('cls_action_button'):
		css_classes.append(action_attrs['cls_action_button'])
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	# Build main action button
	main_button_classes = ["main-action"]
	if action_attrs.get('rotate'):
		main_button_classes.append("rotate")
	if action_attrs.get('cls_main_action'):
		main_button_classes.append(action_attrs['cls_main_action'])
	
	main_button_attrs = {"class": " ".join(main_button_classes)}
	
	if action_attrs.get('main_href'):
		main_button_attrs["href"] = action_attrs['main_href']
	
	if action_attrs.get('main_title'):
		main_button_attrs["title"] = action_attrs['main_title']
	
	if action_attrs.get('main_onclick'):
		main_button_attrs["onclick"] = action_attrs['main_onclick']
	
	main_button = render_tag(
		"button",
		main_button_attrs,
		render_tag("span", {"class": "icon"}, render_tag("span", {"class": main_icon}))
	)
	
	# Build sub-actions
	actions_classes = ["actions"]
	if action_attrs.get('cls_actions'):
		actions_classes.append(action_attrs['cls_actions'])
	
	sub_actions = []
	for action in actions:
		sub_action_classes = ["sub-action"]
		if action_attrs.get('cls_sub_action'):
			sub_action_classes.append(action_attrs['cls_sub_action'])
		
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
	
	return render_tag("div", attrs=final_attrs, content=content)
