import logging

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from constants import subURLs, URLs
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class CMSPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.CMS_PAGE

    def open(self):
        super().open(self.subURL)  # Добавляем под-URL

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

    def click_button_tariff_table(self):
        button_tariff = self.driver.find_element(*Locators.button_tariff)
        self.scroll_to_element(button_tariff)
        self._click_element(button_tariff)


    def get_data_card_cms(self):
        url = URLs.MAIN_PAGE + subURLs.CMS_PAGE  # Укажите нужный URL
        self.get_data_card_(self.get_card_data, 'data_card_block_packages.json',
                                             'cms_card_data', url)


    def get_data_card_tiles_cms(self):
        url = URLs.MAIN_PAGE + subURLs.CMS_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tiles, 'data_card_block_packages.json',
                                    'tiles_section_card_data_cms', url)


# метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_cms(self):
        url = URLs.MAIN_PAGE + subURLs.CMS_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tiles_card, 'section_how_it_staff_tiles.json',
                                    'how_it_staff_cms', url)

