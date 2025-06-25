import allure
import pytest

from pages.cms_page import CMSPage
from pages.web_design_page import WebDesignPage


# тест с мета-тегами вынесен в main_page_test

@allure.feature('Проверка данных в карточках блока Website packages')
def test_design_page_data_card_packages(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_card_design()

@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Custom design solutions')
def test_design_page_why_do_you_need_data_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_card("how_it_staff_design")

@pytest.mark.prod_test
@allure.feature('Проверка данных в FAQ')
def test_design_page_faq_data_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_card("accordeon_faq_design")


@pytest.mark.fill_form_request_faq
@allure.feature('Успешная отправка заявки из FAQ')
def test_design_page_add_request_in_faq(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.click_button_in_faq()
    popup_modal_page = design_page_test.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "


@allure.feature('Проверка заголовка и текста в блоке Website development')
def test_design_page_assert_title_and_text_block_website_dev(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_title_and_text_in_blocks("website_development_design")

@allure.feature('Проверка заголовка и текста в блоке Website design')
def test_design_page_assert_title_and_text_block_website_design(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_title_and_text_in_blocks("website_design")

@pytest.mark.prod_test
@allure.feature('Проверка заголовка и текста в блоке Custom design solutions')
def test_design_page_custom_design_solutions_title_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_title_and_text_in_blocks("custom_design_solutions")




