import allure
import pytest

from pages.framework_page import FrameworkPage

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

@allure.feature('Добавление мета-тегов')
def test_framework_page_add_title_descr_and_canonical(driver):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    form_page_test = framework_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Web Development on Frameworks in the USA: website development in Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Explore top web development frameworks in the USA with Godev. Save time and enhance coding efficiency for your projects by leveraging powerful software infrastructure!", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/website-development/framework/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("project_type, expected_url, expected_title", [
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites")
])
def test_framework_page_click_project_and_open_pages(driver, project_type, expected_url, expected_title):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    project_element = framework_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(project_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@pytest.mark.parametrize("index, price_left_title, price_left_text, price_right_title, price_right_text", [
    (1 , "Hours per month", "up to 30", "Price", "30 $"),
    (2 , "Hours per month", "from 30 to 100", "Price", "27 $"),
    (3 , "Hours per month", "from 100 to 150", "Price", "25 $"),
    (4, "Hours per month", "from 150", "Price", "22 $"),
])
def test_framework_page_table_data_assert(driver, index, price_left_title, price_left_text, price_right_title, price_right_text):
    framework_page_test = FrameworkPage(driver)
    framework_page_test.open()
    framework_page_test.get_data_block_price(index, price_left_title, price_left_text, price_right_title, price_right_text)