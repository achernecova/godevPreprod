import allure
import pytest
from allure_commons._allure import feature, story

from pages.services_page import ServicesPage

@feature('Открытие страниц услуг')
@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("mobile_dev", "https://dev.godev.agency/services/mobile-development/", "Application development services"),
    ("website_dev", "https://dev.godev.agency/services/website-development/", "Website development"),
    ("support", "https://dev.godev.agency/services/tech-support/", "Maintenance and Support"),
    ("web_development", "https://dev.godev.agency/services/web-development/", "Web development services"),
    ("e_commerce", "https://dev.godev.agency/services/website-development/e-commerce/", "E-commerce web development for scalable business growth"),
    ("website_design", "https://dev.godev.agency/services/website-design-and-development-services/", "Website design and development services"),
    ("outstaffing", "https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", "IT Staff Augmentation")
])
def test_services_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    project_element = services_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

@feature('Добавление мета-тегов')
def test_services_page_add_title_descr_and_canonical(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    form_page_test = services_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "IT services for you and your business", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "In godev studio you can order the creation of a website, portal or application of any complexity. We use a wide technology stack", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@feature('Количество элементов в блоке')
def test_services_page_count_card_advantages_of_working(driver):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    blocks = services_page_test.get_count_elements()
    blocks.count_cards_assert("adv_item", 6)

@feature('Открытие страниц проектов')
@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement")
])
def test_services_page_click_project_and_open_pages(driver, card_type, expected_url, expected_title):
    services_page_test = ServicesPage(driver)
    services_page_test.open()
    project_element = services_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"