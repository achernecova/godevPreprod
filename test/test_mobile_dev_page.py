import time

from pages.mobile_dev_page import MobileDevPage

def test_mobile_dev_page_add_title_and_descr(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    form_page_test = mobile_page.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Mobile App Development Services in USA, Leading Mobile Application Development Company Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Transform your ideas into reality with our mobile app development services. As a leading mobile app development company, we specialize in custom solutions for iOS and Android, including cross-platform apps", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/mobile-development/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"


def test_mobile_dev_page_add_request_in_card_select(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.click_button_in_card_select()
    mobile_page.click_topping_dev_banner()
    mobile_page.input_name_in_banner()
    mobile_page.input_email_in_banner()
    mobile_page.input_comment_in_banner()
    mobile_page.click_button_in_banner()
    time.sleep(3)

def test_mobile_dev_page_add_request_in_faq(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.click_button_in_faq()
    mobile_page.click_topping_dev_banner()
    mobile_page.input_name_in_banner()
    mobile_page.input_email_in_banner()
    mobile_page.input_comment_in_banner()
    mobile_page.click_button_in_banner()
    time.sleep(3)

def test_mobile_dev_page_count_card_advantages(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    count_card = mobile_page.count_card_advantages()
    assert count_card == 7, f"Получено количество карточек:  {count_card}"