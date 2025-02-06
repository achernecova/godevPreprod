from allure_commons._allure import feature

from pages.mobile_dev_page import MobileDevPage

@feature('Успешная отправка заявки')
def test_mobile_dev_page_add_request_in_card_select(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.click_button_in_card_select()
    popup_modal_page = mobile_page.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True , f"Не появилось окно успешности "

@feature('Успешная отправка заявки')
def test_mobile_dev_page_add_request_in_faq(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.click_button_in_faq()
    popup_modal_page = mobile_page.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "

@feature('Добавление мета-тегов')
def test_mobile_dev_page_add_title_and_descr(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    form_page_test = mobile_page.get_meta_data()
    assert form_page_test.get_title_ceo_page() == "Mobile App Development Services in USA, Leading Mobile Application Development Company Godev", f"Получен Title:  {form_page_test.get_title_ceo_page()}"
    assert form_page_test.get_descr_ceo_page() == "Transform your ideas into reality with our mobile app development services. As a leading mobile app development company, we specialize in custom solutions for iOS and Android, including cross-platform apps", f"Получен Title:  {form_page_test.get_descr_ceo_page()}"
    assert form_page_test.get_canonical_ceo_page() == "https://dev.godev.agency/services/mobile-development/", f"Получен canonical:  {form_page_test.get_canonical_ceo_page()}"

@feature('Количество элементов в блоке')
def test_mobile_dev_page_count_card_advantages(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    blocks = mobile_page.get_count_elements()
    blocks.count_cards_assert("count_card_advantages", 7)
