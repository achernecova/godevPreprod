from selenium.webdriver.common.by import By

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData


class WebDevServicesPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/services/web-development/')

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text

    def get_count_elements(self):
        return CountElements(self.driver)

