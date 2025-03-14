import pytest
from allure_commons._allure import feature

from pages.services_page import ServicesPage
from utils.data_loader import load_service_data_review

#загрузка данных из json файла
filtered_data = load_service_data_review()
@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_services_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    project_element = services_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@feature('Количество элементов в блоке')
def test_services_page_count_card_advantages_of_working(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    blocks = services_page_test.get_count_elements()
    blocks.count_cards_assert("adv_item", 6)


@feature('Проверка заголовка в блоке Services')
def test_main_page_app_and_web_title_assert(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    title_block = services_page_test.get_title_block_app_and_web_development_services()
    assert title_block == 'Services', f"Получен Title:  {title_block}"

@feature('Проверка данных в карточках блока App and Web Development Services')
def test_landing_page_why_do_you_need_data_assert(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    services_page_test.get_data_card_app_and_web_services_service()

@feature('Проверка данных в карточках блока Advantages of working with us')
def test_landing_page_why_do_you_need_data_assert(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    services_page_test.get_data_card_app_and_web_services_advant()


@feature('Успешная отправка заявки из баннера')
def test_add_request_success_services_page(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    services_page_test.click_button_banner()
    form_page_test = services_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@feature('Успешная отправка заявки из футера')
def test_fill_form_request_footer_services_page(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    form_page_test = services_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'