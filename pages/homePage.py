from selenium.webdriver.common.by import By
import time

class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, "//a[text() = 'Samsung galaxy s6']")
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_products_count(self, count):
        time.sleep(3)
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        time.sleep(3)
        assert len(monitors) == count

