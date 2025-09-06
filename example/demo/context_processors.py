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
                    {
                        'text': 'Layout & Structure',
                        'icon': 'mif-layout',
                        'dropdown': [
                            {'text': 'App Bar', 'href': '/app-bar-demo/', 'icon': 'mif-menu'},
                            {'text': 'Container', 'href': '/container-demo/', 'icon': 'mif-layout'},
                            {'text': 'Box', 'href': '/box-demo/', 'icon': 'mif-folder'},
                            {'text': 'Breadcrumb', 'href': '/breadcrumb-demo/', 'icon': 'mif-arrow-right'}
                        ]
                    },
                    {
                        'text': 'Navigation & Menus',
                        'icon': 'mif-list',
                        'dropdown': [
                            {'text': 'Accordion', 'href': '/accordion-demo/', 'icon': 'mif-list'},
                            {'text': 'Catalog Menu', 'href': '/catalog-menu-demo/', 'icon': 'mif-list'},
                            {'text': 'Collapse', 'href': '/collapse-demo/', 'icon': 'mif-chevron-down'},
                            {'text': 'Drop Menu', 'href': '/drop-menu-demo/', 'icon': 'mif-menu'},
                            {'text': 'Dropdown', 'href': '/dropdown-demo/', 'icon': 'mif-chevron-down'},
                            {'text': 'Dropdown Button', 'href': '/dropdown-button-demo/', 'icon': 'mif-play'}
                        ]
                    },
                    {
                        'text': 'Buttons & Actions',
                        'icon': 'mif-play',
                        'dropdown': [
                            {'text': 'Button', 'href': '/button-demo/', 'icon': 'mif-play'},
                            {'text': 'Action Button', 'href': '/action-button-demo/', 'icon': 'mif-plus'},
                            {'text': 'Command Button', 'href': '/command-button-demo/', 'icon': 'mif-cursor'},
                            {'text': 'Button Group', 'href': '/button-group-demo/', 'icon': 'mif-menu'}
                        ]
                    },
                    {
                        'text': 'Forms & Inputs',
                        'icon': 'mif-checkmark',
                        'dropdown': [
                            {'text': 'Checkbox', 'href': '/checkbox-demo/', 'icon': 'mif-checkmark'},
                            {'text': 'Custom Checkbox', 'href': '/custom-checkbox-demo/', 'icon': 'mif-checkmark'},
                            {'text': 'Cutter', 'href': '/cutter-demo/', 'icon': 'mif-scissors'},
                            {'text': 'D-Menu', 'href': '/d-menu-demo/', 'icon': 'mif-menu'},
                            {'text': 'Double Select Box', 'href': '/double-select-box-demo/', 'icon': 'mif-list'},
                            {'text': 'Double Slider', 'href': '/double-slider-demo/', 'icon': 'mif-equalizer'},
                            {'text': 'Color Picker', 'href': '/color-picker-demo/', 'icon': 'mif-palette'},
                            {'text': 'Color Selector', 'href': '/color-selector-demo/', 'icon': 'mif-palette'}
                        ]
                    },
                    {
                        'text': 'Data Display',
                        'icon': 'mif-chart',
                        'dropdown': [
                            {'text': 'Badge', 'href': '/badge-demo/', 'icon': 'mif-bookmark'},
                            {'text': 'Card', 'href': '/card-demo/', 'icon': 'mif-credit-card'},
                            {'text': 'Chart Card', 'href': '/chart-card-demo/', 'icon': 'mif-chart'},
                            {'text': 'Bar3d', 'href': '/bar3d-demo/', 'icon': 'mif-chart'},
                            {'text': 'Counter', 'href': '/counter-demo/', 'icon': 'mif-plus'},
                            {'text': 'Cube', 'href': '/cube-demo/', 'icon': 'mif-cube'},
                            {'text': 'Donut', 'href': '/donut-demo/', 'icon': 'mif-chart'}
                        ]
                    },
                    {
                        'text': 'Media & Content',
                        'icon': 'mif-music-note',
                        'dropdown': [
                            {'text': 'Audio Button', 'href': '/audio-button-demo/', 'icon': 'mif-volume-high'},
                            {'text': 'Audio Player', 'href': '/audio-player-demo/', 'icon': 'mif-music-note'},
                            {'text': 'Carousel', 'href': '/carousel-demo/', 'icon': 'mif-images'}
                        ]
                    },
                    {
                        'text': 'Communication',
                        'icon': 'mif-comment',
                        'dropdown': [
                            {'text': 'Chat', 'href': '/chat-demo/', 'icon': 'mif-comment'},
                            {'text': 'Activity', 'href': '/activity-demo/', 'icon': 'mif-spinner'}
                        ]
                    },
                    {
                        'text': 'Interactive Elements',
                        'icon': 'mif-apps',
                        'dropdown': [
                            {'text': 'Chips', 'href': '/chips-demo/', 'icon': 'mif-tag'},
                            {'text': 'Charms', 'href': '/charms-demo/', 'icon': 'mif-apps'},
                            {'text': 'Bulls', 'href': '/bulls-demo/', 'icon': 'mif-checkmark'},
                            {'text': 'Drag Items', 'href': '/drag-items-demo/', 'icon': 'mif-move'},
                            {'text': 'Draggable', 'href': '/draggable-demo/', 'icon': 'mif-drag'}
                        ]
                    },
                    {
                        'text': 'Utility Components',
                        'icon': 'mif-tools',
                        'dropdown': [
                            {'text': 'Cloak', 'href': '/cloak-demo/', 'icon': 'mif-eye-slash'}
                        ]
                    },
                    {
                        'text': 'Calendar & Time',
                        'icon': 'mif-calendar',
                        'dropdown': [
                            {'text': 'Calendar', 'href': '/calendar-demo/', 'icon': 'mif-calendar'},
                            {'text': 'Calendar Picker', 'href': '/calendar-picker-demo/', 'icon': 'mif-calendar'},
                            {'text': 'Date Picker', 'href': '/date-picker-demo/', 'icon': 'mif-calendar'}
                        ]
                    },
                    {
                        'text': 'Modals & Dialogs',
                        'icon': 'mif-window',
                        'dropdown': [
                            {'text': 'Dialog', 'href': '/dialog-demo/', 'icon': 'mif-window'},
                            {'text': 'Modal', 'href': '/modal-demo/', 'icon': 'mif-window'}
                        ]
                    },
                    {
                        'text': 'Content & Information',
                        'icon': 'mif-info',
                        'dropdown': [
                            {'text': 'Directive', 'href': '/directive-demo/', 'icon': 'mif-info'},
                            {'text': 'Alert', 'href': '/alert-demo/', 'icon': 'mif-warning'}
                        ]
                    }
                ]
            },
            {
                'text': 'Утилиты',
                'icon': 'mif-tools',
                'dropdown': [
                    {
                        'text': 'Time & Clocks',
                        'icon': 'mif-clock',
                        'dropdown': [
                            {'text': 'Clock', 'href': '/clock-demo/', 'icon': 'mif-clock'},
                            {'text': 'Analog Clock', 'href': '/analog-clock-demo/', 'icon': 'mif-clock'}
                        ]
                    },
                    {
                        'text': 'Security & Detection',
                        'icon': 'mif-shield',
                        'dropdown': [
                            {'text': 'Adblock Detection', 'href': '/adblock-demo/', 'icon': 'mif-shield'}
                        ]
                    },
                    {
                        'text': 'User & Identity',
                        'icon': 'mif-user',
                        'dropdown': [
                            {'text': 'Avatars', 'href': '/initials-avatars/', 'icon': 'mif-user'}
                        ]
                    }
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
