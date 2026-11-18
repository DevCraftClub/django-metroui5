"""
MetroUI Input Components
"""

import json
from ..html import render_tag


def add_role(roles_string, new_role):
	"""Helper function to add a role to the roles string if not already present."""
	if new_role not in roles_string:
		return f"{roles_string}, {new_role}"
	return roles_string


def render_input(input_type="text", placeholder="", **attrs):
	"""
	Renders MetroUI input component with advanced features.

	Args:
		input_type: Input field type (text, password, email, search, etc.)
		placeholder: Placeholder text
		**attrs: Additional HTML attributes including:
			# Basic Parameters
			- label: Input label text
			- disabled: Disable the input (boolean)
			- readonly: Make input readonly (boolean)
			- required: Mark as required (boolean)
			- size: Custom width for the input
			- default_value: Default value for the input
			- prevent_submit: Prevent form submission on Enter key (boolean)
			- input_deferred: Delay in milliseconds before initializing (number)
			
			# Button Parameters
			- clear_button: Show clear button (boolean)
			- reveal_button: Show password reveal button (boolean)
			- search_button: Show search button (boolean)
			- random_button: Show random generator button (boolean)
			- clear_button_icon: Icon for clear button (string)
			- reveal_button_icon: Icon for reveal button (string)
			- search_button_icon: Icon for search button (string)
			- random_button_icon: Icon for random button (string)
			- search_button_click: Action for search button (string)
			- custom_buttons: Custom buttons configuration (array)
			
			# Autocomplete Parameters
			- autocomplete: Static autocomplete data (string/array)
			- autocomplete_url: URL to fetch autocomplete data (string)
			- autocomplete_url_method: HTTP method for autocomplete URL (string)
			- autocomplete_url_key: Key to extract data from JSON response (string)
			- autocomplete_divider: Divider for autocomplete string data (string)
			- autocomplete_list_height: Maximum height of autocomplete dropdown (number)
			
			# History Parameters
			- history: Enable input history functionality (boolean)
			- history_preset: Preset history items (string)
			- history_divider: Divider for history preset string (string)
			
			# Prepend/Append Parameters
			- prepend: Text to prepend to the input (string)
			- append: Text to append to the input (string)
			- prepend_options: Dropdown options to prepend (string)
			- append_options: Dropdown options to append (string)
			- prepend_options_sep: Separator for prepend options (string)
			- append_options_sep: Separator for append options (string)
			
			# Random Generation Parameters
			- random_symbols: Symbol groups for random generation (string)
			- random_length: Length of generated random string (number)
			
			# Mask Parameters
			- mask: The mask pattern defining the input format (string)
			- mask_pattern: Regular expression pattern for editable positions (string)
			- mask_placeholder: Character(s) used as placeholders in the mask (string)
			- mask_editable_start: Starting position from which user can edit (number)
			- threshold_interval: Time in milliseconds for cursor positioning threshold (number)
			- on_char: Callback function to transform characters (string)
			- on_input_mask_create: Callback function when input mask is created (string)
			
			# Styling Parameters
			- material: Use material design style (boolean)
			- pill: Use pill-shaped input (boolean)
			- rtl: Right-to-left text direction (boolean)
			- badge: Badge text to display (string)
			- cls_component: Additional CSS class for component container (string)
			- cls_input: Additional CSS class for input element (string)
			- cls_label: Additional CSS class for label (string)
			- cls_prepend: Additional CSS class for prepend element (string)
			- cls_append: Additional CSS class for append element (string)
			- cls_clear_button: Additional CSS class for clear button (string)
			- cls_reveal_button: Additional CSS class for reveal button (string)
			- cls_custom_button: Additional CSS class for custom buttons (string)
			- cls_search_button: Additional CSS class for search button (string)
			- cls_random_button: Additional CSS class for random button (string)
			
			# Validation Parameters
			- error: Show error state (boolean)
			- error_message: Error message text (string)
			- success: Show success state (boolean)
			- success_message: Success message text (string)
			- warning: Show warning state (boolean)
			- warning_message: Warning message text (string)
			- info: Show info state (boolean)
			- info_message: Info message text (string)
			- help_text: Help text to display (string)
			- max_length: Maximum input length (number)
			- min_length: Minimum input length (number)
			- pattern: HTML5 pattern validation (string)
			- step: Step value for number inputs (number)
			- min: Minimum value for number inputs (number)
			- max: Maximum value for number inputs (number)
			- multiple: Allow multiple values (boolean)
			- accept: File types to accept (string)
			- capture: Camera capture mode (string)
	Example:
		render_input()

	Empty or invalid:
		`render_input()` returns `<input type="text" data-role="input, input-common" class="input">`.

	"""
	# Extract MetroUI-specific attributes
	metro_attrs = {}
	standard_attrs = {}
	
	# MetroUI-specific parameters
	metro_params = [
		# Basic parameters
		'label', 'disabled', 'readonly', 'required', 'size', 'default_value',
		'prevent_submit', 'input_deferred',
		
		# Button parameters
		'clear_button', 'reveal_button', 'search_button', 'random_button',
		'clear_button_icon', 'reveal_button_icon', 'search_button_icon', 'random_button_icon',
		'search_button_click', 'custom_buttons',
		
		# Autocomplete parameters
		'autocomplete', 'autocomplete_url', 'autocomplete_url_method', 'autocomplete_url_key',
		'autocomplete_divider', 'autocomplete_list_height',
		
		# History parameters
		'history', 'history_preset', 'history_divider',
		
		# Prepend/Append parameters
		'prepend', 'append', 'prepend_options', 'append_options',
		'prepend_options_sep', 'append_options_sep',
		
		# Random generation parameters
		'random_symbols', 'random_length',
		
		# Mask parameters
		'mask', 'mask_pattern', 'mask_placeholder', 'mask_editable_start',
		'threshold_interval', 'on_char', 'on_input_mask_create',
		
		# Styling parameters
		'material', 'pill', 'rtl', 'badge', 'cls_component', 'cls_input', 'cls_label',
		'cls_prepend', 'cls_append', 'cls_clear_button', 'cls_reveal_button',
		'cls_custom_button', 'cls_search_button', 'cls_random_button',
		
		# Validation parameters
		'error', 'error_message', 'success', 'success_message', 'warning', 'warning_message',
		'info', 'info_message', 'help_text', 'max_length', 'min_length', 'pattern',
		'step', 'min', 'max', 'multiple', 'accept', 'capture'
	]
	
	# Separate MetroUI attributes from standard HTML attributes
	for key, value in attrs.items():
		if key in metro_params:
			metro_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	# Build base attributes
	default_attrs = {
		"type": input_type,
		"data-role": "input, input-common"  # input-common is always included for basic functionality
	}
	
	# Add placeholder if provided
	if placeholder:
		default_attrs["placeholder"] = placeholder
	
	# Add MetroUI-specific data attributes
	if metro_attrs.get('label'):
		default_attrs["data-label"] = metro_attrs['label']
	
	if metro_attrs.get('clear_button'):
		default_attrs["data-clear-button"] = "true"
	
	if metro_attrs.get('reveal_button'):
		default_attrs["data-reveal-button"] = "true"
	
	if metro_attrs.get('search_button'):
		default_attrs["data-search-button"] = "true"
	
	if metro_attrs.get('random_button'):
		default_attrs["data-random-button"] = "true"
	
	if metro_attrs.get('autocomplete'):
		default_attrs["data-autocomplete"] = metro_attrs['autocomplete']
	
	if metro_attrs.get('autocomplete_url'):
		default_attrs["data-autocomplete-url"] = metro_attrs['autocomplete_url']
		if metro_attrs.get('autocomplete_url_method'):
			default_attrs["data-autocomplete-url-method"] = metro_attrs['autocomplete_url_method']
	
	if metro_attrs.get('history'):
		default_attrs["data-history"] = "true"
		if metro_attrs.get('history_preset'):
			default_attrs["data-history-preset"] = metro_attrs['history_preset']
	
	if metro_attrs.get('prepend'):
		default_attrs["data-prepend"] = metro_attrs['prepend']
	
	if metro_attrs.get('append'):
		default_attrs["data-append"] = metro_attrs['append']
	
	if metro_attrs.get('prepend_options'):
		default_attrs["data-prepend-options"] = metro_attrs['prepend_options']
	
	if metro_attrs.get('append_options'):
		default_attrs["data-append-options"] = metro_attrs['append_options']
	
	if metro_attrs.get('custom_buttons'):
		if isinstance(metro_attrs['custom_buttons'], (list, dict)):
			default_attrs["data-custom-buttons"] = json.dumps(metro_attrs['custom_buttons'])
		else:
			default_attrs["data-custom-buttons"] = metro_attrs['custom_buttons']
	
	if metro_attrs.get('mask'):
		default_attrs["data-mask"] = metro_attrs['mask']
		default_attrs["data-role"] = add_role(default_attrs["data-role"], "input-mask")
	
	if metro_attrs.get('material'):
		default_attrs["data-material"] = "true"
		default_attrs["data-role"] = add_role(default_attrs["data-role"], "input-material")
	
	if metro_attrs.get('pill'):
		default_attrs["data-pill"] = "true"
	
	if metro_attrs.get('rtl'):
		default_attrs["data-rtl"] = "true"
	
	if metro_attrs.get('badge'):
		default_attrs["data-badge"] = metro_attrs['badge']
	
	if metro_attrs.get('autocomplete_list_height'):
		default_attrs["data-autocomplete-list-height"] = str(metro_attrs['autocomplete_list_height'])
	
	if metro_attrs.get('random_symbols'):
		default_attrs["data-random-symbols"] = metro_attrs['random_symbols']
	
	if metro_attrs.get('random_length'):
		default_attrs["data-random-length"] = str(metro_attrs['random_length'])
	
	# Add basic parameters
	if metro_attrs.get('input_deferred'):
		default_attrs["data-input-deferred"] = str(metro_attrs['input_deferred'])
	
	if metro_attrs.get('default_value'):
		default_attrs["data-default-value"] = metro_attrs['default_value']
	
	if metro_attrs.get('prevent_submit'):
		default_attrs["data-prevent-submit"] = "true"
	
	if metro_attrs.get('size') and metro_attrs['size'] != 'default':
		default_attrs["data-size"] = metro_attrs['size']
	
	# Add button icon parameters
	if metro_attrs.get('clear_button_icon'):
		default_attrs["data-clear-button-icon"] = metro_attrs['clear_button_icon']
	
	if metro_attrs.get('reveal_button_icon'):
		default_attrs["data-reveal-button-icon"] = metro_attrs['reveal_button_icon']
	
	if metro_attrs.get('search_button_icon'):
		default_attrs["data-search-button-icon"] = metro_attrs['search_button_icon']
	
	if metro_attrs.get('random_button_icon'):
		default_attrs["data-random-button-icon"] = metro_attrs['random_button_icon']
	
	if metro_attrs.get('search_button_click'):
		default_attrs["data-search-button-click"] = metro_attrs['search_button_click']
	
	# Add autocomplete advanced parameters
	if metro_attrs.get('autocomplete_url_key'):
		default_attrs["data-autocomplete-url-key"] = metro_attrs['autocomplete_url_key']
	
	if metro_attrs.get('autocomplete_divider'):
		default_attrs["data-autocomplete-divider"] = metro_attrs['autocomplete_divider']
	
	# Add history advanced parameters
	if metro_attrs.get('history_divider'):
		default_attrs["data-history-divider"] = metro_attrs['history_divider']
	
	# Add prepend/append advanced parameters
	if metro_attrs.get('prepend_options_sep'):
		default_attrs["data-prepend-options-sep"] = metro_attrs['prepend_options_sep']
	
	if metro_attrs.get('append_options_sep'):
		default_attrs["data-append-options-sep"] = metro_attrs['append_options_sep']
	
	# Add mask advanced parameters
	if metro_attrs.get('mask_pattern'):
		default_attrs["data-mask-pattern"] = metro_attrs['mask_pattern']
	
	if metro_attrs.get('mask_placeholder'):
		default_attrs["data-mask-placeholder"] = metro_attrs['mask_placeholder']
	
	if metro_attrs.get('mask_editable_start'):
		default_attrs["data-mask-editable-start"] = str(metro_attrs['mask_editable_start'])
	
	if metro_attrs.get('threshold_interval'):
		default_attrs["data-threshold-interval"] = str(metro_attrs['threshold_interval'])
	
	# Add callback functions (as JavaScript function names)
	if metro_attrs.get('on_char'):
		default_attrs["data-on-char"] = metro_attrs['on_char']
	
	if metro_attrs.get('on_input_mask_create'):
		default_attrs["data-on-input-mask-create"] = metro_attrs['on_input_mask_create']
	
	# Add validation and state attributes
	if metro_attrs.get('error') or metro_attrs.get('error_message'):
		default_attrs["data-error"] = "true"
		if metro_attrs.get('error_message'):
			default_attrs["data-error-message"] = metro_attrs['error_message']
	
	if metro_attrs.get('success') or metro_attrs.get('success_message'):
		default_attrs["data-success"] = "true"
		if metro_attrs.get('success_message'):
			default_attrs["data-success-message"] = metro_attrs['success_message']
	
	if metro_attrs.get('warning') or metro_attrs.get('warning_message'):
		default_attrs["data-warning"] = "true"
		if metro_attrs.get('warning_message'):
			default_attrs["data-warning-message"] = metro_attrs['warning_message']
	
	if metro_attrs.get('info') or metro_attrs.get('info_message'):
		default_attrs["data-info"] = "true"
		if metro_attrs.get('info_message'):
			default_attrs["data-info-message"] = metro_attrs['info_message']
	
	if metro_attrs.get('help_text'):
		default_attrs["data-help"] = metro_attrs['help_text']
	
	# Add HTML5 validation attributes
	if metro_attrs.get('max_length'):
		default_attrs["maxlength"] = str(metro_attrs['max_length'])
	
	if metro_attrs.get('min_length'):
		default_attrs["minlength"] = str(metro_attrs['min_length'])
	
	if metro_attrs.get('pattern'):
		default_attrs["pattern"] = metro_attrs['pattern']
	
	if metro_attrs.get('step'):
		default_attrs["step"] = str(metro_attrs['step'])
	
	if metro_attrs.get('min'):
		default_attrs["min"] = str(metro_attrs['min'])
	
	if metro_attrs.get('max'):
		default_attrs["max"] = str(metro_attrs['max'])
	
	if metro_attrs.get('size'):
		default_attrs["size"] = str(metro_attrs['size'])
	
	if metro_attrs.get('multiple'):
		default_attrs["multiple"] = "multiple"
	
	if metro_attrs.get('accept'):
		default_attrs["accept"] = metro_attrs['accept']
	
	if metro_attrs.get('capture'):
		default_attrs["capture"] = metro_attrs['capture']
	
	# Build CSS classes
	css_classes = ["input"]
	
	if metro_attrs.get('material'):
		css_classes.append("material-input")
	
	if metro_attrs.get('pill'):
		css_classes.append("pill-input")
	
	if metro_attrs.get('rtl'):
		css_classes.append("rtl")
	
	# Add validation state classes
	if metro_attrs.get('error') or metro_attrs.get('error_message'):
		css_classes.append("error")
	
	if metro_attrs.get('success') or metro_attrs.get('success_message'):
		css_classes.append("success")
	
	if metro_attrs.get('warning') or metro_attrs.get('warning_message'):
		css_classes.append("warning")
	
	if metro_attrs.get('info') or metro_attrs.get('info_message'):
		css_classes.append("info")
	
	if metro_attrs.get('cls_component'):
		css_classes.append(metro_attrs['cls_component'])
	
	if metro_attrs.get('cls_input'):
		css_classes.append(metro_attrs['cls_input'])
	
	# Add additional CSS classes for specific elements
	additional_classes = []
	if metro_attrs.get('cls_prepend'):
		additional_classes.append(f"prepend-{metro_attrs['cls_prepend']}")
	if metro_attrs.get('cls_append'):
		additional_classes.append(f"append-{metro_attrs['cls_append']}")
	if metro_attrs.get('cls_clear_button'):
		additional_classes.append(f"clear-{metro_attrs['cls_clear_button']}")
	if metro_attrs.get('cls_reveal_button'):
		additional_classes.append(f"reveal-{metro_attrs['cls_reveal_button']}")
	if metro_attrs.get('cls_custom_button'):
		additional_classes.append(f"custom-{metro_attrs['cls_custom_button']}")
	if metro_attrs.get('cls_search_button'):
		additional_classes.append(f"search-{metro_attrs['cls_search_button']}")
	if metro_attrs.get('cls_random_button'):
		additional_classes.append(f"random-{metro_attrs['cls_random_button']}")
	
	if additional_classes:
		css_classes.extend(additional_classes)
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Add standard HTML attributes
	if metro_attrs.get('disabled'):
		default_attrs["disabled"] = "disabled"
	
	if metro_attrs.get('readonly'):
		default_attrs["readonly"] = "readonly"
	
	if metro_attrs.get('required'):
		default_attrs["required"] = "required"
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("input", attrs=final_attrs, close=False)


def render_material_input(input_type="text", placeholder="", **attrs):
	"""
	Renders MetroUI material input component with material design features.

	Args:
		input_type: Input field type (text, password, email, search, etc.)
		placeholder: Placeholder text
		**attrs: Additional HTML attributes including:
			# Material Design Parameters
			- label: Text for the floating label (string)
			- informer: Helper text displayed below the input (string)
			- icon: Icon displayed to the left of the input (string)
			- permanent_label: When true, the label is always visible (boolean)
			- search_button: When true, displays a search button (boolean)
			- clear_button: When true, displays a clear button (boolean)
			- reveal_button: When true, displays a reveal button for password inputs (boolean)
			- clear_button_icon: Icon for the clear button (string)
			- reveal_button_icon: Icon for the reveal button (string)
			- search_button_icon: Icon for the search button (string)
			- search_button_click: Action for search button click (string)
			- custom_buttons: Array of custom button objects (array)
			- cls_component: Additional CSS class for the component container (string)
			- cls_input: Additional CSS class for the input element (string)
			- cls_label: Additional CSS class for the label (string)
			- cls_informer: Additional CSS class for the informer (string)
			- cls_icon: Additional CSS class for the icon (string)
			- cls_line: Additional CSS class for the underline (string)
			- disabled: Disable the input (boolean)
			- readonly: Make input readonly (boolean)
			- required: Mark as required (boolean)
			- max_length: Maximum input length (number)
			- min_length: Minimum input length (number)
			- pattern: HTML5 pattern validation (string)
			- step: Step value for number inputs (number)
			- min: Minimum value for number inputs (number)
			- max: Maximum value for number inputs (number)
			- multiple: Allow multiple values (boolean)
			- accept: File types to accept (string)
			- capture: Camera capture mode (string)
	"""
	# Extract material-specific attributes
	material_attrs = {}
	standard_attrs = {}
	
	material_params = [
		'label', 'informer', 'icon', 'permanent_label', 'search_button', 'clear_button',
		'reveal_button', 'clear_button_icon', 'reveal_button_icon', 'search_button_icon',
		'search_button_click', 'custom_buttons', 'cls_component', 'cls_input', 'cls_label',
		'cls_informer', 'cls_icon', 'cls_line', 'disabled', 'readonly', 'required',
		'max_length', 'min_length', 'pattern', 'step', 'min', 'max', 'multiple',
		'accept', 'capture'
	]
	
	for key, value in attrs.items():
		if key in material_params:
			material_attrs[key] = value
		else:
			standard_attrs[key] = value
	
	default_attrs = {
		"type": input_type,
		"data-role": "material-input"
	}
	
	if placeholder:
		default_attrs["placeholder"] = placeholder
	
	# Add Material-specific data attributes
	if material_attrs.get('label'):
		default_attrs["data-label"] = material_attrs['label']
	
	if material_attrs.get('informer'):
		default_attrs["data-informer"] = material_attrs['informer']
	
	if material_attrs.get('icon'):
		default_attrs["data-icon"] = material_attrs['icon']
	
	if material_attrs.get('permanent_label'):
		default_attrs["data-permanent-label"] = "true"
	
	if material_attrs.get('search_button'):
		default_attrs["data-search-button"] = "true"
	
	if material_attrs.get('clear_button'):
		default_attrs["data-clear-button"] = "true"
	
	if material_attrs.get('reveal_button'):
		default_attrs["data-reveal-button"] = "true"
	
	if material_attrs.get('clear_button_icon'):
		default_attrs["data-clear-button-icon"] = material_attrs['clear_button_icon']
	
	if material_attrs.get('reveal_button_icon'):
		default_attrs["data-reveal-button-icon"] = material_attrs['reveal_button_icon']
	
	if material_attrs.get('search_button_icon'):
		default_attrs["data-search-button-icon"] = material_attrs['search_button_icon']
	
	if material_attrs.get('search_button_click'):
		default_attrs["data-search-button-click"] = material_attrs['search_button_click']
	
	if material_attrs.get('custom_buttons'):
		if isinstance(material_attrs['custom_buttons'], (list, dict)):
			default_attrs["data-custom-buttons"] = json.dumps(material_attrs['custom_buttons'])
		else:
			default_attrs["data-custom-buttons"] = material_attrs['custom_buttons']
	
	# Build CSS classes
	css_classes = ["input-material"]
	
	if material_attrs.get('icon'):
		css_classes.append("with-icon")
	
	if material_attrs.get('permanent_label'):
		css_classes.append("permanent-label")
	
	if material_attrs.get('cls_component'):
		css_classes.append(material_attrs['cls_component'])
	
	if material_attrs.get('cls_input'):
		css_classes.append(material_attrs['cls_input'])
	
	if material_attrs.get('cls_label'):
		css_classes.append(f"label-{material_attrs['cls_label']}")
	
	if material_attrs.get('cls_informer'):
		css_classes.append(f"informer-{material_attrs['cls_informer']}")
	
	if material_attrs.get('cls_icon'):
		css_classes.append(f"icon-{material_attrs['cls_icon']}")
	
	if material_attrs.get('cls_line'):
		css_classes.append(f"line-{material_attrs['cls_line']}")
	
	default_attrs["class"] = " ".join(css_classes)
	
	# Add standard HTML attributes
	if material_attrs.get('disabled'):
		default_attrs["disabled"] = "disabled"
	
	if material_attrs.get('readonly'):
		default_attrs["readonly"] = "readonly"
	
	if material_attrs.get('required'):
		default_attrs["required"] = "required"
	
	if material_attrs.get('max_length'):
		default_attrs["maxlength"] = str(material_attrs['max_length'])
	
	if material_attrs.get('min_length'):
		default_attrs["minlength"] = str(material_attrs['min_length'])
	
	if material_attrs.get('pattern'):
		default_attrs["pattern"] = material_attrs['pattern']
	
	if material_attrs.get('step'):
		default_attrs["step"] = str(material_attrs['step'])
	
	if material_attrs.get('min'):
		default_attrs["min"] = str(material_attrs['min'])
	
	if material_attrs.get('max'):
		default_attrs["max"] = str(material_attrs['max'])
	
	if material_attrs.get('multiple'):
		default_attrs["multiple"] = "multiple"
	
	if material_attrs.get('accept'):
		default_attrs["accept"] = material_attrs['accept']
	
	if material_attrs.get('capture'):
		default_attrs["capture"] = material_attrs['capture']
	
	# Merge with custom standard attributes
	final_attrs = {**default_attrs, **standard_attrs}
	
	return render_tag("input", attrs=final_attrs, close=False)
