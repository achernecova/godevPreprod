from allure_commons._allure import link, feature
import pytest

from utils.data_loader import load_package_data_main
from utils.page_factory import get_page_instance
from pages.main_page import MainPage

# Загрузка данных из JSON-файла с фильтрацией
load_package_data = load_package_data_main()
@pytest.mark.parametrize("package_data", load_package_data)
def test_main_page_data_card_packages(driver, package_data):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.check_packages_data(package_data.project_type, package_data.experience, package_data.bullits,
                                       package_data.price)


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
    assert form_page_test.popup_success_displayed() == True, "Окно подтверждения не появилось"


@feature('Успешная отправка заявки')
def test_main_page_add_request_header(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    popup_element_test = main_page_test.get_popup_element()
    popup_element_test.add_request_success()
    assert popup_element_test.popup_success_displayed() == True, "Окно подтверждения не появилось"


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


@link(url='https://team-v5ka.testit.software/projects/664/tests/908',
      name='Корректно указаны title, description, canonical ')
@feature('Добавление мета-тегов')
def test_page_meta_data(driver, meta_data):
    main_page_test = get_page_instance(meta_data["page"], driver)
    main_page_test.open()
    form_page_test = main_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == meta_data[
        "title"], f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == meta_data[
        "description"], f"Получен Description:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == meta_data[
        "canonical"], f"Получен Canonical:  {form_page_test.get_canonical_ceo_page()}"


    # скрытие констант в фикстуру
@link(url='https://team-v5ka.testit.software/projects/664/tests/907',
      name='Отображение блока App and Web Development Services и переходы на страницы')
@feature('Открытие страниц услуг')
def test_main_page_click_more_packages_and_data_pages(driver, test_data):
    index, page_url, page_title = test_data
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_more_packages_and_data_pages(index, page_url, page_title)
