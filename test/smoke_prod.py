import json
import os

import allure
import pytest
from allure_commons._allure import feature, link

from constants import ECOM_PAGE_TYPES, OUTSTAFF_PROJECT_TYPES
from pages.b2b_page import B2BPage
from pages.cms_page import CMSPage
from pages.e_com_page import EComPage
from pages.main_page import MainPage
from pages.project_page import ProjectPage
from pages.web_outstaff_page import WebOutstaffPage


@feature('Успешная отправка заявки')
def test_main_page_add_request_header(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    popup_element_test = main_page_test.get_popup_element()
    popup_element_test.add_request_success()
    assert popup_element_test.popup_success_displayed() == True, "Окно не появилось"

@link(url='https://team-v5ka.testit.software/projects/664/tests/908', name='Корректно указаны title, description, canonical ')
@feature('Добавление мета-тегов')
def test_main_page_add_title_descr_and_canonical(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    form_page_test = main_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Web Development Company in USA | Web Design, App & Web Development Services – Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Godev is a leading web development company in the USA. We specialize in custom web design, web applications, app and web development services", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://godev.agency/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

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
@link(url='https://team-v5ka.testit.software/projects/664/tests/746',name='Отображение блока IT staff augmentation и переход на страницу')
@feature('Открытие страниц услуг')
@pytest.mark.parametrize("card_type, expected_url, expected_title",
                         [(d['card_type'], d['expected_url'], d['expected_title']) for d in test_data])
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    project_element = main_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

@feature('Добавление мета-тегов')
def test_project_page_add_title_descr_canonical(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    form_page_test = project_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Web Development and Designs Portfolio - Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Godev's portfolio consist of completed projects in Design and Web Development. We help clients grow and prosper for over 10 years", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://godev.agency/projects/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@allure.feature('Количество элементов в блоке')
def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 4)

@allure.feature('Количество элементов в блоке')
def test_cms_page_cms_services_cards_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("cms_services_cards", 4)



current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', 'package_card_data.json')
try:
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError as e:
    raise RuntimeError('Файл service_pages_data.json не найден: ' + str(e))
except json.JSONDecodeError as e:
    raise RuntimeError('Ошибка при разборе JSON в service_pages_data.json: ' + str(e))
except Exception as e:  # Ловим все остальные ошибки
    raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
filtered_data = [
    item for item in data
    if item['project_type'] in ECOM_PAGE_TYPES
]
# Использование отфильтрованных данных в тестах
@pytest.mark.parametrize("project_type, bullits, price",
    [(d['project_type'], d['bullits'], d['price']) for d in filtered_data])
def test_ecom_page_data_card_packages(driver, project_type, bullits, price):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    e_com_page_test.check_packages_data_not_experience(project_type, bullits, price)


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', 'package_card_data.json')
try:
    with open(file_path, encoding='utf-8') as f:
        package_data_list = json.load(f)
except FileNotFoundError as e:
    raise RuntimeError('Файл service_pages_data.json не найден: ' + str(e))
except json.JSONDecodeError as e:
    raise RuntimeError('Ошибка при разборе JSON в service_pages_data.json: ' + str(e))
except Exception as e:  # Ловим все остальные ошибки
    raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
# Фильтрация данных по конкретным project_type
filtered_data = [
    item for item in package_data_list
    if item['project_type'] in OUTSTAFF_PROJECT_TYPES
]
# Использование отфильтрованных данных в тестах
@pytest.mark.parametrize("project_type, experience, bullits, price",
    [(d['project_type'], d['experience'], d['bullits'], d['price']) for d in filtered_data])
def test_outstaff_page_data_card_packages(driver, project_type, experience, bullits, price):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.check_packages_data(project_type, experience, bullits, price)

@feature('Количество элементов в блоке')
@pytest.mark.parametrize("project_type, count", [
    ("benefits", 6),
    ("types_of_it", 3),
    ("what_to_choose", 3)
])
def test_main_page_benefits_types_of_it_what_to_choose_count_cards(driver, project_type, count):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    blocks = outstaff_page_test.get_count_elements()
    blocks.count_cards_assert(project_type, count)