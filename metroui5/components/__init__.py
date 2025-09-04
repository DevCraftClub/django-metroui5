"""
MetroUI5 Components Package

This package contains all the render functions for MetroUI5 components,
organized into separate modules for better maintainability.
"""

# Import all render functions from their respective modules
from .alert import render_alert
from .avatar import (
    render_avatar,
    render_initials_avatar,
    render_icon_avatar,
    render_image_avatar,
    render_responsive_avatar
)
from .badge import render_badge
from .breadcrumb import render_breadcrumb
from .button import render_button
from .calendar import render_calendar
from .calendar_picker import render_calendar_picker
from .carousel import render_carousel
from .card import render_card
from .catalog_menu import render_catalog_menu
from .charms import render_charms
from .chart_card import render_chart_card
from .chat import render_chat
from .checkbox import render_checkbox
from .chips import render_chips
from .cloak import render_cloak
from .dialog import render_dialog
from .dropdown import render_dropdown
from .input import render_input, render_material_input
from .list import render_list
from .menu import render_menu
from .modal import render_modal
from .navigation import render_navigation
from .pagination import render_pagination
from .panel import render_panel
from .progress import render_progress
from .rating import render_rating
from .sidebar import render_sidebar
from .table import render_table
from .tabs import render_tabs
from .tile import render_tile
from .toolbar import render_toolbar
from .accordion import render_accordion
from .action_button import render_action_button
from .activity import render_activity
from .adblock import render_adblock_detection
from .analog_clock import render_analog_clock
from .app_bar import render_app_bar
from .audio_button import render_audio_button
from .audio_player import render_audio_player
from .bar3d import render_bar3d
from .box import render_box
from .breadcrumb import render_breadcrumb
from .bulls import render_bulls
from .button_group import render_button_group

# Export all render functions
__all__ = [
    # Core components
    'render_alert',
    'render_button',
    'render_tile',
    'render_card',
    'render_progress',
    
    # Layout components
    'render_accordion',
    'render_action_button',
    'render_activity',
    'render_adblock_detection',
    'render_analog_clock',
    'render_app_bar',
    'render_audio_button',
    'render_audio_player',
    'render_bar3d',
    'render_box',
    'render_calendar',
    'render_calendar_picker',
    'render_carousel',
    'render_card',
    'render_catalog_menu',
    'render_charms',
    'render_chart_card',
    'render_chat',
    'render_checkbox',
    'render_chips',
    'render_cloak',
    'render_dialog',
    'render_dropdown',
    'render_input',
    'render_material_input',
    'render_list',
    'render_menu',
    'render_navigation',
    'render_panel',
    'render_sidebar',
    'render_table',
    'render_tabs',
    'render_toolbar',
    'render_modal',
    
    # Navigation components
    'render_breadcrumb',
    'render_pagination',
    
    # Content components
    'render_badge',
    'render_avatar',
    'render_initials_avatar',
    'render_icon_avatar',
    'render_image_avatar',
    'render_responsive_avatar',
    'render_rating',
    'render_bulls',
    'render_button_group',
]
