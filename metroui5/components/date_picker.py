"""
MetroUI Date Picker Component

A wheel-based date picker that allows users to select a date by scrolling through months, days, and years.
"""

from ..html import render_tag


def render_date_picker(**attrs):
    """
    Renders MetroUI date picker component.

    Args:
        **attrs: Additional HTML attributes including:
            # Basic Parameters
            - label: Label for the datepicker (string)
            - disabled: Disable the datepicker (boolean)
            - readonly: Make datepicker readonly (boolean)
            - required: Mark as required (boolean)
            - value: Initial value for the datepicker (string)
            - placeholder: Placeholder text (string)
            
            # Date Picker Parameters
            - datepicker_deferred: Deferred initialization time in milliseconds (number)
            - gmt: GMT timezone adjustment (number)
            - format: Output date format (string, default: "YYYY-MM-DD")
            - input_format: Input date format if different from output format (string)
            - distance: Number of visible items before and after selected item (number, default: 3)
            - month: Show month selector (boolean, default: true)
            - day: Show day selector (boolean, default: true)
            - year: Show year selector (boolean, default: true)
            - min_year: Minimum selectable year (number)
            - max_year: Maximum selectable year (number)
            - default_year_distance: Default distance for min/max year calculation (number, default: 100)
            - scroll_speed: Scrolling speed for the wheel picker (number, default: 4)
            - copy_inline_styles: Copy inline styles from input to picker (boolean, default: false)
            - open_mode: Mode for opening picker - "auto", "dialog", or "up" (string, default: "auto")
            - locale: Specific locale for the datepicker (string)
            
            # Styling Parameters
            - cls_picker: Additional CSS class for the picker (string)
            - cls_part: Additional CSS class for the date parts (string)
            - cls_month: Additional CSS class for the month element (string)
            - cls_day: Additional CSS class for the day element (string)
            - cls_year: Additional CSS class for the year element (string)
            - cls_label: Additional CSS class for the label (string)
            - cls_button: Additional CSS class for buttons (string)
            - cls_ok_button: Additional CSS class for the OK button (string)
            - cls_cancel_button: Additional CSS class for the Cancel button (string)
            
            # Button Icons
            - ok_button_icon: Icon for the OK button (string, default: "✓")
            - cancel_button_icon: Icon for the Cancel button (string, default: "✕")
            
            # Event Handlers
            - on_set: Callback when a date is set (string)
            - on_open: Callback when picker is opened (string)
            - on_close: Callback when picker is closed (string)
            - on_scroll: Callback when scrolling through date options (string)
            - on_date_picker_create: Callback when datepicker is created (string)
            
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
    """
    # Extract MetroUI-specific attributes
    metro_attrs = {}
    standard_attrs = {}
    
    # MetroUI-specific parameters
    metro_params = [
        # Basic parameters
        'label', 'disabled', 'readonly', 'required', 'value', 'placeholder',
        
        # Date picker parameters
        'datepicker_deferred', 'gmt', 'format', 'input_format', 'distance',
        'month', 'day', 'year', 'min_year', 'max_year', 'default_year_distance',
        'scroll_speed', 'copy_inline_styles', 'open_mode', 'locale',
        
        # Styling parameters
        'cls_picker', 'cls_part', 'cls_month', 'cls_day', 'cls_year',
        'cls_label', 'cls_button', 'cls_ok_button', 'cls_cancel_button',
        
        # Button icons
        'ok_button_icon', 'cancel_button_icon',
        
        # Event handlers
        'on_set', 'on_open', 'on_close', 'on_scroll', 'on_date_picker_create',
        
        # Validation parameters
        'error', 'error_message', 'success', 'success_message', 'warning',
        'warning_message', 'info', 'info_message', 'help_text'
    ]
    
    # Separate MetroUI attributes from standard HTML attributes
    for key, value in attrs.items():
        if key in metro_params:
            metro_attrs[key] = value
        else:
            standard_attrs[key] = value
    
    # Build base attributes
    default_attrs = {
        "type": "text",
        "data-role": "date-picker"
    }
    
    # Add placeholder if provided
    if metro_attrs.get('placeholder'):
        default_attrs["placeholder"] = metro_attrs['placeholder']
    
    # Add value if provided
    if metro_attrs.get('value'):
        default_attrs["value"] = metro_attrs['value']
    
    # Add MetroUI-specific data attributes
    if metro_attrs.get('label'):
        default_attrs["data-label"] = metro_attrs['label']
    
    if metro_attrs.get('datepicker_deferred'):
        default_attrs["data-datepicker-deferred"] = str(metro_attrs['datepicker_deferred'])
    
    if metro_attrs.get('gmt'):
        default_attrs["data-gmt"] = str(metro_attrs['gmt'])
    
    if metro_attrs.get('format'):
        default_attrs["data-format"] = metro_attrs['format']
    
    if metro_attrs.get('input_format'):
        default_attrs["data-input-format"] = metro_attrs['input_format']
    
    if metro_attrs.get('distance'):
        default_attrs["data-distance"] = str(metro_attrs['distance'])
    
    if metro_attrs.get('month') is not None:
        default_attrs["data-month"] = "true" if metro_attrs['month'] else "false"
    
    if metro_attrs.get('day') is not None:
        default_attrs["data-day"] = "true" if metro_attrs['day'] else "false"
    
    if metro_attrs.get('year') is not None:
        default_attrs["data-year"] = "true" if metro_attrs['year'] else "false"
    
    if metro_attrs.get('min_year'):
        default_attrs["data-min-year"] = str(metro_attrs['min_year'])
    
    if metro_attrs.get('max_year'):
        default_attrs["data-max-year"] = str(metro_attrs['max_year'])
    
    if metro_attrs.get('default_year_distance'):
        default_attrs["data-default-year-distance"] = str(metro_attrs['default_year_distance'])
    
    if metro_attrs.get('scroll_speed'):
        default_attrs["data-scroll-speed"] = str(metro_attrs['scroll_speed'])
    
    if metro_attrs.get('copy_inline_styles'):
        default_attrs["data-copy-inline-styles"] = "true"
    
    if metro_attrs.get('open_mode'):
        default_attrs["data-open-mode"] = metro_attrs['open_mode']
    
    if metro_attrs.get('locale'):
        default_attrs["data-locale"] = metro_attrs['locale']
    
    # Add styling parameters
    if metro_attrs.get('cls_picker'):
        default_attrs["data-cls-picker"] = metro_attrs['cls_picker']
    
    if metro_attrs.get('cls_part'):
        default_attrs["data-cls-part"] = metro_attrs['cls_part']
    
    if metro_attrs.get('cls_month'):
        default_attrs["data-cls-month"] = metro_attrs['cls_month']
    
    if metro_attrs.get('cls_day'):
        default_attrs["data-cls-day"] = metro_attrs['cls_day']
    
    if metro_attrs.get('cls_year'):
        default_attrs["data-cls-year"] = metro_attrs['cls_year']
    
    if metro_attrs.get('cls_label'):
        default_attrs["data-cls-label"] = metro_attrs['cls_label']
    
    if metro_attrs.get('cls_button'):
        default_attrs["data-cls-button"] = metro_attrs['cls_button']
    
    if metro_attrs.get('cls_ok_button'):
        default_attrs["data-cls-ok-button"] = metro_attrs['cls_ok_button']
    
    if metro_attrs.get('cls_cancel_button'):
        default_attrs["data-cls-cancel-button"] = metro_attrs['cls_cancel_button']
    
    # Add button icons
    if metro_attrs.get('ok_button_icon'):
        default_attrs["data-ok-button-icon"] = metro_attrs['ok_button_icon']
    
    if metro_attrs.get('cancel_button_icon'):
        default_attrs["data-cancel-button-icon"] = metro_attrs['cancel_button_icon']
    
    # Add event handlers
    if metro_attrs.get('on_set'):
        default_attrs["data-on-set"] = metro_attrs['on_set']
    
    if metro_attrs.get('on_open'):
        default_attrs["data-on-open"] = metro_attrs['on_open']
    
    if metro_attrs.get('on_close'):
        default_attrs["data-on-close"] = metro_attrs['on_close']
    
    if metro_attrs.get('on_scroll'):
        default_attrs["data-on-scroll"] = metro_attrs['on_scroll']
    
    if metro_attrs.get('on_date_picker_create'):
        default_attrs["data-on-date-picker-create"] = metro_attrs['on_date_picker_create']
    
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
    
    # Build CSS classes
    css_classes = ["date-picker"]
    
    # Add validation state classes
    if metro_attrs.get('error') or metro_attrs.get('error_message'):
        css_classes.append("error")
    
    if metro_attrs.get('success') or metro_attrs.get('success_message'):
        css_classes.append("success")
    
    if metro_attrs.get('warning') or metro_attrs.get('warning_message'):
        css_classes.append("warning")
    
    if metro_attrs.get('info') or metro_attrs.get('info_message'):
        css_classes.append("info")
    
    # Add custom CSS classes
    if metro_attrs.get('cls_picker'):
        css_classes.append(metro_attrs['cls_picker'])
    
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
