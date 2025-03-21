from time import sleep

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

from test.locators import Locators


class FormPage:
    def __init__(self, driver):
        self.driver = driver
    fake = Faker()
    locators = {
        "element": (By.XPATH, "//section[@class='section-form']"),
        "topping_click": (By.XPATH, "//label[@class='topping'][@for='t1']"),
        "close_modal": (By.XPATH, "//*[@class='close-modal']"),
        "menu_contacts_locator": (By.XPATH, "//*[@class='menu-wrapper']//a[@href= 'https://dev.godev.agency/contacts/']"),
        "name_input": (By.XPATH, "//*[@class='section-form']//input[@name='name']"),
        "email_input": (By.XPATH, "//*[@class='section-form']//input[@name='email']"),
        "message_input": (By.XPATH, "//*[@class='section-form']//*[@name='description']"),
        "submit_button": (By.XPATH, "//*[@class='section-form']//*[@class='button']")
    }

    def get_form_section(self):
        try:
            # Явное ожидание появления секции формы
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(Locators.section_form_element_locator)
            )
            # Скролл к элементу с помощью JavaScript
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            sleep(1)  # Даем время на завершение скролла
            return element
        except Exception as e:
            print(f"Error in get_form_section: {e}")
            self.driver.save_screenshot("scroll_error.png")
            raise


    def fill_form(self):
        sleep(5)
        self.get_form_section()
        close_modal = self.driver.find_element(*Locators.close_modal)
        close_modal.click()
        topping_click = self.driver.find_element(*Locators.topping_click_locator)
        topping_click.click()
        name_input = self.driver.find_element(*Locators.name_input_locator)
        name_input.send_keys('TEST' + self.fake.name())
        email_input = self.driver.find_element(*Locators.email_input_locator)
        email_input.send_keys('TEST' + self.fake.email())
        message_input = self.driver.find_element(*Locators.message_input_locator)
        message_input.send_keys('TEST' + self.fake.text(max_nb_chars=300))
        #submit_button = self.driver.find_element(*Locators.submit_button_locator)
        #submit_button.click()

        # Находим элемент и ждем его кликабельности
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.submit_button_locator)
        )
        # Прокрутка элемента в видимую часть окна
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        # Проверка, кликабельность элемента и выполнение клика через JavaScript
        try:
            self.driver.execute_script("arguments[0].click();", submit_button)
        except Exception as e:
            print(f"Ошибка: {str(e)}")



    def popup_success_displayed(self, timeout=20):
        try:
            # Ожидание видимости элемента с указанным XPath
            popup_success = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(Locators.popup_success)
            )
            return popup_success.is_displayed()
        except (NoSuchElementException, TimeoutException):
            # Если элемент не найден или не виден в течение указанного времени, возвращаем False
            return False