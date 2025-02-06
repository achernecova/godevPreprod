from faker import Faker
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage


class WebOutstaffPage(BasePage):
    fake = Faker()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/outstaffing-and-outsourcing-of-it-specialists/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def click_button_outsource(self):
        button_request = self.driver.find_element(By.XPATH, "(//button[@class='button outsource-button open-modal'])[1]")
        self.scroll_to_element(button_request)
        button_request.click()

    def check_packages_data(self, project_type, experience, bullits, price, index):
        print('move cursor to element')
        self.team_card = self.driver.find_element(By.XPATH, "(//*[@class='team-card'])["+index+"]")
        self.scroll_to_element(self.team_card)
        self.project_title = self.driver.find_element(By.XPATH, "(//*[@class='team-card-title']//*[@class='exp'])["+index+"]")
        self.project_bullits = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='level'])["+index+"]")
        self.project_name = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='spec fs24'])[" + index + "]")
        self.project_price = self.driver.find_element(By.XPATH, "(//*[@class='price'])[" + index + "]")
        assert self.project_title.text == experience, f"Ожидался заголовок '{experience}', но получен '{self.project_title.text}'"
        assert self.project_bullits.text == bullits, f"Ожидался заголовок '{bullits}', но получен '{self.project_bullits.text}'"
        assert self.project_name.text == project_type, f"Ожидался заголовок '{project_type}', но получен '{self.project_name.text}'"
        assert self.project_price.text == price, f"Ожидался заголовок '{price}', но получен '{self.project_price.text}'"


