import logging
import os

import allure

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators


class CMSPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('CMS_PAGE', 'services/website-development/cms/')  # Значение по умолчанию

    @allure.step("Открытие страницы лендинга по URL: services/website-development/cms/")
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
        self.scroll_new(Locators.button_banner_page)
        click_button_banner = self.driver.find_element(*Locators.button_banner_page)
        click_button_banner.click()

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def get_data_card_cms(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('CMS_PAGE', 'services/website-development/cms/')
        self.get_data_card_(self.get_card_data, 'data_card_block_packages.json',
                            'cms_card_data', url)

    def get_data_card_tiles_cms(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('CMS_PAGE', 'services/website-development/cms/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_cms',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_cms(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('CMS_PAGE', 'services/website-development/cms/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_cms',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)