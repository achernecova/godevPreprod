import pytest

from pages.e_com_page import EComPage


def test_cms_page_benefits_count_cards_assert(driver):
    cms_page_test = EComPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("types_of_websites_count_card", 7)

def test_cms_page_how_we_make_web_count_cards_assert(driver):
    cms_page_test = EComPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("how_we_make_web", 5)

def test_cms_page_our_proven_web_dev_count_cards_assert(driver):
    cms_page_test = EComPage(driver)
    cms_page_test.open()
    blocks = cms_page_test.get_count_elements()
    blocks.count_cards_assert("our_proven_web_dev", 7)

#Надо подумать - выносить код этот в отдельный pageElement или нет. Он используется еще в mainPage
@pytest.mark.parametrize("project_type, bullits, price, index", [
    ("E-commerce web development", "business / security / design", "30 $ / hour", "1"),
    ("E-commerce web design", "design / affordable price", "22 $ / hour", "2"),
    ("Online shops", "business / security / design", "660 $ from", "3"),
    ("Search engine optimization", "experience / affordable price", "2000 $ / month", "4"),
    ("Front-end development", "HTML / JavaScript / CSS", "30 $ / hour", "5"),
    ("Back-end development", "experience / knowledge / microservices", "30 $ / hour", "6")
])
def test_main_page_data_card_packages(driver, project_type, bullits, price, index):
    cms_page_test = EComPage(driver)
    cms_page_test.open()
    cms_page_test.check_packages_data_not_experience(project_type, bullits, price, index)

@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions")
])
def test_cms_page_click_services_and_project_and_open_pages(driver, card_type, expected_url, expected_title):
    cms_page_test = EComPage(driver)
    cms_page_test.open()
    project_element = cms_page_test.get_project_service_element()
    project_element.test_click_card_and_open_page(card_type, expected_url, expected_title)