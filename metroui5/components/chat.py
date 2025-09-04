"""
MetroUI Chat Component
"""

from .base import ComplexComponent
from ..html import render_tag


class ChatComponent(ComplexComponent):
	"""
	MetroUI Chat Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/chat/>`_.
	
	You can also reference specific sections:
	- `Dependencies <https://v5.metroui.org.ua/components/chat/#dependencies>`_
	- `Basic Usage <https://v5.metroui.org.ua/components/chat/#basic-usage>`_
	- `With Configuration Options <https://v5.metroui.org.ua/components/chat/#with-configuration-options>`_
	- `Programmatic Initialization <https://v5.metroui.org.ua/components/chat/#programmatic-initialization>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/chat/#plugin-parameters>`_
	- `Message Structure <https://v5.metroui.org.ua/components/chat/#message-structure>`_
	- `API Methods <https://v5.metroui.org.ua/components/chat/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/chat/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/chat/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/chat/#available-css-classes>`_
	- `Best Practices <https://v5.metroui.org.ua/components/chat/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="chat",
			base_css_class="chat",
			component_params=[
				'chatDeferred', 'inputTimeFormat', 'timeFormat', 'name', 'avatar', 'welcome',
				'welcomeAvatar', 'title', 'width', 'height', 'initialHeight', 'messages',
				'attachAccept', 'readonly', 'sendMode', 'useEmoji', 'useLink', 'useCode',
				'buttons', 'clsChat', 'clsName', 'clsTime', 'clsInput', 'clsSendButton',
				'clsMessageLeft', 'clsMessageRight', 'onMessage', 'onSend', 'onSendButtonClick',
				'onChatCreate'
			]
		)
	
	def render(self, messages=None, **attrs):
		"""
		Renders MetroUI chat component for interactive messaging interface.

		Args:
			messages: Initial messages to display (list of message objects)
			**attrs: Additional HTML attributes including:
				chatDeferred (int): Deferred initialization time in milliseconds
				inputTimeFormat (str): Format for parsing input time strings
				timeFormat (str): Format for displaying message timestamps
				name (str): Default name for outgoing messages
				avatar (str): HTML for the avatar of outgoing messages
				welcome (str): Welcome message text
				welcomeAvatar (str): HTML for the avatar of the welcome message
				title (str): Title for the chat component
				width (str): Width of the chat component
				height (str): Height of the chat component
				initialHeight (int): Initial Height of the chat component
				attachAccept (str): Attach file types
				readonly (bool): Whether the chat is in read-only mode
				sendMode (str): Trigger for message send (enter, control+enter, button)
				useEmoji (bool): Use emoji in message
				useLink (bool): Use link in message
				useCode (bool): Use code blocks in message
				buttons (str): Buttons to use
				clsChat (str): Additional CSS class for the chat container
				clsName (str): Additional CSS class for the sender name
				clsTime (str): Additional CSS class for the message time
				clsInput (str): Additional CSS class for the input field
				clsSendButton (str): Additional CSS class for the send button
				clsMessageLeft (str): CSS class for left-aligned messages
				clsMessageRight (str): CSS class for right-aligned messages
				onMessage (str): Callback function when message is added
				onSend (str): Callback function when message is sent
				onSendButtonClick (str): Callback function when send button is clicked
				onChatCreate (str): Callback function when chat is created
		
		Returns:
			str: Rendered HTML div element with chat functionality
			
		References:
			.. _MetroUI Chat: https://v5.metroui.org.ua/components/chat/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Generate unique ID for each chat component to avoid conflicts
		import uuid
		unique_id = f"chat-{uuid.uuid4().hex[:8]}"
		base_attrs["id"] = unique_id
		
		# Add chat-specific data attributes
		base_attrs["data-role"] = "chat"
		
		# Add configuration parameters
		if component_attrs.get('name'):
			base_attrs["data-name"] = component_attrs['name']
		
		if component_attrs.get('avatar'):
			base_attrs["data-avatar"] = component_attrs['avatar']
		
		if component_attrs.get('welcome'):
			base_attrs["data-welcome"] = component_attrs['welcome']
		
		if component_attrs.get('welcomeAvatar'):
			base_attrs["data-welcome-avatar"] = component_attrs['welcomeAvatar']
		
		if component_attrs.get('title'):
			base_attrs["data-title"] = component_attrs['title']
		
		if component_attrs.get('width'):
			base_attrs["data-width"] = component_attrs['width']
		
		if component_attrs.get('height'):
			base_attrs["data-height"] = component_attrs['height']
		
		if component_attrs.get('initialHeight'):
			base_attrs["data-initial-height"] = str(component_attrs['initialHeight'])
		
		if component_attrs.get('attachAccept'):
			base_attrs["data-attach-accept"] = component_attrs['attachAccept']
		
		if component_attrs.get('readonly'):
			base_attrs["data-readonly"] = str(component_attrs['readonly']).lower()
		
		if component_attrs.get('sendMode'):
			base_attrs["data-send-mode"] = component_attrs['sendMode']
		
		if component_attrs.get('useEmoji'):
			base_attrs["data-use-emoji"] = str(component_attrs['useEmoji']).lower()
		
		if component_attrs.get('useLink'):
			base_attrs["data-use-link"] = str(component_attrs['useLink']).lower()
		
		if component_attrs.get('useCode'):
			base_attrs["data-use-code"] = str(component_attrs['useCode']).lower()
		
		if component_attrs.get('buttons'):
			base_attrs["data-buttons"] = component_attrs['buttons']
		
		if component_attrs.get('timeFormat'):
			base_attrs["data-time-format"] = component_attrs['timeFormat']
		
		if component_attrs.get('inputTimeFormat'):
			base_attrs["data-input-time-format"] = component_attrs['inputTimeFormat']
		
		# Add deferred initialization if specified
		if component_attrs.get('chatDeferred'):
			base_attrs["data-chat-deferred"] = str(component_attrs['chatDeferred'])
		
		# Add callback functions if specified
		if component_attrs.get('onMessage'):
			base_attrs["data-on-message"] = component_attrs['onMessage']
		
		if component_attrs.get('onSend'):
			base_attrs["data-on-send"] = component_attrs['onSend']
		
		if component_attrs.get('onSendButtonClick'):
			base_attrs["data-on-send-button-click"] = component_attrs['onSendButtonClick']
		
		if component_attrs.get('onChatCreate'):
			base_attrs["data-on-chat-create"] = component_attrs['onChatCreate']
		
		# Add CSS class parameters
		if component_attrs.get('clsName'):
			base_attrs["data-cls-name"] = component_attrs['clsName']
		
		if component_attrs.get('clsTime'):
			base_attrs["data-cls-time"] = component_attrs['clsTime']
		
		if component_attrs.get('clsInput'):
			base_attrs["data-cls-input"] = component_attrs['clsInput']
		
		if component_attrs.get('clsSendButton'):
			base_attrs["data-cls-send-button"] = component_attrs['clsSendButton']
		
		if component_attrs.get('clsMessageLeft'):
			base_attrs["data-cls-message-left"] = component_attrs['clsMessageLeft']
		
		if component_attrs.get('clsMessageRight'):
			base_attrs["data-cls-message-right"] = component_attrs['clsMessageRight']
		
		# For MetroUI chat, we only render the container and let MetroUI handle the internal structure
		# The messages parameter will be handled by MetroUI's JavaScript initialization
		return self.render_component("div", base_attrs, content="")


# Create component instance
_chat_component = ChatComponent()


def render_chat(messages=None, **attrs):
	"""
	Renders MetroUI chat component for interactive messaging interface.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/chat/>`_.
	
	You can also reference specific sections:
	- `Dependencies <https://v5.metroui.org.ua/components/chat/#dependencies>`_
	- `Basic Usage <https://v5.metroui.org.ua/components/chat/#basic-usage>`_
	- `With Configuration Options <https://v5.metroui.org.ua/components/chat/#with-configuration-options>`_
	- `Programmatic Initialization <https://v5.metroui.org.ua/components/chat/#programmatic-initialization>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/chat/#plugin-parameters>`_
	- `Message Structure <https://v5.metroui.org.ua/components/chat/#message-structure>`_
	- `API Methods <https://v5.metroui.org.ua/components/chat/#api-methods>`_
	- `Events <https://v5.metroui.org.ua/components/chat/#events>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/chat/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/chat/#available-css-classes>`_
	- `Best Practices <https://v5.metroui.org.ua/components/chat/#best-practices>`_

	Args:
		messages: Initial messages to display (list of message objects)
		**attrs: Additional HTML attributes including:
			chatDeferred (int): Deferred initialization time in milliseconds
			inputTimeFormat (str): Format for parsing input time strings
			timeFormat (str): Format for displaying message timestamps
			name (str): Default name for outgoing messages
			avatar (str): HTML for the avatar of outgoing messages
			welcome (str): Welcome message text
			welcomeAvatar (str): HTML for the avatar of the welcome message
			title (str): Title for the chat component
			width (str): Width of the chat component
			height (str): Height of the chat component
			initialHeight (int): Initial Height of the chat component
			attachAccept (str): Attach file types
			readonly (bool): Whether the chat is in read-only mode
			sendMode (str): Trigger for message send (enter, control+enter, button)
			useEmoji (bool): Use emoji in message
			useLink (bool): Use link in message
			useCode (bool): Use code blocks in message
			buttons (str): Buttons to use
			clsChat (str): Additional CSS class for the chat container
			clsName (str): Additional CSS class for the sender name
			clsTime (str): Additional CSS class for the message time
			clsInput (str): Additional CSS class for the input field
			clsSendButton (str): Additional CSS class for the send button
			clsMessageLeft (str): CSS class for left-aligned messages
			clsMessageRight (str): CSS class for right-aligned messages
			onMessage (str): Callback function when message is added
			onSend (str): Callback function when message is sent
			onSendButtonClick (str): Callback function when send button is clicked
			onChatCreate (str): Callback function when chat is created
		
		Returns:
			str: Rendered HTML div element with chat functionality
			
		References:
			.. _MetroUI Chat: https://v5.metroui.org.ua/components/chat/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	"""
	return _chat_component.render(messages, **attrs)
