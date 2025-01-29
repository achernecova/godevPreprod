import pytest

from pages.ProjectPage import ProjectPage


@pytest.mark.parametrize("project_type, expected_url, expected_title, index", [
    ("euro_VPN", "https://dev.godev.agency/projects/information-security-service/", "Information security service redesign", "1"),
    ("vegan_hotel", "https://dev.godev.agency/projects/vegan-hotel/", "Website development for a conceptual hotel in the Dolomites", "2"),
    ("find_a_builder", "https://dev.godev.agency/projects/find-a-builder/", "Website development for London construction company", "3"),
    ("sls", "https://dev.godev.agency/projects/swift-logistic-solutions/","Building a robust logistics platform for Swift Logistic Solutions", "4"),
    ("mint_link", "https://dev.godev.agency/projects/mint-links/", "Enhancing Mint Link’s MICE platform for optimal user engagement", "5")
])
def test_project_page_click_project_and_open_pages(driver, project_type, expected_url, expected_title, index):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    project_page_test.click_project(index)
    project_page_test.assert_data_page(expected_url, expected_title)

def test_project_page_add_title_descr_canonical(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    form_page_test = project_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Web Development and Designs Portfolio - Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Godev's portfolio consist of completed projects in Design and Web Development. We help clients grow and prosper for over 10 years", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/projects/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

def test_project_page_count_card_reviews(driver):
    project_page_test = ProjectPage(driver)
    project_page_test.open()
    blocks = project_page_test.get_count_elements()
    blocks.count_cards_assert("customer_reviews", 3)
