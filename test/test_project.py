import allure
import pytest
from allure_commons._allure import feature

from pages.project_page import ProjectPage

@feature('Открытие страниц проектов')
@pytest.mark.parametrize("project_type, expected_url, expected_title", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/","Building a robust logistics platform for Swift Logistic Solutions"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement")
])
def test_project_page_click_project_and_pen_pages(driver, project_type, expected_url, expected_title):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    project_element = project_page_test.get_project_service_element()
    page = project_element.test_click_card_and_open_page(project_type, expected_url, expected_title)
    assert driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{driver.current_url}'"
    assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

@feature('Добавление мета-тегов')
def test_project_page_add_title_descr_canonical(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    form_page_test = project_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Web Development and Designs Portfolio - Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Godev's portfolio consist of completed projects in Design and Web Development. We help clients grow and prosper for over 10 years", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/projects/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@feature('Количество элементов в блоке')
def test_project_page_count_card_reviews(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    blocks = project_page_test.get_count_elements()
    blocks.count_cards_assert("customer_reviews", 3)
