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
        elif project_type == "how_we_make_web":
            block = self.driver.find_element(By.XPATH, "//*[contains(@class, 'advant-slider swiper images')]")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'advant-slider swiper images')]//*[@class='advant-card']")
            count_card = len(cards_block)
        elif project_type == "advantages_outsourcing":
            block = self.driver.find_element(By.XPATH, "//*[@class='advantages-outsourcing']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='advantages-outsourcing__item']")
            count_card = len(cards_block)
        elif project_type == "our_proven_web_dev":
            block = self.driver.find_element(By.XPATH, "//*[contains(@class, 'advant-slider swiper icons ')]")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'advant-slider swiper icons ')]//*[@class='advant-card']")
            count_card = len(cards_block)
        elif project_type == "why_choose_godev":
            block = self.driver.find_element(By.XPATH, "//*[@class='advant images']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='advant images']//*[contains(@class, 'advant-card ')]")
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
        elif project_type == "advantages_cards_tiles_count": ###########################################################
            advantages_cards_tiles_block = self.driver.find_element(By.XPATH, "//*[@class='cards-tiles col-2']")
            self.scroll_to_element(advantages_cards_tiles_block)
            card_types_of_websites_count = self.driver.find_elements(By.XPATH, "//*[@class='card']")
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
        elif project_type == "count_card_cooperation_formats":
            carousel = self.driver.find_element(By.XPATH, "//*[@id='cooperation-formats']")
            self.scroll_to_element(carousel)
            cards = self.driver.find_elements(By.XPATH, "//*[@class='cooperation-formats-card']")
            count_card = len(cards)  # Получаем количество элементов в списке
        elif project_type == "web_dev_services":
            blocks = self.driver.find_element(By.XPATH, "//*[@class='web-dev-services']")
            self.scroll_to_element(blocks)
            cards = self.driver.find_elements(By.XPATH, "//*[@class='card']")
            count_card = len(cards)  # Получаем количество элементов в списке

        elif project_type == "best_web_frameworks":
            blocks = self.driver.find_element(By.XPATH, "//*[@class='best-frameworks']")
            self.scroll_to_element(blocks)
            cards = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'best-frameworks__item ')]")
            count_card = len(cards)  # Получаем количество элементов в списке

        elif project_type == "cms_services_cards":
            blocks = self.driver.find_element(By.XPATH, "//*[@class='cms-services-cards']")
            self.scroll_to_element(blocks)
            cards = self.driver.find_elements(By.XPATH, "//button[contains(@class, 'card-wrapper')]")
            count_card = len(cards)  # Получаем количество элементов в списке

        elif project_type == "back_end_frameworks":
            blocks = self.driver.find_element(By.XPATH, "//*[text()='Back-end frameworks']")
            self.scroll_to_element(blocks)
            cards = self.driver.find_elements(By.XPATH, "//*[@class='best-frameworks__inner']//*[contains(@class, 'swiper-slide')]")
            count_card = len(cards)  # Получаем количество элементов в списке
        elif project_type == "platforms":
            blocks = self.driver.find_element(By.XPATH, "//*[contains(@class, 'cards-tiles')]")
            self.scroll_to_element(blocks)
            cards = self.driver.find_elements(By.XPATH, "//*[@class='card']")
            count_card = len(cards)  # Получаем количество элементов в списке

        else:
            raise ValueError("Неверный тип карточки")
        assert count_card == count, f"Получено количество карточек: {count_card}, ожидаемое: {count}"


    def check_packages_data(self, project_type, experience, bullits, price, index):
        print('move cursor to element')
        team_card = self.driver.find_element(By.XPATH, "(//*[@class='team-card'])["+index+"]")
        self.scroll_to_element(team_card)
        self.project_title = self.driver.find_element(By.XPATH, "(//*[@class='team-card-title']//*[@class='exp'])["+index+"]")
        self.project_bullits = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='level'])["+index+"]")
        self.project_name = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='spec fs24'])[" + index + "]")
        self.project_price = self.driver.find_element(By.XPATH, "(//*[@class='price'])[" + index + "]")
        assert self.project_title.text == experience, f"Ожидался заголовок '{experience}', но получен '{self.project_title.text}'"
        assert self.project_bullits.text == bullits, f"Ожидался заголовок '{bullits}', но получен '{self.project_bullits.text}'"
        assert self.project_name.text == project_type, f"Ожидался заголовок '{project_type}', но получен '{self.project_name.text}'"
        assert self.project_price.text == price, f"Ожидался заголовок '{price}', но получен '{self.project_price.text}'"

    def check_packages_data_services(self, index, project_type, price):
        print('move cursor to element')
        blocks = self.driver.find_element(By.XPATH, "//*[@class='web-dev-services']")
        self.scroll_to_element(blocks)
        self.project_title_1 = self.driver.find_elements(By.XPATH, "//*[@class='card-title']")[index]
        self.project_price = self.driver.find_elements(By.XPATH, "//*[@class='price']")[index]
        print(self.project_title_1.text)
        print(self.project_price.text)
        assert self.project_title_1.text.strip() == project_type, f"Ожидался заголовок '{project_type}', но получен '{self.project_title_1.text}'"
        assert self.project_price.text.strip() == price.strip(), f"Ожидался заголовок '{price}', но получен '{self.project_price.text}'"