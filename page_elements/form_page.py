from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

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
        element = self.driver.find_element(*self.locators["element"])
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        return element

    def fill_form(self):
        self.get_form_section()
        close_modal = self.driver.find_element(*self.locators["close_modal"]).click()# Убедитесь, что форма загружена
        topping_click = self.driver.find_element(*self.locators["topping_click"]).click()
        name_input = self.driver.find_element(*self.locators["name_input"]).send_keys(self.fake.name())
        email_input = self.driver.find_element(*self.locators["email_input"]).send_keys(self.fake.email())
        message_input = self.driver.find_element(*self.locators["message_input"]).send_keys(self.fake.text(max_nb_chars=300))
        submit_button = self.driver.find_element(*self.locators["submit_button"])
        submit_button.click()



    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def popup_success_displayed(self, timeout=20):
        try:
            # Ожидание видимости элемента с указанным XPath
            popup_success = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@class='sendmail-popup success']"))
            )
            return popup_success.is_displayed()
        except (NoSuchElementException, TimeoutException):
            # Если элемент не найден или не виден в течение указанного времени, возвращаем False
            return False