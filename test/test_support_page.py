import json

import allure
import pytest
from allure_commons._allure import feature

from constants import PROJECTS_TYPES_ECOM, SUPPORT_PROJECTS_TYPES
from pages.support_pages import SupportPage

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

@feature('Добавление мета-тегов')
def test_support_page_add_title_descr_and_canonical(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    form_page_test = support_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "IT maintenance and support services in USA", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Discover top-notch IT maintenance and support services in the USA, ensuring your software and applications run smoothly with timely updates and expert assistance Godev", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/tech-support/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@feature('Успешная отправка заявки')
def test_support_page_add_request(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    support_page_test.click_button_tariff_table()
    popup_element_test = support_page_test.get_popup_element()
    popup_element_test.add_request_success()
    assert popup_element_test.popup_success_displayed() == True, "Окно не появилось"

try:
    with open('../service_pages_data.json') as f:
        test_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
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


