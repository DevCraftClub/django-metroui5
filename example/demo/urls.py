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
]
