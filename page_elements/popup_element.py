from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopupElement:

    def __init__(self, driver):
        self.driver = driver

    def click_topping_dev_banner(self):
        topping_dev_button = self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t11']")
        topping_dev_button.click()

    def input_name_in_banner(self, name):
        input_name = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='name']")
        input_name.send_keys(name)

    def input_email_in_banner(self, email):
        input_email = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='email']")
        input_email.send_keys(email)

    def input_comment_in_banner(self, comment):
        input_comment = self.driver.find_element(By.XPATH, "//*[@class='form-textarea']//*[@placeholder='Comment']")
        input_comment.send_keys(comment)

    def click_button_in_banner(self):
        button_click = self.driver.find_element(By.XPATH, "//*[@class='request-offer-bottom']//button")
        button_click.click()

    def click_button_in_header(self):
        button_header_click = self.driver.find_element(By.XPATH, "//*[@class='right']//button")
        button_header_click.click()

    def click_topping_analysts_banner(self):
        topping_analysts_button = self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t14']")
        topping_analysts_button.click()


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

    def close_modal_popup(self):
        close_modal = self.driver.find_element(By.XPATH, "//*[@class='close-modal']")
        close_modal.click()

    def add_request_success(self, name, email, comment):
        self.close_modal_popup()
        self.click_topping_dev_banner()
        self.click_topping_analysts_banner()
        self.input_name_in_banner(name)
        self.input_email_in_banner(email)
        self.input_comment_in_banner(comment)
        self.click_button_in_banner()
        self.popup_success_displayed()
