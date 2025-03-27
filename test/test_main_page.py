import pytest
from allure_commons._allure import link, feature

from pages.main_page import MainPage
from utils.data_loader import load_package_data_main
from utils.page_factory import get_page_instance


# Загрузка данных из JSON-файла с фильтрацией
@pytest.mark.parametrize('package_data', load_package_data_main())
@pytest.mark.prod_test
def test_main_page_data_card_packages(driver, package_data):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.check_packages_data(package_data.project_type, package_data.experience, package_data.bullits,
                                       package_data.price, package_data.text)


@feature('Успешная отправка заявки из баннера')
def test_add_request_success_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    form_page_test = main_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@pytest.mark.fill_form_request_footer
@feature('Успешная отправка заявки из футера')
def test_fill_form_request_footer_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    form_page_test = main_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@feature('Успешная отправка заявки из блока Get in touch')
def test_main_page_add_request_header(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_get_in_touch()
    popup_element_test = main_page_test.get_popup_element()
    popup_element_test.add_request_success()
    assert popup_element_test.popup_success_displayed() == True, 'Окно подтверждения не появилось'


@link(url='https://team-v5ka.testit.software/projects/664/tests/759', name='Отображение блока Customer Reviews')
@feature('Количество элементов в блоке')
@pytest.mark.prod_test
def test_main_page_count_card_reviews(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    blocks = main_page_test.get_count_elements()
    blocks.count_cards_assert('customer_reviews', 3)


# забираем title из блока с каруселью отзывов
@link(url='https://team-v5ka.testit.software/projects/664/tests/759', name='Отображение блока Customer Reviews')
@feature('Получение заголовка карусели')
def test_main_page_get_title_carousel(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.get_data_title_carousel()


@feature('Проверка данных в карусели с отзывами')
def test_main_page_count_card_reviews(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.get_data_review()


@feature('Количество элементов в блоке')
def test_main_page_count_card_packages(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    blocks = main_page_test.get_count_elements()
    blocks.count_cards_assert('web_packages_count', 9)


@link(url='https://team-v5ka.testit.software/projects/664/tests/908',
      name='Корректно указаны title, description, canonical ')
@feature('Добавление мета-тегов')
@pytest.mark.prod_test
def test_page_meta_data(driver, meta_data):
    main_page_test = get_page_instance(meta_data['page'], driver)
    main_page_test.open()
    form_page_test = main_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == meta_data[
        'title'], f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == meta_data[
        'description'], f"Получен Description:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == meta_data[
        'canonical'], f"Получен Canonical:  {form_page_test.get_canonical_ceo_page()}"

    # скрытие констант в фикстуру


@link(url='https://team-v5ka.testit.software/projects/664/tests/907',
      name='Отображение блока App and Web Development Services и переходы на страницы')
@feature('Открытие страниц услуг')
@pytest.mark.prod_test
def test_main_page_click_more_packages_and_data_pages(driver, test_data):
    index, page_url, page_title = test_data
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_more_packages_and_data_pages(index, page_url, page_title)


@feature('Проверка данных в карточках блока Digital Agency Godev')
def test_main_page_benefits_count_cards_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.get_data_card_tiles_main()


@feature('Проверка данных в карточках блока IT staff augmentation')
def test_main_page_why_do_you_need_data_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.get_data_card_how_it_staff_main()


@pytest.mark.prod_test
@feature('Проверка данных в карточках блока Web Development Process')
def test_main_page_web_development_process_data_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.get_data_advant_carousel_card()


@pytest.mark.prod_test
@feature('Проверка заголовка и текста в блоке App and Web Development Services')
def test_main_page_app_and_web_title_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    errors = []
    title_block = main_page_test.get_title_block_app_and_web_development_services()
    if title_block != 'App and Web Development Services':
        errors.append(f"Ошибка заголовка. Получен Title: {title_block}")
    text_block = main_page_test.get_text_block_app_and_web_development_services()
    if text_block != 'With a development team of 80 in-house specialists, we provide a variety of services related to online business practices, starting from web design and ending with creating brand-new downloadable apps':
        errors.append(f"Ошибка текста. Получен текст: {text_block}")
        # Если есть ошибки, выводим их
    if errors:
        pytest.fail("\n".join(errors))


@pytest.mark.prod_test
@feature('Проверка заголовка и текста в блоке IT staff augmentation')
def test_main_page_it_staff_title_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    errors = []
    title_block = main_page_test.get_title_block_it_staff()
    if title_block != 'IT staff augmentation':
        errors.append(f"Ошибка заголовка. Получен Title: {title_block}")
    text_block = main_page_test.get_text_block_it_staff()
    if text_block != 'Godev offers outsourcing services: allow yourself more. Experienced programmers at affordable prices: Middle and Senior levels':
        errors.append(f"Ошибка текста. Получен текст: {text_block}")
        # Если есть ошибки, выводим их
    if errors:
        pytest.fail("\n".join(errors))


@feature('Проверка заголовка и текста в блоке Web Development Process')
def test_main_page_web_dev_process_title_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    errors = []
    title_block = main_page_test.get_title_block_web_dev_process()
    if title_block != 'Web Development Process':
        errors.append(f"Ошибка заголовка. Получен Title: {title_block}")
    text_block = main_page_test.get_text_block_web_dev_process()
    if text_block != 'Godev has a comprehensive approach to creating software for our clients. Let us break down the main stages of the development cycle for a web application':
        errors.append(f"Ошибка текста. Получен текст: {text_block}")
        # Если есть ошибки, выводим их
    if errors:
        pytest.fail("\n".join(errors))


@pytest.mark.prod_test
@feature('Проверка заголовка и текста в блоке Digital Agency Godev')
def test_main_page_digital_agency_godev_title_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    errors = []
    title_block = main_page_test.get_title_block_digital_agency_godev()
    if title_block != 'Digital Agency Godev':
        errors.append(f"Ошибка заголовка. Получен Title: {title_block}")
    text_block = main_page_test.get_text_block_digital_agency_godev()
    if text_block != 'Selecting the right staff augmentation partner is crucial to your project’s success. Godev is a top-tier provider of staff augmentation services with several key advantages:':
        errors.append(f"Ошибка текста. Получен текст: {text_block}")
        # Если есть ошибки, выводим их
    if errors:
        pytest.fail("\n".join(errors))


@pytest.mark.prod_test
@feature('Проверка данных в карточках блока App and Web Development Services')
def test_landing_page_why_do_you_need_data_assert(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.get_data_card_app_and_web_services_main()
