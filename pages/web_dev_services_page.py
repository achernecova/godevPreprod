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

    def get_data_card(self, card_type):
        config = {
            'card_tiles_web_dev_services': { # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_webdev',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'faq_card_web_dev_services': { # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_web_dev',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            }
        }
        if card_type not in config:
            raise ValueError(f"Такого блока не существует: {card_type}")
        # забираем нужный блок из списка config
        conf = config[card_type]
        url = self.get_base_url()
        # грузим данные, забирая конкретные параметры из нужного блока (отдаем файл, какой метод, ключ, локаторы)
        self.get_data_card_with_type_project(
            conf['file_load'],
            conf['url_method'],
            conf['json_key'],
            conf['locator_block'],
            conf['locator_element'],
            conf['locator_section'],
            url
        )

    def get_base_url(self):
        base_url = put_a_secret()
        return base_url + self.subURL