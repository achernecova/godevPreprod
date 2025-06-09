#в процессе
import logging
import os

import allure

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.menu_element import MenuElement
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage, put_a_secret
from test.locators import Locators


class ServicesPage(BasePage):

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)  # Передаем base_url в базовый класс
        self.subURL = os.getenv('SERVICES_PAGE', 'services/')

    @allure.step("Открытие страницы лендинга по URL: services/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL


    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)


    def click_button_banner(self):
        click_button_banner = self.driver.find_element(*Locators.button_banner_services)
        click_button_banner.click()


    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_menu_element(self):
        return MenuElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)


    # тянем данные из названия блока Services
    def get_title_block_app_and_web_development_services(self):
        title = self.get_title_block_from_page_all(Locators.title_block_app_and_web_development_services_locator)
        return title


    def get_data_card(self, card_type):
        config = {
            'app_and_web_services_advant': { # для черно-белых карточек
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'advantages_of_working_with_us',
                'locator_block': "//*[@class='adv-item']",
                'locator_element': ".//*[@class='adv-item_descr']",
                'locator_section': ".//*[@class='adv-item_title']//span",
            },
            'app_and_web_services_service': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'app_and_web_services_service',
                'locator_block': "//*[@class='service-item']",
                'locator_element': ".//*[@class='service-descr']" ,
                'locator_section': './/h3',
            }
        }
        if card_type not in config:
            raise ValueError(f"Такого блока не существует: {card_type}")
        # забираем нужный блок из списка config
        conf = config[card_type]
        url = self.get_base_url()
        # грузим данные, забирая конкретные параметры из нужного блока (отдаем файл, какой метод, ключ, локаторы)
        self.get_data_card_with_type_project(
            conf['file_load'],
            conf['url_method'],
            conf['json_key'],
            conf['locator_block'],
            conf['locator_element'],
            conf['locator_section'],
            url
        )

    def get_base_url(self):
        base_url = put_a_secret()
        return base_url + self.subURL