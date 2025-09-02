"""
MetroUI Alert Component
"""

from .base import SimpleComponent
from ..html import render_tag


class AlertComponent(SimpleComponent):
	"""
	MetroUI Alert Component
	"""
	
	def __init__(self):
		super().__init__(
			component_name="alert",
			base_css_class="alert",
			tag_name="div",
			component_params=['alert_type', 'dismissible', 'cls_alert']
		)
	
	def render(self, content, alert_type="info", dismissible=False, **attrs):
		"""
		Renders MetroUI alert component.

		Args:
			content: Alert content
			alert_type: Alert type (info, success, warning, danger, error)
			dismissible: Whether alert can be dismissed
			**attrs: Additional HTML attributes including:
				cls_alert (str): Additional CSS class for the alert container
		"""
		# Build additional classes based on parameters
		additional_classes = [f"alert-{alert_type}"]
		if dismissible:
			additional_classes.append("alert-dismissible")
		
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build CSS classes
		css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)
		
		# Build final attributes
		final_attrs = {
			"class": " ".join(css_classes),
			"role": "alert",
			**standard_attrs
		}
		
		# Add close button if dismissible
		if dismissible:
			close_button = render_tag(
				"button",
				{
					"type": "button",
					"class": "button button-mini",
					"data-role": "close",
					"aria-label": "Close"
				},
				"&times;"
			)
			content = f"{content}{close_button}"
		
		return self.render_component(self.tag_name, final_attrs, content=content)


# Create component instance
_alert_component = AlertComponent()


def render_alert(content, alert_type="info", dismissible=False, **attrs):
	"""
	Renders MetroUI alert component.

	Args:
		content: Alert content
		alert_type: Alert type (info, success, warning, danger, error)
		dismissible: Whether alert can be dismissed
		**attrs: Additional HTML attributes including:
			cls_alert (str): Additional CSS class for the alert container
	"""
	return _alert_component.render(content, alert_type, dismissible, **attrs)
