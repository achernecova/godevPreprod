import json

import allure
import pytest
from allure_commons._allure import feature

from constants import PROJECTS_TYPES
from pages.reviews_page import ReviewsPage

@feature('Количество элементов в блоке')
def test_main_page_count_card_reviews(driver):
    reviews_page_test = ReviewsPage(driver)
    reviews_page_test.open()
    blocks = reviews_page_test.get_count_elements()
    blocks.count_cards_assert("swiper_slide", 3)

@feature('Добавление мета-тегов')
def test_reviews_page_add_title_descr_and_canonical(driver):
    reviews_page_test = ReviewsPage(driver)
    reviews_page_test.open()
    form_page_test = reviews_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Godev Reviews | Web development in USA", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Reviews from our clients about web development with Godev", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/reviews/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"


# Загрузка данных из JSON-файла
try:
    with open('../service_pages_data.json') as f:
        test_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
# Фильтрация данных по card_type
filtered_data = [
    (d['card_type'], d['expected_url'], d['expected_title'])
    for d in test_data
    if d['card_type'] in PROJECTS_TYPES]
@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_reviews_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    reviews_page_test = ReviewsPage(driver)
    reviews_page_test.open()
    project_element = reviews_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"