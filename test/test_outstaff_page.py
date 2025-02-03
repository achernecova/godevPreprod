import pytest

from pages.web_outstaff_page import WebOutstaffPage

def test_web_outstaff_add_title_and_descr(driver):
    web_outstaff_page_test = WebOutstaffPage(driver)
    web_outstaff_page_test.open()
    form_page_test = web_outstaff_page_test.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "IT staff augmentation company in USA, cost of outsorce tech teams and software developers", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "IT staff augmentation – hire tech teams and software developers for your projects with lower cost in USA. Software, databases, websites, applications, microservices, mobile applications", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"


def test_web_outstaff_add_success_request(driver):
    web_outstaff_page_test = WebOutstaffPage(driver)
    web_outstaff_page_test.open()
    web_outstaff_page_test.click_button_request_add()

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