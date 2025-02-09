from selenium.webdriver.common.by import By

from data_url import subURLs
from pages.base_page import BasePage


class WebDesignPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.DESIGN_PAGE

    def open(self):
        super().open(self.subURL)  # Добавляем под-URL
