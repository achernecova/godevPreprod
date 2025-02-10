@echo off
REM Запуск тестов и сохранение результатов
pytest --alluredir=allure_results

REM Генерация отчета Allure
allure generate allure_results -o allure_report --clean

REM Открытие отчета в браузере
allure open allure_report