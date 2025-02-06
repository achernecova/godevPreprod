import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from pages.base_page import BasePage


class WebDevelopPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/website-development/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        self.team_card_more = self.driver.find_element(By.XPATH, "(//*[contains(@class, 'tile ')]//a[@class='more'])["+index+"]")
        self.scroll_to_element(self.team_card_more)
        self._click_element(self.team_card_more)
        self.title_page = self.driver.find_element(By.XPATH, "//h1")
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"
