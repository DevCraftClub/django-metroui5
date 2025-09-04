"""
Context processors for the demo application.
"""

def app_bar_data(request):
    """
    Provides app bar data for all templates.
    """
    return {
        'app_bar_brand': {
            'text': 'MetroUI5 Demo',
            'icon': 'mif-crown mif-3x'
        },
        'app_bar_menu_items': [
            {'text': 'Главная', 'href': '/', 'icon': 'mif-home'},
            {
                'text': 'Формы',
                'icon': 'mif-form',
                'dropdown': [
                    {'text': 'Основные формы', 'href': '/forms/'},
                    {'text': 'Расширенные Inputs', 'href': '/advanced-inputs/'},
                    {'text': 'Сравнение Inputs', 'href': '/input-comparison/'}
                ]
            },
            {
                'text': 'Компоненты',
                'icon': 'mif-apps',
                'dropdown': [
                    {'text': 'Основные компоненты', 'href': '/components/'},
                    {'text': 'Расширенные компоненты', 'href': '/advanced-components/'},
                    {'text': 'Tiles', 'href': '/tiles/'}
                ]
            },
            {
                'text': 'UI Компоненты',
                'icon': 'mif-cog',
                'dropdown': [
                    {'text': 'Accordion', 'href': '/accordion-demo/', 'icon': 'mif-list'},
                    {'text': 'Action Button', 'href': '/action-button-demo/', 'icon': 'mif-plus'},
                    {'text': 'Activity', 'href': '/activity-demo/', 'icon': 'mif-spinner'},
                    {'text': 'App Bar', 'href': '/app-bar-demo/', 'icon': 'mif-menu'},
                    {'text': 'Audio Button', 'href': '/audio-button-demo/', 'icon': 'mif-volume-high'},
                    {'text': 'Audio Player', 'href': '/audio-player-demo/', 'icon': 'mif-music-note'},
                    {'text': 'Badge', 'href': '/badge-demo/', 'icon': 'mif-bookmark'},
                    {'text': 'Bar3d', 'href': '/bar3d-demo/', 'icon': 'mif-chart'},
                    {'text': 'Box', 'href': '/box-demo/', 'icon': 'mif-folder'},
                    {'text': 'Breadcrumb', 'href': '/breadcrumb-demo/', 'icon': 'mif-arrow-right'},
                    {'text': 'Bulls', 'href': '/bulls-demo/', 'icon': 'mif-checkmark'},
                    {'text': 'Button', 'href': '/button-demo/', 'icon': 'mif-play'},
                    {'text': 'Button Group', 'href': '/button-group-demo/', 'icon': 'mif-menu'},
                    {'text': 'Calendar', 'href': '/calendar-demo/', 'icon': 'mif-calendar'},
                    {'text': 'Calendar Picker', 'href': '/calendar-picker-demo/', 'icon': 'mif-calendar'},
                    {'text': 'Card', 'href': '/card-demo/', 'icon': 'mif-credit-card'},
                    {'text': 'Carousel', 'href': '/carousel-demo/', 'icon': 'mif-images'},
                    {'text': 'Catalog Menu', 'href': '/catalog-menu-demo/', 'icon': 'mif-list'},
                    {'text': 'Charms', 'href': '/charms-demo/', 'icon': 'mif-apps'},
                    {'text': 'Chart Card', 'href': '/chart-card-demo/', 'icon': 'mif-chart'},
                    {'text': 'Chat', 'href': '/chat-demo/', 'icon': 'mif-comment'},
                    {'text': 'Checkbox', 'href': '/checkbox-demo/', 'icon': 'mif-checkmark'},
                    {'text': 'Chips', 'href': '/chips-demo/', 'icon': 'mif-tag'},
                    {'text': 'Cloak', 'href': '/cloak-demo/', 'icon': 'mif-eye-slash'},
                    {'text': 'Collapse', 'href': '/collapse-demo/', 'icon': 'mif-chevron-down'},
                    {'text': 'Color Picker', 'href': '/color-picker-demo/', 'icon': 'mif-palette'}
                ]
            },
            {
                'text': 'Утилиты',
                'icon': 'mif-tools',
                'dropdown': [
                    {'text': 'Clock', 'href': '/clock-demo/', 'icon': 'mif-clock'},
                    {'text': 'Adblock Detection', 'href': '/adblock-demo/', 'icon': 'mif-shield'},
                    {'text': 'Analog Clock', 'href': '/analog-clock-demo/', 'icon': 'mif-clock'},
                    {'text': 'Avatars', 'href': '/initials-avatars/', 'icon': 'mif-user'}
                ]
            },
            {'text': 'Темы', 'href': '/themes/', 'icon': 'mif-palette'}
        ],
        'app_bar_static_items': [
            {
                'ml_auto': True,
                'content': '''
                    <input data-role="input" class="small" data-prepend="<span class='mif-search'>"/>
                    <button class="small square ml-1">
                        <span class="mif-run"></span>
                    </button>
                    <button class="small ml-1">
                        Logout
                    </button>
                '''
            },
            {
                'no_hover': True,
                'content': '<input type="checkbox" data-role="theme-switcher"/>'
            }
        ]
    }
