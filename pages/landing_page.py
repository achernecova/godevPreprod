import logging

import requests
from bs4 import BeautifulSoup

from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from constants import URLs, subURLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from test.locators import Locators
from utils.data_loader import load_file


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/development-of-a-landing-page/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)


        # метод для цветных карточек
    def get_data_card_tile_squad(self):
        url = URLs.MAIN_PAGE + subURLs.LANDING  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tile_squad, 'data_card_block_packages.json',
                                                 'tile_squad', url)


        # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_landing(self):
        url = URLs.MAIN_PAGE+subURLs.LANDING  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_landing',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

        # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = URLs.MAIN_PAGE+subURLs.LANDING
        self.get_data_advant_carousel(self.get_data_advant_section_carousel,'advant_section_carousel.json', 'advant_section_landing', url)


        # метод для черно-белых карточек
    def get_data_card_tiles_landing(self):
        url = URLs.MAIN_PAGE+subURLs.LANDING  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_landing',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)


        # метод для карточек в блоке rates
    def get_data_card_rates_landing(self):
        url = URLs.MAIN_PAGE+subURLs.LANDING  # Укажите нужный URL
        self.get_data_card_with_type_project_rates(self.get_card_data_rates, 'data_card_block_packages.json',
                                                 'card_data_rates_landing', url)

        # получение данных с карточек с отзывами
    def get_data_review_landing(self):
        url = URLs.MAIN_PAGE + subURLs.LANDING
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json',
                                  'reviews-wrapper', url)


    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)


    def click_button_rates_landing(self):
        button = self.driver.find_element(*Locators.button_rates_locator)
        self.scroll_to_element(button)
        button.click()