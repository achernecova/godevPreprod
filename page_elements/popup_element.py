import re

import allure
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from test.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class PopupElement(BasePage):
    fake = Faker()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def click_topping_dev_banner(self):
        click_topping = self.driver.find_element(*Locators.topping_dev_button_locator)
        self.driver.execute_script("arguments[0].click();", click_topping)


    @allure.step("Ввод имени в поле Name")
    def input_name_in_banner(self):
        input_name = self.driver.find_element(*Locators.input_name_locator)
        input_name.send_keys('TEST' + self.fake.name())


    @allure.step("Ввод email в поле Email")
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


    @allure.step("Ввод данных в поле комментарий")
    def input_comment_in_banner(self):
        input_comment = self.driver.find_element(*Locators.input_comment_locator)
        input_comment.send_keys('TEST' + self.fake.text(max_nb_chars=200))


    @allure.step("Клик по кнопке Get in touch в баннере")
    def click_button_in_banner(self):
        # Находим элемент и ждем его кликабельности
        button_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.button_click_locator)
        )
        # Прокрутка элемента в видимую часть окна
        self.driver.execute_script("arguments[0].scrollIntoView();", button_click)
        # Проверка, кликабельность элемента и выполнение клика через JavaScript
        try:
            self.driver.execute_script("arguments[0].click();", button_click)
        except Exception as e:
            print(f"Ошибка: {str(e)}")


    @allure.step("Клик по буллиту Аналитика")
    def click_topping_analysts_banner(self):
        topping_analysts = self.driver.find_element(*Locators.topping_analysts_locator)
        self.driver.execute_script("arguments[0].click();", topping_analysts)


    @allure.step("Полное заполнение заявки")
    def add_request_success(self):
        #self.close_modal_popup()
        self.click_topping_dev_banner()
        self.click_topping_analysts_banner()
        self.input_name_in_banner()
        self.input_email_in_banner()
        self.input_comment_in_banner()
        self.click_button_in_banner()
