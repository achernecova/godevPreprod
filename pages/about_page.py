import logging
import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from utils.data_loader import load_file

class AboutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('ABOUT', 'about-us/')  # Значение по умолчанию

    @allure.step("Открытие страницы About по URL: about-us/")
    def open(self, sub_url=None):
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL

    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    @allure.step("Получаем заголовок блока")
    def get_header_block_left_img(self):
        title_element = self.driver.find_element(Locators.simple_section_title)
        if title_element is not None:
            title_text = title_element.text.strip()
            logging.info(f"Заголовок на странице: '{title_text}'")
            return title_text
        else:
            logging.error('Ошибка!!! Заголовок не найден.')
            return 'Ошибка!!!'