import json

import allure
import pytest
from allure_commons._allure import feature, link

from pages.b2b_page import B2BPage

@feature('Количество элементов в блоке')
def test_b2b_page_platforms_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("platforms", 4)

@feature('Количество элементов в блоке')
def test_b2b_page_benefits_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)

@link(url='https://team-v5ka.testit.software/projects/664/tests/908', name='Корректно указаны title, description, canonical')
@feature('Добавление мета-тегов')
def test_main_page_add_title_descr_and_canonical(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    form_page_test = b2b_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "B2B Ecommerce Website Development Services in USA: Design Strategies for Success with Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Transform your B2B ecommerce website with Godev's expert design strategies. Our web development services create high-converting platforms for success", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/website-development/b2b/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement")
])
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    project_element = b2b_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


# Загрузка данных из JSON файла
with open('../package_card_data.json') as f:
    data = json.load(f)
filtered_data = [
    item for item in data
    if item['project_type'] in ['E-Commerce', 'Corporate', 'Online shops', 'B2B sites', 'WordPress', 'OpenCart', 'Joomla']
]
# Использование отфильтрованных данных в тестах
@pytest.mark.parametrize("project_type, experience, bullits, price",
    [(d['project_type'], d['experience'], d['bullits'], d['price']) for d in filtered_data])
def test_main_page_data_card_packages(driver, project_type, experience, bullits, price):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.check_packages_data(project_type, experience, bullits, price)