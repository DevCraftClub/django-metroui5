"""
Demo views для демонстрации MetroUI5.
"""

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ContactForm, UserProfileForm


def index(request):
    """Главная страница с обзором возможностей MetroUI5."""
    context = {
        'page_title': 'Django MetroUI5 - Главная',
    }
    return render(request, 'demo/index.html', context)


def forms_demo(request):
    """Демонстрация рендеринга форм с MetroUI."""
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if contact_form.is_valid():
            messages.success(request, 'Форма контактов успешно отправлена!')
            contact_form = ContactForm()  # Reset form
            # Сбрасываем форму
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            
        if profile_form.is_valid():
            messages.success(request, 'Профиль пользователя успешно обновлен!')
            profile_form = UserProfileForm()  # Reset form
            # Сбрасываем форму
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме профиля.')
    else:
        contact_form = ContactForm()
        profile_form = UserProfileForm()
    
    context = {
        'page_title': 'Демонстрация форм',
        'contact_form': contact_form,
        'profile_form': profile_form,
    }
    return render(request, 'demo/forms.html', context)


def components_demo(request):
    """Демонстрация основных компонентов MetroUI."""
    context = {
        'page_title': 'Демонстрация компонентов',
    }
    return render(request, 'demo/components.html', context)


def tiles_demo(request):
    """Демонстрация MetroUI tiles."""
    context = {
        'page_title': 'Демонстрация Tiles',
    }
    return render(request, 'demo/tiles.html', context)


def advanced_components_demo(request):
    """Демонстрация расширенных компонентов MetroUI."""
    # Data for accordion
    # Данные для accordion
    accordion_items = [
        {
            'title': 'Основы MetroUI',
            'content': 'MetroUI - это современный CSS фреймворк для создания адаптивных веб-приложений с красивым дизайном.'
        },
        {
            'title': 'Компоненты',
            'content': 'Фреймворк включает более 150 готовых компонентов: кнопки, формы, таблицы, навигация и многое другое.'
        },
        {
            'title': 'Адаптивность',
            'content': 'Все компоненты автоматически адаптируются под различные размеры экранов и устройств.'
        },
        {
            'title': 'Кастомизация',
            'content': 'Легко настраивайте цвета, размеры и стили компонентов под ваши потребности.'
        }
    ]


def themes_demo(request):
    """Демонстрация тем MetroUI 5."""
    context = {
        'page_title': 'Демонстрация тем',
    }
    return render(request, 'demo/themes.html', context)
    
    # Data for tabs
    # Данные для tabs
    tabs_data = [
        {
            'title': 'Описание',
            'content': 'MetroUI предоставляет богатый набор UI компонентов для создания современных веб-приложений.'
        },
        {
            'title': 'Возможности',
            'content': 'Поддержка всех современных браузеров, адаптивный дизайн, легкая кастомизация.'
        },
        {
            'title': 'Документация',
            'content': 'Подробная документация с примерами использования каждого компонента.'
        },
        {
            'title': 'Поддержка',
            'content': 'Активное сообщество разработчиков и регулярные обновления.'
        }
    ]
    
    # Data for table
    # Данные для таблицы
    table_headers = ['Компонент', 'Описание', 'Статус', 'Версия']
    table_rows = [
        ['Button', 'Кнопки различных стилей и размеров', 'Готов', '5.1.17'],
        ['Form', 'Стилизованные формы', 'Готов', '5.1.17'],
        ['Table', 'Таблицы с сортировкой', 'Готов', '5.1.17'],
        ['Navigation', 'Навигационные элементы', 'Готов', '5.1.17'],
        ['Modal', 'Модальные окна', 'Готов', '5.1.17'],
        ['Tabs', 'Вкладки', 'Готов', '5.1.17']
    ]
    
    # Data for navigation
    # Данные для навигации
    navigation_items = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'О проекте', 'url': '/about/'},
        {'text': 'Документация', 'url': '/docs/'},
        {'text': 'Примеры', 'url': '/examples/'},
        {'text': 'Контакты', 'url': '/contact/'}
    ]
    
    # Data for sidebar
    # Данные для sidebar
    sidebar_items = [
        {'text': 'Дашборд', 'url': '/dashboard/'},
        {'text': 'Пользователи', 'url': '/users/'},
        {'text': 'Настройки', 'url': '/settings/'},
        {'text': 'Статистика', 'url': '/stats/'},
        {'text': 'Уведомления', 'url': '/notifications/'}
    ]
    
    # Data for dropdown
    # Данные для dropdown
    dropdown_items = [
        {'text': 'Опция 1', 'url': '/option1/'},
        {'text': 'Опция 2', 'url': '/option2/'},
        {'text': 'Опция 3', 'url': '/option3/'}
    ]
    
    action_items = [
        {'text': 'Редактировать', 'url': '/edit/', 'type': 'button', 'button_attrs': {'button_type': 'primary'}},
        {'text': 'Удалить', 'url': '/delete/', 'type': 'button', 'button_attrs': {'button_type': 'danger'}},
        {'text': 'Просмотр', 'url': '/view/', 'type': 'button', 'button_attrs': {'button_type': 'secondary'}}
    ]
    
    # Data for lists
    # Данные для списков
    list_items = [
        {'text': 'Элемент списка 1', 'url': '/item1/'},
        {'text': 'Элемент списка 2', 'url': '/item2/'},
        {'text': 'Элемент списка 3', 'url': '/item3/'},
        {'text': 'Элемент списка 4', 'url': '/item4/'}
    ]
    
    # Data for menu
    # Данные для меню
    menu_items = [
        {'text': 'Файл', 'url': '/file/'},
        {'text': 'Правка', 'url': '/edit/'},
        {'text': 'Вид', 'url': '/view/'},
        {'text': 'Справка', 'url': '/help/'}
    ]
    
    # Data for toolbar
    # Данные для toolbar
    toolbar_items = [
        {'text': 'Создать', 'type': 'button', 'button_attrs': {'button_type': 'primary'}},
        {'text': 'Открыть', 'type': 'button', 'button_attrs': {'button_type': 'secondary'}},
        {'text': 'Сохранить', 'type': 'button', 'button_attrs': {'button_type': 'success'}},
        {'text': 'Печать', 'type': 'button', 'button_attrs': {'button_type': 'info'}}
    ]
    
    # Data for breadcrumb
    # Данные для breadcrumb
    breadcrumb_items = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Документация', 'url': '/docs/'},
        {'text': 'Компоненты', 'url': '/docs/components/'},
        {'text': 'Расширенные', 'url': '/docs/components/advanced/'}
    ]
    
    # Data for stepper
    # Данные для stepper
    stepper_steps = ['Шаг 1', 'Шаг 2', 'Шаг 3', 'Шаг 4']
    
    # Data for wizard
    # Данные для wizard
    wizard_steps = [
        {'title': 'Настройка', 'content': 'Настройте основные параметры проекта'},
        {'title': 'Конфигурация', 'content': 'Выберите дополнительные опции'},
        {'title': 'Проверка', 'content': 'Проверьте все настройки'},
        {'title': 'Завершение', 'content': 'Проект успешно создан!'}
    ]
    
    # Data for tree
    # Данные для tree
    tree_items = [
        {
            'text': 'Проект A',
            'children': [
                {'text': 'Модуль 1', 'children': [{'text': 'Функция 1'}, {'text': 'Функция 2'}]},
                {'text': 'Модуль 2', 'children': [{'text': 'Функция 3'}]}
            ]
        },
        {
            'text': 'Проект B',
            'children': [
                {'text': 'Модуль 1'},
                {'text': 'Модуль 2'}
            ]
        }
    ]
    
    context = {
        'page_title': 'Расширенные компоненты',
        'accordion_items': accordion_items,
        'tabs_data': tabs_data,
        'table_headers': table_headers,
        'table_rows': table_rows,
        'navigation_items': navigation_items,
        'sidebar_items': sidebar_items,
        'dropdown_items': dropdown_items,
        'action_items': action_items,
        'list_items': list_items,
        'menu_items': menu_items,
        'toolbar_items': toolbar_items,
        'breadcrumb_items': breadcrumb_items,
        'stepper_steps': stepper_steps,
        'wizard_steps': wizard_steps,
        'tree_items': tree_items,
    }
    return render(request, 'demo/advanced_components.html', context)
