import re

from faker import Faker

from pages.base_page import BasePage
from test.locators import Locators


class PopupElement(BasePage):
    fake = Faker()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_topping_dev_banner(self):
        click_topping = self.driver.find_element(*Locators.topping_dev_button_locator)
        click_topping.click()

    def input_name_in_banner(self):
        input_name = self.driver.find_element(*Locators.input_name_locator)
        input_name.send_keys('TEST' + self.fake.name())

    def input_email_in_banner(self):
        input_email = self.driver.find_element(*Locators.input_email_locator)

        # Генерируем email и убираем пробелы и тире
        email = self.fake.email()
        email = re.sub(r'\s+', '', email)  # Удаляем все пробелы из email
        email = re.sub(r'-', '', email)  # Удаляем все тире из email

        # Проверяем, что email не содержит пробелов или тире
        if ' ' in email or '-' in email:
            print("Сгенерированный email содержит пробелы или тире, генерируем заново.")
            email = self.fake.email()  # Генерируем email заново, если есть пробелы или тире

        input_email.send_keys('TEST' + email)

    def input_comment_in_banner(self):
        input_comment = self.driver.find_element(*Locators.input_comment_locator)
        input_comment.send_keys('TEST' + self.fake.text(max_nb_chars=200))

    def click_button_in_banner(self):
        button_click = self.driver.find_element(*Locators.button_click_locator)
        button_click.click()

    def click_topping_analysts_banner(self):
        topping_analysts = self.driver.find_element(*Locators.topping_analysts_locator)
        topping_analysts.click()

    def add_request_success(self):
        self.close_modal_popup()
        self.click_topping_dev_banner()
        self.click_topping_analysts_banner()
        self.input_name_in_banner()
        self.input_email_in_banner()
        self.input_comment_in_banner()
        self.click_button_in_banner()
