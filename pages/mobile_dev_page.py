from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData


class MobileDevPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/services/mobile-development/')

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text

    def click_button_banner(self):
        button_banner = self.driver.find_element(By.XPATH, "//*[@class='banner']//button")
        button_banner.click()

    def click_button_in_card_select(self):
        button_in_card_select = self.driver.find_element(By.XPATH, "//*[@class='info-card selected']//button")
        self.scroll_to_element(button_in_card_select)
        button_in_card_select.click()

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def click_button_in_faq(self):
        button_in_faq = self.driver.find_element(By.XPATH, "//*[@class='faq-section']//button")
        self.scroll_to_element(button_in_faq)
        button_in_faq.click()

    def get_meta_data(self):
        return MetaData(self.driver)

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

    def get_count_elements(self):
        return CountElements(self.driver)

