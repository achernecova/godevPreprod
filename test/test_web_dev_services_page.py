import pytest

from pages.web_dev_services_page import WebDevServicesPage

def test_web_dev_serv_page_add_title_descr_and_canonical(driver):
    web_dev_serv_page = WebDevServicesPage(driver)
    web_dev_serv_page.open()
    data_meta_page_test = web_dev_serv_page.get_meta_data()
    assert data_meta_page_test.get_title_ceo_page() == "Web Development Services in USA, Custom Website and Web App Development Solutions | Godev", f"Получен Title:  {data_meta_page_test.get_title_ceo_page()}"
    assert data_meta_page_test.get_descr_ceo_page() == "Looking for expert web development services in the USA? Godev offers high-quality, custom website development and responsive web design solutions tailored to your needs.", f"Получен Title:  {data_meta_page_test.get_descr_ceo_page()}"
    assert data_meta_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/web-development/", f"Получен canonical:  {data_meta_page_test.get_canonical_ceo_page()}"

def test_web_dev_serv_page_count_card_services(driver):
    web_dev_serv_page = WebDevServicesPage(driver)
    web_dev_serv_page.open()
    blocks = web_dev_serv_page.get_count_elements()
    blocks.count_cards_assert("web_dev_services", 12)

@pytest.mark.parametrize("index, project_type, price", [
    (0, "Web App development", "3000 $\nfrom"),
    (1, "Design and redesign", "1000 $\nfrom"),
    (2, "E-Commerce Web Development", "3000 $\nfrom "),
    (3, "CMS-based projects", "2000 $\nfrom "),
    (4, "Technical assistance and web project scaling", "600 $\nfrom "),
    (5, "Frontend development", "30 $\n/ hour"),
    (6, "Backend development", "30 $\n/ hour"),
    (7, "UI design", "1000 $\nfrom "),
    (8, "UX development", "1000 $\nfrom "),
    (9, "Performance optimization", "600 $\nfrom "),
    (10, "Web App security", "100 $\nfrom "),
    (11, "Testing", "28 $\n/ hour")
])
def test_web_dev_serv_page_data_card_packages(driver, index, project_type, price):
    web_dev_serv_page = WebDevServicesPage(driver)
    web_dev_serv_page.open()
    blocks = web_dev_serv_page.get_count_elements()
    blocks.check_packages_data_services(index, project_type, price)

