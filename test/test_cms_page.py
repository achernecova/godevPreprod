import pytest

from pages.cms_page import CMSPage

def test_cms_page_add_title_descr_and_canonical(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    form_page_test = cms_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Custom CMS Development Services in USA: Company for Your Website Needs", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Unlock your website's potential with our custom CMS development services in the USA. Tailored solutions to meet your business needs, backed by years of Godev's experience", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/website-development/cms/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement")
])
def test_cms_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    project_element = cms_page_test.get_project_service_element()
    project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)

def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 4)

def test_cms_page_cms_services_cards_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("cms_services_cards", 4)

def test_cms_page_cms_types_of_it_count_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_it", 3)

def test_cms_page_platforms_count_cards_assert(driver):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("platforms", 4)

#Надо подумать - выносить код этот в отдельный pageElement или нет. Он используется еще в mainPage
@pytest.mark.parametrize("project_type, experience, bullits, price, index", [
    ("E-Commerce", "3+ years of experience", "business / security / design", "30 $ / hour", "1"),
    ("Corporate", "3+ years of experience", "design / affordable price", "35 $ / hour", "2"),
    ("Online shops", "3+ years of experience", "business / security / design", "660 $ from", "3"),
    ("B2B sites", "3+ years of experience", "business / security / design", "3300 $ from", "4"),
    ("WordPress", "3+ years of experience", "design / affordable price", "390 $ from", "5"),
    ("OpenCart", "3+ years of experience", "design / affordable price", "650 $ from", "6"),
    ("Joomla", "3+ years of experience", "design / affordable price", "690 $ from", "7")
])
def test_main_page_data_card_packages(driver, project_type, experience, bullits, price, index):
    cms_page_test = CMSPage(driver)
    cms_page_test.open()
    cms_page_test.check_packages_data(project_type, experience, bullits, price, index)