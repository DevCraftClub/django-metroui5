"""
MetroUI Base Component

Abstract base class for all MetroUI components with DRY methods
for common functionality like CSS class handling and attribute processing.
"""

from abc import ABC, abstractmethod
from ..html import render_tag


class BaseComponent(ABC):
    """
    Abstract base class for MetroUI components.
    
    Provides common functionality for:
    - CSS class handling
    - Parameter separation
    - Attribute processing
    - HTML rendering
    """
    
    def __init__(self, component_name, base_css_class, component_params=None):
        """
        Initialize the base component.
        
        Args:
            component_name: Name of the component (e.g., 'badge', 'bar3d')
            base_css_class: Base CSS class for the component (e.g., 'badge', 'bar3d')
            component_params: List of component-specific parameters
        """
        self.component_name = component_name
        self.base_css_class = base_css_class
        self.component_params = component_params or []
    
    def separate_attributes(self, attrs):
        """
        Separate attributes into different categories.
        
        Args:
            attrs: Dictionary of all attributes
            
        Returns:
            tuple: (component_attrs, standard_attrs, cls_attrs)
        """
        component_attrs = {}
        standard_attrs = {}
        cls_attrs = {}
        
        # Add component-specific parameter name
        component_param_name = f'cls_{self.component_name}'
        if component_param_name not in self.component_params:
            self.component_params.append(component_param_name)
        
        for key, value in attrs.items():
            if key in self.component_params:
                component_attrs[key] = value
            elif key == 'cls' or key.startswith('cls_'):
                cls_attrs[key] = value
            else:
                standard_attrs[key] = value
        
        return component_attrs, standard_attrs, cls_attrs
    
    def build_css_classes(self, component_attrs, cls_attrs, standard_attrs, additional_classes=None):
        """
        Build CSS classes from various sources.
        
        Args:
            component_attrs: Component-specific attributes
            cls_attrs: CSS class attributes
            standard_attrs: Standard HTML attributes
            additional_classes: Additional classes to add (list)
            
        Returns:
            list: List of CSS classes
        """
        css_classes = [self.base_css_class]
        
        # Add additional classes if provided
        if additional_classes:
            css_classes.extend(additional_classes)
        
        # Add component-specific class
        component_param_name = f'cls_{self.component_name}'
        if component_attrs.get(component_param_name):
            css_classes.append(component_attrs[component_param_name])
        
        # Add any additional cls parameters
        for key, value in cls_attrs.items():
            if key != component_param_name:
                css_classes.append(value)
        
        # Add existing classes from cls parameter
        if "cls" in standard_attrs:
            existing_classes = standard_attrs["cls"].split()
            css_classes.extend([cls for cls in existing_classes if cls not in css_classes])
            del standard_attrs["cls"]
        
        return css_classes
    
    def build_data_attributes(self, component_attrs, data_attr_mapping=None):
        """
        Build data attributes from component parameters.
        
        Args:
            component_attrs: Component-specific attributes
            data_attr_mapping: Mapping of parameter names to data attribute names
            
        Returns:
            dict: Dictionary of data attributes
        """
        data_attrs = {}
        
        if data_attr_mapping is None:
            data_attr_mapping = {}
        
        for param, value in component_attrs.items():
            if param.startswith('on_'):
                # Handle callback functions
                data_attr_name = f"data-{param.replace('_', '-')}"
                data_attrs[data_attr_name] = value
            elif param.startswith('cls_'):
                # Skip CSS class parameters
                continue
            else:
                # Handle regular parameters
                if param in data_attr_mapping:
                    data_attr_name = data_attr_mapping[param]
                else:
                    data_attr_name = f"data-{param.replace('_', '-')}"
                data_attrs[data_attr_name] = str(value)
        
        return data_attrs
    
    def render_component(self, tag_name, attrs, content="", close=True):
        """
        Render the component HTML.
        
        Args:
            tag_name: HTML tag name (e.g., 'div', 'span')
            attrs: HTML attributes
            content: Tag content
            close: Whether to close the tag
            
        Returns:
            str: Rendered HTML
        """
        return render_tag(tag_name, attrs=attrs, content=content, close=close)
    
    @abstractmethod
    def render(self, **attrs):
        """
        Abstract method to render the component.
        
        Args:
            **attrs: Component attributes
            
        Returns:
            str: Rendered HTML
        """
        pass


class SimpleComponent(BaseComponent):
    """
    Simple component that renders a single HTML element.
    
    Suitable for components like badge, bar3d, etc.
    """
    
    def __init__(self, component_name, base_css_class, tag_name, component_params=None, data_attr_mapping=None, default_data_attrs=None):
        """
        Initialize the simple component.
        
        Args:
            component_name: Name of the component
            base_css_class: Base CSS class
            tag_name: HTML tag name
            component_params: List of component-specific parameters
            data_attr_mapping: Mapping of parameter names to data attribute names
            default_data_attrs: Default data attributes
        """
        super().__init__(component_name, base_css_class, component_params)
        self.tag_name = tag_name
        self.data_attr_mapping = data_attr_mapping or {}
        self.default_data_attrs = default_data_attrs or {}
    
    def render(self, **attrs):
        """
        Render the simple component.
        
        Args:
            **attrs: Component attributes
            
        Returns:
            str: Rendered HTML
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
        
        # Build CSS classes
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)
        
        # Build data attributes
        data_attrs = self.build_data_attributes(component_attrs, self.data_attr_mapping)
        
        # Build final attributes
        final_attrs = {
            "class": " ".join(css_classes),
            **self.default_data_attrs,
            **data_attrs,
            **standard_attrs
        }
        
        return self.render_component(self.tag_name, final_attrs)


class ComplexComponent(BaseComponent):
    """
    Complex component that renders multiple HTML elements or has custom logic.
    
    Suitable for components like breadcrumb, accordion, etc.
    """
    
    def __init__(self, component_name, base_css_class, component_params=None):
        """
        Initialize the complex component.
        
        Args:
            component_name: Name of the component
            base_css_class: Base CSS class
            component_params: List of component-specific parameters
        """
        super().__init__(component_name, base_css_class, component_params)
    
    def build_base_attributes(self, component_attrs, cls_attrs, standard_attrs, additional_classes=None):
        """
        Build base attributes for the component.
        
        Args:
            component_attrs: Component-specific attributes
            cls_attrs: CSS class attributes
            standard_attrs: Standard HTML attributes
            additional_classes: Additional classes to add
            
        Returns:
            dict: Base attributes
        """
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs, additional_classes)
        
        return {
            "class": " ".join(css_classes),
            **standard_attrs
        }
    
    @abstractmethod
    def render(self, **attrs):
        """
        Abstract method to render the complex component.
        
        Args:
            **attrs: Component attributes
            
        Returns:
            str: Rendered HTML
        """
        pass
