from django import template
from django.contrib.messages import constants as message_constants
from django.utils.safestring import mark_safe

from ..components import (
    render_alert,
    render_button,
    render_tile,
    render_card,
    render_progress,
    render_accordion,
    render_action_button,
    render_activity,
    render_adblock_detection,
    render_analog_clock,
    render_app_bar,
    render_audio_button,
    render_audio_player,
    render_bar3d,
    render_box,
    render_calendar,
    render_calendar_picker,
    render_carousel,
    render_card,
    render_catalog_menu,
    render_charms,
    render_chart_card,
    render_chat,
    render_checkbox,
    render_chips,
    render_cloak,
    render_clock,
    render_collapse,
    render_color_picker,
    render_color_selector,
    render_command_button,
    render_container,
    render_counter,
    render_cube,
    render_custom_checkbox,
    render_cutter,
    render_d_menu,
    render_date_picker,
    render_dialog,
    render_dialog_create,
    render_directive,
    render_donut,
    render_double_select_box,
    render_double_slider,
    render_drag_items,
    render_draggable,
    render_drop_menu,
    render_dropdown,
    render_dropdown_button,
    render_file,
    render_file_button,
    render_file_drop,
    render_file_with_icon,
    render_file_multiple,
    render_flip_card,
    render_flip_card_hover,
    render_flip_card_active,
    render_flip_card_horizontal,
    render_flip_card_with_dimensions,
    render_input,
    render_material_input,
    render_list,
    render_menu,
    render_navigation,
    render_panel,
    render_sidebar,
    render_spinner,
    render_image_carousel,
    render_image_button,
    render_icon_box,
    render_html_container,
    render_hero,
    render_hamburger,
    render_h_menu,
    render_gravatar,
    render_github_box,
    render_eval,
    render_cookie_disclaimer,
    render_working_tree,
    render_window,
    render_viewport_check,
    render_video_player,
    render_typer,
    render_tokenizer,
    render_textarea,
    render_tag_input,
    render_streamer,
    render_slider,
    render_sidenav_simple,
    render_sidenav_counter,
    render_select,
    render_resizable_container,
    render_resizable,
    render_remote_table,
    render_remote_dataset,
    render_popover,
    render_package_manager,
    render_navview,
    render_marquee,
    render_listview,
    render_linked_block,
    render_keypad,
    render_image_placeholder,
    render_image_box,
    render_hover_box,
    render_gradient_box,
    render_gauge,
    render_countdown,
    render_table,
    render_tabs,
    render_toolbar,
    render_modal,
    render_breadcrumb,
    render_bulls,
    render_button_group,
    render_pagination,
    render_badge,
    render_avatar,
    render_initials_avatar,
    render_icon_avatar,
    render_image_avatar,
    render_responsive_avatar,
    render_rating,
)

from ..core import css_url, get_metroui5_setting, javascript_url, icons_css_url
from ..css import merge_css_classes
from ..forms import (
    render_field,
    render_form,
    render_form_errors,
    render_formset,
)
from ..html import render_link_tag, render_script_tag, render_tag

MESSAGE_ALERT_TYPES = {
    message_constants.DEBUG: "warning",
    message_constants.INFO: "info",
    message_constants.SUCCESS: "success",
    message_constants.WARNING: "warning",
    message_constants.ERROR: "danger",
}

register = template.Library()


@register.simple_tag
def metroui5_setting(value):
    """Returns MetroUI5 setting value."""
    return get_metroui5_setting(value)


@register.simple_tag
def metroui5_css_url():
    """Returns URL for MetroUI CSS file."""
    return css_url()


@register.simple_tag
def metroui5_javascript_url():
    """Returns URL for MetroUI JavaScript file."""
    return javascript_url()


@register.simple_tag
def metroui5_icons_css_url():
    """Returns URL for MetroUI icons CSS file."""
    return icons_css_url()


@register.simple_tag
def metroui5_css():
    """Includes MetroUI CSS file."""
    return mark_safe(render_link_tag(css_url()))


@register.simple_tag
def metroui5_javascript():
    """Includes MetroUI JavaScript file."""
    return mark_safe(render_script_tag(javascript_url()))


@register.simple_tag
def metroui5_icons_css():
    """Includes MetroUI icons CSS file."""
    return mark_safe(render_link_tag(icons_css_url()))


@register.simple_tag
def metroui5_custom_css():
    """Includes custom CSS files specified in settings."""
    from metroui5.html import render_custom_css_files
    from metroui5.core import custom_css_files
    return mark_safe(render_custom_css_files(custom_css_files()))


@register.simple_tag
def metroui5_custom_javascript():
    """Includes custom JavaScript files specified in settings."""
    from metroui5.html import render_custom_javascript_files
    from metroui5.core import custom_javascript_files
    return mark_safe(render_custom_javascript_files(custom_javascript_files()))


@register.simple_tag
def metroui5_all_css():
    """Includes all MetroUI CSS files (core + custom)."""
    from metroui5.html import render_custom_css_files
    from metroui5.core import custom_css_files
    html = metroui5_css()
    # Add custom CSS files
    custom_css = render_custom_css_files(custom_css_files())
    if custom_css:
        html += "\n" + custom_css
    return mark_safe(html)


@register.simple_tag
def metroui5_all_javascript():
    """Includes all MetroUI JavaScript files (core + custom)."""
    from metroui5.html import render_custom_javascript_files
    from metroui5.core import custom_javascript_files
    html = metroui5_javascript()
    # Add custom JavaScript files
    custom_js = render_custom_javascript_files(custom_javascript_files())
    if custom_js:
        html += "\n" + custom_js
    return mark_safe(html)


@register.simple_tag
def metroui5_cdn_mode():
    """Returns whether CDN mode is enabled."""
    from metroui5.core import is_cdn_mode
    return is_cdn_mode()


@register.simple_tag
def metroui5_form(form, **kwargs):
    """Renders form with MetroUI styling."""
    return mark_safe(render_form(form, **kwargs))


@register.simple_tag
def metroui5_field(field, **kwargs):
    """Renders form field with MetroUI styling."""
    return mark_safe(render_field(field, **kwargs))


@register.simple_tag
def metroui5_form_errors(form, **kwargs):
    """Renders form errors in MetroUI style."""
    return mark_safe(render_form_errors(form, **kwargs))


@register.simple_tag
def metroui5_formset(formset, **kwargs):
    """Renders formset with MetroUI styling."""
    return mark_safe(render_formset(formset, **kwargs))


@register.simple_tag
def metroui5_button(content, **kwargs):
    """Renders MetroUI button."""
    return mark_safe(render_button(content, **kwargs))


@register.simple_tag
def metroui5_tile(title, **kwargs):
    """Renders MetroUI tile."""
    return mark_safe(render_tile(title, **kwargs))


@register.simple_tag
def metroui5_card(**kwargs):
    """Renders MetroUI card."""
    return mark_safe(render_card(**kwargs))


@register.simple_tag
def metroui5_carousel(**kwargs):
    """Renders MetroUI carousel."""
    return mark_safe(render_carousel(**kwargs))


@register.simple_tag
def metroui5_catalog_menu(**kwargs):
    """Renders MetroUI catalog menu."""
    return mark_safe(render_catalog_menu(**kwargs))


@register.simple_tag
def metroui5_charms(**kwargs):
    """Renders MetroUI charms."""
    return mark_safe(render_charms(**kwargs))


@register.simple_tag
def metroui5_chart_card(**kwargs):
    """Renders MetroUI chart card."""
    return mark_safe(render_chart_card(**kwargs))


@register.simple_tag
def metroui5_chat(**kwargs):
    """Renders MetroUI chat."""
    return mark_safe(render_chat(**kwargs))


@register.simple_tag
def metroui5_checkbox(**kwargs):
    """Renders MetroUI checkbox."""
    return mark_safe(render_checkbox(**kwargs))


@register.simple_tag
def metroui5_chips(**kwargs):
    """Renders MetroUI chips."""
    return mark_safe(render_chips(**kwargs))


@register.simple_tag
def metroui5_cloak(**kwargs):
    """Renders MetroUI cloak."""
    return mark_safe(render_cloak(**kwargs))


@register.simple_tag
def metroui5_clock(**kwargs):
    """Renders MetroUI clock."""
    return mark_safe(render_clock(**kwargs))


@register.simple_tag
def metroui5_collapse(content="", **kwargs):
    """Renders MetroUI collapse."""
    return mark_safe(render_collapse(content=content, **kwargs))


@register.simple_tag
def metroui5_color_picker(**kwargs):
    """Renders MetroUI color picker."""
    return mark_safe(render_color_picker(**kwargs))


@register.simple_tag
def metroui5_color_selector(**kwargs):
    """Renders MetroUI color selector."""
    return mark_safe(render_color_selector(**kwargs))


@register.simple_tag
def metroui5_command_button(icon="", caption="", description="", **kwargs):
    """Renders MetroUI command button."""
    return mark_safe(render_command_button(icon=icon, caption=caption, description=description, **kwargs))


@register.tag
def metroui5_container(parser, token):
    """Renders MetroUI container as a block tag."""
    try:
        tag_name, *args = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(f"{token.contents.split()[0]} requires arguments")
    
    # Parse arguments
    kwargs = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            # Remove quotes from value
            value = value.strip('"\'')
            # Convert boolean values
            if value.lower() in ('true', 'false'):
                value = value.lower() == 'true'
            kwargs[key] = value
        else:
            # Boolean flag
            kwargs[arg] = True
    
    nodelist = parser.parse(('endmetroui5_container',))
    parser.delete_first_token()
    
    return ContainerNode(nodelist, kwargs)


@register.tag
def endmetroui5_container(parser, token):
    """End tag for MetroUI container block tag."""
    return None


@register.simple_tag
def metroui5_counter(value=0, from_value=0, duration=2000, prefix="", suffix="", delimiter=",", size=16, 
                     start_on_viewport=False, counter_deferred=0, timeout=0, **kwargs):
    """Renders MetroUI counter."""
    return mark_safe(render_counter(
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
    ))


@register.simple_tag
def metroui5_cube(show_axis=False, axis_style="arrow", cells=4, numbers=False, color="", flash_color="", 
                  rules=None, flash_interval=1000, auto_restart=0, cell_click=False, **kwargs):
    """Renders MetroUI cube."""
    return mark_safe(render_cube(
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
    ))


@register.simple_tag
def metroui5_custom_checkbox(state_on="✓", state_off="✗", caption_on="", caption_off="", 
                            caption_position="right", name="", value="", checked=False, disabled=False, **kwargs):
    """Renders MetroUI custom checkbox."""
    return mark_safe(render_custom_checkbox(
        state_on=state_on,
        state_off=state_off,
        caption_on=caption_on,
        caption_off=caption_off,
        caption_position=caption_position,
        name=name,
        value=value,
        checked=checked,
        disabled=disabled,
        **kwargs
    ))


@register.simple_tag
def metroui5_cutter(content="", icon="", text="", **kwargs):
    """Renders MetroUI cutter."""
    return mark_safe(render_cutter(
        content=content,
        icon=icon,
        text=text,
        **kwargs
    ))


@register.simple_tag
def metroui5_d_menu(items=None, **kwargs):
    """Renders MetroUI D-Menu."""
    return mark_safe(render_d_menu(
        items=items,
        **kwargs
    ))




class ContainerNode(template.Node):
    def __init__(self, nodelist, kwargs):
        self.nodelist = nodelist
        self.kwargs = kwargs
    
    def render(self, context):
        content = self.nodelist.render(context)
        return render_container(content, **self.kwargs)


@register.simple_tag
def metroui5_progress(value, **kwargs):
    """Renders MetroUI progress bar."""
    return mark_safe(render_progress(value, **kwargs))


@register.simple_tag
def metroui5_alert(content, **kwargs):
    """Renders MetroUI alert."""
    return mark_safe(render_alert(content, **kwargs))


@register.simple_tag
def metroui5_messages(*args, **kwargs):
    """Renders Django messages in MetroUI style."""
    from django.contrib.messages import get_messages
    messages = get_messages(kwargs.get('request'))
    if not messages:
        return ""
    alerts = []
    for message in messages:
        alert_type = metroui5_message_alert_type(message)
        alerts.append(render_alert(str(message), alert_type=alert_type))
    return mark_safe("".join(alerts))


@register.filter
def metroui5_message_alert_type(message):
    """Returns alert type for Django message."""
    return MESSAGE_ALERT_TYPES.get(message.level, "info")


@register.simple_tag
def metroui5_classes(*args):
    """Combines CSS classes."""
    return merge_css_classes(*args)


# New template tags for advanced components
@register.simple_tag
def metroui5_accordion(items, **kwargs):
    """Renders MetroUI accordion."""
    return mark_safe(render_accordion(items, **kwargs))


@register.simple_tag
def metroui5_action_button(actions, main_icon="mif-plus", **kwargs):
    """Renders MetroUI action button with expandable sub-actions."""
    return mark_safe(render_action_button(actions, main_icon, **kwargs))


@register.simple_tag
def metroui5_activity(**kwargs):
    """Renders MetroUI activity component with animated loading indicators."""
    return mark_safe(render_activity(**kwargs))


@register.simple_tag
def metroui5_adblock_detection(**kwargs):
    """Renders MetroUI adblock detection component."""
    return mark_safe(render_adblock_detection(**kwargs))


@register.simple_tag
def metroui5_analog_clock(**kwargs):
    """Renders MetroUI analog clock component."""
    return mark_safe(render_analog_clock(**kwargs))


@register.simple_tag
def metroui5_app_bar(**kwargs):
    """Renders MetroUI app bar component."""
    # Extract brand, menu_items, and static_items from kwargs if they exist
    brand = kwargs.pop('brand', None)
    menu_items = kwargs.pop('menu_items', None)
    static_items = kwargs.pop('static_items', None)
    return mark_safe(render_app_bar(brand, menu_items, static_items, **kwargs))


@register.simple_tag
def metroui5_audio_button(content="", **kwargs):
    """Renders MetroUI audio button component."""
    return mark_safe(render_audio_button(content, **kwargs))


@register.simple_tag
def metroui5_audio_player(src="", **kwargs):
    """Renders MetroUI audio player component."""
    return mark_safe(render_audio_player(src, **kwargs))


@register.simple_tag
def metroui5_calendar(**kwargs):
    """Renders MetroUI calendar."""
    return mark_safe(render_calendar(**kwargs))


@register.simple_tag
def metroui5_calendar_picker(**kwargs):
    """Renders MetroUI calendar picker component."""
    return mark_safe(render_calendar_picker(**kwargs))


@register.simple_tag
def metroui5_date_picker(**kwargs):
    """Renders MetroUI date picker component."""
    return mark_safe(render_date_picker(**kwargs))


@register.simple_tag
def metroui5_dialog(title, content, **kwargs):
    """Renders MetroUI dialog."""
    return mark_safe(render_dialog(title, content, **kwargs))


@register.simple_tag
def metroui5_dialog_create(**kwargs):
    """Renders JavaScript code to create a dialog dynamically using Metro.dialog.create()."""
    return mark_safe(render_dialog_create(**kwargs))


@register.simple_tag
def metroui5_directive(content="", **kwargs):
    """Renders MetroUI directive."""
    return mark_safe(render_directive(content, **kwargs))


@register.simple_tag
def metroui5_donut(**kwargs):
    """Renders MetroUI donut."""
    return mark_safe(render_donut(**kwargs))


@register.simple_tag
def metroui5_double_select_box(left_options=None, right_options=None, **kwargs):
    """Renders MetroUI double select box."""
    return mark_safe(render_double_select_box(left_options, right_options, **kwargs))


@register.simple_tag
def metroui5_double_slider(**kwargs):
    """Renders MetroUI double slider."""
    return mark_safe(render_double_slider(**kwargs))


@register.simple_tag
def metroui5_drag_items(items=None, **kwargs):
    """Renders MetroUI drag items."""
    return mark_safe(render_drag_items(items, **kwargs))


@register.simple_tag
def metroui5_draggable(content="", **kwargs):
    """Renders MetroUI draggable."""
    return mark_safe(render_draggable(content, **kwargs))


@register.simple_tag
def metroui5_drop_menu(items=None, button_text="Menu", **kwargs):
    """Renders MetroUI drop menu."""
    return mark_safe(render_drop_menu(items, button_text, **kwargs))


@register.simple_tag
def metroui5_dropdown(content="", button_text="", toggle_element=None, items=None, **kwargs):
    """
    Renders MetroUI dropdown component.
    
    Args:
        content: The HTML content to be displayed in the dropdown (string).
        button_text: Text for the dropdown toggle button (string, default: "").
        toggle_element: Custom toggle element HTML (string, default: None).
        items: List of dropdown items to auto-generate menu (list, default: None).
        **kwargs: Additional attributes for dropdown configuration.
    """
    return mark_safe(render_dropdown(content=content, button_text=button_text, 
                                   toggle_element=toggle_element, items=items, **kwargs))


@register.simple_tag
def metroui5_input(*args, **kwargs):
    """Renders MetroUI input with advanced features."""
    # Handle positional arguments
    input_type = "text"
    placeholder = ""
    
    if len(args) > 0:
        input_type = args[0]
    if len(args) > 1:
        placeholder = args[1]
    
    # If placeholder is provided as a keyword argument, use it instead of the positional one
    if 'placeholder' in kwargs:
        placeholder = kwargs.pop('placeholder')
    
    return mark_safe(render_input(input_type, placeholder, **kwargs)    )


@register.simple_tag
def metroui5_dropdown_button(button_text="Options", items=None, content="", **kwargs):
    """
    Renders MetroUI dropdown button component.
    
    Args:
        button_text: Text for the dropdown toggle button (string, default: "Options")
        items: List of dropdown menu items (list of strings or dicts, default: None)
        content: Custom HTML content for dropdown (string, default: "")
        **kwargs: Additional component attributes including:
            # Button styling
            - button_style: Button style ("primary", "success", "warning", "danger", "info", "dark", "light")
            - button_size: Button size ("large", "small", "mini")
            - outline: Outline button style (boolean)
            - flat: Flat button style (boolean)
            - rounded: Rounded button style (boolean)
            - icon: Icon class for button (string)
            - icon_position: Icon position ("left", "right", default: "left")
            
            # Dropdown configuration
            - dropdown_deferred: Delay before dropdown appears (number, default: 0)
            - drop_filter: CSS selector to filter dropdowns (string, default: null)
            - align: Dropdown alignment ("left" or "right", default: "left")
            - no_close: Won't close when clicking outside (boolean, default: false)
            - duration: Animation duration in milliseconds (number, default: 50)
            - open_mode: How dropdown opens ("auto", "up", default: "auto")
            - height: Height of dropdown (string, default: "auto")
            
            # Positioning
            - drop_left, drop_right, drop_up, drop_down, etc.: Positioning options (boolean)
            - keep_open: Prevent closing when clicking outside (boolean)
            
            # Events
            - on_drop: Triggered when dropdown is opened (string)
            - on_up: Triggered when dropdown is closed (string)
            - on_dropdown_create: Triggered when dropdown is created (string)
            
            # CSS classes
            - cls_dropdown_button: Additional CSS class for container (string)
            - cls_button: Additional CSS class for button (string)
            - cls_dropdown: Additional CSS class for dropdown menu (string)
    """
    return mark_safe(render_dropdown_button(
        button_text=button_text,
        items=items,
        content=content,
        **kwargs
    ))


@register.simple_tag
def metroui5_file(**kwargs):
    """
    Renders MetroUI file component.
    
    Args:
        **kwargs: Component attributes including:
            # Configuration
            - file_deferred: Delay before initialization in milliseconds (number, default: 0)
            - label: Label text for the file input (string, default: "")
            - mode: Mode of operation - "input", "button", or "drop" (string, default: "input")
            - button_title: Text for the select files button (string, default: "")
            - files_selected_title: Text for displaying selected files count (string, default: "")
            - drop_title: Text for the drop zone (string, default: "")
            - drop_icon: Icon for the drop zone (string, default: "📥")
            - clear_button_icon: Icon for the clear button (string, default: "❌")
            - prepend: HTML content to prepend to the input (string, default: "")
            
            # Styling
            - cls_component: Additional CSS class for component container (string)
            - cls_prepend: Additional CSS class for prepend element (string)
            - cls_button: Additional CSS class for button (string)
            - cls_caption: Additional CSS class for caption (string)
            - cls_label: Additional CSS class for label (string)
            
            # Events
            - on_select: Callback function when files are selected (string)
            - on_file_create: Callback function when component is created (string)
            
            # Validation
            - error: Show error state (boolean)
            - error_message: Error message text (string)
            - success: Show success state (boolean)
            - success_message: Success message text (string)
            
            # Standard input attributes
            - multiple: Allow multiple file selection (boolean)
            - accept: File types to accept (string)
            - disabled: Disable the input (boolean)
            - required: Make the input required (boolean)
    """
    return mark_safe(render_file(**kwargs))


@register.simple_tag
def metroui5_file_button(button_text="Choose File", **kwargs):
    """
    Renders MetroUI file component in button mode.
    
    Args:
        button_text: Text for the button (string, default: "Choose File")
        **kwargs: Additional component attributes
    """
    return mark_safe(render_file_button(button_text=button_text, **kwargs))


@register.simple_tag
def metroui5_file_drop(drop_text="Drop file here", **kwargs):
    """
    Renders MetroUI file component in drop zone mode.
    
    Args:
        drop_text: Text for the drop zone (string, default: "Drop file here")
        **kwargs: Additional component attributes
    """
    return mark_safe(render_file_drop(drop_text=drop_text, **kwargs))


@register.simple_tag
def metroui5_file_with_icon(icon_class="mif-folder", **kwargs):
    """
    Renders MetroUI file component with an icon prepend.
    
    Args:
        icon_class: CSS class for the icon (string, default: "mif-folder")
        **kwargs: Additional component attributes
    """
    return mark_safe(render_file_with_icon(icon_class=icon_class, **kwargs))


@register.simple_tag
def metroui5_file_multiple(**kwargs):
    """
    Renders MetroUI file component that accepts multiple files.
    
    Args:
        **kwargs: Additional component attributes
    """
    return mark_safe(render_file_multiple(**kwargs    ))


@register.simple_tag
def metroui5_flip_card(**kwargs):
    """
    Renders MetroUI flip card component.
    
    Args:
        **kwargs: Component attributes including:
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
    return mark_safe(render_flip_card(**kwargs))


@register.simple_tag
def metroui5_flip_card_hover(front_content, back_content, **kwargs):
    """
    Renders MetroUI flip card that flips on hover.
    
    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        **kwargs: Additional component attributes
    """
    return mark_safe(render_flip_card_hover(front_content=front_content, back_content=back_content, **kwargs))


@register.simple_tag
def metroui5_flip_card_active(front_content, back_content, **kwargs):
    """
    Renders MetroUI flip card that flips when active class is added.
    
    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        **kwargs: Additional component attributes
    """
    return mark_safe(render_flip_card_active(front_content=front_content, back_content=back_content, **kwargs))


@register.simple_tag
def metroui5_flip_card_horizontal(front_content, back_content, **kwargs):
    """
    Renders MetroUI flip card that flips horizontally.
    
    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        **kwargs: Additional component attributes
    """
    return mark_safe(render_flip_card_horizontal(front_content=front_content, back_content=back_content, **kwargs))


@register.simple_tag
def metroui5_flip_card_with_dimensions(front_content, back_content, width, height, **kwargs):
    """
    Renders MetroUI flip card with specific dimensions.
    
    Args:
        front_content: Content for the front side (string/HTML)
        back_content: Content for the back side (string/HTML)
        width: Width of the flip card (string)
        height: Height of the flip card (string)
        **kwargs: Additional component attributes
    """
    return mark_safe(render_flip_card_with_dimensions(
        front_content=front_content, 
        back_content=back_content, 
        width=width, 
        height=height, 
        **kwargs
    ))


@register.simple_tag
def metroui5_material_input(*args, **kwargs):
    """Renders MetroUI material input with material design features."""
    # Handle positional arguments
    input_type = "text"
    placeholder = ""
    
    if len(args) > 0:
        input_type = args[0]
    if len(args) > 1:
        placeholder = args[1]
    
    # If placeholder is provided as a keyword argument, use it instead of the positional one
    if 'placeholder' in kwargs:
        placeholder = kwargs.pop('placeholder')
    
    return mark_safe(render_material_input(input_type, placeholder, **kwargs))


@register.simple_tag
def metroui5_list(items, list_type="ul", **kwargs):
    """Renders MetroUI list."""
    return mark_safe(render_list(items, list_type, **kwargs))


@register.simple_tag
def metroui5_menu(items, **kwargs):
    """Renders MetroUI menu."""
    return mark_safe(render_menu(items, **kwargs))


@register.simple_tag
def metroui5_navigation(items, **kwargs):
    """Renders MetroUI navigation."""
    return mark_safe(render_navigation(items, **kwargs))


@register.simple_tag
def metroui5_panel(title=None, content=None, **kwargs):
    """Renders MetroUI panel."""
    return mark_safe(render_panel(title, content, **kwargs))


@register.simple_tag
def metroui5_sidebar(items, **kwargs):
    """Renders MetroUI sidebar."""
    return mark_safe(render_sidebar(items, **kwargs))


@register.simple_tag
def metroui5_spinner(**kwargs):
    """Поле с шагом."""
    return mark_safe(render_spinner(**kwargs))

@register.simple_tag
def metroui5_image_carousel(content="", **kwargs):
    """Компонент image-carousel."""
    return mark_safe(render_image_carousel(content, **kwargs))


@register.simple_tag
def metroui5_image_button(content="", **kwargs):
    """Компонент image-button."""
    return mark_safe(render_image_button(content, **kwargs))


@register.simple_tag
def metroui5_icon_box(content="", **kwargs):
    """Компонент icon-box."""
    return mark_safe(render_icon_box(content, **kwargs))


@register.simple_tag
def metroui5_html_container(content="", **kwargs):
    """Компонент html-container."""
    return mark_safe(render_html_container(content, **kwargs))


@register.simple_tag
def metroui5_hero(content="", **kwargs):
    """Компонент hero."""
    return mark_safe(render_hero(content, **kwargs))


@register.simple_tag
def metroui5_hamburger(content="", **kwargs):
    """Компонент hamburger."""
    return mark_safe(render_hamburger(content, **kwargs))


@register.simple_tag
def metroui5_h_menu(content="", **kwargs):
    """Компонент h-menu."""
    return mark_safe(render_h_menu(content, **kwargs))


@register.simple_tag
def metroui5_gravatar(**kwargs):
    """Компонент gravatar."""
    return mark_safe(render_gravatar(**kwargs))


@register.simple_tag
def metroui5_github_box(content="", **kwargs):
    """Компонент github-box."""
    return mark_safe(render_github_box(content, **kwargs))


@register.simple_tag
def metroui5_eval(content="", **kwargs):
    """Компонент eval."""
    return mark_safe(render_eval(content, **kwargs))


@register.simple_tag
def metroui5_cookie_disclaimer(content="", **kwargs):
    """Компонент cookie-disclaimer."""
    return mark_safe(render_cookie_disclaimer(content, **kwargs))



@register.simple_tag
def metroui5_working_tree(content="", **kwargs):
    """Компонент working-tree."""
    return mark_safe(render_working_tree(content, **kwargs))


@register.simple_tag
def metroui5_window(content="", **kwargs):
    """Компонент window."""
    return mark_safe(render_window(content, **kwargs))


@register.simple_tag
def metroui5_viewport_check(content="", **kwargs):
    """Компонент viewport-check."""
    return mark_safe(render_viewport_check(content, **kwargs))


@register.simple_tag
def metroui5_video_player(content="", **kwargs):
    """Компонент video-player."""
    return mark_safe(render_video_player(content, **kwargs))


@register.simple_tag
def metroui5_typer(content="", **kwargs):
    """Компонент typer."""
    return mark_safe(render_typer(content, **kwargs))


@register.simple_tag
def metroui5_tokenizer(content="", **kwargs):
    """Компонент tokenizer."""
    return mark_safe(render_tokenizer(content, **kwargs))


@register.simple_tag
def metroui5_textarea(content="", **kwargs):
    """Компонент textarea."""
    return mark_safe(render_textarea(content, **kwargs))


@register.simple_tag
def metroui5_tag_input(content="", **kwargs):
    """Компонент tag-input."""
    return mark_safe(render_tag_input(content, **kwargs))


@register.simple_tag
def metroui5_streamer(content="", **kwargs):
    """Компонент streamer."""
    return mark_safe(render_streamer(content, **kwargs))


@register.simple_tag
def metroui5_slider(content="", **kwargs):
    """Компонент slider."""
    return mark_safe(render_slider(content, **kwargs))


@register.simple_tag
def metroui5_sidenav_simple(content="", **kwargs):
    """Компонент sidenav-simple."""
    return mark_safe(render_sidenav_simple(content, **kwargs))


@register.simple_tag
def metroui5_sidenav_counter(content="", **kwargs):
    """Компонент sidenav-counter."""
    return mark_safe(render_sidenav_counter(content, **kwargs))


@register.simple_tag
def metroui5_select(content="", **kwargs):
    """Компонент select."""
    return mark_safe(render_select(content, **kwargs))


@register.simple_tag
def metroui5_resizable_container(content="", **kwargs):
    """Компонент resizable-container."""
    return mark_safe(render_resizable_container(content, **kwargs))


@register.simple_tag
def metroui5_resizable(content="", **kwargs):
    """Компонент resizable."""
    return mark_safe(render_resizable(content, **kwargs))


@register.simple_tag
def metroui5_remote_table(content="", **kwargs):
    """Компонент remote-table."""
    return mark_safe(render_remote_table(content, **kwargs))


@register.simple_tag
def metroui5_remote_dataset(content="", **kwargs):
    """Компонент remote-dataset."""
    return mark_safe(render_remote_dataset(content, **kwargs))


@register.simple_tag
def metroui5_popover(content="", **kwargs):
    """Компонент popover."""
    return mark_safe(render_popover(content, **kwargs))


@register.simple_tag
def metroui5_package_manager(content="", **kwargs):
    """Компонент package-manager."""
    return mark_safe(render_package_manager(content, **kwargs))


@register.simple_tag
def metroui5_navview(content="", **kwargs):
    """Компонент navview."""
    return mark_safe(render_navview(content, **kwargs))


@register.simple_tag
def metroui5_marquee(content="", **kwargs):
    """Компонент marquee."""
    return mark_safe(render_marquee(content, **kwargs))


@register.simple_tag
def metroui5_listview(content="", **kwargs):
    """Компонент listview."""
    return mark_safe(render_listview(content, **kwargs))


@register.simple_tag
def metroui5_linked_block(content="", **kwargs):
    """Компонент linked-block."""
    return mark_safe(render_linked_block(content, **kwargs))


@register.simple_tag
def metroui5_keypad(content="", **kwargs):
    """Компонент keypad."""
    return mark_safe(render_keypad(content, **kwargs))


@register.simple_tag
def metroui5_image_placeholder(content="", **kwargs):
    """Компонент image-placeholder."""
    return mark_safe(render_image_placeholder(content, **kwargs))


@register.simple_tag
def metroui5_image_box(content="", **kwargs):
    """Компонент image-box."""
    return mark_safe(render_image_box(content, **kwargs))


@register.simple_tag
def metroui5_hover_box(content="", **kwargs):
    """Компонент hover-box."""
    return mark_safe(render_hover_box(content, **kwargs))


@register.simple_tag
def metroui5_gradient_box(content="", **kwargs):
    """Компонент gradient-box."""
    return mark_safe(render_gradient_box(content, **kwargs))


@register.simple_tag
def metroui5_gauge(content="", **kwargs):
    """Компонент gauge."""
    return mark_safe(render_gauge(content, **kwargs))


@register.simple_tag
def metroui5_countdown(content="", **kwargs):
    """Компонент countdown."""
    return mark_safe(render_countdown(content, **kwargs))


@register.simple_tag
def metroui5_table(headers, rows, **kwargs):
    """Renders MetroUI table."""
    return mark_safe(render_table(headers, rows, **kwargs))


@register.simple_tag
def metroui5_tabs(tabs, **kwargs):
    """Renders MetroUI tabs."""
    return mark_safe(render_tabs(tabs, **kwargs))


@register.simple_tag
def metroui5_toolbar(items, **kwargs):
    """Renders MetroUI toolbar."""
    return mark_safe(render_toolbar(items, **kwargs))


@register.simple_tag
def metroui5_modal(title, content, **kwargs):
    """Renders MetroUI modal."""
    return mark_safe(render_modal(title, content, **kwargs))


@register.simple_tag
def metroui5_breadcrumb(items, **kwargs):
    """Renders MetroUI breadcrumb."""
    return mark_safe(render_breadcrumb(items, **kwargs))


@register.simple_tag
def metroui5_pagination(current_page, total_pages, **kwargs):
    """Renders MetroUI pagination."""
    return mark_safe(render_pagination(current_page, total_pages, **kwargs))


@register.simple_tag
def metroui5_badge(content, corner=False, corner_outside=False, **kwargs):
    """Renders MetroUI badge."""
    return mark_safe(render_badge(content, corner, corner_outside, **kwargs))


@register.simple_tag
def metroui5_bar3d(**kwargs):
    """Renders MetroUI bar3d component."""
    return mark_safe(render_bar3d(**kwargs))


@register.simple_tag
def metroui5_box(content="", title=None, secondary_title=None, **kwargs):
    """Renders MetroUI box component."""
    return mark_safe(render_box(content, title, secondary_title, **kwargs))


@register.simple_tag
def metroui5_bulls(bull_type="success", size=16, **kwargs):
    """Renders MetroUI bulls component."""
    return mark_safe(render_bulls(bull_type, size, **kwargs))


@register.simple_tag
def metroui5_button_group(buttons, mode="one", **kwargs):
    """Renders MetroUI button group component."""
    return mark_safe(render_button_group(buttons, mode, **kwargs))


@register.simple_tag
def metroui5_avatar(image_url, **kwargs):
    """Renders MetroUI avatar."""
    return mark_safe(render_avatar(image_url, **kwargs))


@register.simple_tag
def metroui5_rating(value, max_value=5, **kwargs):
    """Renders MetroUI rating."""
    return mark_safe(render_rating(value, max_value, **kwargs))


# Utility template tags
@register.simple_tag
def metroui5_icon(icon_name, size=None, **kwargs):
    """Renders MetroUI icon."""
    icon_classes = [f"mif-{icon_name}"]
    if size:
        icon_classes.append(f"mif-{size}")
    attrs = {"class": " ".join(icon_classes)}
    attrs.update(kwargs)
    return mark_safe(render_tag("span", attrs=attrs, content=""))


@register.simple_tag
def metroui5_grid(columns=12, **kwargs):
    """Renders MetroUI grid container."""
    attrs = {"class": f"grid grid-{columns}"}
    attrs.update(kwargs)
    return mark_safe(render_tag("div", attrs=attrs, content=""))


@register.simple_tag
def metroui5_row(**kwargs):
    """Renders MetroUI row."""
    attrs = {"class": "row"}
    attrs.update(kwargs)
    return mark_safe(render_tag("div", attrs=attrs, content=""))


@register.simple_tag
def metroui5_cell(size, **kwargs):
    """Renders MetroUI cell."""
    attrs = {"class": f"cell-{size}"}
    attrs.update(kwargs)
    return mark_safe(render_tag("div", attrs=attrs, content=""))




@register.simple_tag
def metroui5_fluid_container(**kwargs):
    """Renders MetroUI fluid container."""
    attrs = {"class": "container-fluid"}
    attrs.update(kwargs)
    return mark_safe(render_tag("div", attrs=attrs, content=""))




@register.simple_tag
def metroui5_notify(message, **kwargs):
    """Renders MetroUI notify."""
    attrs = {"class": "notify", "data-role": "notify"}
    attrs.update(kwargs)
    return mark_safe(render_tag("div", attrs=attrs, content=message))


@register.simple_tag
def metroui5_hint(text, **kwargs):
    """Renders MetroUI hint."""
    attrs = {"class": "hint", "data-role": "hint", "data-hint-text": text}
    attrs.update(kwargs)
    return mark_safe(render_tag("div", attrs=attrs, content=""))


@register.simple_tag
def metroui5_loading(**kwargs):
    """Renders MetroUI loading indicator."""
    attrs = {"class": "loading", "data-role": "loading"}
    attrs.update(kwargs)
    return mark_safe(render_tag("div", attrs=attrs, content=""))


@register.simple_tag
def metroui5_stepper(steps, **kwargs):
    """Renders MetroUI stepper."""
    attrs = {"class": "stepper", "data-role": "stepper"}
    attrs.update(kwargs)
    stepper_items = []
    for i, step in enumerate(steps):
        step_class = "active" if i == 0 else ""
        step_html = render_tag("div", {"class": f"step {step_class}"}, step)
        stepper_items.append(step_html)
    return mark_safe(render_tag("div", attrs=attrs, content="".join(stepper_items)))


@register.simple_tag
def metroui5_tree(items, **kwargs):
    """Renders MetroUI tree."""
    attrs = {"class": "tree", "data-role": "tree"}
    attrs.update(kwargs)

    def render_tree_item(item):
        if isinstance(item, dict):
            item_html = render_tag("span", {}, item.get('text', ''))
            if 'children' in item:
                children_html = "".join([render_tree_item(child) for child in item['children']])
                item_html += render_tag("ul", {}, children_html)
            return render_tag("li", {}, item_html)
        else:
            return render_tag("li", {}, str(item))

    tree_items = [render_tree_item(item) for item in items]
    return mark_safe(render_tag("div", attrs=attrs, content=render_tag("ul", {}, "".join(tree_items))))


@register.simple_tag
def metroui5_wizard(steps, **kwargs):
    """Renders MetroUI wizard."""
    attrs = {"class": "wizard", "data-role": "wizard"}
    attrs.update(kwargs)

    wizard_nav = []
    wizard_content = []
    for i, step in enumerate(steps):
        is_active = "active" if i == 0 else ""
        step_title = step.get('title', f'Step {i + 1}')
        step_content = step.get('content', '')
        wizard_nav.append(render_tag("a", {"class": f"step {is_active}", "href": f"#step-{i}"}, step_title))
        wizard_content.append(
            render_tag("div", {"class": f"step-content {is_active}", "id": f"step-{i}"}, step_content))

    nav = render_tag("div", {"class": "wizard-nav"}, "".join(wizard_nav))
    content = render_tag("div", {"class": "wizard-content"}, "".join(wizard_content))
    return mark_safe(render_tag("div", attrs=attrs, content=nav + content))


@register.simple_tag
def metroui5_theme_meta():
	"""Returns the meta tag for theme configuration."""
	from metroui5.core import get_theme_meta_tag
	return mark_safe(get_theme_meta_tag())


@register.simple_tag
def metroui5_theme_class():
    """Returns the theme class to apply to the target element."""
    from metroui5.core import get_theme_class
    return get_theme_class()


@register.simple_tag
def metroui5_theme_switcher():
    """Returns HTML for the theme switcher component."""
    from metroui5.core import get_theme_switcher_html
    return mark_safe(get_theme_switcher_html())


@register.simple_tag
def metroui5_theme_switcher_switch():
    """Returns HTML for the theme switcher in switch mode."""
    from metroui5.core import is_theme_switcher_enabled, get_theme_target
    if not is_theme_switcher_enabled():
        return ""
    theme_target = get_theme_target()
    target_attr = f'data-target="{theme_target}"' if theme_target != "html" else ""
    return mark_safe(f'<input type="checkbox" class="theme-switch" data-role="theme-switch" {target_attr}>')


@register.simple_tag
def metroui5_theme_switcher_button():
    """Returns HTML for the theme switcher in button mode."""
    from metroui5.core import is_theme_switcher_enabled, get_theme_target
    if not is_theme_switcher_enabled():
        return ""
    theme_target = get_theme_target()
    target_attr = f'data-target="{theme_target}"' if theme_target != "html" else ""
    return mark_safe(f'<button class="button" data-role="theme-switcher" {target_attr}>Switch Theme</button>')


@register.simple_tag
def metroui5_theme_info():
    """Returns theme information for debugging."""
    from metroui5.core import get_theme, get_theme_target, is_theme_switcher_enabled
    return {
        'theme': get_theme(),
        'target': get_theme_target(),
        'switcher_enabled': is_theme_switcher_enabled(),
    }
