import json
import os

import allure
import pytest

from constants import PROJECTS_TYPES_FRAMEWORK
from pages.framework_page import FrameworkPage

# тест с мета-тегами вынесен в main_page_test

@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_reviews(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("advantages_cards_tiles_count", 5)

@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_advantages_outsourcing(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("advantages_outsourcing", 5)

@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_advant_card(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("benefits", 5)

@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_best_web_frameworks(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("best_web_frameworks", 5)

@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_why_choose_godev(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("why_choose_godev", 5)

@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_back_end_frameworks(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("back_end_frameworks", 5)

#Загрузка данных из json файла
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
    if d['card_type'] in PROJECTS_TYPES_FRAMEWORK]
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_e_com_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    project_element = framework_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@pytest.mark.parametrize("index, price_left_title, price_left_text, price_right_title, price_right_text", [
    (1 , "Hours per month", "up to 30", "Price", "30 $"),
    (2 , "Hours per month", "from 30 to 100", "Price", "27 $"),
    (3 , "Hours per month", "from 100 to 150", "Price", "25 $"),
    (4, "Hours per month", "from 150", "Price", "22 $"),
])
def test_framework_page_table_data_assert(driver, index, price_left_title, price_left_text, price_right_title, price_right_text):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_block_price(index, price_left_title, price_left_text, price_right_title, price_right_text)