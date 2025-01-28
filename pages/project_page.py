from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_elements.meta_data_page import MetaData


class project_page:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/projects/')

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_meta_data(self):
        return MetaData(self.driver)

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def click_project(self, index):
        print('move cursor to element')
        project = self.driver.find_element(By.XPATH, "(//*[@class='projects-title'])["+index+"]")
        self.scroll_to_element(project)
        project.click()

    def assert_data_page(self, expected_url, expected_title):
        assert self.get_url() == expected_url, f"Ожидался URL '{expected_url}', но получен '{self.driver.current_url}'"
        assert self.get_title_page() == expected_title, f"Получен Title: {self.get_title_page()}"

    def count_customer_reviews(self):
        customer_reviews = self.driver.find_element(By.XPATH, "//*[@class='reviews-wrapper']")
        self.scroll_to_element(customer_reviews)
        count_card_reviews = self.driver.find_elements(By.XPATH, "//*[@class='review-card']")
        count_card_count = len(count_card_reviews)  # Получаем количество элементов в списке
        return count_card_count
