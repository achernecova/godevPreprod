import logging
import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from test.locators import Locators



class LandingPage(BasePage):

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)  # Передаем base_url в базовый класс
        self.subURL = os.getenv('LANDING', 'services/development-of-a-landing-page/')  # Значение по умолчанию


    @allure.step("Открытие страницы лендинга по URL: /services/development-of-a-landing-page/")
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

    def get_popup_element(self):
        return PopupElement(self.driver)


        # метод для цветных карточек
    @allure.step("Получение данных из блока Boost your business with a landing page")
    def get_data_card_tile_squad(self):
        # Получаем базовый URL с помощью функции put_a_secret
        base_url = put_a_secret()
        url = base_url + os.getenv('LANDING', 'services/development-of-a-landing-page/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_card_data_tiles_card,
            'tile_squad',
            "//*[@class='tile-squad-item card']",
            './/h3',
            ".//*[@class='tile-squad-descr']",
            url)


        # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_landing(self):
        # Получаем базовый URL с помощью функции put_a_secret
        base_url = put_a_secret()
        url = base_url + os.getenv('LANDING', 'services/development-of-a-landing-page/')
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
        # Получаем базовый URL с помощью функции put_a_secret
        base_url = put_a_secret()
        url = base_url + os.getenv('LANDING', 'services/development-of-a-landing-page/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel,'advant_section_carousel.json', 'advant_section_landing', url)


        # метод для черно-белых карточек
    def get_data_card_tiles_landing(self):
        # Получаем базовый URL с помощью функции put_a_secret
        base_url = put_a_secret()
        url = base_url + os.getenv('LANDING', 'services/development-of-a-landing-page/')
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
        # Получаем базовый URL с помощью функции put_a_secret
        base_url = put_a_secret()
        url = base_url + os.getenv('LANDING', 'services/development-of-a-landing-page/')
        self.get_data_card_with_type_project_rates(self.get_card_data_rates, 'data_card_block_packages.json',
                                                 'card_data_rates_landing', url)

        # получение данных с карточек с отзывами

    def get_data_review_landing(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('LANDING', 'services/development-of-a-landing-page/')
        self.driver.get(url)
        # Явное ожидание, что элемент с классом 'reviews-wrapper' появится на странице
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'reviews-wrapper'))
        )
        # После этого можно извлекать данные, как и раньше
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json',
                              'reviews-wrapper', url)


    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)


    @allure.step("Кликаем по кнопке Get in touch в блоке Rates")
    def click_button_rates_landing(self):
        self.close_modal_popup()
        self.scroll_to_element(Locators.title_rates_locator)
        button = self.driver.find_element(*Locators.button_rates_locator)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.button_rates_locator)
        )
        if self.driver.execute_script("return arguments[0].getBoundingClientRect().height > 0;", button):
            self.driver.execute_script("arguments[0].click();", button)  # Клик через JS
        else:
            print("Элемент недоступен для клика")