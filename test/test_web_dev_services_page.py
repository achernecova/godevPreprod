from pages.WebDevServicesPage import WebDevServicesPage
from pages.WebDevelopPage import WebDevelopPage


def test_web_develop_page_add_title_descr_and_canonical(driver):
    web_dev_page = WebDevServicesPage(driver)
    web_dev_page.open()
    form_page_test = web_dev_page.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Website Development Company in USA, Leading Web Design and Development Services Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Discover Godev, a leading web development company in the USA, offering top-notch web design and development services to elevate your online business. Professional web developers with 10+ years of experience.", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/web-development/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"


def test_web_develop_page_count_card_how_me_make(driver):
    web_dev_page = WebDevServicesPage(driver)
    web_dev_page.open()
    count_card = web_dev_page.carousel_how_make()
    assert count_card == 6, f"Получено количество карточек:  {count_card}"
