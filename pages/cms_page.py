import logging
import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from utils.data_loader import load_file

class CMSPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('CMS_PAGE', 'services/website-development/cms/')  # Значение по умолчанию

    @allure.step("Открытие страницы цмс по URL: services/website-development/cms/")
    def open(self, sub_url=None):
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL

    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def get_data_card_cms(self):
        url = self.get_base_url()
        self.get_data_card_name_price_text_button_more(self.get_card_data, 'data_card_block_packages.json',
                            'cms_card_data', url)

    """
    Метод для определения атрибутов шрифта блока: цвет, сам шрифт, размер
    click_body_element() - метод для клика в пустой области страницы.
    Тянем данные из json файла, в который внесены все шрифты с атрибутикой. 
    Вытаскиваем данные со страницы через обращения к атрибутам (например, value_of_css_property) 
    """
    @allure.step(
        "загружаем данные из json и тянем данные со страницы через обращение к атрибутам элемента")
    def get_font_attributes1(self, locator, block_name):
        # Загружаем данные из JSON в методе get_font_attributes
        font_data = load_file('attribute_font.json')
        data = font_data[block_name]

        self.click_body_element()
        element = self.driver.find_element(*getattr(Locators, locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.close_modal)
        )

        # Получаем атрибуты
        color = element.value_of_css_property("color")
        font_family = element.value_of_css_property("font-family")
        font_size = element.value_of_css_property("font-size")

        # Возвращаем атрибуты и ожидаемые значения
        return {
            "color": color,
            "font_family": font_family,
            "font_size": font_size,
            "expected_color": data['expected_color'],
            "expected_font_family": data['expected_font_family'],
            "expected_font_size": data['expected_font_size']
        }

