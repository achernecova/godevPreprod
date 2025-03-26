import json
import os

import pytest
from allure_commons._allure import feature

from pages.reviews_page import ReviewsPage
from utils.data_loader import load_service_data_review


# тест с мета-тегами вынесен в main_page_test

@feature('Количество элементов в блоке')
@pytest.mark.prod_test
def test_main_page_count_card_reviews(driver):
    reviews_page_test = ReviewsPage(driver)
    reviews_page_test.open()
    blocks = reviews_page_test.get_count_elements()
    blocks.count_cards_assert("swiper_slide", 3)


    # Загрузка данных из JSON-файла
@feature('Открытие страниц проектов')
@pytest.mark.prod_test
@pytest.mark.parametrize("card_type, expected_url, expected_title", load_service_data_review())
def test_reviews_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    reviews_page_test = ReviewsPage(driver)
    reviews_page_test.open()
    project_element = reviews_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"
