import json

import allure
import pytest
from allure_commons._allure import feature

from constants import ECOM_PAGE_TYPES, PROJECTS_TYPES, PROJECTS_TYPES_ECOM
from pages.e_com_page import EComPage

@allure.feature('Добавление мета-тегов')
def test_e_com_page_add_title_descr_and_canonical(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    form_page_test = e_com_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Ecommerce Website Development Company in USA: Expert Web Design & Solutions", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Transform your online business with our ecommerce website development company in the USA. Godev offer expert web design and solutions for high-converting sites", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/website-development/e-commerce/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@feature('Количество элементов в блоке')
def test_e_com_page_benefits_count_cards_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    blocks = e_com_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)

@allure.feature('Количество элементов в блоке')
def test_e_com_page_how_we_make_web_count_cards_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    blocks = e_com_page_test.get_count_elements()
    blocks.count_cards_assert("how_we_make_web", 5)

@allure.feature('Количество элементов в блоке')
def test_e_com_page_our_proven_web_dev_count_cards_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    blocks = e_com_page_test.get_count_elements()
    blocks.count_cards_assert("our_proven_web_dev", 7)


#Загрузка данных из json файла
try:
    with open('../package_card_data.json') as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
filtered_data = [
    item for item in data
    if item['project_type'] in ECOM_PAGE_TYPES
]
# Использование отфильтрованных данных в тестах
@pytest.mark.parametrize("project_type, bullits, price",
    [(d['project_type'], d['bullits'], d['price']) for d in filtered_data])
def test_ecom_page_data_card_packages(driver, project_type, bullits, price):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    e_com_page_test.check_packages_data_not_experience(project_type, bullits, price)


# Загрузка данных из JSON-файла
try:
    with open('../service_pages_data.json') as f:
        test_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
# Фильтрация данных по card_type
filtered_data = [
    (d['card_type'], d['expected_url'], d['expected_title'])
    for d in test_data
    if d['card_type'] in PROJECTS_TYPES_ECOM]
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_e_com_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    project_element = e_com_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"
