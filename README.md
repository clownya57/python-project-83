### Page Analyzer
### Hexlet tests and linter status:
[![Actions Status](https://github.com/clownya57/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/clownya57/python-project-83/actions)
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=clownya57_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=clownya57_python-project-83)
Анализатор страниц — веб-приложение для анализа сайтов на SEO-пригодность.

Приложение позволяет добавлять сайты, выполнять проверку их доступности и анализировать основные SEO-элементы страницы:
заголовок страницы (title);
заголовок первого уровня (h1);
мета-описание (description);
HTTP-статус страницы.

### Demo
[Page Analyzer](https://python-project-83-izee.onrender.com/)

### Установка
Установите зависимости проекта:
make install

Подготовьте структуру базы данных:
make db-prepare

### Локальный запуск
Для запуска приложения в режиме разработки выполните:
make dev

После запуска приложение будет доступно по адресу:
http://127.0.0.1:5000

### Проверка кода
Для проверки кода с помощью Ruff выполните:
make lint
