from allure_commons._allure import feature

from pages.mobile_dev_page import MobileDevPage

# тест с мета-тегами вынесен в main_page_test

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


@feature('Количество элементов в блоке')
def test_mobile_dev_page_count_card_advantages(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    blocks = mobile_page.get_count_elements()
    blocks.count_cards_assert("count_card_advantages", 7)


@feature('Проверка данных в карточках блока Benefits for business from creating a mobile application и We specialize in')
def test_mobile_page_why_do_you_need_data_assert(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.get_data_card_how_it_staff_mobile()


@feature('Проверка данных в FAQ')
def test_mobile_page_faq_data_assert(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.get_data_faq_card()