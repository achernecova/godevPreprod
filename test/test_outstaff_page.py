
import pytest
from allure_commons._allure import feature

from pages.web_outstaff_page import WebOutstaffPage


# тест с мета-тегами вынесен в main_page_test

@feature('Успешная отправка заявки')
def test_web_outstaff_add_success_request(driver):
    web_outstaff_page_test = WebOutstaffPage(driver)
    web_outstaff_page_test.open()
    web_outstaff_page_test.click_button_outsource()
    form_page_test = web_outstaff_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, "Окно не появилось"

@feature('Успешная отправка заявки из блока Outstaffing and outsourcing of IT-teams')
def test_web_outstaff_get_text(driver):
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


# либо тут проверку делать на заголовок и текст либо в другим похожим тестом.
def test_description_contains_value(driver):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.get_data_carousel()


def test_outstaff_team_and_spec_assert_data(driver):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.get_data_team_and_spec()



@feature('Проверка данных в карточках блока Why Godev is the right staff augmentation partner')
def test_outstaff_page_benefits_count_cards_assert(driver):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.get_data_card_tiles_outstaff()


@feature('Проверка данных в карточках блока How IT staff augmentation works')
def test_support_page_why_do_you_need_data_assert(driver):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.get_data_card_how_it_staff_outstaff()



@feature('Проверка данных в FAQ')
def test_outstaff_page_faq_data_assert(driver):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.get_data_faq_card_new()


@feature('Проверка данных в Benefits of team augmentation services')
def test_outstaff_page_web_development_process_data_assert(driver):
    outstaff_page_test = WebOutstaffPage(driver)
    outstaff_page_test.open()
    outstaff_page_test.get_data_advant_carousel_card()