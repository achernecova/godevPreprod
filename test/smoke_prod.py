

import allure
import pytest
from allure_commons._allure import feature, link

from pages.cms_page import CMSPage
from pages.e_com_page import EComPage
from pages.main_page import MainPage
from pages.web_outstaff_page import WebOutstaffPage
from utils.data_loader import load_package_data_outstaff, load_package_data_e_com, load_file
from utils.page_factory import get_page_instance


@feature('Успешная отправка заявки')
def test_main_page_add_request_header(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    popup_element_test = main_page_test.get_popup_element()
    popup_element_test.add_request_success()
    assert popup_element_test.popup_success_displayed() == True, "Окно не появилось"


@link(url='https://team-v5ka.testit.software/projects/664/tests/908',
      name='Корректно указаны title, description, canonical ')
@feature('Добавление мета-тегов')
def test_page_meta_data(driver, meta_data):
    main_page_test = get_page_instance(meta_data["page"], driver)
    main_page_test.open()
    form_page_test = main_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == meta_data[
        "title"], f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == meta_data[
        "description"], f"Получен Description:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == meta_data[
        "canonical"], f"Получен Canonical:  {form_page_test.get_canonical_ceo_page()}"


# Загрузка данных из JSON-файла
test_data = load_file('service_pages_data.json')
@pytest.mark.parametrize("card_type, expected_url, expected_title",
                         [(d['card_type'], d['expected_url'], d['expected_title']) for d in test_data])
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    project_element = main_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


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


filtered_data = load_package_data_e_com()
# Использование отфильтрованных данных в тестах
@pytest.mark.parametrize("project_type, bullits, price",
                         [(d['project_type'], d['bullits'], d['price']) for d in filtered_data])
def test_ecom_page_data_card_packages(driver, project_type, bullits, price):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    e_com_page_test.check_packages_data_not_experience(project_type, bullits, price)


# Использование отфильтрованных данных в тестах
filtered_data = load_package_data_outstaff()
@pytest.mark.parametrize("project_type, experience, bullits, price",
                         [(d['project_type'], d['experience'], d['bullits'], d['price']) for d in filtered_data])
def test_outstaff_page_data_card_packages(driver, project_type, experience, bullits, price):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.check_packages_data(project_type, experience, bullits, price)


@feature('Количество элементов в блоке')
@pytest.mark.parametrize("project_type, count", [
    ("benefits", 6),
    ("types_of_it", 3),
    ("what_to_choose", 3)
])
def test_main_page_benefits_types_of_it_what_to_choose_count_cards(driver, project_type, count):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    blocks = outstaff_page_test.get_count_elements()
    blocks.count_cards_assert(project_type, count)
