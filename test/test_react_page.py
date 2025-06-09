from time import sleep

import allure
import pytest
from allure_commons._allure import feature

from pages.reactjs import ReactjsPage


# не работает
@pytest.mark.short_test
@feature('Успешная отправка заявки из баннера')
def test_add_request_success_react_page(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.click_button_banner()
    form_page_test = react_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@pytest.mark.short_test
@pytest.mark.fill_form_request_footer
@feature('Успешная отправка заявки из футера')
def test_fill_form_request_footer_react_page(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    form_page_test = react_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


# не работает.
@pytest.mark.short_test
@feature('Успешная отправка заявки из блока Get in touch')
def test_react_page_add_request_header(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    popup_element_test = react_page_test.get_popup_element()
    popup_element_test.add_request_success_get_in_touch()
    assert popup_element_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@allure.feature('Проверка данных в FAQ')
@pytest.mark.prod_test
def test_react_page_faq_data_assert(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.get_data_card("faq_card_react")


@pytest.mark.fill_form_request_faq
@feature('Успешная отправка заявки из FAQ')
def test_react_page_add_request_in_faq(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    #react_page_test.click_button_in_faq()
    react_page_test.click_button_new()
    sleep(5)
    #popup_modal_page = react_page_test.get_popup()
    #popup_modal_page.add_request_success()
    #success = popup_modal_page.popup_success_displayed()
    #assert success == True, f"Не появилось окно успешности "


@pytest.mark.prod_test
@pytest.mark.parametrize("index, price_left_title, price_left_text, price_right_title, price_right_text", [
    (1, "Hours per month", "up to 30", "Price", "30 $"),
    (2, "Hours per month", "from 30 to 100", "Price", "27 $"),
    (3, "Hours per month", "from 100 to 150", "Price", "25 $"),
    (4, "Hours per month", "from 150", "Price", "22 $"),
])
def test_react_page_table_data_assert(driver, index, price_left_title, price_left_text, price_right_title,
                                          price_right_text):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.get_data_block_price(index, price_left_title, price_left_text, price_right_title,
                                             price_right_text)

@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Why choose Godev')
def test_react_type_of_ready_data_cards_assert(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.get_data_card("tiles_react")

@feature('Проверка данных в карточках блока Advantages of React')
def test_react_page_why_do_you_need_data_assert(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.get_data_card("how_it_staff_react")


@pytest.mark.prod_test
@feature('Проверка данных в карточках блока App and Web Development Services')
def test_react_page_why_do_you_need_data_assert(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.get_data_card("app_and_web_services_react")

@allure.feature('Проверка данных в карточках карусели Why partner with us?')
def test_react_page_web_limitations_of_frameworks_data_assert(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.get_data_card("advant_of_outsource_react")

@allure.feature('Проверка данных в карточках карусели Technologies we use with ReactJS')
def test_react_page_web_limitations_of_frameworks_data_assert(driver):
    react_page_test = ReactjsPage(driver)
    react_page_test.open()
    react_page_test.get_data_card("card_best_framework_react")