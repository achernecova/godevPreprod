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

    @allure.step("Открытие страницы цмс по URL: services/website-development/cms/")
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

    def get_base_url(self):
        base_url = put_a_secret()
        return base_url + self.subURL

    def get_data_card_cms(self):
        url = self.get_base_url()
        self.get_data_card_(self.get_card_data, 'data_card_block_packages.json',
                            'cms_card_data', url)

    """ def get_data_card_tiles_cms(self):
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
    """

    def get_data_card(self, card_type):
        config = {
            'tiles_cms': {
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_cms',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'how_it_staff_cms': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_cms',
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