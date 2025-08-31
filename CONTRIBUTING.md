# Вклад в проект / Contributing

| Русский                                                                                                                    | English                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Мы приветствуем вклад в развитие django-metroui5! Этот документ содержит информацию о том, как внести свой вклад в проект. | We welcome contributions to django-metroui5! This document contains information on how to contribute to the project. |

---

## 🚀 Как начать / Getting Started

### Предварительные требования / Prerequisites

- Python 3.13+
- Django 5.2.5+
- Git

### Установка для разработки / Development Setup

| Русский                                   | English                                     |
| ----------------------------------------- | ------------------------------------------- |
| 1. Fork репозиторий                       | 1. Fork the repository                      |
| 2. Клонируйте ваш fork:                   | 2. Clone your fork:                         |
| 3. Установите пакет в режиме разработки:  | 3. Install the package in development mode: |
| 4. Установите зависимости для разработки: | 4. Install development dependencies:        |

```bash
git clone https://github.com/DevCraftClub/django-metroui5.git
cd django-metroui5
pip install -e .
pip install -e .[dev]
```

## 🧪 Тестирование / Testing

### Запуск тестов / Running Tests

| Русский                   | English                 |
| ------------------------- | ----------------------- |
| Запуск всех тестов        | Run all tests           |
| Запуск тестов с покрытием | Run tests with coverage |
| Запуск тестов Django      | Run Django tests        |

```bash
# Запуск всех тестов / Run all tests
pytest

# Запуск тестов с покрытием / Run tests with coverage
pytest --cov=metroui5

# Запуск тестов Django / Run Django tests
python manage.py test
```

### Проверка кода / Code Quality

| Русский               | English                |
| --------------------- | ---------------------- |
| Форматирование кода   | Code formatting        |
| Проверка стиля        | Style checking         |
| Проверка типов        | Type checking          |
| Проверка документации | Documentation checking |

```bash
# Форматирование кода / Code formatting
black .

# Проверка стиля / Style checking
flake8 .

# Проверка типов / Type checking
mypy .

# Проверка документации / Documentation checking
pydocstyle .
```

## 📝 Стиль кода / Code Style

### Python

| Русский                                                                 | English                                                     |
| ----------------------------------------------------------------------- | ----------------------------------------------------------- |
| - Следуйте [PEP 8](https://www.python.org/dev/peps/pep-0008/)           | - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) |
| - Используйте [Black](https://black.readthedocs.io/) для форматирования | - Use [Black](https://black.readthedocs.io/) for formatting |
| - Добавляйте type hints для всех функций                                | - Add type hints for all functions                          |
| - Пишите docstrings на русском языке                                    | - Write docstrings in Russian                               |
| - Максимальная длина строки: 88 символов                                | - Maximum line length: 88 characters                        |

### Django

| Русский                                                                                                                      | English                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| - Следуйте [Django coding style](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/) | - Follow [Django coding style](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/) |
| - Используйте Django best practices                                                                                          | - Use Django best practices                                                                                                |
| - Добавляйте тесты для новой функциональности                                                                                | - Add tests for new functionality                                                                                          |

### Template Tags

| Русский                                          | English                                   |
| ------------------------------------------------ | ----------------------------------------- |
| - Следуйте соглашениям Django template tags      | - Follow Django template tag conventions  |
| - Добавляйте документацию для всех template tags | - Add documentation for all template tags |
| - Включайте примеры использования                | - Include usage examples                  |

## 🔧 Процесс разработки / Development Process

### 1. Создание ветки / Create a Branch

| Русский                                   | English                       |
| ----------------------------------------- | ----------------------------- |
| Создание ветки для новой функциональности | Create branch for new feature |
| Создание ветки для исправления ошибки     | Create branch for bug fix     |

```bash
git checkout -b feature/amazing-feature
# или / or
git checkout -b fix/bug-description
```

### 2. Внесение изменений / Make Changes

| Русский                                            | English                                 |
| -------------------------------------------------- | --------------------------------------- |
| - Делайте небольшие, логически связанные изменения | - Make small, logically related changes |
| - Пишите понятные commit сообщения                 | - Write clear commit messages           |
| - Добавляйте тесты для новой функциональности      | - Add tests for new functionality       |

### 3. Commit сообщения / Commit Messages

| Русский                       | English                   |
| ----------------------------- | ------------------------- |
| Используйте следующий формат: | Use the following format: |

```
type(scope): краткое описание / brief description

Подробное описание изменений / Detailed description of changes

Closes #123
```

| Русский                            | English                         |
| ---------------------------------- | ------------------------------- |
| **Типы:**                          | **Types:**                      |
| - `feat`: новая функциональность   | - `feat`: new functionality     |
| - `fix`: исправление ошибки        | - `fix`: bug fix                |
| - `docs`: изменения в документации | - `docs`: documentation changes |
| - `style`: форматирование кода     | - `style`: code formatting      |
| - `refactor`: рефакторинг кода     | - `refactor`: code refactoring  |
| - `test`: добавление тестов        | - `test`: adding tests          |
| - `chore`: обновление зависимостей | - `chore`: dependency updates   |

### 4. Тестирование / Testing

| Русский                            | English                              |
| ---------------------------------- | ------------------------------------ |
| Перед отправкой PR убедитесь, что: | Before submitting a PR, ensure that: |
| - Все тесты проходят               | - All tests pass                     |
| - Код соответствует стандартам     | - Code meets standards               |
| - Документация обновлена           | - Documentation is updated           |
| - Примеры работают корректно       | - Examples work correctly            |

### 5. Pull Request

| Русский                                | English                           |
| -------------------------------------- | --------------------------------- |
| 1. Обновите CHANGELOG.md               | 1. Update CHANGELOG.md            |
| 2. Добавьте описание изменений         | 2. Add description of changes     |
| 3. Укажите связанные issues            | 3. Reference related issues       |
| 4. Добавьте скриншоты для UI изменений | 4. Add screenshots for UI changes |

## 📚 Документация / Documentation

### Обновление документации / Updating Documentation

| Русский                                                      | English                                          |
| ------------------------------------------------------------ | ------------------------------------------------ |
| - Обновляйте README.md при добавлении новой функциональности | - Update README.md when adding new functionality |
| - Добавляйте примеры использования                           | - Add usage examples                             |
| - Обновляйте docstrings в коде                               | - Update docstrings in code                      |

### Создание документации / Building Documentation

| Русский                                 | English                            |
| --------------------------------------- | ---------------------------------- |
| Установка зависимостей для документации | Install documentation dependencies |
| Сборка документации                     | Build documentation                |

```bash
# Установка зависимостей для документации / Install documentation dependencies
pip install -e .[docs]

# Сборка документации / Build documentation
cd docs
make html
```

## 🐛 Отчеты об ошибках / Bug Reports

### Создание issue / Creating an Issue

| Русский                      | English                                 |
| ---------------------------- | --------------------------------------- |
| При создании issue укажите:  | When creating an issue, please include: |
| - Версию Django              | - Django version                        |
| - Версию Python              | - Python version                        |
| - Описание проблемы          | - Problem description                   |
| - Шаги для воспроизведения   | - Steps to reproduce                    |
| - Ожидаемое поведение        | - Expected behavior                     |
| - Фактическое поведение      | - Actual behavior                       |
| - Скриншоты (если применимо) | - Screenshots (if applicable)           |

## 💡 Предложения по улучшению / Feature Requests

| Русский                                                                 | English                                                       |
| ----------------------------------------------------------------------- | ------------------------------------------------------------- |
| Мы приветствуем предложения по улучшению! При создании feature request: | We welcome feature requests! When creating a feature request: |
| - Опишите предлагаемую функциональность                                 | - Describe the proposed functionality                         |
| - Объясните, почему это полезно                                         | - Explain why it's useful                                     |
| - Предложите способ реализации                                          | - Suggest implementation approach                             |
| - Добавьте примеры использования                                        | - Add usage examples                                          |

## 🤝 Получение помощи / Getting Help

| Русский                        | English                              |
| ------------------------------ | ------------------------------------ |
| Если у вас есть вопросы:       | If you have questions:               |
| - Создайте issue с вопросом    | - Create an issue with your question |
| - Обратитесь к документации    | - Check the documentation            |
| - Присоединитесь к обсуждениям | - Join discussions                   |

## 📄 Лицензия / License

| Русский                                                                                              | English                                                                                                     |
| ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Внося вклад в проект, вы соглашаетесь с тем, что ваш вклад будет распространяться под лицензией MIT. | By contributing to the project, you agree that your contribution will be distributed under the MIT license. |

## 🙏 Благодарности / Acknowledgments

| Русский                                                    | English                                                |
| ---------------------------------------------------------- | ------------------------------------------------------ |
| Спасибо всем, кто вносит вклад в развитие django-metroui5! | Thanks to everyone who contributes to django-metroui5! |

---

**Спасибо за ваш вклад! / Thank you for your contribution!** 🎉
