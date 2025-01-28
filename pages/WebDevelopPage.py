from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_elements.meta_data_page import MetaData


class WebDevelopPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/services/website-development/')

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def carousel_how_make(self):
        carousel_block = self.driver.find_element(By.XPATH, "//*[contains(@class, 'advant-slider swiper icons swiper-initialized')]")
        self.scroll_to_element(carousel_block)
        card_carousel = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'swiper-slide grabbable ')]")
        count_card_count = len(card_carousel)  # Получаем количество элементов в списке
        return count_card_count

    def get_meta_data(self):
        return MetaData(self.driver)

    def types_of_websites_count_card(self):
        types_of_websites_block = self.driver.find_element(By.XPATH, "//*[@class='tiles-section']")
        self.scroll_to_element(types_of_websites_block)
        card_types_of_websites_count = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'tile w-')]")
        count_card_count = len(card_types_of_websites_count)  # Получаем количество элементов в списке
        return count_card_count
