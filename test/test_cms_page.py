import allure
import pytest

from pages.cms_page import CMSPage
from utils.data_loader import load_service_data_review

# тест с мета-тегами вынесен в main_page_test

@allure.feature('Количество элементов в блоке')
def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('types_of_websites_count_card', 4)

@allure.feature('Количество элементов в блоке')
def test_cms_page_cms_services_cards_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('cms_services_cards', 4)

@allure.feature('Количество элементов в блоке')
def test_cms_page_cms_types_of_it_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('types_of_it', 3)

@allure.feature('Количество элементов в блоке')
def test_cms_page_platforms_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('platforms', 4)


# Загрузка данных из JSON-файла
filtered_data = load_service_data_review()
@allure.feature('Проверка открытия страниц проектов')
@pytest.mark.parametrize('card_type, expected_url, expected_title', filtered_data)
def test_cms_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    project_element = cms_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f'Получен Title: {page.get_title_page()}'



@allure.feature('Проверка данных в карточках блока Website packages')
def test_main_page_data_card_packages(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.get_data_card_cms()


@allure.feature('Проверка данных в карточках блока Digital Benefits of using content management systems')
def test_e_com_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.get_data_card_tiles_cms()


@allure.feature('Проверка данных в карточках блока Developing a website based on an existing CMS')
def test_support_page_why_do_you_need_data_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.get_data_card_how_it_staff_cms()


@allure.feature('Успешная отправка заявки')
def test_b2b_page_add_request_success(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.click_button_banner()
    form_page_test = cms_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@allure.feature('Успешная отправка заявки из футера')
def test_cms_page_fill_form_request_footer(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    form_page_test = cms_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'