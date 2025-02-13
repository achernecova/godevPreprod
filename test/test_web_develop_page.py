import json
import os

import allure
import pytest
from allure_commons._allure import feature

from constants import SUPPORT_PROJECTS_TYPES
from pages.web_develop_page import WebDevelopPage

# тест с мета-тегами вынесен в main_page_test

@feature('Количество элементов в блоке')
def test_web_develop_page_count_card_how_me_make(driver):
    web_dev_page = WebDevelopPage(driver)
    web_dev_page.open()
    blocks = web_dev_page.get_count_elements()
    blocks.count_cards_assert("carousel_how_make", 6)


@feature('Количество элементов в блоке')
def test_web_develop_page_count_card_types_of_websites(driver):
    web_dev_page = WebDevelopPage(driver)
    web_dev_page.open()
    blocks = web_dev_page.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)


@feature('Переходы на страницы из карточек')
@pytest.mark.parametrize("index, page_url, page_title", [
    ("1", "https://dev.godev.agency/services/website-development/b2b/", "B2B e-commerce website development"),
    ("2", "https://dev.godev.agency/services/website-development/cms/", "Custom CMS development service"),
    ("3", "https://dev.godev.agency/services/website-development/framework/",
     "What is a framework and why it’s essential for web development")
])
def test_main_page_click_more_packages_and_data_pages(driver, index, page_url, page_title):
    main_page_test = WebDevelopPage(driver)
    main_page_test.open()
    main_page_test.click_more_packages_and_data_pages(index, page_url, page_title)


#загрузка данных из json файла
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', 'service_pages_data.json')
try:
    with open(file_path, encoding='utf-8') as f:
        test_data = json.load(f)
except FileNotFoundError as e:
    raise RuntimeError('Файл service_pages_data.json не найден: ' + str(e))
except json.JSONDecodeError as e:
    raise RuntimeError('Ошибка при разборе JSON в service_pages_data.json: ' + str(e))
except Exception as e:  # Ловим все остальные ошибки
    raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
# Фильтрация данных по card_type
filtered_data = [
    (d['card_type'], d['expected_url'], d['expected_title'])
    for d in test_data
    if d['card_type'] in SUPPORT_PROJECTS_TYPES]

# Загрузка данных из JSON-файла
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_web_dev_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    support_page_test = WebDevelopPage(driver)
    support_page_test.open()
    support_element_test = support_page_test.get_project_service_element()
    page = support_element_test.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"
