import allure
import pytest

from pages.cms_page import CMSPage
from utils.data_loader import load_service_data_review


# тест с мета-тегами вынесен в main_page_test

@allure.feature('Количество элементов в блоке Benefits of using content management systems (3д карточки')
def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('types_of_websites_count_card', 4)

@pytest.mark.prod_test
@allure.feature('Количество элементов в блоке Godev services (переключатель)')
def test_cms_page_cms_services_cards_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('cms_services_cards', 4)

@allure.feature('Количество элементов в блоке Benefits of choosing Godev (карусель)')
def test_cms_page_cms_types_of_it_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('types_of_it', 3)

@allure.feature('Количество элементов в блоке Developing a website based on an existing CMS (карточки с точками и порядковым номером)')
def test_cms_page_platforms_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert('platforms', 4)


# Загрузка данных из JSON-файла
@pytest.mark.prod_test
@allure.feature('Проверка открытия страниц проектов блока Our projects')
@pytest.mark.parametrize('card_type, expected_url, expected_title', load_service_data_review())
def test_cms_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    project_element = cms_page_test.get_project_service_element()
    page = project_element.click_card_and_open_page(card_type)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f'Получен Title: {page.get_title_page()}'



@allure.feature('Проверка данных в карточках блока Website packages')
def test_cms_page_data_card_packages(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.get_data_card_cms()

@pytest.mark.prod_test
@allure.feature('Проверка данных в карточках блока Digital Benefits of using content management systems')
def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.get_data_card('tiles_cms')


@allure.feature('Проверка данных в карточках блока Developing a website based on an existing CMS')
def test_cms_page_why_do_you_need_data_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.get_data_card('how_it_staff_cms')


@allure.feature('Успешная отправка заявки из верхнего баннера')
def test_cms_page_add_request_success(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.click_button_banner()
    form_page_test = cms_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@pytest.mark.fill_form_request_footer
@allure.feature('Успешная отправка заявки из футера')
def test_cms_page_fill_form_request_footer(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    form_page_test = cms_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@pytest.mark.parametrize("block_name, locator_name", [
    ("banner_title", "banner_title"),
    ("block_header", "project_title"),
    ("block_header", "technologies_title"),
    ("choose_number", "choose_smg_number"),
    ("mini_text_block", "choose_smg_text"),
    ("block_header", "title_block_custom_design_solutions_locator"),
    ("mini_text_block", "text_block_it_staff_locator"),
    ("header_tiles_card", "tiles_card_title_locator"),
    ("text_tiles_card", "tiles_card_text_locator"),
    ("header_tiles_card", "block_get_in_touch_text"),
    ("block_header", "title_block_stages_of_creating_locator"),
    ("mini_text_block", "text_block_stages_of_creating_locator"),
    ("block_header", "header_tiles_card"),
    ("text_tiles_card", "tiles_card_3d_text"),
])
@allure.feature('Проверка шрифтов в блоках')
def test_fonts(driver, block_name, locator_name):
    page = CMSPage(driver)
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