import allure

from pages.cms_page import CMSPage
from pages.web_design_page import WebDesignPage


# тест с мета-тегами вынесен в main_page_test

@allure.feature('Количество элементов в блоке')
def test_design_page_benefits_count_cards_assert(driver):
    design_page_test = CMSPage(driver)
    design_page_test.open()
    blocks = design_page_test.get_count_elements()
    blocks.count_cards_assert('types_of_websites_count_card', 4)


@allure.feature('Проверка данных в карточках блока Website packages')
def test_design_page_data_card_packages(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_card_design()


@allure.feature('Проверка данных в карточках блока Custom design solutions')
def test_design_page_why_do_you_need_data_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_card_how_it_staff_design()


@allure.feature('Проверка данных в FAQ')
def test_design_page_faq_data_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()
    design_page_test.get_data_faq_card()