from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def get_form_section(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "section.section-form")
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        return element

    def fill_form(self, name, email, message):
        self.get_form_section()  # Убедитесь, что форма загружена
        topping_click = self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t1']")
        close_modal = self.driver.find_element(By.XPATH, "//*[@class='close-modal']")
        name_input = self.driver.find_element(By.XPATH, "//*[@class='section-form']//input[@name='name']")
        email_input = self.driver.find_element(By.XPATH, "//*[@class='section-form']//input[@name='email']")
        message_input = self.driver.find_element(By.XPATH, "//*[@class='section-form']//*[@name='description']")
        submit_button = self.driver.find_element(By.XPATH, "//*[@class='section-form']//*[@class='button']")
#
        topping_click.click()
        close_modal.click()
        name_input.send_keys(name)
        email_input.send_keys(email)
        message_input.send_keys(message)
        submit_button.click()

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()