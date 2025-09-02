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


def initials_avatars(request):
	"""Demo page for initials avatars"""
	from metroui5.components import render_initials_avatar
	import os
	from django.conf import settings
	
	# Sample names for demonstration
	sample_names = [
		"John Doe",
		"Jane Smith",
		"Robert Johnson",
		"Maria Garcia",
		"David Wilson",
		"Sarah Brown",
		"Michael Davis",
		"Lisa Miller",
		"James Taylor",
		"Jennifer Anderson"
	]
	
	# Generate avatars with different configurations
	avatars = []
	
	# Basic avatars (saved to default path)
	for name in sample_names[:5]:
		avatars.append({
			"name": name,
			"html": render_initials_avatar(name),
			"config": "Responsive avatar (all sizes generated automatically)",
			"type": "file"
		})
	
	# Different sizes
	sizes = ["small", "medium", "large", "xlarge"]
	for i, size in enumerate(sizes):
		if i < len(sample_names):
			avatars.append({
				"name": sample_names[i],
				"html": render_initials_avatar(sample_names[i], size=size),
				"config": f"Size: {size}",
				"type": "file"
			})
	
	# Different shapes
	shapes = ["circle", "square", "rounded"]
	for i, shape in enumerate(shapes):
		if i + 5 < len(sample_names):
			avatars.append({
				"name": sample_names[i + 5],
				"html": render_initials_avatar(sample_names[i + 5], shape=shape),
				"config": f"Shape: {shape}",
				"type": "file"
			})
	
	# Custom colors
	custom_colors = [
		("#e74c3c", "Red background"),
		("#3498db", "Blue background"),
		("#2ecc71", "Green background"),
		("#f39c12", "Orange background"),
		("#9b59b6", "Purple background")
	]
	
	for i, (color, desc) in enumerate(custom_colors):
		if i < len(sample_names):
			avatars.append({
				"name": sample_names[i],
				"html": render_initials_avatar(sample_names[i], bg_color=color),
				"config": desc,
				"type": "file"
			})
	
	# Multiple initials
	long_names = ["John Michael Smith", "Maria Isabella Rodriguez", "Robert James Wilson Jr"]
	for i, name in enumerate(long_names):
		avatars.append({
			"name": name,
			"html": render_initials_avatar(name, max_initials=3),
			"config": "3 initials",
			"type": "file"
		})
	
	# File-based avatars (save to disk)
	avatars_files = []
	avatars_dir = os.path.join(settings.MEDIA_ROOT, "avatars", "generated")
	os.makedirs(avatars_dir, exist_ok=True)
	
	for i, name in enumerate(sample_names[:3]):
		filename = f"avatar_{i+1}.png"
		filepath = os.path.join(avatars_dir, filename)
		
		avatars_files.append({
			"name": name,
			"html": render_initials_avatar(
				name, 
				save_path=filepath,
				output_format="png"
			),
			"config": f"Saved to file: {filename}",
			"type": "file",
			"filepath": filepath
		})
	
	# Different formats
	formats = ["png", "jpg", "webp"]
	for i, fmt in enumerate(formats):
		if i < len(sample_names):
			filename = f"avatar_{fmt}.{fmt}"
			filepath = os.path.join(avatars_dir, filename)
			
			avatars_files.append({
				"name": sample_names[i],
				"html": render_initials_avatar(
					sample_names[i], 
					save_path=filepath,
					output_format=fmt
				),
				"config": f"Format: {fmt.upper()}",
				"type": "file",
				"filepath": filepath
			})
	
	context = {
		"avatars": avatars,
		"avatars_files": avatars_files,
		"title": "Initials Avatars Demo"
	}
	
	return render(request, "demo/initials_avatars.html", context)


def advanced_inputs(request):
	"""Demo page for advanced input components."""
	context = {
		'page_title': 'Advanced Inputs - MetroUI5 Demo',
	}
	return render(request, 'demo/advanced_inputs.html', context)


def input_comparison(request):
	"""Demo page comparing simple input vs material input components."""
	context = {
		'page_title': 'Input Components Comparison - MetroUI5 Demo',
	}
	return render(request, 'demo/input_comparison.html', context)


def accordion_demo(request):
	"""Demo page for accordion components."""
	accordion_items = [
		{'title': 'Section 1', 'content': 'This is the content for section 1. It can contain any HTML content including <strong>bold text</strong> and <em>italic text</em>.'},
		{'title': 'Section 2', 'content': 'This is the content for section 2. You can include <a href="#">links</a> and other interactive elements.'},
		{'title': 'Section 3 (Initially Open)', 'content': 'This section is initially open. It demonstrates the active state functionality.', 'active': True},
		{'title': 'Section 4', 'content': 'This is section 4 with more content to demonstrate the accordion functionality.'},
		{'title': 'Section 5', 'content': 'Final section with additional content to show the full accordion behavior.'}
	]
	
	context = {
		'page_title': 'Accordion Components - MetroUI5 Demo',
		'accordion_items': accordion_items,
	}
	return render(request, 'demo/accordion_demo.html', context)


def action_button_demo(request):
	"""Demo page for action button components."""
	action_items = [
		{'icon': 'mif-home', 'href': '#', 'title': 'Home'},
		{'icon': 'mif-user', 'href': '#', 'title': 'User Profile'},
		{'icon': 'mif-cog', 'href': '#', 'title': 'Settings'},
		{'icon': 'mif-search', 'href': '#', 'title': 'Search'}
	]
	
	extended_action_items = [
		{'icon': 'mif-home', 'href': '#', 'title': 'Home'},
		{'icon': 'mif-user', 'href': '#', 'title': 'User'},
		{'icon': 'mif-cog', 'href': '#', 'title': 'Settings'},
		{'icon': 'mif-search', 'href': '#', 'title': 'Search'},
		{'icon': 'mif-mail', 'href': '#', 'title': 'Mail'},
		{'icon': 'mif-phone', 'href': '#', 'title': 'Phone'},
		{'icon': 'mif-camera', 'href': '#', 'title': 'Camera'},
		{'icon': 'mif-location', 'href': '#', 'title': 'Location'}
	]
	
	context = {
		'page_title': 'Action Button Components - MetroUI5 Demo',
		'action_items': action_items,
		'extended_action_items': extended_action_items,
	}
	return render(request, 'demo/action_button_demo.html', context)


def activity_demo(request):
	"""Demo page for activity components."""
	context = {
		'page_title': 'Activity Components - MetroUI5 Demo',
	}
	return render(request, 'demo/activity_demo.html', context)


def adblock_demo(request):
	"""Demo page for adblock detection component."""
	context = {
		'page_title': 'Adblock Detection Component - MetroUI5 Demo',
	}
	return render(request, 'demo/adblock_demo.html', context)


def analog_clock_demo(request):
	"""Demo page for analog clock component."""
	context = {
		'page_title': 'Analog Clock Component - MetroUI5 Demo',
	}
	return render(request, 'demo/analog_clock_demo.html', context)
