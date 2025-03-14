from allure_commons._allure import feature

from pages.mobile_dev_page import MobileDevPage

# тест с мета-тегами вынесен в main_page_test

@feature('Успешная отправка заявки из блока со сплошным текстом')
def test_mobile_dev_page_add_request_in_card_select(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.click_button_get_in_touch()
    popup_modal_page = mobile_page.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True , f"Не появилось окно успешности "

@feature('Успешная отправка заявки из FAQ')
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

@feature('Проверка заголовка в блоке What we do')
def test_mobile_page_what_we_do_title_assert(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    title_block = mobile_page.get_title_block_what_we_do()
    assert title_block == 'What we do', f"Получен Title:  {title_block}"


@feature('Проверка текста в блоке What we do')
def test_mobile_page_what_we_do_text_assert(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    text_block = mobile_page.get_text_block_what_we_do()
    assert text_block == 'We offer comprehensive mobile application development services that cover every aspect from design to maintenance. Our aim is to deliver reliable, scalable apps ready to perform in any market', f"Получен Title:  {text_block}"


@feature('Успешная отправка заявки из Development cost')
def test_mobile_dev_page_add_request_in_dev_coast(driver):
    mobile_page = MobileDevPage(driver)
    mobile_page.open()
    mobile_page.click_button_in_develop_table()
    popup_modal_page = mobile_page.get_popup()
    popup_modal_page.add_request_success()
    success = popup_modal_page.popup_success_displayed()
    assert success == True, f"Не появилось окно успешности "