import logging
import logging
import os

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class B2BPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('B2B_PAGE', 'services/website-development/b2b/')  # Значение по умолчанию

    @allure.step("Открытие страницы b2b по URL: services/website-development/b2b/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
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

    """
    Метод для получения данных из json файла. 
    Отправляем данные в метод get_data_card_name_price_text_button_more. Хранится в базовом классе, т.к. данный метод используется еще на 5 страницах
    file_load - файл из которого загружаются данные
    b2b_card_data - ключ по которому будем искать данные в json (в данном случае ищем блок Website packages - карточки с ценами, буллитами, описанием)
    """
    def get_data_card_b2b(self):
        url = self.get_base_url()
        self.get_data_card_name_price_text_button_more(self.get_card_data, 'data_card_block_packages.json',
                                             'b2b_card_data', url)

    """
    Метод для определения атрибутов шрифта блока: цвет, сам шрифт, размер
    click_body_element() - метод для клика в пустой области страницы.
    Для блока Benefits of a B2B e-commerce solution from Godev
    """
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


    @allure.step("Получение и проверка заголовка и текста из блоков")
    def get_data_title_and_text_in_blocks(self, block_name):
        # Конфигурация для разных блоков
        config = {
            'card_tiles_b2b': {
                'file_load': 'data_card_block_packages.json',
                'title_method': self.get_title_block_website_dev,
                'text_method': self.get_text_block_website_dev,
                'json_keys': {
                    'title': 'tiles_section_card_data_b2b',
                    'text_section': 'tiles_section_card_data_b2b'
                }
            },
            'how_it_staff_b2b': {
                'file_load': 'section_how_it_staff_tiles.json',
                'title_method': self.get_title_block_b2b_platforms,
                'text_method': self.get_text_block_b2b_platforms,
                'json_keys': {
                    'title': 'how_it_staff_b2b',
                    'text_section': 'how_it_staff_b2b'
                }
            }
        }

        if block_name not in config:
            raise ValueError(f"Неизвестный блок: {block_name}")
        conf = config[block_name]

        # Загрузка данных из файла
        data = load_file(conf['file_load'])

        # Получение данных со страницы
        title_data = conf['title_method']()
        text_data = conf['text_method']()

        print(f"Заголовок со страницы: {title_data}")
        print(f"Текст со страницы: {text_data}")

        # Получение ожидаемых данных из JSON
        json_key = conf['json_keys']['title']
        title_data_json = data[json_key]['title']
        text_section_key = conf['json_keys']['title']
        text_data_json = data[text_section_key]['text_section']

        print(f"Ожидаемый заголовок из JSON: {title_data_json}")
        print(f"Ожидаемый текст из JSON: {text_data_json}")

        # Проверка совпадения
        assert title_data == title_data_json, f"Заголовок на странице не совпадает с данными из json"
        assert text_data == text_data_json, f"Текст на странице не совпадает с данными из json"

    # Метод для получения заголовка блока
    def get_title_block_website_dev(self):
        return self.get_title_block(Locators.title_block_stages_of_creating_locator)

    # тянем данные из названия блока App and Web Development Services
    def get_text_block_website_dev(self):
        return self.get_text_block(Locators.text_block_stages_of_creating_locator)

    # Метод для получения заголовка блока
    def get_title_block_b2b_platforms(self):
        return self.get_title_block(Locators.title_block_custom_design_solutions_locator)

    # тянем данные из названия блока App and Web Development Services
    def get_text_block_b2b_platforms(self):
        return self.get_text_block(Locators.text_block_custom_design_solutions_locator)




