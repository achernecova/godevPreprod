import logging
import os

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import allure
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators
from utils.data_loader import load_file


class WebDesignPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('DESIGN_PAGE', 'services/website-design-and-development-services/')

    def get_popup(self):
        return PopupElement(self.driver)

    @allure.step("Открытие страницы лендинга по URL: services/website-design-and-development-services/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL

    def get_count_elements(self):
        return CountElements(self.driver)


    @allure.step("Получение и проверка заголовка и текста из блоков")
    def get_data_title_and_text_in_blocks(self, block_name):
        # Конфигурация для разных блоков
        config = {
            'website_development_design': {
                'file_load': 'section_how_it_staff_tiles.json',
                'title_method': self.get_title_block_website_dev,
                'text_method': self.get_text_block_website_dev,
                'json_keys': {
                    'title': 'website_development_design',
                    'text_section': 'website_development_design'
                }
            },
            'website_design': {
                'file_load': 'section_how_it_staff_tiles.json',
                'title_method': self.get_title_block_website_design,
                'text_method': self.get_text_block_website_design,
                'json_keys': {
                    'title': 'website_design',
                    'text_section': 'website_design'
                }
            },
            'custom_design_solutions': {
                'file_load': 'section_how_it_staff_tiles.json',
                'title_method': self.get_title_block_custom_design_solutions,
                'text_method': self.get_text_block_custom_design_solutions,
                'json_keys': {
                    'title': 'how_it_staff_design',
                    'text_section': 'how_it_staff_design'
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


    # переделываем метод
    def get_data_card_design(self):
        # Загрузите данные из JSON
        data = load_file('data_card_block_packages.json')

        # Получаем данные из блока карусели на странице
        base_url = put_a_secret()
        card_data_data_from_page = self.get_card_data_design(base_url + self.subURL)

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_data_from_page:
            print(review)

        # Смотрим, что каждое описание из cms_card_data присутствует на странице
        descriptions = data['website_design_card_data']['descriptions']

        # Выводим данные из JSON
        print("Данные из JSON:")
        for desc in descriptions:
            print(desc)

        for desc in descriptions:
            # Обработаем каждое описание из b2b_card_data
            # Проверяем все
            found = any(
                review['project_type'].strip() == desc['project_type'].strip() and
                review['level'].strip() == desc['level'].strip() and
                review['price'].strip() == desc['price'].strip()
                for review in card_data_data_from_page
            )

            assert found, f"Данные из JSON не найдены на странице для: {desc['project_type']} | {desc['level']} | {desc['price']}"

    def get_card_data_design(self, url):
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
            project_type = section.find(class_='spec fs24').get_text(strip=True)
            price = section.find(class_='price').get_text(strip=True).replace('\xa0', ' ')

            logging.info(
                f"project_type: {project_type}, level: {level}, price: {price}")

            team_data.append({
                'level': level,
                'project_type': project_type,
                'price': price
            })

        return team_data

    # Метод для получения заголовка блока
    def get_title_block_website_dev(self):
        return self.get_title_block(Locators.title_block_website_dev_locator)


    # тянем данные из названия блока App and Web Development Services
    def get_text_block_website_dev(self):
        return self.get_text_block(Locators.text_block_website_dev_locator)


    # Метод для получения заголовка блока
    def get_title_block_website_design(self):
        return self.get_title_block(Locators.title_block_website_design_locator)


    # тянем данные из названия блока App and Web Development Services
    def get_text_block_website_design(self):
        return self.get_text_block(Locators.text_block_website_design_locator)

    # Метод для получения заголовка блока
    def get_title_block_custom_design_solutions(self):
        return self.get_title_block(Locators.title_block_custom_design_solutions_locator)


    # тянем данные из текста блока design_solutions
    def get_text_block_custom_design_solutions(self):
        return self.get_text_block(Locators.text_block_custom_design_solutions_locator)