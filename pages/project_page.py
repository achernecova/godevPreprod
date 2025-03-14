import logging

import allure

from constants import subURLs, URLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from pages.base_page import BasePage
from test.locators import Locators


class ProjectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.PROJECT_PAGE

    @allure.step("Открытие мобильной страницы по URL: services/mobile-development/")
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

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def click_project(self, index):
        print('move cursor to element')
        project = self.driver.find_element(*Locators.get_project_locator(index))
        self.scroll_to_element(project)
        self._click_element(project)

    def assert_data_page(self, expected_url, expected_title):
        assert self.get_url() == expected_url, f"Ожидался URL '{expected_url}', но получен '{self.driver.current_url}'"
        assert self.get_title_page() == expected_title, f"Получен Title: {self.get_title_page()}"


        # получение данных с карточек с отзывами
    def get_data_review(self):
        url = URLs.MAIN_PAGE + subURLs.PROJECT_PAGE
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json',
                                  'reviews-wrapper', url)
