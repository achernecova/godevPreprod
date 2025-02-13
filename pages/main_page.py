import json
import logging

from selenium.webdriver.common.by import By

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.menu_element import MenuElement
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage
from package_data import PackageData

class MainPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    @classmethod
    def load_package_data(cls, filename):
        with open(filename) as f:
            package_data_list = json.load(f)
        return [PackageData(data) for data in package_data_list]

    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.driver = driver

    def click_button_banner(self):
        click_button_banner = self.driver.find_element(By.XPATH, "//*[@class='banner']//button")
        click_button_banner.click()

    def open(self):
        super().open('')  # Добавляем под-URL

    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_menu_element(self):
        return MenuElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        self.team_card_more = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//a[@class='more'])["+index+"]")
        self.scroll_to_element(self.team_card_more)
        self._click_element(self.team_card_more)
        self.title_page = self.driver.find_element(By.XPATH, "//h1")
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"
