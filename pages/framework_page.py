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

    # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_framework(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')

        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_framework',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)


        # метод для faq
    def get_data_faq_card_new(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_framework',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)


    def get_data_card_advant_of_outsource_frame(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'advantages_of_outsourcing_framework',
            "//*[@class='advantages-outsourcing__item']",
            ".//*[@class='advantages-outsourcing__text']" ,
            ".//*[@class='advantages-outsourcing__title']" ,
            url)


        # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                          'advant_section_framework', url)

    def get_data_advant_card(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')
        self.get_data_advant_carousel(self.get_data_advant_section_card, 'advant_section_carousel.json',
                                          'advant_card_framework', url)