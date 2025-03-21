import allure
import pytest
from allure_commons._allure import feature

from pages.d2c_page import D2C
from utils.data_loader import load_service_data_review


@feature('Успешная отправка заявки из баннера')
def test_add_request_success_d2c_page(driver):
    d2c_page_test = D2C(driver)
    d2c_page_test.open()
    d2c_page_test.click_button_banner()
    form_page_test = d2c_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


#@pytest.mark.fill_form_request_footer
@feature('Успешная отправка заявки из футера')
def test_fill_form_request_footer_d2c_page(driver):
    d2c_page_test = D2C(driver)
    d2c_page_test.open()
    form_page_test = d2c_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@feature('Проверка данных в карточках блока Direct to Consumer vs. Wholesale:')
def test_d2c_page_web_development_process_data_assert(driver):
    d2c_page_test = D2C(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_advant_carousel_card()


@feature('Проверка данных в карусели с отзывами')
def test_web_develop_page_count_card_reviews(driver):
    d2c_page_test = D2C(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_review()


@allure.feature('Проверка данных в карточках блока Website Packages')
def test_web_develop_page_data_card_packages_new(driver):
    d2c_page_test = D2C(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_card_website()


@feature('Проверка данных в карточках блока Why Godev is the right staff augmentation partner')
def test_outstaff_page_benefits_count_cards_assert(driver):
    d2c_page_test = D2C(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_card_tiles_outstaff()


#загрузка данных из json файла
filtered_data = load_service_data_review()
@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_services_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    d2c_page_test = D2C(driver)
    d2c_page_test.open()
    project_element = d2c_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"