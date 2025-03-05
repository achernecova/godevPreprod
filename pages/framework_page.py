import logging

from constants import subURLs, URLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData

from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class FrameworkPage(BasePage):

    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.FRAMEWORK_PAGE

    def open(self):
        super().open(self.subURL)  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def get_data_block_price(self, index, price_left_title, price_left_text, price_right_title, price_right_text):
        team_card = self.driver.find_element(*Locators.team_card)
        self.scroll_to_element(team_card)
        price_left_title_locator = self.driver.find_elements(*Locators.price_left_title_locator)
        price_left_text_locator = self.driver.find_elements(*Locators.price_left_text_locator)
        price_right_title_locator = self.driver.find_elements(*Locators.price_right_title_locator)
        price_right_text_locator = self.driver.find_elements(*Locators.price_right_text_locator)

        assert price_left_title_locator[index - 1].text == price_left_title, f"Ожидался заголовок '{price_left_title}', но получен '{price_left_title_locator[index - 1].text}'"
        assert price_left_text_locator[index - 1].text == price_left_text, f"Ожидался текст '{price_left_text}', но получен '{price_left_text_locator[index - 1].text}'"
        assert price_right_title_locator[index - 1].text == price_right_title, f"Ожидался заголовок '{price_right_title}', но получен '{price_right_title_locator[index - 1].text}'"
        assert price_right_text_locator[index - 1].text == price_right_text, f"Ожидался текст '{price_right_text}', но получен '{price_right_text_locator[index - 1].text}'"

# метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_framework(self):
        url = URLs.MAIN_PAGE + subURLs.FRAMEWORK_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tiles_card, 'section_how_it_staff_tiles.json',
                                    'how_it_staff_framework', url)


        # метод для faq
    def get_data_faq_card(self):
        url = URLs.MAIN_PAGE+subURLs.FRAMEWORK_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_data_faq, 'faq_block_data.json', 'faq_framework', url)