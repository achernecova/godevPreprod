import json

import allure
import pytest

from constants import CMS_PAGE_TYPES, PROJECTS_TYPES
from package_data import PackageData
from pages.cms_page import CMSPage

@allure.feature('Добавление мета-тегов')
def test_cms_page_add_title_descr_and_canonical(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    form_page_test = cms_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Custom CMS Development Services in USA: Company for Your Website Needs", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Unlock your website's potential with our custom CMS development services in the USA. Tailored solutions to meet your business needs, backed by years of Godev's experience", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/website-development/cms/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@allure.feature('Количество элементов в блоке')
def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 4)

@allure.feature('Количество элементов в блоке')
def test_cms_page_cms_services_cards_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("cms_services_cards", 4)

@allure.feature('Количество элементов в блоке')
def test_cms_page_cms_types_of_it_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_it", 3)

@allure.feature('Количество элементов в блоке')
def test_cms_page_platforms_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("platforms", 4)



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
    if d['card_type'] in PROJECTS_TYPES]
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_cms_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    project_element = cms_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


#Загрузка данных из json файла
try:
    with open('../package_card_data.json') as f:
        package_data_list = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
package_data_list = [
    PackageData(**data) for data in package_data_list
    if data['project_type'] in CMS_PAGE_TYPES  # Используем импортированную константу
]
# Использование отфильтрованных данных в тестах
@pytest.mark.parametrize("package_data", package_data_list)
def test_cms_page_data_card_packages(driver, package_data):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.check_packages_data(package_data.project_type, package_data.experience, package_data.bullits, package_data.price)


