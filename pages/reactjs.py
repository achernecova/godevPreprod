import logging
import os
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators


class ReactjsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('REACTJS', 'services/web-development/reactjs/')  # Значение по умолчанию

    @allure.step("Открытие страницы лендинга по URL: services/web-development/reactjs/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL

    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)

    def click_button_banner(self):
        self.scroll_new(Locators.click_button_banner)
        click_button_banner = self.driver.find_element(*Locators.click_button_banner)
        click_button_banner.click()

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def get_popup(self):
        return PopupElement(self.driver)

        # метод для faq
    def get_data_faq_card(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('REACTJS', 'services/web-development/reactjs/')
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_reactjs',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)


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

# метод для черно-белых карточек
    def get_data_card_tiles_react(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('REACTJS', 'services/web-development/reactjs/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_react',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

        # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_react(self):
        # Получаем базовый URL с помощью функции put_a_secret
        base_url = put_a_secret()
        url = base_url + os.getenv('REACTJS', 'services/web-development/reactjs/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_react',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

    def get_data_card_app_and_web_services_react(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('REACTJS', 'services/web-development/reactjs/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'app_and_web_services_react',
            "//*[@class='service-item']",
            ".//*[@class='service-descr']",
            './/h3',
            url)

    def get_data_card_advant_of_outsource_react(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('REACTJS', 'services/web-development/reactjs/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'advantages_of_outsourcing_react',
            "//*[@class='advantages-outsourcing__item']",
            ".//*[@class='advantages-outsourcing__text']" ,
            ".//*[@class='advantages-outsourcing__title']" ,
            url)

    def get_data_card_best_framework_react(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('REACTJS', 'services/web-development/reactjs/')
        block_cards = Locators.block_cards_best_frameworks_item
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'best_framework_card_blocks_react',
            #"//*[contains(@class, 'best-frameworks__item ')]",
            block_cards,
            ".//*[@class='best-frameworks__item-text']" ,
            ".//*[@class='best-frameworks__item-title']" ,
            url)