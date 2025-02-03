import pytest

from pages.web_develop_page import WebDevelopPage

def test_web_develop_page_title_descr_and_canonical(driver):
    web_dev_page = WebDevelopPage(driver)
    web_dev_page.open()
    form_page_test = web_dev_page.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Website Development Company in USA, Leading Web Design and Development Services Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Discover Godev, a leading web development company in the USA, offering top-notch web design and development services to elevate your online business. Professional web developers with 10+ years of experience.", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/website-development/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

def test_web_develop_page_count_card_how_me_make(driver):
    web_dev_page = WebDevelopPage(driver)
    web_dev_page.open()
    blocks = web_dev_page.get_count_elements()
    blocks.count_cards_assert("carousel_how_make", 6)

def test_web_develop_page_count_card_types_of_websites(driver):
    web_dev_page = WebDevelopPage(driver)
    web_dev_page.open()
    blocks = web_dev_page.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)

@pytest.mark.parametrize("project_type, expected_url, expected_title", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/","Building a robust logistics platform for Swift Logistic Solutions"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites")
])
def test_web_develop_page_click_project_open_page(driver, project_type, expected_url, expected_title):
    support_page_test = WebDevelopPage(driver)
    support_page_test.open()
    _element_test = support_page_test.get_project_service_element()
    _element_test.test_click_card_and_open_page(project_type, expected_url, expected_title)

