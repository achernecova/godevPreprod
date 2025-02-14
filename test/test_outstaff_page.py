import json
import os

import pytest
from allure_commons._allure import feature

from constants import OUTSTAFF_PROJECT_TYPES
from pages.web_outstaff_page import WebOutstaffPage
from utils.data_loader import load_package_data_outstaff


# тест с мета-тегами вынесен в main_page_test

@feature('Успешная отправка заявки')
def test_web_outstaff_add_success_request(driver):
    web_outstaff_page_test = WebOutstaffPage(driver)
    web_outstaff_page_test.open()
    web_outstaff_page_test.click_button_outsource()
    form_page_test = web_outstaff_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, "Окно не появилось"

@feature('Количество элементов в блоке')
@pytest.mark.parametrize("project_type, count", [
    ("benefits", 6),
    ("types_of_it", 3),
    ("what_to_choose", 3)
])
def test_main_page_benefits_types_of_it_what_to_choose_count_cards(driver, project_type, count):
    main_page_test = WebOutstaffPage(driver)
    main_page_test.open()
    blocks = main_page_test.get_count_elements()
    blocks.count_cards_assert(project_type, count)


# Использование отфильтрованных данных в тестах
filtered_data = load_package_data_outstaff()
@pytest.mark.parametrize("project_type, experience, bullits, price",
    [(d['project_type'], d['experience'], d['bullits'], d['price']) for d in filtered_data])
def test_outstaff_page_data_card_packages(driver, project_type, experience, bullits, price):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.check_packages_data(project_type, experience, bullits, price)


