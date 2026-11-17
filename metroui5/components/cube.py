"""
MetroUI Cube Component

This module provides the MetroUI Cube component implementation.
The Cube component is a 3D-styled cube visualization composed of three visible sides (left, right, top),
each divided into a grid of cells. Cells can "flash" (light up) over time according to configurable rules,
making the component useful for status dashboards, activity indicators, or decorative effects.

References:
    https://v5.metroui.org.ua/components/cube/
"""

import json
from .base import SimpleComponent


def render_cube(show_axis=False, axis_style="arrow", cells=4, numbers=False, color="", flash_color="", 
                rules=None, flash_interval=1000, auto_restart=0, cell_click=False, **kwargs):
    """
    Renders MetroUI cube component.
    
    The cube is a 3D-styled visualization with three visible sides (left, right, top),
    each divided into a grid of cells. Cells can "flash" (light up) over time according
    to configurable rules, making it useful for status dashboards, activity indicators,
    or decorative effects.
    
    Args:
        show_axis (bool, optional): Whether to show axis lines for orientation. Defaults to False.
        axis_style (str, optional): Style of axis lines. Options: 'arrow', 'line', 'no-style'. Defaults to 'arrow'.
        cells (int, optional): Number of cells per side (N×N grid). Defaults to 4.
        numbers (bool, optional): Whether to render cell numbers for development. Defaults to False.
        color (str, optional): Base cell background color. Defaults to "".
        flash_color (str, optional): Flashing (active) cell color. Defaults to "".
        rules (list, optional): Custom flashing rules as JSON string or list. Defaults to None.
        flash_interval (int, optional): Interval between rule ticks in milliseconds. Defaults to 1000.
        auto_restart (int, optional): Auto-restart delay in milliseconds. Defaults to 0.
        cell_click (bool, optional): Whether cells can be clicked to toggle. Defaults to False.
        **kwargs: Additional attributes for the cube element.
    
    Returns:
        str: HTML string for the cube component.
    
    References:
        https://v5.metroui.org.ua/components/cube/
	Example:
		render_cube()

	Empty or invalid:
		`render_cube()` returns `<div data-role="cube" data-show-axis="false" data-axis-style="arrow" data-cells="4" data-numbers="false" data-flash-interval="1000" data-auto-restart="0" data-cell-click="false" class="cube" id="cube-component"></div>`. An empty call returns `<div data-role="cube" data-show-axis="[]" data-axis-style="arrow" data-cells="[]" data-numbers="[]" data-flash-interval="1000" data-auto-restart="0" data-cell-click="false" data-rules="[]" class="cube" id="cube-component...`.

    """
    component = CubeComponent()
    return component.render(
        show_axis=show_axis,
        axis_style=axis_style,
        cells=cells,
        numbers=numbers,
        color=color,
        flash_color=flash_color,
        rules=rules,
        flash_interval=flash_interval,
        auto_restart=auto_restart,
        cell_click=cell_click,
        **kwargs
    )


class CubeComponent(SimpleComponent):
    """
    MetroUI Cube Component.
    
    A 3D-styled cube visualization with three visible sides (left, right, top),
    each divided into a grid of cells. Cells can "flash" (light up) over time
    according to configurable rules.
    """
    
    def __init__(self):
        super().__init__(
            component_name="cube",
            base_css_class="cube",
            tag_name="div",
            component_params=[
                'show_axis', 'axis_style', 'cells', 'numbers', 'color', 'flash_color',
                'rules', 'flash_interval', 'auto_restart', 'cell_click'
            ],
            data_attr_mapping={
                'show_axis': 'data-show-axis',
                'axis_style': 'data-axis-style',
                'cells': 'data-cells',
                'numbers': 'data-numbers',
                'color': 'data-color',
                'flash_color': 'data-flash-color',
                'rules': 'data-rules',
                'flash_interval': 'data-flash-interval',
                'auto_restart': 'data-auto-restart',
                'cell_click': 'data-cell-click'
            },
            default_data_attrs={
                'show_axis': 'false',
                'axis_style': 'arrow',
                'cells': '4',
                'numbers': 'false',
                'color': '',
                'flash_color': '',
                'rules': '',
                'flash_interval': '1000',
                'auto_restart': '0',
                'cell_click': 'false'
            }
        )
    
    def render(self, show_axis=False, axis_style="arrow", cells=4, numbers=False, color="", flash_color="", 
               rules=None, flash_interval=1000, auto_restart=0, cell_click=False, **kwargs):
        """
        Renders the cube component.
        
        Args:
            show_axis (bool): Whether to show axis lines for orientation
            axis_style (str): Style of axis lines ('arrow', 'line', 'no-style')
            cells (int): Number of cells per side (N×N grid)
            numbers (bool): Whether to render cell numbers for development
            color (str): Base cell background color
            flash_color (str): Flashing (active) cell color
            rules (list): Custom flashing rules as JSON string or list
            flash_interval (int): Interval between rule ticks in milliseconds
            auto_restart (int): Auto-restart delay in milliseconds
            cell_click (bool): Whether cells can be clicked to toggle
            **kwargs: Additional attributes
            
        Returns:
            str: HTML string for the cube
        """
        # Separate attributes
        attrs, css_classes, data_attrs = self.separate_attributes(kwargs)
        
        # Build CSS classes - for cube we just use any additional classes
        final_css_classes = [self.base_css_class]
        if css_classes:
            final_css_classes.extend(css_classes)
        if 'cls' in kwargs:
            final_css_classes.append(kwargs['cls'])
        css_classes_str = ' '.join(final_css_classes) if final_css_classes else self.base_css_class
        
        # Build data attributes
        data_attrs = self.build_data_attributes(attrs, self.data_attr_mapping)
        
        # Set specific data attributes
        data_attrs['data-role'] = 'cube'
        data_attrs['data-show-axis'] = str(show_axis).lower()
        data_attrs['data-axis-style'] = axis_style
        data_attrs['data-cells'] = str(cells)
        data_attrs['data-numbers'] = str(numbers).lower()
        data_attrs['data-flash-interval'] = str(flash_interval)
        data_attrs['data-auto-restart'] = str(auto_restart)
        data_attrs['data-cell-click'] = str(cell_click).lower()
        
        # Handle color attributes
        if color:
            data_attrs['data-color'] = color
        if flash_color:
            data_attrs['data-flash-color'] = flash_color
        
        # Handle rules - convert to JSON string if it's a list
        if rules is not None:
            if isinstance(rules, list):
                data_attrs['data-rules'] = json.dumps(rules)
            elif isinstance(rules, str):
                data_attrs['data-rules'] = rules
        
        # Build all attributes
        all_attrs = {**attrs, **data_attrs}
        if css_classes_str:
            all_attrs['class'] = css_classes_str
        
        # Generate unique ID
        cube_id = self.build_id_attribute(attrs, {})
        all_attrs['id'] = cube_id
        
        # Build the cube HTML
        cube_html = f'<{self.tag_name} {self._build_attributes_string(all_attrs)}></{self.tag_name}>'
        
        return cube_html
    
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
