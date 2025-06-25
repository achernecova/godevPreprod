import json

import allure
import pytest

from pages.b2b_page import B2BPage
from utils.data_loader import load_service_data_review


# тест с мета-тегами вынесен в main_page_test

@allure.feature('Количество элементов в блоке B2B e-commerce platforms')
def test_b2b_page_platforms_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("platforms", 4)


@allure.feature('Количество элементов в блоке Benefits of a B2B e-commerce solution from Godev')
def test_b2b_page_benefits_count_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    blocks = b2b_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)


#загрузка данных из json файла
@pytest.mark.prod_test
@allure.feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", load_service_data_review())
def test_services_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    project_element = b2b_page_test.get_project_service_element()
    page = project_element.click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"


@allure.feature('Проверка данных в карточках блока Website packages')
def test_b2b_page_data_card_packages(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.get_data_card_b2b()


@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Benefits of a B2B e-commerce solution from Godev')
def test_b2b_page_benefits_data_cards_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.get_data_card("card_tiles_b2b")


@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока B2B e-commerce platforms')
def test_b2b_page_why_do_you_need_data_assert(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.get_data_card("how_it_staff_b2b")



@allure.feature('Успешная отправка заявки из баннера')
def test_b2b_page_add_request_success(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    b2b_page_test.click_button_banner()
    form_page_test = b2b_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@pytest.mark.fill_form_request_footer
@allure.feature('Успешная отправка заявки из футера')
def test_b2b_page_fill_form_request_footer(driver):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    form_page_test = b2b_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@pytest.mark.parametrize("block_name, locator_name", [
    ("banner_title", "banner_title"),
    ("block_header", "simple_section_title"),
    ("block_header", "title_block_custom_design_solutions_locator"),
    ("block_header", "project_title"),
    ("block_header", "technologies_title"),
    ("block_header", "title_block_stages_of_creating_locator"),
    ("text_block", "simple_section_text"),
    ("mini_text_block", "text_block_it_staff_locator"),
    ("mini_text_block", "text_block_stages_of_creating_locator"),
    ("header_tiles_card", "tiles_card_title_locator"),
    ("text_tiles_card", "tiles_card_text_locator"),
    ("button_text", "button_banner_services"),
    ("text_block", "team_card_name"),
    ("text_block", "team_card_text_in_card"),
    ("header_tiles_card", "tiles_card_header"),
    ("text_tiles_card", "tiles_card_text")
])
@allure.feature('Проверка шрифтов в блоках')
def test_fonts(driver, block_name, locator_name):
    page = B2BPage(driver)
    page.open()

    # Получаем атрибуты
    attributes = page.get_font_attributes1(locator_name, block_name)
    errors = []

    # Выполняем проверки и добавляем ошибки в список
    if attributes["color"] != attributes["expected_color"]:
        errors.append(
            f"Цвет не соответствует для {locator_name}: "
            f"ожидалось {attributes['expected_color']}, получено {attributes['color']}"
        )

    if attributes["expected_font_family"] not in attributes["font_family"]:
        errors.append(
            f"Шрифт не соответствует для {locator_name}: "
            f"ожидалось включение '{attributes['expected_font_family']}', "
            f"получено '{attributes['font_family']}'"
        )

    if attributes["font_size"] != attributes["expected_font_size"]:
        errors.append(
            f"Размер шрифта не соответствует для {locator_name}: "
            f"ожидалось {attributes['expected_font_size']}, получено {attributes['font_size']}"
        )

    # Если есть ошибки, выбрасываем исключение
    if errors:
        pytest.fail("; ".join(errors))
