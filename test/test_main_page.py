import pytest
from allure_commons._allure import link, feature

from pages.main_page import MainPage


@feature('Успешная отправка заявки')
def test_add_request_success_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    form_page_test = main_page_test.get_popup_element()
    form_page_test.add_request_success()
    assert form_page_test.popup_success_displayed() == True, "Окно не появилось"

@feature('Успешная отправка заявки')
def test_fill_form_request_footer_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    form_page_test = main_page_test.get_form_page()
    form_page_test.fill_form()
    assert form_page_test.popup_success_displayed()==True, "Окно не появилось"

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

@link(url='https://team-v5ka.testit.software/projects/664/tests/746', name='Отображение блока IT staff augmentation и переход на страницу')
@feature('Открытие страниц услуг')
@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("mobile_dev", "https://dev.godev.agency/services/mobile-development/", "Application development services"),
    ("website_dev", "https://dev.godev.agency/services/website-development/", "Website development"),
    ("support", "https://dev.godev.agency/services/tech-support/", "Maintenance and Support"),
    ("web_development", "https://dev.godev.agency/services/web-development/", "Web development services"),
    ("e_commerce", "https://dev.godev.agency/services/website-development/e-commerce/", "E-commerce web development for scalable business growth"),
    ("website_design", "https://dev.godev.agency/services/website-design-and-development-services/", "Website design and development services"),
    ("outstaffing", "https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", "IT Staff Augmentation"),
    ("b2b", "https://dev.godev.agency/services/website-development/b2b/", "B2B e-commerce website development"),
    ("section_outstaffing", "https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", "IT Staff Augmentation"),
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement")
])
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    project_element = main_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

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

@link(url='https://team-v5ka.testit.software/projects/664/tests/758', name='Отображение таблицы Website Packages')
@pytest.mark.parametrize("project_type, experience, bullits, price, index", [
    ("E-Commerce", "3+ years of experience", "business / security / design", "30 $ / hour", "1"),
    ("Corporate", "3+ years of experience", "design / affordable price", "35 $ / hour", "2"),
    ("Landing", "3+ years of experience", "design / affordable price", "30 $ / hour", "3"),
    ("Online Shops", "3+ years of experience", "business / security / design", "660 $ from", "4"),
    ("Web Portals", "3+ years of experience", "workload / security / design", "2000 $ from", "5"),
    ("B2B Sites", "3+ years of experience", "business / security / design", "3300 $ from", "6"),
    ("WordPress", "3+ years of experience", "design / affordable price", "390 $ from", "7"),
    ("Framework-Based Sites", "3+ years of experience", "workload / security / design", "33 $ / hour", "8"),
    ("Joomla", "3+ years of experience", "design / affordable price", "650 $ from", "9")
])
def test_main_page_data_card_packages(driver, project_type, experience, bullits, price, index):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.check_packages_data(project_type, experience, bullits, price, index)

@link(url='https://team-v5ka.testit.software/projects/664/tests/907', name='Отображение блока App and Web Development Services и переходы на страницы')
@pytest.mark.parametrize("index, page_url, page_title", [
    ("1", "https://dev.godev.agency/services/website-development/e-commerce/", "E-commerce web development for scalable business growth"),
    ("2", "https://dev.godev.agency/services/website-development/b2b/", "B2B e-commerce website development"),
    ("3", "https://dev.godev.agency/services/website-development/framework/", "What is a framework and why it’s essential for web development")
])
def test_main_page_click_more_packages_and_data_pages(driver, index, page_url, page_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_more_packages_and_data_pages(index, page_url, page_title)

