from selenium.webdriver.common.by import By


class support_page:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/services/tech-support/')

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text