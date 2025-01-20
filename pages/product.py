from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        title_page = self.driver.find_element(By.XPATH, '//h2')
        assert title_page.text == 'Samsung galaxy s6'