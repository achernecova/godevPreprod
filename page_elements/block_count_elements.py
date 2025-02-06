from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class CountElements:
    def __init__(self, driver):
        self.driver = driver

    XPATH_MAP = {
        "blocks": "//*[@class='web-dev-services']",
        "benefits": "//*[@class='advant-card']",
        "how_we_make_web": "//*[contains(@class, 'advant-slider swiper images')]//*[@class='advant-card']",
        "advantages_outsourcing": "//*[@class='advantages-outsourcing__item']",
        "our_proven_web_dev": "//*[contains(@class, 'advant-slider swiper icons ')]//*[@class='advant-card']",
        "why_choose_godev": "//*[@class='advant images']//*[contains(@class, 'advant-card ')]",
        "types_of_it": "//*[@class='types-of-it-card']",
        "what_to_choose": "//*[@class='choise-card']",
        "customer_reviews": "//*[@class='review-card']",
        "web_packages_count": "//*[@class='team-card']",
        "types_of_websites_count_card": "//*[contains(@class, 'tile w-')]",
        "advantages_cards_tiles_count": "//*[@class='cards-tiles col-2']//*[@class='card']",
        "carousel_how_make": "//*[contains(@class, 'swiper-slide grabbable ')]",
        "count_card_advantages": "//*[contains(@class, 'swiper-slide grabbable')]",
        "count_card_cooperation_formats": "//*[@class='cooperation-formats-card']",
        "web_dev_services": "//*[@class='card']",
        "swiper_slide": "//*[@class='swiper-slide']",
        "best_web_frameworks": "//*[contains(@class, 'best-frameworks__item ')]",
        "cms_services_cards": "//button[contains(@class, 'card-wrapper')]",
        "back_end_frameworks": "//*[@class='best-frameworks__inner']//*[contains(@class, 'swiper-slide')]",
        "platforms": "//*[@class='card']",
        "adv_item": "//*[@class='adv-item']",
        "block-right": "//*[@class= 'blog__block-right']",
        "block-left": "//*[contains(@class, 'blog__block-left--item')]",
        "popular_news": "//*[contains(@class, 'swiper-slide grabbable ')]"
    }

    def count_cards_assert(self, project_type, expected_count):
        if project_type not in self.XPATH_MAP:
            raise ValueError("Неверный тип карточки")

        xpath = self.XPATH_MAP[project_type]
        cards = self.driver.find_elements(By.XPATH, xpath)
        count_card = len(cards)

        assert count_card == expected_count, f"Получено количество карточек: {count_card}, ожидаемое: {expected_count}"

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

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
        xpath = self.XPATH_MAP["blocks"]
        blocks = self.driver.find_element(By.XPATH, xpath)
        self.scroll_to_element(blocks)
        self.project_title = self.driver.find_elements(By.XPATH, "//*[@class='card-title']")[index]
        self.project_price = self.driver.find_elements(By.XPATH, "//*[@class='price']")[index]
        assert self.project_title.text.strip() == project_type, f"Ожидался заголовок '{project_type}', но получен '{self.project_title.text}'"
        assert self.project_price.text.strip() == price.strip(), f"Ожидался заголовок '{price}', но получен '{self.project_price.text}'"