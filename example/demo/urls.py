"""
URL configuration for demo app.
"""

from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms_demo, name='forms'),
    path('components/', views.components_demo, name='components'),
    path('tiles/', views.tiles_demo, name='tiles'),
    path('advanced-components/', views.advanced_components_demo, name='advanced_components'),
    path('themes/', views.themes_demo, name='themes'),
    path('initials-avatars/', views.initials_avatars, name='initials_avatars'),
    path('advanced-inputs/', views.advanced_inputs, name='advanced_inputs'),
    path('input-comparison/', views.input_comparison, name='input_comparison'),
    path('accordion-demo/', views.accordion_demo, name='accordion_demo'),
    path('action-button-demo/', views.action_button_demo, name='action_button_demo'),
    path('activity-demo/', views.activity_demo, name='activity_demo'),
    path('adblock-demo/', views.adblock_demo, name='adblock_demo'),
    path('analog-clock-demo/', views.analog_clock_demo, name='analog_clock_demo'),
    path('app-bar-demo/', views.app_bar_demo, name='app_bar_demo'),
    path('audio-button-demo/', views.audio_button_demo, name='audio_button_demo'),
    path('audio-player-demo/', views.audio_player_demo, name='audio_player_demo'),
    path('badge-demo/', views.badge_demo, name='badge_demo'),
    path('bar3d-demo/', views.bar3d_demo, name='bar3d_demo'),
    path('box-demo/', views.box_demo, name='box_demo'),
    path('breadcrumb-demo/', views.breadcrumb_demo, name='breadcrumb_demo'),
    path('bulls-demo/', views.bulls_demo, name='bulls_demo'),
]
