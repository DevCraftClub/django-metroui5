"""
MetroUI Flip Card Component

A purely CSS-based component that creates a card with front and back sides that can be flipped 
either horizontally or vertically. The flip effect can be triggered on hover or when the card 
has an "active" class.
"""

from .base import ComplexComponent


class FlipCardComponent(ComplexComponent):
    """
    MetroUI Flip Card component.

    Creates a card with front and back sides that can be flipped either horizontally or vertically.
    The flip effect can be triggered on hover or when the card has an "active" class.

    This is a CSS-only component with no JavaScript dependencies.
    """

    def __init__(self):
        super().__init__(
            component_name="flip_card",
            base_css_class="flip-card",
            component_params=[
                # Content
                'front_content', 'back_content',
                # Flip behavior
                'flip_horizontal', 'effect_on_hover', 'effect_on_active',
                # Styling
                'cls_flip_card', 'cls_front', 'cls_back',
                # Dimensions
                'width', 'height',
                # Animation
                'animation_speed', 'perspective'
            ]
        )

    def render(self, **attrs):
        """
        Render the flip card component.

        Args:
            **attrs: Component attributes including:
                # Content
                - front_content: Content for the front side of the card (string/HTML)
                - back_content: Content for the back side of the card (string/HTML)
                
                # Flip behavior
                - flip_horizontal: Make the card flip horizontally instead of vertically (boolean, default: false)
                - effect_on_hover: Trigger flip effect on hover (boolean, default: false)
                - effect_on_active: Trigger flip effect when card has active class (boolean, default: false)
                
                # Styling
                - cls_flip_card: Additional CSS class for flip card container (string)
                - cls_front: Additional CSS class for front side (string)
                - cls_back: Additional CSS class for back side (string)
                
                # Dimensions
                - width: Width of the flip card (string, e.g., "300px", "100%")
                - height: Height of the flip card (string, e.g., "200px", "100%")
                
                # Animation
                - animation_speed: Duration of the flip animation (string, e.g., "0.3s", "0.5s")
                - perspective: Perspective value for 3D effect (string, e.g., "600px", "1000px")
        """
        # Separate attributes
        component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)

        # Build CSS classes
        css_classes = self.build_css_classes(component_attrs, cls_attrs, standard_attrs)

        # Filter out None values from css_classes
        css_classes = [cls for cls in css_classes if cls is not None]

        # Add flip behavior classes
        if component_attrs.get('flip_horizontal'):
            css_classes.append("flip-horizontal")

        if component_attrs.get('effect_on_hover'):
            css_classes.append("effect-on-hover")

        if component_attrs.get('effect_on_active'):
            css_classes.append("effect-on-active")

        # Build final attributes
        final_attrs = {
            "class": " ".join(css_classes),
            "data-role": "flip-card",
            **standard_attrs
        }

        # Add inline styles for dimensions and animation
        style_parts = []
        if component_attrs.get('width'):
            style_parts.append(f"width: {component_attrs['width']}")
        if component_attrs.get('height'):
            style_parts.append(f"height: {component_attrs['height']}")
        if component_attrs.get('animation_speed'):
            style_parts.append(f"--defaultAnimationSpeed: {component_attrs['animation_speed']}")
        if component_attrs.get('perspective'):
            style_parts.append(f"--defaultPerspective: {component_attrs['perspective']}")

        if style_parts:
            final_attrs["style"] = "; ".join(style_parts)

        # Build content
        content = self.build_flip_card_content(component_attrs)

        return self.render_component("div", final_attrs, content)

    def build_flip_card_content(self, component_attrs):
        """Build the flip card content with front and back sides."""
        content = ""

        # Front side
        front_content = component_attrs.get('front_content', '')
        front_class = "front"
        if component_attrs.get('cls_front'):
            front_class += f" {component_attrs['cls_front']}"

        content += f'<div class="{front_class}">{front_content}</div>'

        # Back side
        back_content = component_attrs.get('back_content', '')
        back_class = "back"
        if component_attrs.get('cls_back'):
            back_class += f" {component_attrs['cls_back']}"

        content += f'<div class="{back_class}">{back_content}</div>'

        return content


# Create component instance
_flip_card = FlipCardComponent()


def render_flip_card(**attrs):
    """
    Renders MetroUI flip card component using the base component class.

    Args:
        **attrs: Component attributes (see FlipCardComponent.render for details)
    """
    return _flip_card.render(**attrs)


# Utility functions for common flip card patterns
def render_flip_card_hover(front_content, back_content, **attrs):
    """
    Renders a flip card that flips on hover.

    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        **attrs: Additional component attributes
    """
    return _flip_card.render(
        front_content=front_content,
        back_content=back_content,
        effect_on_hover=True,
        **attrs
    )


def render_flip_card_active(front_content, back_content, **attrs):
    """
    Renders a flip card that flips when active class is added.

    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        **attrs: Additional component attributes
    """
    return _flip_card.render(
        front_content=front_content,
        back_content=back_content,
        effect_on_active=True,
        **attrs
    )


def render_flip_card_horizontal(front_content, back_content, **attrs):
    """
    Renders a flip card that flips horizontally.

    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        **attrs: Additional component attributes
    """
    return _flip_card.render(
        front_content=front_content,
        back_content=back_content,
        flip_horizontal=True,
        **attrs
    )


def render_flip_card_with_dimensions(front_content, back_content, width, height, **attrs):
    """
    Renders a flip card with specific dimensions.

    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        width: Width of the flip card (string)
        height: Height of the flip card (string)
        **attrs: Additional component attributes
    """
    return _flip_card.render(
        front_content=front_content,
        back_content=back_content,
        width=width,
        height=height,
        **attrs
    )
