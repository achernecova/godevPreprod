import allure
import pytest

from pages.b2b_page import B2BPage
from utils.data_loader import load_service_data_review


# тест с мета-тегами вынесен в main_page_test

@allure.feature('Количество элементов в блоке')
def test_b2b_page_platforms_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("platforms", 4)


@allure.feature('Количество элементов в блоке')
def test_b2b_page_benefits_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)


#загрузка данных из json файла
@pytest.mark.prod_test
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", load_service_data_review())
def test_services_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    project_element = b2b_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@allure.feature('Проверка данных в карточках блока Website packages')
def test_b2b_page_data_card_packages(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.get_data_card_b2b()

@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Benefits of a B2B e-commerce solution from Godev')
def test_b2b_page_benefits_data_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.get_data_card_tiles_b2b()

@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока B2B e-commerce platforms')
def test_b2b_page_why_do_you_need_data_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.get_data_card_how_it_staff_b2b()


@allure.feature('Успешная отправка заявки')
def test_b2b_page_add_request_success(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.click_button_banner()
    form_page_test = b2b_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'

@pytest.mark.prod_test
@pytest.mark.fill_form_request_footer
@allure.feature('Успешная отправка заявки из футера')
#@patch('path.to.your.recaptcha_verification_function', return_value=True)
def test_b2b_page_fill_form_request_footer(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    form_page_test = b2b_page_test.get_form_page()
    form_page_test.fill_form()
    #form_page_test.click_button_add_request()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'

