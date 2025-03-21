import logging
import os

import allure

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.menu_element import MenuElement
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from test.locators import Locators


class D2C(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('D2C', 'services/website-development/d2c/')  # Значение по умолчанию

    @allure.step(
        "Кликаем по кнопке в баннере")
    def click_button_banner(self):
        click_button_banner = self.driver.find_element(*Locators.click_button_banner)
        click_button_banner.click()

    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_menu_element(self):
        return MenuElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)


    @allure.step("Открытие страницы лендинга по URL: /services/website-development/d2c/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL

        # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel,'advant_section_carousel.json', 'advant_section_d2c', url)

    # получение данных с карточек с отзывами
    def get_data_review(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json', 'reviews-wrapper', url)

    def get_data_card_website(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_card_(self.get_card_data, 'data_card_block_packages.json',
                            'web_site_develop_card_data', url)

# метод для черно-белых карточек
    def get_data_card_tiles_outstaff(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_d2c',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)