from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WebDesignPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/website-design-and-development-services/')  # Добавляем под-URL

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text