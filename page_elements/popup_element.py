
from faker import Faker
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class PopupElement(BasePage):
    fake = Faker()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_topping_dev_banner(self):
        self._click_element(self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t11']"))

    def input_name_in_banner(self):
        input_name = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='name']")
        input_name.send_keys(self.fake.name())

    def input_email_in_banner(self):
        input_email = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='email']")
        input_email.send_keys(self.fake.email())

    def input_comment_in_banner(self):
        input_comment = self.driver.find_element(By.XPATH, "//*[@class='form-textarea']//*[@placeholder='Comment']")
        input_comment.send_keys(self.fake.text(max_nb_chars=500))

    def click_button_in_banner(self):
        self._click_element(self.driver.find_element(By.XPATH, "//*[@class='request-offer-bottom']//button"))

    def click_button_in_header(self):
        self._click_element(self.driver.find_element(By.XPATH, "//*[@class='right']//button"))

    def click_topping_analysts_banner(self):
        self._click_element(self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t14']"))

    def add_request_success(self):
        self.close_modal_popup()
        self.click_topping_dev_banner()
        self.click_topping_analysts_banner()
        self.input_name_in_banner()
        self.input_email_in_banner()
        self.input_comment_in_banner()
        self.click_button_in_banner()
