import pytest
from allure_commons._allure import feature

from pages.landing_page import LandingPage
from utils.data_loader import load_service_data_review

@pytest.mark.prod_test
@feature('Проверка данных в карточках блока Web Development Process')
def test_landing_page_web_development_process_data_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_card("tile_squad_landing")


@feature('Проверка данных в карточках блока How a landing page helps your business')
def test_landing_page_why_do_you_need_data_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_card("how_it_staff_landing")

@pytest.mark.prod_test
@feature('Проверка данных в карточках блока Work process')
def test_landing_page_web_development_process_data_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_advant_carousel_card()


@feature('Проверка данных в карточках блока Godev’s advantages')
def test_landing_page_benefits_count_cards_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_card("tiles_landing")

@pytest.mark.prod_test
@feature('Проверка данных в карточках блока Rates')
def test_landing_page_benefits_count_cards_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_card_rates_landing()


@feature('Заявка из блока Rates')
def test_landing_page_add_request_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.click_button_rates_landing()
    form_page_test = landing_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@feature('Проверка данных в карусели с отзывами')
def test_main_page_count_card_reviews(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_review_landing()


# загрузка данных из json файла
@pytest.mark.prod_test
@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", load_service_data_review())
def test_services_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    project_element = landing_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

