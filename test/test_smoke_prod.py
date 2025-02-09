import allure
import pytest
from allure_commons._allure import feature, link

from pages.b2b_page import B2BPage
from pages.cms_page import CMSPage
from pages.e_com_page import EComPage
from pages.main_page import MainPage
from pages.project_page import ProjectPage
from pages.web_outstaff_page import WebOutstaffPage


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
    assert form_page_test.get_canonical_ceo_page() == "https://godev.agency/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@link(url='https://team-v5ka.testit.software/projects/664/tests/746', name='Отображение блока IT staff augmentation и переход на страницу')
@feature('Открытие страниц услуг')
@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("mobile_dev", "https://godev.agency/services/mobile-development/", "Application development services"),
    ("website_dev", "https://godev.agency/services/website-development/", "Website development"),
    ("support", "https://godev.agency/services/tech-support/", "Maintenance and Support"),
    ("web_development", "https://godev.agency/services/web-development/", "Web development services"),
    ("e_commerce", "https://godev.agency/services/website-development/e-commerce/", "E-commerce web development for scalable business growth"),
    ("website_design", "https://godev.agency/services/website-design-and-development-services/", "Website design and development services"),
    ("outstaffing", "https://godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", "IT Staff Augmentation"),
    ("b2b", "https://godev.agency/services/website-development/b2b/", "B2B e-commerce website development"),
    ("section_outstaffing", "https://godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", "IT Staff Augmentation"),
    ("euro_VPN", "https://godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions"),
    ("mint_link", "https://godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement")
])
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    project_element = main_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("euro_VPN", "https://godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions"),
    ("mint_link", "https://godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement")
])
def test_main_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    b2b_page_test = B2BPage(driver)
    b2b_page_test.open()
    project_element = b2b_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

@feature('Добавление мета-тегов')
def test_project_page_add_title_descr_canonical(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    form_page_test = project_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Web Development and Designs Portfolio - Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Godev's portfolio consist of completed projects in Design and Web Development. We help clients grow and prosper for over 10 years", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://godev.agency/projects/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@allure.feature('Количество элементов в блоке')
def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 4)

@allure.feature('Количество элементов в блоке')
def test_cms_page_cms_services_cards_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("cms_services_cards", 4)

#Надо подумать - выносить код этот в отдельный pageElement или нет. Он используется еще в mainPage
@pytest.mark.parametrize("project_type, bullits, price, index", [
    ("E-commerce web development", "business / security / design", "30 $ / hour", "1"),
    ("E-commerce web design", "design / affordable price", "22 $ / hour", "2"),
    ("Online shops", "business / security / design", "660 $ from", "3"),
    ("Search engine optimization", "experience / affordable price", "2000 $ / month", "4"),
    ("Front-end development", "HTML / JavaScript / CSS", "30 $ / hour", "5"),
    ("Back-end development", "experience / knowledge / microservices", "30 $ / hour", "6")
])
def test_e_com_page_data_card_packages(driver, project_type, bullits, price, index):
    e_com_page_test = EComPage(driver)
    e_com_page_test.open()
    e_com_page_test.check_packages_data_not_experience(project_type, bullits, price, index)

@pytest.mark.parametrize("project_type, experience, bullits, price, index", [
    ("Backend", "3+ years of experience", "middle / middle+ / senior", "30$ / hour", "1"),
    ("Mobile", "3+ years of experience", "middle / middle+ / senior", "35$ / hour", "2"),
    ("Frontend", "3+ years of experience", "middle / middle+ / senior", "30$ / hour", "3"),
    ("Analysts", "3+ years of experience", "middle / middle+ / senior", "26$ / hour", "4"),
    ("Design", "3+ years of experience", "middle / middle+ / senior", "22$ / hour", "5"),
    ("Testers", "3+ years of experience", "middle / middle+ / senior", "28$ / hour", "6")
])
def test_main_page_data_card_packages(driver, project_type, experience, bullits, price, index):
    main_page_test = WebOutstaffPage(driver)
    main_page_test.open()
    main_page_test.check_packages_data(project_type, experience, bullits, price, index)

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