import logging

import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class MobileDevPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)  # Передаем base_url в базовый класс
        self.subURL = os.getenv('MOBILE_PAGE', 'services/mobile-development/')  # Значение по умолчанию

    @allure.step("Открытие мобильной страницы по URL: services/mobile-development/")
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

    def get_popup(self):
        return PopupElement(self.driver)

    def click_button_get_in_touch(self):
        self.click_body_element()
        # Находим элемент и ждем его кликабельности
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.close_modal)
        )
        # Находим элемент с помощью правильного метода
        click_button_banner = self.driver.find_element(*Locators.button_in_card_select_locator)

        # Используем новый метод для прокрутки
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_button_banner)

        # Находим элемент и ждем его кликабельности
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.close_modal)
        )
        # Кликаем по элементу
        self.driver.execute_script("arguments[0].click();", click_button_banner)

    # Метод для получения заголовка блока
    @allure.step("Получение заголовка из блока What we do")
    def get_title_block_what_we_do(self):
        self.scroll_to_element(Locators.title_block_app_and_web_development_services_locator)
        title = self.get_title_block_from_page_all(Locators.title_block_app_and_web_development_services_locator)
        return title

    # тянем данные из названия блока What we do
    @allure.step("Получение текста из блока What we do")
    def get_text_block_what_we_do(self):
        self.scroll_to_element(Locators.text_block_app_and_web_development_services_locator)
        text = self.get_text_block_from_page_all(Locators.text_block_app_and_web_development_services_locator)
        return text

    # Метод для получения заголовка блока Stages of creating
    @allure.step("Получение заголовка из блока Stages of creating")
    def get_title_block_stages_of_creating(self):
        self.scroll_to_element(Locators.title_block_stages_of_creating_locator)
        title = self.get_title_block_from_page_all(Locators.title_block_stages_of_creating_locator)
        return title

    # тянем данные из названия блока Stages of creating
    @allure.step("Получение текста из блока Stages of creating")
    def get_text_block_stages_of_creating(self):
        self.scroll_to_element(Locators.text_block_stages_of_creating_locator)
        text = self.get_text_block_from_page_all(Locators.text_block_stages_of_creating_locator)
        return text

    # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = self.get_base_url()
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                      'advant_card_mobile', url)
