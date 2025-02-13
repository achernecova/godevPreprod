import json
import os

import allure
import pytest
from allure_commons._allure import feature

from constants import PROJECTS_TYPES
from pages.project_page import ProjectPage

# тест с мета-тегами вынесен в main_page_test

#загрузка данных из json файла
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', 'service_pages_data.json')
try:
    with open(file_path, encoding='utf-8') as f:
        test_data = json.load(f)
except FileNotFoundError as e:
    raise RuntimeError('Файл service_pages_data.json не найден: ' + str(e))
except json.JSONDecodeError as e:
    raise RuntimeError('Ошибка при разборе JSON в service_pages_data.json: ' + str(e))
except Exception as e:  # Ловим все остальные ошибки
    raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
# Фильтрация данных по card_type
filtered_data = [
    (d['card_type'], d['expected_url'], d['expected_title'])
    for d in test_data
    if d['card_type'] in PROJECTS_TYPES]
@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_project_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    project_element = project_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

@feature('Количество элементов в блоке')
def test_project_page_count_card_reviews(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    blocks = project_page_test.get_count_elements()
    blocks.count_cards_assert("customer_reviews", 3)
