# MetroUI5 Django Documentation

Добро пожаловать в документацию MetroUI5 Django - пакета для интеграции MetroUI 5 с Django.

## Содержание

### 🚀 [Начало работы](getting-started/)

- [Быстрый старт](getting-started/quick-start.md) ✅
- [Установка](getting-started/installation.md) ✅
- [Базовое использование](getting-started/basic-usage.md) ✅
- [Примеры](getting-started/examples.md) ✅

### 🧩 [Компоненты](components/)

- [Алерты](components/alerts.md) ✅
- [Кнопки](components/buttons.md) ✅
- [Карточки](components/cards.md) ✅
- [Плитки](components/tiles.md) ✅
- [Формы](components/forms.md) ✅
- [Таблицы](components/tables.md) ✅
- [Навигация](components/navigation.md) ✅
- [Модальные окна](components/modals.md) ✅
- [Панели](components/panels.md) ✅
- [Прогресс-бары](components/progress.md) ✅
- [Аккордеоны](components/accordions.md) ✅
- [Календари](components/calendars.md) ✅
- [Диалоги](components/dialogs.md) ✅
- [Выпадающие списки](components/dropdowns.md) ✅
- [Поля ввода](components/inputs.md) ✅
- [Списки](components/lists.md) ✅
- [Меню](components/menus.md) ✅
- [Боковые панели](components/sidebars.md) ✅
- [Вкладки](components/tabs.md) ✅
- [Панели инструментов](components/toolbars.md) ✅
- [Хлебные крошки](components/breadcrumbs.md) ✅
- [Пагинация](components/pagination.md) ✅
- [Бейджи](components/badges.md) ✅
- [Аватары](components/avatars.md) ✅
- [Рейтинги](components/ratings.md) ✅
- [Иконки](components/icons.md) ✅

### 📚 [API Справочник](api-reference/)

- [Основные функции](api-reference/core.md) ✅
- [HTML утилиты](api-reference/html.md) ✅
- [CSS утилиты](api-reference/css.md) ✅
- [Рендереры](api-reference/renderers.md) ✅
- [Формы](api-reference/forms.md) ✅
- [Компоненты](api-reference/components.md) ✅
- [Шаблонные теги](api-reference/templatetags.md) ✅

## О MetroUI5

MetroUI5 Django - это пакет, который предоставляет удобные функции для создания современных веб-интерфейсов с
использованием MetroUI 5.1.17 в Django проектах. Пакет включает в себя:

- Готовые компоненты для быстрого создания UI
- Утилиты для работы с HTML, CSS и JavaScript
- Систему рендеринга форм
- Шаблонные теги для Django
- Поддержку CDN и локальных файлов

### CDN поддержка

Пакет поддерживает официальный CDN MetroUI5 с возможностью перезаписи URL:

- **JavaScript**: `https://cdn.metroui.org.ua/current/metro.js`
- **CSS**: `https://cdn.metroui.org.ua/current/metro.css`
- **Иконки**: `https://cdn.metroui.org.ua/current/icons.css`

Пользователи могут:

- Включить CDN режим через `USE_CDN: True`
- Перезаписать CDN URL через `cdn_js_url`, `cdn_css_url`, `cdn_icons_url`
- Использовать дефолтные CDN URL если перезапись не указана

## Требования

- Python 3.8+
- Django 3.2+
- MetroUI 5.1.17+

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](../LICENSE) для получения дополнительной информации.

## Статус документации

- ✅ **Завершено**: Полностью документировано с примерами и лучшими практиками
- ⏳ **В ожидании**: Документация должна быть создана

### Недавние дополнения

**🎉 Полная библиотека компонентов**: Все 25 компонентов MetroUI5 теперь полностью документированы!

**Последние добавленные компоненты:**

- **Иконки** - Система иконок MetroUI с поддержкой размеров и стилей
- **Аккордеоны** - Сворачиваемые секции контента с различными типами
- **Календари** - Интерактивные виджеты календаря с событиями
- **Диалоги** - Модальные диалоги и всплывающие окна
- **Выпадающие списки** - Меню выбора с различными опциями
- **Меню** - Навигационные и контекстные меню

**API Справочник:**

- **Рендереры** - Низкоуровневые утилиты рендеринга и базовые классы
- **Компоненты** - Полный справочник по всем 25 функциям рендеринга компонентов
- **CSS Утилиты** - Полная система управления CSS классами
- **Формы** - Комплексная система рендеринга форм

**Начало работы:**

- Все основные руководства по началу работы теперь доступны на русском языке

Все новые документы включают:

- Базовые примеры использования
- Продвинутые паттерны использования
- Интеграцию с JavaScript
- Лучшие практики
- Связанные компоненты
