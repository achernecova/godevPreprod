
import allure
import pytest
from allure_commons._allure import feature

from pages.support_pages import SupportPage
from utils.data_loader import load_service_data_support


# тест с мета-тегами вынесен в main_page_test

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

@feature('Успешная отправка заявки')
def test_support_page_add_request(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    support_page_test.click_button_tariff_table()
    popup_element_test = support_page_test.get_popup_element()
    popup_element_test.add_request_success()
    assert popup_element_test.popup_success_displayed() == True, "Окно не появилось"


filtered_data = load_service_data_support()
# Загрузка данных из JSON-файла
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_support_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    click_element_test = support_page_test.get_project_service_element()
    page = click_element_test.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@allure.feature('Проверка данных в карточках блока Benefits of choosing Godev')
def test_support_page_benefits_count_cards_assert(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    support_page_test.get_data_card_tiles_support()




@allure.feature('Проверка данных в карточках блока Why do you need maintenance?')
def test_support_page_why_do_you_need_data_assert(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    support_page_test.get_data_card_how_it_staff_support()


@allure.feature('Проверка данных в FAQ')
def test_support_page_faq_data_assert(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    support_page_test.get_data_faq_card()

@pytest.mark.fill_form_request_faq
@allure.feature('Успешная отправка заявки из FAQ')
def test_support_page_add_request_in_faq(driver):
    support_page_test = SupportPage(driver)
    support_page_test.open()
    support_page_test.click_button_in_faq()
    popup_modal_page = support_page_test.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "