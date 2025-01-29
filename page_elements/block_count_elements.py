from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class CountElements:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def count_cards_assert(self, project_type, count):
        count_card = 0  # Инициализируем переменную по умолчанию
        if project_type == "benefits":
            block = self.driver.find_element(By.XPATH, "//*[@class='advant-section']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='advant-card']")
            count_card = len(cards_block)
        elif project_type == "types_of_it":
            block = self.driver.find_element(By.XPATH, "//*[@class='types-of-it']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='types-of-it-card']")
            count_card = len(cards_block)
        elif project_type == "what_to_choose":
            block = self.driver.find_element(By.XPATH, "//*[@class='choise-cards']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='choise-card']")
            count_card = len(cards_block)
        elif project_type == "customer_reviews":
            customer_reviews = self.driver.find_element(By.XPATH, "//*[@class='reviews-wrapper']")
            self.scroll_to_element(customer_reviews)
            count_card_reviews = self.driver.find_elements(By.XPATH, "//*[@class='review-card']")
            count_card = len(count_card_reviews)
        elif project_type == "web_packages_count":
            web_packages_block = self.driver.find_element(By.XPATH, "//*[@class='team']")
            self.scroll_to_element(web_packages_block)
            count_card_packages = self.driver.find_elements(By.XPATH, "//*[@class='team-card']")
            count_card = len(count_card_packages)
        elif project_type == "types_of_websites_count_card":
            types_of_websites_block = self.driver.find_element(By.XPATH, "//*[@class='tiles-section']")
            self.scroll_to_element(types_of_websites_block)
            card_types_of_websites_count = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'tile w-')]")
            count_card = len(card_types_of_websites_count)
        elif project_type == "carousel_how_make":
            carousel_block = self.driver.find_element(By.XPATH, "//*[contains(@class, 'advant-slider swiper icons swiper-initialized')]")
            self.scroll_to_element(carousel_block)
            card_carousel = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'swiper-slide grabbable ')]")
            count_card = len(card_carousel)
        elif project_type == "count_card_advantages":
            carousel = self.driver.find_element(By.XPATH, "//*[@class='swiper-wrapper']")
            self.scroll_to_element(carousel)
            cards = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'swiper-slide grabbable')]")
            count_card = len(cards)  # Получаем количество элементов в списке
        else:
            raise ValueError("Неверный тип карточки")
        assert count_card == count, f"Получено количество карточек: {count_card}, ожидаемое: {count}"