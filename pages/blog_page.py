import logging
import os

import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from test.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('BLOG_PAGE', 'blog/')  # Значение по умолчанию


    @allure.step("Открытие страницы лендинга по URL: blog/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL


    def get_date_blog(self):
        date_blog = self.driver.find_element(*Locators.date_blog)
        return date_blog.text

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


    def wait_until_visible(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )


    def click_block_page(self, index, side, page_url, page_title, date_blog):
        logging.info('move cursor to element')
        self.close_modal_popup()

        block_class = 'blog__block-right' if side == 'right' else 'blog__block-left--item'
        locator = Locators.get_click_block_class_and_index_locator(block_class, index)  # Получаем локатор

        # Ожидание видимости элемента
        self.wait_until_visible(locator)

        # Прокрутка к элементу перед кликом
        element = self.driver.find_element(*locator)
        self.scroll_to_element(locator)

        # Попробовать выполнить клик через JavaScript, если основной клик не успешен
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

        # Проверки после клика
        title_page = self.driver.find_element(*Locators.title_page)

        assert self.get_url() == page_url, f"Ожидался URL '{page_url}', но получен '{self.get_url()}'"
        assert title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{title_page.text}'"
        assert self.get_date_blog() == date_blog, f"Ожидалась дата '{date_blog}', но получен '{self.get_date_blog()}'"