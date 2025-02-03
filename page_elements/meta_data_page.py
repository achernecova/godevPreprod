from selenium.webdriver.common.by import By
class MetaData:

    def __init__(self, driver):
        self.driver = driver

    def get_title_ceo_page(self):
        title_page_dev = self.driver.title
        return title_page_dev

    def get_descr_ceo_page(self):
        description_element = self.driver.find_element(By.XPATH, "//meta[@name='description']")
        return description_element.get_attribute("content")

    def get_canonical_ceo_page(self):
        canonical_element = self.driver.find_element(By.XPATH, "//link[@rel='canonical']")
        return canonical_element.get_attribute("href")
