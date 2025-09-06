"""
MetroUI Date Picker Component

A wheel-based date picker that allows users to select a date by scrolling through months, days, and years.
"""

from .base import SimpleComponent


class DatePickerComponent(SimpleComponent):
    """
    MetroUI Date Picker component.
    
    A wheel-based date picker that allows users to select a date by scrolling through months, days, and years.
    """
    
    def __init__(self):
        super().__init__(
            component_name="date_picker",
            base_css_class="date-picker",
            tag_name="input",
            component_params=[
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
            ],
            data_attr_mapping={
                'datepicker_deferred': 'data-datepicker-deferred',
                'gmt': 'data-gmt',
                'format': 'data-format',
                'input_format': 'data-input-format',
                'distance': 'data-distance',
                'month': 'data-month',
                'day': 'data-day',
                'year': 'data-year',
                'min_year': 'data-min-year',
                'max_year': 'data-max-year',
                'default_year_distance': 'data-default-year-distance',
                'scroll_speed': 'data-scroll-speed',
                'copy_inline_styles': 'data-copy-inline-styles',
                'open_mode': 'data-open-mode',
                'locale': 'data-locale',
                'cls_picker': 'data-cls-picker',
                'cls_part': 'data-cls-part',
                'cls_month': 'data-cls-month',
                'cls_day': 'data-cls-day',
                'cls_year': 'data-cls-year',
                'cls_label': 'data-cls-label',
                'cls_button': 'data-cls-button',
                'cls_ok_button': 'data-cls-ok-button',
                'cls_cancel_button': 'data-cls-cancel-button',
                'ok_button_icon': 'data-ok-button-icon',
                'cancel_button_icon': 'data-cancel-button-icon',
                'on_set': 'data-on-set',
                'on_open': 'data-on-open',
                'on_close': 'data-on-close',
                'on_scroll': 'data-on-scroll',
                'on_date_picker_create': 'data-on-date-picker-create',
                'error': 'data-error',
                'error_message': 'data-error-message',
                'success': 'data-success',
                'success_message': 'data-success-message',
                'warning': 'data-warning',
                'warning_message': 'data-warning-message',
                'info': 'data-info',
                'info_message': 'data-info-message',
                'help_text': 'data-help'
            },
            default_data_attrs={
                "type": "text",
                "data-role": "date-picker"
            }
        )
    
    def render(self, **attrs):
        """
        Render the date picker component.
        
        Args:
            **attrs: Component attributes including:
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
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Build CSS classes
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
        
        # Add validation state classes
        if component_attrs.get('error') or component_attrs.get('error_message'):
            css_classes.append("error")
        
        if component_attrs.get('success') or component_attrs.get('success_message'):
            css_classes.append("success")
        
        if component_attrs.get('warning') or component_attrs.get('warning_message'):
            css_classes.append("warning")
        
        if component_attrs.get('info') or component_attrs.get('info_message'):
            css_classes.append("info")
        
        # Build data attributes
        data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
        
        # Handle special boolean attributes
        if component_attrs.get('month') is not None:
            data_attrs['data-month'] = "true" if component_attrs['month'] else "false"
        
        if component_attrs.get('day') is not None:
            data_attrs['data-day'] = "true" if component_attrs['day'] else "false"
        
        if component_attrs.get('year') is not None:
            data_attrs['data-year'] = "true" if component_attrs['year'] else "false"
        
        if component_attrs.get('copy_inline_styles'):
            data_attrs['data-copy-inline-styles'] = "true"
        
        # Handle validation states
        if component_attrs.get('error') or component_attrs.get('error_message'):
            data_attrs['data-error'] = "true"
        
        if component_attrs.get('success') or component_attrs.get('success_message'):
            data_attrs['data-success'] = "true"
        
        if component_attrs.get('warning') or component_attrs.get('warning_message'):
            data_attrs['data-warning'] = "true"
        
        if component_attrs.get('info') or component_attrs.get('info_message'):
            data_attrs['data-info'] = "true"
        
        # Build final attributes
        final_attrs = {
            "class": " ".join(css_classes),
            **self.default_data_attrs,
            **data_attrs,
            **standard_attrs
        }
        
        # Add special attributes
        if component_attrs.get('placeholder'):
            final_attrs["placeholder"] = component_attrs['placeholder']
        
        if component_attrs.get('value'):
            final_attrs["value"] = component_attrs['value']
        
        if component_attrs.get('label'):
            final_attrs["data-label"] = component_attrs['label']
        
        if component_attrs.get('disabled'):
            final_attrs["disabled"] = "disabled"
        
        if component_attrs.get('readonly'):
            final_attrs["readonly"] = "readonly"
        
        if component_attrs.get('required'):
            final_attrs["required"] = "required"
        
        return self.render_component(self.tag_name, final_attrs, close=False)


# Create component instance
_date_picker_component = DatePickerComponent()


def render_date_picker(**attrs):
    """
    Renders MetroUI date picker component using the base component class.
    
    Args:
        **attrs: Component attributes (see DatePickerComponent.render for details)
    """
    return _date_picker_component.render(**attrs)
