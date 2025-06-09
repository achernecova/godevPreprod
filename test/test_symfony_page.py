import allure
import pytest
from allure_commons._allure import feature

from pages.symfony_page import SymfonyPage


@pytest.mark.short_test
@pytest.mark.fill_form_request_footer
@feature('Успешная отправка заявки из футера')
def test_fill_form_request_footer_symfony_page(driver):
    symfony_page_test = SymfonyPage(driver)
    symfony_page_test.open()
    form_page_test = symfony_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@allure.feature('Проверка данных в FAQ')
@pytest.mark.prod_test
def test_symfony_page_faq_data_assert(driver):
    symfony_page_test = SymfonyPage(driver)
    symfony_page_test.open()
    symfony_page_test.get_data_faq_card()


@pytest.mark.fill_form_request_faq
@feature('Успешная отправка заявки из FAQ')
def test_symfony_page_add_request_in_faq(driver):
    symfony_page_test = SymfonyPage(driver)
    symfony_page_test.open()
    symfony_page_test.click_button_in_faq()
    popup_modal_page = symfony_page_test.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "