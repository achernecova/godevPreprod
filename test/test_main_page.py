import time
import pytest
from pages.MainPage import MainPage

def test_add_request_success_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    popup_element_test = main_page_test.get_popup_element()
    popup_element_test.add_request_success("Test Name", "test@example.com", "This is a test message.")

def test_fill_form_request_footer_main_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    form_page_test = main_page_test.get_form_page()
    form_page_test.fill_form("Test Name", "test@example.com", "This is a test message.")

def test_main_page_add_title_descr_and_canonical(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    form_page_test = main_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Web Development Company in USA | Web Design, App & Web Development Services – Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Godev is a leading web development company in the USA. We specialize in custom web design, web applications, app and web development services", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

def test_main_page_add_request_header(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_button_banner()
    popup_element_test = main_page_test.get_popup_element()
    popup_element_test.add_request_success("Test Name 2", "test2@example.com", "This is a test message.")

@pytest.mark.parametrize("card_type, expected_url, expected_title", [
    ("mobile_dev", "https://dev.godev.agency/services/mobile-development/", "Application development services"),
    ("website_dev", "https://dev.godev.agency/services/website-development/", "Website development"),
    ("support", "https://dev.godev.agency/services/tech-support/", "Maintenance and Support"),
    ("web_development", "https://dev.godev.agency/services/web-development/", "Web development services"),
    ("e_commerce", "https://dev.godev.agency/services/website-development/e-commerce/", "E-commerce web development for scalable business growth"),
    ("website_design", "https://dev.godev.agency/services/website-design-and-development-services/", "Website design and development services"),
    ("outstaffing", "https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", "IT Staff Augmentation"),
    ("b2b", "https://dev.godev.agency/services/website-development/b2b/", "B2B e-commerce website development"),
    ("section_outstaffing", "https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", "IT Staff Augmentation")

])
def test_main_page_click_card_and_open_pages(driver, card_type, expected_url, expected_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.test_click_card_and_open_page(card_type, expected_url, expected_title)

@pytest.mark.parametrize("project_type, expected_url, expected_title, index", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign", "1"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites", "5"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company", "2"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/", "Building a robust logistics platform for Swift Logistic Solutions", "4"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement", "3")
])
def test_main_page_click_project_and_open_pages(driver, project_type, expected_url, expected_title, index):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.test_click_project_and_open_page(project_type, expected_url, expected_title)

def test_main_page_count_card_reviews(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    assert main_page_test.count_customer_reviews() == 3, f"Получено количество карточек:  {main_page_test.count_customer_reviews()}"

def test_main_page_count_card_packages(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    assert main_page_test.web_packages_count() == 9, f"Получено количество карточек:  {main_page_test.web_packages_count()}"

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

@pytest.mark.parametrize("index, page_url, page_title", [
    ("1", "https://dev.godev.agency/services/website-development/e-commerce/", "E-commerce web development for scalable business growth"),
    ("2", "https://dev.godev.agency/services/website-development/b2b/", "B2B e-commerce website development"),
    ("3", "https://dev.godev.agency/services/website-development/framework/", "What is a framework and why it’s essential for web development")
])
def test_main_page_click_more_packages_and_data_pages(driver, index, page_url, page_title):
    main_page_test = MainPage(driver)
    main_page_test.open()
    main_page_test.click_more_packages_and_data_pages(index, page_url, page_title)
