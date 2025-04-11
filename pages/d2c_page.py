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


class D2CPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('D2C', 'services/website-development/d2c/')  # Значение по умолчанию

    @allure.step("Открытие страницы лендинга по URL: services/website-development/d2c/")
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

    def get_data_card_d2c(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_card_(self.get_card_data, 'data_card_block_packages.json',
                            'd2c_card_data', url)

    @allure.step(
        "Проверяем заголовок и урл после клика по кнопке More")
    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        locator = Locators.get_team_card_more_locator(index)
        self.close_modal_popup()
        self.scroll_to_element(locator)  # Передаем локатор на скролл
        time.sleep(3)
        # Явное ожидание, что элемент станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.team_card_more = self.driver.find_element(*locator)  # Найти элемент
        self.driver.execute_script("arguments[0].click();", self.team_card_more)

        # Получаем заголовок страницы
        self.title_page = self.driver.find_element(*Locators.title_page)

        # Проверяем совпадение URL и заголовка
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"

        # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel_d2c, 'advant_section_carousel.json',
                                          'advant_section_d2c', url)

        # метод для карусели адвант
    def get_data_advant_carousel_card_icons(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel_d2c_icons, 'advant_section_carousel.json',
                                          'advant_section_d2c_icons', url)

    def get_data_card_tiles_d2c(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_icon_card_data_d2c',
            "//*[@class='tiles icons']//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    def get_data_card_tiles_d2c_icon(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('D2C', 'services/website-development/d2c/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_d2c',
            "//*[@class='tiles images']//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    def get_data_review_d2c(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('D2C', 'services/website-development/d2c/')
        self.driver.get(url)
        # Явное ожидание, что элемент с классом 'reviews-wrapper' появится на странице
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'reviews-wrapper'))
        )
        # После этого можно извлекать данные, как и раньше
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json',
                              'reviews-wrapper', url)