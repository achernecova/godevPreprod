import logging

from constants import subURLs, URLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from test.locators import Locators


class MobileDevPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.MOBILE_PAGE

    def open(self):
        super().open(self.subURL)  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_popup(self):
        return PopupElement(self.driver)

    def click_button_banner(self):
        button_banner = self.wait_for_element(Locators.button_banner_locator)
        self.scroll_to_element(button_banner)
        self._click_element(button_banner)

    def click_button_in_card_select(self):
        button_in_card_select = self.wait_for_element(Locators.button_in_card_select_locator)
        self.scroll_to_element(button_in_card_select)
        button_in_card_select.click()

    def click_button_in_faq(self):
        button_in_faq = self.wait_for_element(Locators.button_in_faq_locator)
        self.scroll_to_element(button_in_faq)
        button_in_faq.click()



# метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_mobile(self):
        url = URLs.MAIN_PAGE+subURLs.MOBILE_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_mobile',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

# метод для faq
    def get_data_faq_card(self):
        url = URLs.MAIN_PAGE + subURLs.MOBILE_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_mobile',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)