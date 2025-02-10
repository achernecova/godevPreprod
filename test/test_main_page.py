from allure_commons._allure import link, feature
import pytest

import json

from constants import URLs, subURLs, DESIRED_PROJECT_TYPES
from pages.main_page import MainPage
from package_data import PackageData

#загрузка данных из json файла
try:
    with open('../package_card_data.json') as f:
        package_data_list = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError('Error loading package card data: ' + str(e))
# Фильтрация данных по конкретным project_type
package_data_list = [
    PackageData(**data) for data in package_data_list
    if data['project_type'] in DESIRED_PROJECT_TYPES  # Используем импортированную константу
]
@pytest.mark.parametrize("package_data", package_data_list)
def test_main_page_data_card_packages(driver, package_data):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.check_packages_data(package_data.project_type, package_data.experience, package_data.bullits, package_data.price)

# Загрузка данных из JSON-файла
with open('../service_pages_data.json') as f:
    test_data = json.load(f)
@pytest.mark.parametrize("card_type, expected_url, expected_title",
                         [(d['card_type'], d['expected_url'], d['expected_title']) for d in test_data])
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    project_element = main_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

@feature('Успешная отправка заявки')
def test_add_request_success_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    form_page_test = main_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, "Окно подтверждения не появилось"

@feature('Успешная отправка заявки')
def test_fill_form_request_footer_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    form_page_test = main_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed()==True, "Окно подтверждения не появилось"

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
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@link(url='https://team-v5ka.testit.software/projects/664/tests/759', name='Отображение блока Customer Reviews')
@feature('Количество элементов в блоке')
def test_main_page_count_card_reviews(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    blocks = main_page_test.get_count_elements()
    blocks.count_cards_assert("customer_reviews", 3)

@feature('Количество элементов в блоке')
def test_main_page_count_card_packages(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    blocks = main_page_test.get_count_elements()
    blocks.count_cards_assert("web_packages_count", 9)

@link(url='https://team-v5ka.testit.software/projects/664/tests/907', name='Отображение блока App and Web Development Services и переходы на страницы')
@feature('Открытие страниц услуг')
@pytest.mark.parametrize("index, page_url, page_title", [
    ("1", URLs.MAIN_PAGE+subURLs.E_COM_PAGE, "E-commerce web development for scalable business growth"),
    ("2", URLs.MAIN_PAGE+subURLs.B2B_PAGE, "B2B e-commerce website development"),
    ("3", URLs.MAIN_PAGE+subURLs.FRAMEWORK_PAGE, "What is a framework and why it’s essential for web development")
])
def test_main_page_click_more_packages_and_data_pages(driver, index, page_url, page_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_more_packages_and_data_pages(index, page_url, page_title)

