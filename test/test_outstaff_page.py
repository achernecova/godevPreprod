import json

import allure
import pytest
from allure_commons._allure import feature

from constants import OUTSTAFF_PROJECT_TYPES
from pages.web_outstaff_page import WebOutstaffPage

@feature('Успешная отправка заявки')
def test_web_outstaff_add_success_request(driver):
    web_outstaff_page_test = WebOutstaffPage(driver)
    web_outstaff_page_test.open()
    web_outstaff_page_test.click_button_outsource()
    form_page_test = web_outstaff_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, "Окно не появилось"

@feature('Количество элементов в блоке')
@pytest.mark.parametrize("project_type, count", [
    ("benefits", 6),
    ("types_of_it", 3),
    ("what_to_choose", 3)
])
def test_main_page_benefits_types_of_it_what_to_choose_count_cards(driver, project_type, count):
    main_page_test = WebOutstaffPage(driver)
    main_page_test.open()
    blocks = main_page_test.get_count_elements()
    blocks.count_cards_assert(project_type, count)

@feature('Добавление мета-тегов')
def test_web_outstaff_add_title_and_descr(driver):
    web_outstaff_page_test = WebOutstaffPage(driver)
    web_outstaff_page_test.open()
    form_page_test = web_outstaff_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "IT staff augmentation company in USA, cost of outsorce tech teams and software developers", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "IT staff augmentation – hire tech teams and software developers for your projects with lower cost in USA. Software, databases, websites, applications, microservices, mobile applications", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"


#загрузка данных из json файла
try:
    with open('../package_card_data.json') as f:
        package_data_list = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
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


