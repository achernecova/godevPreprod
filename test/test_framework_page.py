import allure
import pytest

from pages.framework_page import FrameworkPage
from utils.data_loader import load_service_data_framework


# тест с мета-тегами вынесен в main_page_test

@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_reviews(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("advantages_cards_tiles_count", 5)


@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_advantages_outsourcing(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("advantages_outsourcing", 5)


@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_advant_card(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("benefits", 5)


@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_best_web_frameworks(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("best_web_frameworks", 5)


@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_why_choose_godev(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("why_choose_godev", 5)


@allure.feature('Количество элементов в блоке')
def test_framework_page_count_card_back_end_frameworks(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    blocks = framework_page_test.get_count_elements()
    blocks.count_cards_assert("back_end_frameworks", 5)


# Загрузка данных из json файла
filtered_data = load_service_data_framework()
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_e_com_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    project_element = framework_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@pytest.mark.parametrize("index, price_left_title, price_left_text, price_right_title, price_right_text", [
    (1, "Hours per month", "up to 30", "Price", "30 $"),
    (2, "Hours per month", "from 30 to 100", "Price", "27 $"),
    (3, "Hours per month", "from 100 to 150", "Price", "25 $"),
    (4, "Hours per month", "from 150", "Price", "22 $"),
])
def test_framework_page_table_data_assert(driver, index, price_left_title, price_left_text, price_right_title,
                                          price_right_text):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_block_price(index, price_left_title, price_left_text, price_right_title,
                                             price_right_text)


@allure.feature('Проверка данных в карточках блока Advantages of development on frameworks')
def test_framework_page_why_do_you_need_data_assert(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_card_how_it_staff_framework()


@allure.feature('Проверка данных в FAQ')
def test_framework_page_faq_data_assert(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_faq_card_new()

@pytest.mark.fill_form_request_faq
@allure.feature('Успешная отправка заявки из FAQ')
def test_framework_page_add_request_in_faq(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.click_button_in_faq()
    popup_modal_page = framework_page_test.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "


@allure.feature('Проверка данных в карточках блока Advantages of outsourcing for web')
def test_framework_page_why_do_you_need_data_assert(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_card_advant_of_outsource_frame()


@allure.feature('Проверка данных в карточках карусели Limitations of frameworks')
def test_framework_page_web_limitations_of_frameworks_data_assert(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_advant_carousel_card()

@allure.feature('Проверка данных в карточках блока Why choose Godev')
def test_framework_page_why_choose_data_assert(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_advant_carousel_card()