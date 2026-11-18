"""
MetroUI Carousel Component
"""

from .base import ComplexComponent
from ..html import render_tag


class CarouselComponent(ComplexComponent):
	"""
	MetroUI Carousel Component
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/carousel/>`_.
	
	You can also reference specific sections:
	- `Basic Carousel <https://v5.metroui.org.ua/components/carousel/#basic-carousel>`_
	- `Carousel with Background Images <https://v5.metroui.org.ua/components/carousel/#carousel-with-background-images>`_
	- `Carousel with Custom Options <https://v5.metroui.org.ua/components/carousel/#carousel-with-custom-options>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/carousel/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/carousel/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/carousel/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/carousel/#available-css-classes>`_
	- `Accessibility <https://v5.metroui.org.ua/components/carousel/#accessibility>`_
	- `Best Practices <https://v5.metroui.org.ua/components/carousel/#best-practices>`_
	"""
	
	def __init__(self):
		super().__init__(
			component_name="carousel",
			base_css_class="carousel",
			component_params=[
				'auto_start', 'width', 'height', 'effect', 'effect_func', 'direction', 
				'duration', 'period', 'stop_on_mouse', 'controls', 'controls_on_mouse',
				'controls_outside', 'control_prev', 'control_next', 'bullets', 
				'bullets_style', 'bullets_size', 'bullets_position', 'cls_carousel',
				'cls_slides', 'cls_slide', 'cls_controls', 'cls_control_next', 
				'cls_control_prev', 'cls_bullets', 'cls_bullet', 'cls_bullet_on',
				'cls_thumb_on', 'onStop', 'onStart', 'onPlay', 'onSlideClick',
				'onBulletClick', 'onThumbClick', 'onMouseEnter', 'onMouseLeave',
				'onNextClick', 'onPrevClick', 'onSlideShow', 'onSlideHide', 'onCarouselCreate'
			]
		)
	
	def render(self, slides=None, **attrs):
		"""
		Renders MetroUI carousel component with slideshow functionality.

		Args:
			slides: List of slide content (strings or dicts with 'content', 'cover', 'alt')
			**attrs: Additional HTML attributes including:
				auto_start (bool): Whether to automatically start the carousel
				width (str): Width of the carousel (default: "100%")
				height (str): Height of the carousel (default: "16/9")
				effect (str): Transition effect between slides (slide, slide-v, fade, switch, zoom, swirl)
				effect_func (str): Easing function for the transition effect (default: "linear")
				direction (str): Direction of carousel movement (left, right)
				duration (int): Duration of transition effect in milliseconds (default: 300)
				period (int): Time between slide transitions in milliseconds (default: 5000)
				stop_on_mouse (bool): Whether to pause when mouse hovers over carousel
				controls (bool): Whether to show next/previous controls (default: true)
				controls_on_mouse (bool): Whether to show controls only on mouse hover
				controls_outside (bool): Whether to position controls outside the carousel
				control_prev (str): HTML content for the previous control
				control_next (str): HTML content for the next control
				bullets (bool): Whether to show bullet navigation (default: true)
				bullets_style (str): Style of bullets (square, circle, rect, diamond)
				bullets_size (str): Size of bullets (default, mini, small, large)
				bullets_position (str): Position of bullets (default, left, right)
				cls_carousel (str): Additional CSS class for carousel element
				cls_slides (str): Additional CSS class for slides container
				cls_slide (str): Additional CSS class for each slide
				cls_controls (str): Additional CSS class for controls
				cls_control_next (str): Additional CSS class for next control
				cls_control_prev (str): Additional CSS class for previous control
				cls_bullets (str): Additional CSS class for bullets container
				cls_bullet (str): Additional CSS class for each bullet
				cls_bullet_on (str): Additional CSS class for active bullet
				cls_thumb_on (str): Additional CSS class for active thumbnail
				onStop (str): Callback when carousel stops
				onStart (str): Callback when carousel starts
				onPlay (str): Callback when carousel plays
				onSlideClick (str): Callback when a slide is clicked
				onBulletClick (str): Callback when a bullet is clicked
				onThumbClick (str): Callback when a thumbnail is clicked
				onMouseEnter (str): Callback when mouse enters carousel
				onMouseLeave (str): Callback when mouse leaves carousel
				onNextClick (str): Callback when next control is clicked
				onPrevClick (str): Callback when previous control is clicked
				onSlideShow (str): Callback when a slide is shown
				onSlideHide (str): Callback when a slide is hidden
				onCarouselCreate (str): Callback when carousel is created
		
		Returns:
			str: Rendered HTML div element with carousel functionality
			
		References:
			.. _MetroUI Carousel: https://v5.metroui.org.ua/components/carousel/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
		"""
		# Separate attributes
		component_attrs, standard_attrs, cls_attrs = self.separate_attributes(attrs)
		
		# Build base attributes
		base_attrs = self.build_base_attributes(component_attrs, cls_attrs, standard_attrs)
		
		# Add carousel-specific data attributes
		base_attrs["data-role"] = "carousel"
		
		# Add carousel-specific data attributes
		if component_attrs.get('auto_start'):
			base_attrs["data-auto-start"] = "true"
		
		if component_attrs.get('width'):
			base_attrs["data-width"] = component_attrs['width']
		
		if component_attrs.get('height'):
			base_attrs["data-height"] = component_attrs['height']
		
		if component_attrs.get('effect'):
			base_attrs["data-effect"] = component_attrs['effect']
		
		if component_attrs.get('effect_func'):
			base_attrs["data-effect-func"] = component_attrs['effect_func']
		
		if component_attrs.get('direction'):
			base_attrs["data-direction"] = component_attrs['direction']
		
		if component_attrs.get('duration'):
			base_attrs["data-duration"] = str(component_attrs['duration'])
		
		if component_attrs.get('period'):
			base_attrs["data-period"] = str(component_attrs['period'])
		
		if component_attrs.get('stop_on_mouse') is False:
			base_attrs["data-stop-on-mouse"] = "false"
		
		if component_attrs.get('controls') is False:
			base_attrs["data-controls"] = "false"
		
		if component_attrs.get('controls_on_mouse'):
			base_attrs["data-controls-on-mouse"] = "true"
		
		if component_attrs.get('controls_outside'):
			base_attrs["data-controls-outside"] = "true"
		
		if component_attrs.get('control_prev'):
			base_attrs["data-control-prev"] = component_attrs['control_prev']
		
		if component_attrs.get('control_next'):
			base_attrs["data-control-next"] = component_attrs['control_next']
		
		if component_attrs.get('bullets') is False:
			base_attrs["data-bullets"] = "false"
		
		if component_attrs.get('bullets_style'):
			base_attrs["data-bullets-style"] = component_attrs['bullets_style']
		
		if component_attrs.get('bullets_size'):
			base_attrs["data-bullets-size"] = component_attrs['bullets_size']
		
		if component_attrs.get('bullets_position'):
			base_attrs["data-bullets-position"] = component_attrs['bullets_position']
		
		# Build slides content
		slides_content = ""
		if slides:
			slides_attrs = {"class": "slides"}
			
			# Add slides CSS class if specified
			if component_attrs.get('cls_slides'):
				slides_attrs["class"] += f" {component_attrs['cls_slides']}"
			
			slide_elements = []
			
			# Handle slides parameter - could be a list or JSON string
			slides_list = slides
			if isinstance(slides, str) and slides.startswith('[') and slides.endswith(']'):
				# Try to parse JSON string
				try:
					import json
					slides_list = json.loads(slides)
				except (json.JSONDecodeError, ValueError):
					# If JSON parsing fails, treat as single slide
					slides_list = [slides]
			elif not isinstance(slides, list):
				# If not a list, treat as single slide
				slides_list = [slides]
			
			for slide in slides_list:
				slide_attrs = {"class": "slide"}
				
				# Add slide CSS class if specified
				if component_attrs.get('cls_slide'):
					slide_attrs["class"] += f" {component_attrs['cls_slide']}"
				
				# Handle slide content
				slide_content = ""
				if isinstance(slide, dict):
					# Complex slide with cover image
					if slide.get('cover'):
						slide_attrs["data-cover"] = slide['cover']
					if slide.get('alt'):
						slide_attrs["alt"] = slide['alt']
					slide_content = slide.get('content', '')
				else:
					# Simple slide content
					slide_content = str(slide)
				
				slide_elements.append(render_tag("div", slide_attrs, slide_content))
			
			slides_content = render_tag("div", slides_attrs, "".join(slide_elements))
		
		return self.render_component("div", base_attrs, content=slides_content)


# Create component instance
_carousel_component = CarouselComponent()


def render_carousel(slides=None, **attrs):
	"""
	Renders MetroUI carousel component with slideshow functionality.
	
	For more details, see the `official documentation <https://v5.metroui.org.ua/components/carousel/>`_.
	
	You can also reference specific sections:
	- `Basic Carousel <https://v5.metroui.org.ua/components/carousel/#basic-carousel>`_
	- `Carousel with Background Images <https://v5.metroui.org.ua/components/carousel/#carousel-with-background-images>`_
	- `Carousel with Custom Options <https://v5.metroui.org.ua/components/carousel/#carousel-with-custom-options>`_
	- `Plugin Parameters <https://v5.metroui.org.ua/components/carousel/#plugin-parameters>`_
	- `API Methods <https://v5.metroui.org.ua/components/carousel/#api-methods>`_
	- `Styling with CSS Variables <https://v5.metroui.org.ua/components/carousel/#styling-with-css-variables>`_
	- `Available CSS Classes <https://v5.metroui.org.ua/components/carousel/#available-css-classes>`_
	- `Accessibility <https://v5.metroui.org.ua/components/carousel/#accessibility>`_
	- `Best Practices <https://v5.metroui.org.ua/components/carousel/#best-practices>`_

	Args:
		slides: List of slide content (strings or dicts with 'content', 'cover', 'alt')
		**attrs: Additional HTML attributes including:
			auto_start (bool): Whether to automatically start the carousel
			width (str): Width of the carousel (default: "100%")
			height (str): Height of the carousel (default: "16/9")
			effect (str): Transition effect between slides (slide, slide-v, fade, switch, zoom, swirl)
			effect_func (str): Easing function for the transition effect (default: "linear")
			direction (str): Direction of carousel movement (left, right)
			duration (int): Duration of transition effect in milliseconds (default: 300)
			period (int): Time between slide transitions in milliseconds (default: 5000)
			stop_on_mouse (bool): Whether to pause when mouse hovers over carousel
			controls (bool): Whether to show next/previous controls (default: true)
			controls_on_mouse (bool): Whether to show controls only on mouse hover
			controls_outside (bool): Whether to position controls outside the carousel
			control_prev (str): HTML content for the previous control
			control_next (str): HTML content for the next control
			bullets (bool): Whether to show bullet navigation (default: true)
			bullets_style (str): Style of bullets (square, circle, rect, diamond)
			bullets_size (str): Size of bullets (default, mini, small, large)
			bullets_position (str): Position of bullets (default, left, right)
			cls_carousel (str): Additional CSS class for carousel element
			cls_slides (str): Additional CSS class for slides container
			cls_slide (str): Additional CSS class for each slide
			cls_controls (str): Additional CSS class for controls
			cls_control_next (str): Additional CSS class for next control
			cls_control_prev (str): Additional CSS class for previous control
			cls_bullets (str): Additional CSS class for bullets container
			cls_bullet (str): Additional CSS class for each bullet
			cls_bullet_on (str): Additional CSS class for active bullet
			cls_thumb_on (str): Additional CSS class for active thumbnail
			onStop (str): Callback when carousel stops
			onStart (str): Callback when carousel starts
			onPlay (str): Callback when carousel plays
			onSlideClick (str): Callback when a slide is clicked
			onBulletClick (str): Callback when a bullet is clicked
			onThumbClick (str): Callback when a thumbnail is clicked
			onMouseEnter (str): Callback when mouse enters carousel
			onMouseLeave (str): Callback when mouse leaves carousel
			onNextClick (str): Callback when next control is clicked
			onPrevClick (str): Callback when previous control is clicked
			onSlideShow (str): Callback when a slide is shown
			onSlideHide (str): Callback when a slide is hidden
			onCarouselCreate (str): Callback when carousel is created
		
		Returns:
			str: Rendered HTML div element with carousel functionality
			
		References:
			.. _MetroUI Carousel: https://v5.metroui.org.ua/components/carousel/
			.. _MetroUI Documentation: https://v5.metroui.org.ua/
	Example:
		render_carousel()

	Empty or invalid:
		`render_carousel()` returns `<div class="carousel" id="carousel-component" data-role="carousel"></div>`.

	"""
	return _carousel_component.render(slides, **attrs)
