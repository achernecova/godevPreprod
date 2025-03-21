import allure
import pytest

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
def test_design_page_app_and_web_title_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()

    # Список для сбора ошибок
    errors = []
    title_block = design_page_test.get_title_block_website_dev()
    if title_block != 'Website development':
        errors.append(f"Ошибка заголовка. Получен Title: {title_block}")
    text_block = design_page_test.get_text_block_website_dev()
    if text_block !=  'Our website development services include crafting customized sites and web apps. Godev can build the website from scratch or rework an existing platform to make it optimized for lead generation':
        errors.append(f"Ошибка текста. Получен текст: {text_block}")
    # Если есть ошибки, выводим их
    if errors:
        pytest.fail("\n".join(errors))


@allure.feature('Проверка заголовка в блоке Website design')
def test_design_page_web_site_design_title_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()

    # Список для сбора ошибок
    errors = []
    title_block = design_page_test.get_title_block_website_design()
    if title_block != 'Website design':
        errors.append(f"Ошибка заголовка. Получен Title: {title_block}")

    text_block = design_page_test.get_text_block_website_design()
    if text_block != 'Godev keeps up with all the main industry trends and we always strive to provide individual results to each client. Our team does its best to both follow the general industry trends to match the expectations of the customers, where the resulting design also has a unique twist to it':
        errors.append(f"Ошибка текста. Получен текст: {text_block}")

    # Если есть ошибки, выводим их
    if errors:
        pytest.fail("\n".join(errors))


@allure.feature('Проверка заголовка в блоке Custom design solutions')
def test_design_page_custom_design_solutions_title_assert(driver):
    design_page_test = WebDesignPage(driver)
    design_page_test.open()

    # Список для сбора ошибок
    errors = []
    title_block = design_page_test.get_title_block_custom_design_solutions()
    if title_block != 'Custom design solutions':
        errors.append(f"Ошибка заголовка. Получен Title: {title_block}")

    text_block = design_page_test.get_text_block_custom_design_solutions()
    if text_block != 'We create customized designs that are tailored to reflect your brand’s identity with a heavy focus on individually adapting them for every client. The resulting project represents the key values of the business, while also pleasing its visitors with appealing aesthetics':
        errors.append(f"Ошибка текста. Получен текст: {text_block}")

    # Если есть ошибки, выводим их
    if errors:
        pytest.fail("\n".join(errors))
