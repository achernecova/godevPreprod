import logging

from selenium.webdriver.common.by import By

from constants import subURLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData

from pages.base_page import BasePage


class FrameworkPage(BasePage):

    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.FRAMEWORK_PAGE

    def open(self):
        super().open(self.subURL)  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def get_data_block_price(self, index, price_left_title, price_left_text, price_right_title, price_right_text):
        team_card = self.driver.find_element(By.XPATH, "//*[@class='price-frameworks']")
        self.scroll_to_element(team_card)
        self.price_left_title_locator = self.driver.find_elements(By.XPATH, "//*[@class='price-frameworks__left']//*[@class='price-frameworks__title']")[index-1]
        self.price_left_text_locator = self.driver.find_elements(By.XPATH, "//*[@class='price-frameworks__left']//*[@class='price-frameworks__text']")[index-1]
        self.price_right_title_locator = self.driver.find_elements(By.XPATH, "//*[@class='price-frameworks__right']//*[@class='price-frameworks__title']")[index-1]
        self.price_right_text_locator = self.driver.find_elements(By.XPATH, "//*[@class='price-frameworks__right']//*[@class='price-frameworks__text']")[index-1]
        assert self.price_left_title_locator.text == price_left_title, f"Ожидался заголовок '{price_left_title}', но получен '{self.price_left_title_locator.text}'"
        assert self.price_left_text_locator.text == price_left_text, f"Ожидался заголовок '{price_left_text}', но получен '{self.price_left_text_locator.text}'"
        assert self.price_right_title_locator.text == price_right_title, f"Ожидался заголовок '{price_right_title}', но получен '{self.price_right_title_locator.text}'"
        assert self.price_right_text_locator.text == price_right_text, f"Ожидался заголовок '{price_right_text}', но получен '{self.price_right_text_locator.text}'"

