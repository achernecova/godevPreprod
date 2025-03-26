import pytest
from allure_commons._allure import feature

from pages.project_page import ProjectPage
from utils.data_loader import load_service_data_review

# тест с мета-тегами вынесен в main_page_test

@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", load_service_data_review())
def test_project_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    project_element = project_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@feature('Количество элементов в блоке')
def test_project_page_count_card_reviews(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    blocks = project_page_test.get_count_elements()
    blocks.count_cards_assert("customer_reviews", 3)


@feature('Проверка данных в карусели с отзывами')
def test_main_page_count_card_reviews(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    project_page_test.get_data_review()