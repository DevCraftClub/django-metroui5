# Security Policy

## Supported Versions

Security fixes go into the current line of the package. Older lines are not maintained.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

Django versions that `django-metroui5` can run on are listed in `pyproject.toml` and the README. That matrix is about compatibility, not about security support for this package.

## Reporting a Vulnerability

Do **not** open a public GitHub issue or pull request about a security problem. That would publish the details before a fix is ready.

Prefer a private report:

1. [GitHub Security Advisories](https://github.com/DevCraftClub/django-metroui5/security/advisories/new) for this repository, or
2. contact the maintainer: [Maxim Harder](https://github.com/MaximHarder)
3. or create an issue

Include what is affected, how to reproduce it, and what impact you expect (for example: HTML injection in a template tag, unsafe URL handling, secret leakage).

You should get a first reply within a few working days. If the report is accepted, we will work on a fix for a supported version and credit you if you want that. If it is declined, we will say why (for example: not reproducible, out of scope, or already fixed).

Ordinary bugs that are not security issues belong in [GitHub Issues](https://github.com/DevCraftClub/django-metroui5/issues) with the bug report form.

---

# Политика безопасности

## Поддерживаемые версии

Исправления по безопасности выходят в текущей линейке пакета. Старые линейки не сопровождаем.

| Версия | Поддержка          |
| ------ | ------------------ |
| 0.1.x  | :white_check_mark: |
| < 0.1  | :x:                |

Версии Django, с которыми пакет умеет работать, описаны в `pyproject.toml` и в README. Это про совместимость, а не про срок поддержки безопасности самого пакета.

## Как сообщить об уязвимости

**Не** открывайте публичную задачу или запрос на слияние с описанием уязвимости — так сведения станут открытыми до исправления.

Пишите по закрытому каналу:

1. [закрытое сообщение на GitHub](https://github.com/DevCraftClub/django-metroui5/security/advisories/new), или
2. письмо сопровождающему: [dev@devcraft.club](mailto:dev@devcraft.club)

Укажите, что затронуто, как повторить и какой вред возможен (например: подстановка HTML в теге шаблона, небезопасная обработка адреса, утечка секрета).

Первый ответ обычно приходит в течение нескольких рабочих дней. Если сообщение принято — готовим исправление для поддерживаемой версии и укажем авторство, если вы этого хотите. Если отклонено — напишем причину (не воспроизводится, вне зоны ответственности пакета, уже исправлено и т.п.).

Обычные ошибки без угрозы безопасности — через [Issues](https://github.com/DevCraftClub/django-metroui5/issues) и форму сообщения об ошибке.
