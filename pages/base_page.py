import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    base_url = 'https://dev.godev.agency/'
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def open(self, suburl=''):
        self.driver.get(self.base_url + suburl)

    def close_modal_popup(self):
        close_modal = self.driver.find_element(By.XPATH, "//*[@class='close-modal']")
        close_modal.click()

    def _click_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logging.info(f"Clicked on element: {locator}")
        except (NoSuchElementException, TimeoutException):
            logging.error(f"Element {locator} not found or not clickable.")

    def _get_element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
        except (NoSuchElementException, TimeoutException):
            logging.error(f"Element {locator} not found.")
            return None

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))



