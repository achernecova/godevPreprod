
import logging

from selenium.webdriver.common.by import By
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.menu_element import MenuElement
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage


class MainPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
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

    def check_packages_data(self, project_type, experience, bullits, price, index):
        logging.info('move cursor to element')
        team_card = self.driver.find_element(By.XPATH, f"(//*[@class='team-card'])[{index}]")
        self.scroll_to_element(team_card)

        attributes = {
            'spec fs24': project_type,
            'exp': experience,
            'level': bullits,
            'price': price
        }

        for attr, expected in attributes.items():
            print(f"(//*[@class='team-card']//*[@class='{attr}'])[{index}]")
            element = self.driver.find_element(By.XPATH, f"(//*[@class='team-card']//*[@class='{attr}'])[{index}]")
            assert element.text == expected, f"Ожидался заголовок '{expected}', но получен '{element.text}'"

    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        self.team_card_more = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//a[@class='more'])["+index+"]")
        self.scroll_to_element(self.team_card_more)
        self._click_element(self.team_card_more)
        self.title_page = self.driver.find_element(By.XPATH, "//h1")
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"
