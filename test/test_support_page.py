import json
import os

import allure
import pytest
from allure_commons._allure import feature

from constants import SUPPORT_PROJECTS_TYPES
from pages.support_pages import SupportPage

# тест с мета-тегами вынесен в main_page_test

@feature('Количество элементов в блоке')
def test_support_page_count_card_packages(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    blocks = support_page_test.get_count_elements()
    blocks.count_cards_assert("count_card_cooperation_formats", 4)


@feature('Количество элементов в блоке')
def test_support_page_count_card_benefits(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    blocks = support_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 8)

@feature('Успешная отправка заявки')
def test_support_page_add_request(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    support_page_test.click_button_tariff_table()
    popup_element_test = support_page_test.get_popup_element()
    popup_element_test.add_request_success()
    assert popup_element_test.popup_success_displayed() == True, "Окно не появилось"


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
    if d['card_type'] in SUPPORT_PROJECTS_TYPES]
# Загрузка данных из JSON-файла
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_support_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    click_element_test = support_page_test.get_project_service_element()
    page = click_element_test.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"
