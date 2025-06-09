import logging
import os

import allure

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage, put_a_secret
from test.locators import Locators


class FrameworkPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')  # Значение по умолчанию

    def get_popup(self):
        return PopupElement(self.driver)

    @allure.step("Открытие мобильной страницы по URL: services/website-development/framework/")
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

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def get_data_block_price(self, index, price_left_title, price_left_text, price_right_title, price_right_text):
        self.scroll_to_element(Locators.team_card)
        price_left_title_locator = self.driver.find_elements(*Locators.price_left_title_locator)
        price_left_text_locator = self.driver.find_elements(*Locators.price_left_text_locator)
        price_right_title_locator = self.driver.find_elements(*Locators.price_right_title_locator)
        price_right_text_locator = self.driver.find_elements(*Locators.price_right_text_locator)

        assert price_left_title_locator[
                   index - 1].text == price_left_title, f"Ожидался заголовок '{price_left_title}', но получен '{price_left_title_locator[index - 1].text}'"
        assert price_left_text_locator[
                   index - 1].text == price_left_text, f"Ожидался текст '{price_left_text}', но получен '{price_left_text_locator[index - 1].text}'"
        assert price_right_title_locator[
                   index - 1].text == price_right_title, f"Ожидался заголовок '{price_right_title}', но получен '{price_right_title_locator[index - 1].text}'"
        assert price_right_text_locator[
                   index - 1].text == price_right_text, f"Ожидался текст '{price_right_text}', но получен '{price_right_text_locator[index - 1].text}'"


    def get_data_card(self, card_type):
        config = {
            'faq_frame': {
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_framework',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'advant_frame': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'advantages_of_outsourcing_framework',
                'locator_block': "//*[@class='advantages-outsourcing__item']",
                'locator_element': ".//*[@class='advantages-outsourcing__text']" ,
                'locator_section': ".//*[@class='advantages-outsourcing__title']",
            },
            'how_it_staff_frame': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_framework',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
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


        # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = self.get_base_url()
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                          'advant_section_framework', url)

    def get_data_advant_card(self):
        url = self.get_base_url()
        self.get_data_advant_carousel(self.get_data_advant_section_card, 'advant_section_carousel.json',
                                          'advant_card_framework', url)

    def get_base_url(self):
        base_url = put_a_secret()
        return base_url + self.subURL