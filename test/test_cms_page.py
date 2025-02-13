import json
import os

import allure
import pytest

from pages.cms_page import CMSPage
from utils.data_loader import load_service_data_review, load_package_data_cms


# тест с мета-тегами вынесен в main_page_test

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
filtered_data = load_service_data_review()
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_cms_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    project_element = cms_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


#загрузка данных из json файла
package_data_list = load_package_data_cms()
@pytest.mark.parametrize("package_data", package_data_list)
def test_cms_page_data_card_packages(driver, package_data):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.check_packages_data(package_data.project_type, package_data.experience, package_data.bullits, package_data.price)


