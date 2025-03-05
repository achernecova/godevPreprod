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

