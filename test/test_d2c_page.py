import allure
import pytest
from allure_commons._allure import link, feature

from pages.d2c_page import D2CPage
from utils.data_loader import load_service_data_review


# работает
@allure.feature('Проверка данных в карточках блока Website packages')
def test_d2c_page_data_card_packages(driver):
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_card_d2c()

# работает
# Загрузка данных из JSON-файла
@pytest.mark.prod_test
@allure.feature('Проверка открытия страниц проектов')
@pytest.mark.parametrize('card_type, expected_url, expected_title', load_service_data_review())
def test_d2c_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    project_element = d2c_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f'Получен Title: {page.get_title_page()}'


@link(url='https://team-v5ka.testit.software/projects/664/tests/907',
      name='Отображение блока App and Web Development Services и переходы на страницы')
@feature('Открытие страниц услуг')
@pytest.mark.prod_test
def test_d2c_page_click_more_packages_and_data_pages(driver, test_data_d2c):
    index, page_url, page_title = test_data_d2c
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    d2c_page_test.click_more_packages_and_data_pages(index, page_url, page_title)


@allure.feature('Проверка данных в карточках карусели Direct to Consumer vs. Wholesale')
def test_d2c_page_web_limitations_of_frameworks_data_assert(driver):
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_advant_carousel_card()


@allure.feature('Проверка данных в карточках карусели Direct to Consumer vs. Wholesale')
def test_d2c_page_web_limitations_of_frameworks_data_assert_icons(driver):
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_advant_carousel_card_icons()

@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока D2C eCommerce Platforms')
def test_d2c_page_d2c_ecommerce_platform_cards_assert(driver):
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_card_tiles_d2c()


@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Our Advantages')
def test_d2c_page_our_advant_assert(driver):
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_card_tiles_d2c_icon()

@pytest.mark.prod_test
@allure.feature('Проверка данных в карусели с отзывами')
def test_main_page_count_card_reviews(driver):
    d2c_page_test = D2CPage(driver)
    d2c_page_test.open()
    d2c_page_test.get_data_review_d2c()