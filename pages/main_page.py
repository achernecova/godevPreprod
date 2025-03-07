import logging

import requests
from bs4 import BeautifulSoup

from constants import URLs, subURLs
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.menu_element import MenuElement
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class MainPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.driver = driver

    def click_button_banner(self):
        click_button_banner = self.driver.find_element(*Locators.click_button_banner)
        click_button_banner.click()

    def open(self):
        super().open('')  # Добавляем под-URL

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

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        self.team_card_more = self.driver.find_element(*Locators.get_team_card_more_locator(index))
        self.scroll_to_element(self.team_card_more)
        self.team_card_more.click()
        self.title_page = self.driver.find_element(*Locators.title_page)
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"

    def get_data_title_carousel(self):
        # грузим данные из json
        data = load_file('carousel_of_review.json')

        # получаем описания со страницы
        title_block_from_page = self.get_title_block_from_page(URLs.MAIN_PAGE)

        # берем данные из секции reviews_wrapper
        reviews_wrapper = data['reviews-wrapper']
        # отладочное.
        logging.info(f"Заголовок из JSON: " + reviews_wrapper['title'])
        logging.info(f"Заголовок на странице: {title_block_from_page}")
        # проверяем данные
        assert reviews_wrapper['title'] in title_block_from_page, \
            f"Заголовок не найден на странице: {reviews_wrapper['title']}"

    # тянем данные из названия блока
    def get_title_block_from_page(self, url):
        title_element = self.driver.find_element(*Locators.title_element)

        if title_element is not None:
            title_text = title_element.text.strip()
            logging.info(f"Заголовок на странице: '{title_text}'")
            return title_text
        else:
            logging.error('Ошибка!!! Заголовок не найден.')
            return 'Ошибка!!!'

    # получение данных с карточек с отзывами
    def get_data_review(self):
        url = URLs.MAIN_PAGE
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json',
                              'reviews-wrapper', url)

    # метод для черно-белых карточек
    def get_data_card_tiles_main(self):
        url = URLs.MAIN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_main',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_main(self):
        url = URLs.MAIN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_main',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

    # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = URLs.MAIN_PAGE
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                      'advant_section', url)
