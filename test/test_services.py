import json
import os

import allure
import pytest
from allure_commons._allure import feature, story

from constants import PROJECTS_TYPES, CARD_B2B_TYPES
from pages.services_page import ServicesPage

# загрузка данных из json файла
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
    if d['card_type'] in CARD_B2B_TYPES]
@feature('Открытие страниц услуг')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_services_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    project_element = services_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


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
    if d['card_type'] in PROJECTS_TYPES]
# Загрузка данных из JSON-файла
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", filtered_data)
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    project_element = services_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@feature('Добавление мета-тегов')
def test_services_page_add_title_descr_and_canonical(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    form_page_test = services_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "IT services for you and your business", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "In godev studio you can order the creation of a website, portal or application of any complexity. We use a wide technology stack", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@feature('Количество элементов в блоке')
def test_services_page_count_card_advantages_of_working(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    blocks = services_page_test.get_count_elements()
    blocks.count_cards_assert("adv_item", 6)

