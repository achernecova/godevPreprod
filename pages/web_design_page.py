from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WebDesignPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/website-design-and-development-services/')  # Добавляем под-URL
