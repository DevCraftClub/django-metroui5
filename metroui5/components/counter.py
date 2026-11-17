"""
MetroUI Counter Component

This module provides the MetroUI Counter component implementation.
The Counter component displays an animated numerical counter that counts up to a specified value.
It's useful for displaying statistics, achievements, or any numerical data in an engaging way.

References:
    https://v5.metroui.org.ua/components/counter/
"""

from .base import SimpleComponent


def render_counter(value=0, from_value=0, duration=2000, prefix="", suffix="", delimiter=",", size=16, 
                  start_on_viewport=False, counter_deferred=0, timeout=0, **kwargs):
    """
    Renders MetroUI counter component.
    
    The counter displays an animated numerical counter that counts up to a specified value.
    It's useful for displaying statistics, achievements, or any numerical data in an engaging way.
    
    Args:
        value (int, optional): The target value to count to. Defaults to 0.
        from_value (int, optional): The starting value to count from. Defaults to 0.
        duration (int, optional): Duration of the counting animation in milliseconds. Defaults to 2000.
        prefix (str, optional): Text to display before the number. Defaults to "".
        suffix (str, optional): Text to display after the number. Defaults to "".
        delimiter (str, optional): Character used as the thousands separator. Defaults to ",".
        size (int, optional): Font size in pixels. Defaults to 16.
        start_on_viewport (bool, optional): When true, the counter starts when it enters the viewport. Defaults to False.
        counter_deferred (int, optional): Delay in milliseconds before the counter starts. Defaults to 0.
        timeout (int, optional): Additional timeout before starting the animation. Defaults to 0.
        **kwargs: Additional attributes for the counter element.
    
    Returns:
        str: HTML string for the counter component.
    
    References:
        https://v5.metroui.org.ua/components/counter/
	Example:
		render_counter()

	Empty or invalid:
		`render_counter()` returns `<div data-role="counter" data-value="0" data-from="0" data-duration="2000" data-prefix="" data-suffix="" data-delimiter="," data-size="16" data-start-on-viewport="false" data-counter-deferred="0" data-timeout="0" id="cou...`. An empty call returns `<div data-role="counter" data-value="0" data-from="0" data-duration="0" data-prefix="" data-suffix="" data-delimiter="," data-size="0" data-start-on-viewport="false" data-counter-deferred="0" data-timeout="0" id="counter...`.

    """
    component = CounterComponent()
    return component.render(
        value=value, 
        from_value=from_value, 
        duration=duration, 
        prefix=prefix, 
        suffix=suffix, 
        delimiter=delimiter, 
        size=size, 
        start_on_viewport=start_on_viewport, 
        counter_deferred=counter_deferred, 
        timeout=timeout, 
        **kwargs
    )


class CounterComponent(SimpleComponent):
    """
    MetroUI Counter Component.
    
    Displays an animated numerical counter that counts up to a specified value.
    Useful for displaying statistics, achievements, or any numerical data in an engaging way.
    """
    
    def __init__(self):
        super().__init__(
            component_name="counter",
            base_css_class="",
            tag_name="div",
            component_params=[
                'value', 'from_value', 'duration', 'prefix', 'suffix', 'delimiter', 
                'size', 'start_on_viewport', 'counter_deferred', 'timeout'
            ],
            data_attr_mapping={
                'value': 'data-value',
                'from_value': 'data-from',
                'duration': 'data-duration',
                'prefix': 'data-prefix',
                'suffix': 'data-suffix',
                'delimiter': 'data-delimiter',
                'size': 'data-size',
                'start_on_viewport': 'data-start-on-viewport',
                'counter_deferred': 'data-counter-deferred',
                'timeout': 'data-timeout'
            },
            default_data_attrs={
                'value': '0',
                'from_value': '0',
                'duration': '2000',
                'prefix': '',
                'suffix': '',
                'delimiter': ',',
                'size': '16',
                'start_on_viewport': 'false',
                'counter_deferred': '0',
                'timeout': '0'
            }
        )
    
    def render(self, value=0, from_value=0, duration=2000, prefix="", suffix="", delimiter=",", size=16, 
               start_on_viewport=False, counter_deferred=0, timeout=0, **kwargs):
        """
        Renders the counter component.
        
        Args:
            value (int): The target value to count to
            from_value (int): The starting value to count from
            duration (int): Duration of the counting animation in milliseconds
            prefix (str): Text to display before the number
            suffix (str): Text to display after the number
            delimiter (str): Character used as the thousands separator
            size (int): Font size in pixels
            start_on_viewport (bool): When true, the counter starts when it enters the viewport
            counter_deferred (int): Delay in milliseconds before the counter starts
            timeout (int): Additional timeout before starting the animation
            **kwargs: Additional attributes
            
        Returns:
            str: HTML string for the counter
        """
        # Separate attributes
        attrs, css_classes, data_attrs = self.separate_attributes(kwargs)
        
        # Build CSS classes - for counter we just use any additional classes
        final_css_classes = []
        if css_classes:
            final_css_classes.extend(css_classes)
        if 'cls' in kwargs:
            final_css_classes.append(kwargs['cls'])
        css_classes_str = ' '.join(final_css_classes) if final_css_classes else ''
        
        # Build data attributes
        data_attrs = self.build_data_attributes(attrs, self.data_attr_mapping)
        
        # Set specific data attributes
        data_attrs['data-role'] = 'counter'
        data_attrs['data-value'] = str(value)
        data_attrs['data-from'] = str(from_value)
        data_attrs['data-duration'] = str(duration)
        data_attrs['data-prefix'] = prefix
        data_attrs['data-suffix'] = suffix
        data_attrs['data-delimiter'] = delimiter
        data_attrs['data-size'] = str(size)
        data_attrs['data-start-on-viewport'] = str(start_on_viewport).lower()
        data_attrs['data-counter-deferred'] = str(counter_deferred)
        data_attrs['data-timeout'] = str(timeout)
        
        # Build all attributes
        all_attrs = {**attrs, **data_attrs}
        if css_classes_str:
            all_attrs['class'] = css_classes_str
        
        # Generate unique ID
        counter_id = self.build_id_attribute(attrs, {})
        all_attrs['id'] = counter_id
        
        # Set initial display value
        initial_value = from_value
        
        # Build the counter HTML
        counter_html = f'<{self.tag_name} {self._build_attributes_string(all_attrs)}>{initial_value}</{self.tag_name}>'
        
        return counter_html
    
    def _build_attributes_string(self, attrs):
        """
        Builds HTML attributes string from dictionary.
        
        Args:
            attrs (dict): Attributes dictionary
            
        Returns:
            str: HTML attributes string
        """
        if not attrs:
            return ""
        
        attr_pairs = []
        for key, value in attrs.items():
            if value is True:
                attr_pairs.append(key)
            elif value is False and key.startswith('data-'):
                # Skip false data attributes
                continue
            elif value is not False and value is not None:
                attr_pairs.append(f'{key}="{value}"')
        
        return ' '.join(attr_pairs)
