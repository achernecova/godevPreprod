import allure
import pytest

from allure_commons._allure import feature

from pages.saas_page import SAASPage
from utils.data_loader import load_service_data_review



@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Team and specialists')
def test_saas_page_team_abd_spec_data_card_packages(driver):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    saas_page_test.get_data_card_saas()


@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Types of ready-made')
def test_saas_type_of_ready_data_cards_assert(driver):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    saas_page_test.get_data_card_tiles_saas()


@allure.feature('Успешная отправка заявки')
def test_saas_page_add_request_success(driver):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    saas_page_test.click_button_banner()
    form_page_test = saas_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@pytest.mark.prod_test
@feature('Проверка данных в карточках блока Development process')
def test_saas_page_web_development_process_data_assert(driver):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    saas_page_test.get_data_advant_carousel_card()


@pytest.mark.prod_test
@pytest.mark.parametrize('card_type, expected_url, expected_title', load_service_data_review())
def test_saas_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    project_element = saas_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f'Получен Title: {page.get_title_page()}'


@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока The benefits of the SaaS model')
def test_saas_page_benefits_saas_model_data_assert(driver):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    saas_page_test.get_data_card_how_it_staff_saas()


@allure.feature('Проверка данных в FAQ')
@pytest.mark.prod_test
def test_web_dev_serv_page_faq_data_assert(driver):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    saas_page_test.get_data_faq_card()


@pytest.mark.fill_form_request_faq
@feature('Успешная отправка заявки из FAQ')
def test_outstaff_dev_page_add_request_in_faq(driver):
    saas_page_test = SAASPage(driver)
    saas_page_test.open()
    saas_page_test.click_button_in_faq()
    popup_modal_page = saas_page_test.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "
