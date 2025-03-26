import allure
import pytest
from allure_commons._allure import feature

from pages.web_develop_page import WebDevelopPage
from utils.data_loader import load_service_data_web_dev


# тест с мета-тегами вынесен в main_page_test

@feature('Количество элементов в блоке How we make websites')
def test_web_develop_page_count_card_how_me_make(driver):
    web_dev_page = WebDevelopPage(driver)
    web_dev_page.open()
    blocks = web_dev_page.get_count_elements()
    blocks.count_cards_assert("carousel_how_make", 6)


@feature('Количество элементов в блоке Types of websites we work with')
@pytest.mark.prod_test
def test_web_develop_page_count_card_types_of_websites(driver):
    web_dev_page = WebDevelopPage(driver)
    web_dev_page.open()
    blocks = web_dev_page.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)


    # скрытие констант в фикстуру
@feature('Переходы на страницы из карточек')
@pytest.mark.prod_test
def test_web_dev_page_click_more_packages_and_data_pages(driver, test_data_cards):
    index, page_url, page_title = test_data_cards
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    web_dev_page_test.click_more_packages_and_data_pages(index, page_url, page_title)


#загрузка данных из json файла с фильтрацией
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", load_service_data_web_dev())
@pytest.mark.prod_test
def test_web_dev_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    support_element_test = web_dev_page_test.get_project_service_element()
    page = support_element_test.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@allure.feature('Проверка данных в карточках блока Website Packages')
@pytest.mark.prod_test
def test_web_develop_page_data_card_packages_new(driver):
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    web_dev_page_test.get_data_card_website()


@allure.feature('Проверка данных в карточках блока Types of websites we work with')
@pytest.mark.prod_test
def test_web_develop_page_benefits_count_cards_assert(driver):
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    web_dev_page_test.get_data_card_tiles_website()


@feature('Проверка данных в Benefits of team augmentation services')
def test_web_develop_page_web_development_process_data_assert(driver):
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    web_dev_page_test.get_data_advant_carousel_card()


@feature('Проверка данных в карусели с отзывами')
def test_web_develop_page_count_card_reviews(driver):
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    web_dev_page_test.get_data_review()


@allure.feature('Проверка данных в FAQ')
@pytest.mark.prod_test
def test_web_develop_page_faq_data_assert(driver):
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    web_dev_page_test.get_data_faq_card()


@pytest.mark.fill_form_request_faq
@feature('Успешная отправка заявки из FAQ')
def test_web_develop_page_add_request_in_faq(driver):
    web_dev_page_test = WebDevelopPage(driver)
    web_dev_page_test.open()
    web_dev_page_test.click_button_in_faq()
    popup_modal_page = web_dev_page_test.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "