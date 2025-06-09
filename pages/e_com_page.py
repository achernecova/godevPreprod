import logging
import os
import re

import allure
import requests
from bs4 import BeautifulSoup

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators
from utils.data_loader import load_file


class EComPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('E_COM_PAGE', 'services/website-development/e-commerce/')  # Значение по умолчанию

    @allure.step("Открытие страницы лендинга по URL: services/website-development/e-commerce/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL

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
        logging.info(f"Индекс: " + str(index))
        team_card = self.driver.find_element(*Locators.get_check_packages_data_not_experience_locator(index))
        self.scroll_to_element(team_card)
        attributes = {
            'spec fs22': project_type,
            'level': bullits,
            'price': price
        }
        for attr, expected in attributes.items():
            element = self.driver.find_element(*Locators.get_data_with_attr_and_index_locator(attr, index))
            logging.info(f"Заголовок на странице: " + element.text)
            assert element.text == expected, f"Ожидался заголовок '{expected}', но получен '{element.text}'"

    # переделываем метод
    def get_data_card_e_com(self):
        # Загрузите данные из JSON
        data = load_file('data_card_block_packages.json')

        base_url = put_a_secret()
        url = base_url + os.getenv('LANDING', 'services/development-of-a-landing-page/')

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = self.get_card_data(
            url + os.getenv('E_COM_PAGE', 'services/website-development/e-commerce/'))

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_data_from_page:
            print(review)

        # Смотрим, что каждое описание из e_com_card_data присутствует на странице
        descriptions = data['e_com_card_data']['descriptions']

        # Выводим данные из JSON
        print("Данные из JSON:")
        for desc in descriptions:
            print(desc)

        for desc in descriptions:
            # Обработаем каждое описание из e_com_card_data
            # Проверяем все
            found = any(
                review['project_type'].strip() == desc['project_type'].strip() and
                review['level'].strip() == desc['level'].strip() and
                review['price'].strip() == desc['price'].strip()
                for review in card_data_data_from_page
            )

            assert found, f"Данные из JSON не найдены на странице для: {desc['project_type']} | {desc['level']} | {desc['price']} "

    def get_base_url(self):
        base_url = put_a_secret()
        return base_url + self.subURL

    def get_card_data(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение всех элементов с классом 'team-card'
        team_data = []
        type_section = soup.find_all(class_='team-card')

        logging.info(f"Найдено {len(type_section)} элементов с классом 'team-card'")

        for section in type_section:
            # Извлечение данных
            level = section.find(class_='level').get_text(strip=True)
            project_type = section.find(class_='spec fs22').get_text(strip=True)
            price = section.find(class_='price').get_text(strip=True).replace('\xa0', ' ')

            logging.info(
                f"project_type: {project_type}, level: {level}, price: {price}")

            team_data.append({
                'level': level,
                'project_type': project_type,
                'price': price
            })

        return team_data

        # метод для черно-белых карточек
    def get_data_card_tiles_e_com(self):
        url = self.get_base_url()
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_e_com',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = self.get_base_url()
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                      'advant_section_e_com', url)
