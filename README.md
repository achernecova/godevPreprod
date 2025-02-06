
# Autotests GoDev
Разработка автотестов для сайта godev. 

Запуск автотестов: python -m pytest
Запуск автотестов с генерацией аллюр отчетов: python -m pytest --alluredir=allure-results
и далее  allure serve allure-results

---
## Технологии и интеграции
Python — основной язык программирования.
PyTest — фреймворк для написания тестов.
Selenium — фреймворк для автоматизации веб-тестирования.
Allure — система для генерации отчетов.
TestIT — платформа для управления тестированием и анализом результатов.
Jira — инструмент управления проектами и отслеживания задач.
---

## Подход к оформлению: 
1. название файлов через нижнее подчеркивание
2. название пакетов в нижнем регистре
3. названия классов - используется CamelCase 
4. названия переменных через нижнее подчеркивание в нижнем регистре

---
## Жизненный цикл теста
1. Инициализация конфигурации
2. Запуск браузера
3. Выполнение тестовых шагов
4. Сбор артефактов
5. Генерация отчета
---

##  Архитектура проекта

### Компоненты:
- **conftest.py** - централизованная конфигурация
- **base_page** - базовый класс с основными методами
- **page_elements** - паттерн для работы с элементами страниц
- **pages** - паттерн для работы со страницами
- **test** - папка с тестами на созданные страницы

## Поиск элементов

1. Уникальные HTML-атрибуты (`id`, `name`)
2. Семантические CSS-селекторы (`input[type="email"]`)
3. Иерархические цепочки (`div.modal > button.confirm`)
4. XPath только для динамического контента

**Запрещено:**
    - Использовать жесткую индексацию 
    - Использовать жесткую иерархическую цепочку
    - Текст на языке интерфейса 

