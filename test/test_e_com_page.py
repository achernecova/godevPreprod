import allure
import pytest
from allure_commons._allure import feature

from pages.e_com_page import EComPage
from utils.data_loader import load_service_data_e_com


@allure.feature('Количество элементов в блоке')
def test_e_com_page_how_we_make_web_count_cards_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    blocks = e_com_page_test.get_count_elements()
    blocks.count_cards_assert('how_we_make_web', 5)


@allure.feature('Количество элементов в блоке')
def test_e_com_page_our_proven_web_dev_count_cards_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    blocks = e_com_page_test.get_count_elements()
    blocks.count_cards_assert('our_proven_web_dev', 7)


#Загрузка данных из json файла
filtered_data = load_service_data_e_com()
@pytest.mark.parametrize('card_type, expected_url, expected_title', filtered_data)
def test_e_com_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    project_element = e_com_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f'Получен Title: {page.get_title_page()}'


def test_e_com_page_data_card_packages(driver):
    ecom_page_test = EComPage(driver)
    ecom_page_test.open()
    ecom_page_test.get_data_card_e_com()


@feature('Количество элементов в блоке с черно-белыми карточками')
def test_e_com_page_benefits_count_cards_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    blocks = e_com_page_test.get_count_elements()
    blocks.count_cards_assert('types_of_websites_count_card', 7)


@feature('Проверка данных в карточках блока Comprehensive E-commerce services')
def test_e_com_page_benefits_cards_data_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    e_com_page_test.get_data_card_tiles_e_com()


@feature('Проверка данных в карточках блока Web Development Process')
def test_e_com_page_web_development_process_data_assert(driver):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    e_com_page_test.get_data_advant_carousel_card()