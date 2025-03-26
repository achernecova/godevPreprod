import logging
import os

import allure

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret


class WebDevServicesPage(BasePage):

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)  # Передаем base_url в базовый класс
        self.subURL = os.getenv('WEB_DEV', 'services/web-development/')

    def get_popup(self):
        return PopupElement(self.driver)

    @allure.step("Открытие страницы лендинга по URL: services/web-development/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL


    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)


        # метод для черно-белых карточек
    def get_data_card_tiles_webdev(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('WEB_DEV', 'services/web-development/')
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
        base_url = put_a_secret()
        url = base_url + os.getenv('WEB_DEV', 'services/web-development/')
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_web_dev',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)
