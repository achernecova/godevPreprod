import logging

from selenium.webdriver.common.by import By

from constants import subURLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage

class EComPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.E_COM_PAGE

    def open(self):
        super().open(self.subURL)  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def check_packages_data_not_experience(self, project_type, bullits, price):
        logging.info('move cursor to element')
        index_mapping = self.create_index_mapping_not_experience()
        if project_type not in index_mapping:
            raise ValueError(f"Project type {project_type} not found on the page.")
        index = index_mapping[project_type]
        print("индекс: " + str(index))  # Преобразовано в строку
        team_card = self.driver.find_element(By.XPATH, f"(//*[@class='team-card'])[{index+1}]")
        self.scroll_to_element(team_card)
        attributes = {
            'spec fs22': project_type,
            'level': bullits,
            'price': price
        }
        for attr, expected in attributes.items():
            print(f"(//*[@class='team-card']//*[@class='{attr}'])[{index+1}]")
            element = self.driver.find_element(By.XPATH, f"(//*[@class='team-card']//*[@class='{attr}'])[{index+1}]")
            print(element.text)
            assert element.text == expected, f"Ожидался заголовок '{expected}', но получен '{element.text}'"
