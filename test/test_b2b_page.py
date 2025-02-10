import json

import allure
import pytest

from constants import CARD_PACKAGES_TYPES, PROJECTS_TYPES
from package_data import PackageData
from pages.b2b_page import B2BPage


@allure.feature('Количество элементов в блоке')
def test_b2b_page_platforms_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("platforms", 4)

@allure.feature('Количество элементов в блоке')
def test_b2b_page_benefits_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)

@allure.link(url='https://team-v5ka.testit.software/projects/664/tests/908', name='Корректно указаны title, description, canonical')
@allure.feature('Добавление мета-тегов')
def test_main_page_add_title_descr_and_canonical(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    form_page_test = b2b_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "B2B Ecommerce Website Development Services in USA: Design Strategies for Success with Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Transform your B2B ecommerce website with Godev's expert design strategies. Our web development services create high-converting platforms for success", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/website-development/b2b/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"


try:
    with open('../service_pages_data.json') as f:
        test_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
# Фильтрация данных по card_type
filtered_data = [
    (d['card_type'], d['expected_url'], d['expected_title'])
    for d in test_data
    if d['card_type'] in PROJECTS_TYPES]
# Загрузка данных из JSON-файла
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_b2b_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    project_element = b2b_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


# Ошибка в 3 параметрах - надо проговорить с Кариной.
# Загрузка данных из json файла
try:
    with open('../package_card_data.json') as f:
        package_data_list = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
# Фильтрация данных по конкретным project_type
package_data_list = [
    PackageData(**data) for data in package_data_list
    if data['project_type'] in CARD_PACKAGES_TYPES  # Используем импортированную константу
]
@pytest.mark.parametrize("package_data", package_data_list)
def test_main_page_data_card_packages(driver, package_data):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.check_packages_data(package_data.project_type, package_data.experience, package_data.bullits, package_data.price)