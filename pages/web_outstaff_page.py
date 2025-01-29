from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData


class web_outstaff_page:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/')

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def click_button_request_add(self):
        button_request = self.driver.find_element(By.XPATH, "(//button[@class='button outsource-button open-modal'])[1]")
        self.scroll_to_element(button_request)
        button_request.click()
        self.click_topping_dev_banner()
        self.input_name_in_banner()
        self.input_email_in_banner()
        self.input_comment_in_banner()
        self.click_button_in_banner()
        assert self.popup_success_displayed()

    def click_topping_dev_banner(self):
        topping_dev_button = self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t11']")
        topping_dev_button.click()

    def input_name_in_banner(self):
        input_name = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='name']")
        input_name.send_keys("Test name")

    def input_email_in_banner(self):
        input_email = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='email']")
        input_email.send_keys("testPochta@test.ru")

    def input_comment_in_banner(self):
        input_comment = self.driver.find_element(By.XPATH, "//*[@class='form-textarea']//*[@placeholder='Comment']")
        input_comment.send_keys("Тестовый комментарий")

    def click_button_in_banner(self):
        button_click = self.driver.find_element(By.XPATH, "//*[@class='request-offer-bottom']//button")
        button_click.send_keys("Тестовый комментарий")

    def popup_success_displayed(self, timeout=10):
        try:
            # Ожидание видимости элемента с указанным XPath
            popup_success = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@class='sendmail-popup success']"))
            )
            return popup_success.is_displayed()
        except (NoSuchElementException, TimeoutException):
            # Если элемент не найден или не виден в течение указанного времени, возвращаем False
            return False

    def check_packages_data(self, project_type, experience, bullits, price, index):
        print('move cursor to element')
        self.team_card = self.driver.find_element(By.XPATH, "(//*[@class='team-card'])["+index+"]")
        self.scroll_to_element(self.team_card)
        self.project_title = self.driver.find_element(By.XPATH, "(//*[@class='team-card-title']//*[@class='exp'])["+index+"]")
        self.project_bullits = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='level'])["+index+"]")
        self.project_name = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='spec fs24'])[" + index + "]")
        self.project_price = self.driver.find_element(By.XPATH, "(//*[@class='price'])[" + index + "]")
        assert self.project_title.text == experience, f"Ожидался заголовок '{experience}', но получен '{self.project_title.text}'"
        assert self.project_bullits.text == bullits, f"Ожидался заголовок '{bullits}', но получен '{self.project_bullits.text}'"
        assert self.project_name.text == project_type, f"Ожидался заголовок '{project_type}', но получен '{self.project_name.text}'"
        assert self.project_price.text == price, f"Ожидался заголовок '{price}', но получен '{self.project_price.text}'"







    def benefits_types_of_it_what_to_choose_count_cards(self, project_type, count):
        if project_type == "benefits":
            block = self.driver.find_element(By.XPATH, "//*[@class='advant-section']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='advant-card']")
            count_cards = len(cards_block)  # Получаем количество элементов в списке
            print(count_cards)
        elif project_type == "types_of_it":
            block = self.driver.find_element(By.XPATH, "//*[@class='types-of-it']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='types-of-it-card']")
            count_cards = len(cards_block)  # Получаем количество элементов в списке
            print(count_cards)
        elif project_type == "what_to_choose":
            block = self.driver.find_element(By.XPATH, "//*[@class='choise-cards']")
            self.scroll_to_element(block)
            cards_block = self.driver.find_elements(By.XPATH, "//*[@class='choise-card']")
            count_cards = len(cards_block)  # Получаем количество элементов в списке
            print(count_cards)
        else:
            raise ValueError("Неверный тип карточки")
        assert count_cards == count, f"Получено количество карточек:  {count_cards}"



