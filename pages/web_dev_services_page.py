from selenium.webdriver.common.by import By

from constants import URLs, subURLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from pages.base_page import BasePage
from utils.data_loader import load_file


class WebDevServicesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/web-development/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)


        # метод для черно-белых карточек
    def get_data_card_tiles_webdev(self):
        url = URLs.MAIN_PAGE + subURLs.WEB_DEV  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_webdev',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

# метод для faq
    def get_data_faq_card(self):
        url = URLs.MAIN_PAGE + subURLs.WEB_DEV  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_web_dev',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)
