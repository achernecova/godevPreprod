@echo off
REM Запуск тестов (конкретный файл) и сохранение результатов
pytest test\test_blog_page.py --alluredir=allure-results > pytest_output.log 2>&1

REM Генерация отчета Allure
allure generate allure-results -o allure_report --clean >> allure_output.log 2>&1

REM Открытие отчета в браузере
allure open allure_report