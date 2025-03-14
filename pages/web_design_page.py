import logging

import allure
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from constants import subURLs, URLs
from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class WebDesignPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = subURLs.DESIGN_PAGE



    @allure.step("Открытие страницы лендинга по URL: services/website-design-and-development-services/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL



    # переделываем метод
    def get_data_card_design(self):
        # Загрузите данные из JSON
        data = load_file('data_card_block_packages.json')

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = self.get_card_data(URLs.MAIN_PAGE + subURLs.DESIGN_PAGE)

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


    # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_design(self):
        url = URLs.MAIN_PAGE + subURLs.DESIGN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_design',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)



# метод для faq
    def get_data_faq_card(self):
        url = URLs.MAIN_PAGE + subURLs.DESIGN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_design',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)

    # Метод для получения заголовка блока
    def get_title_block_website_dev(self):
        # Сначала сделаем скролл к элементу
        self.scroll_to_element(Locators.title_block_website_dev_locator)
        title = self.get_title_block_from_page_all(Locators.title_block_website_dev_locator)
        return title


    # тянем данные из названия блока App and Web Development Services
    def get_text_block_website_dev(self):
        self.scroll_to_element(Locators.text_block_website_dev_locator)
        text = self.get_text_block_from_page_all(Locators.text_block_website_dev_locator)
        return text


    # Метод для получения заголовка блока
    def get_title_block_website_design(self):
        # Сначала сделаем скролл к элементу
        self.scroll_to_element(Locators.title_block_website_design_locator)
        title = self.get_title_block_from_page_all(Locators.title_block_website_design_locator)
        return title


    # тянем данные из названия блока App and Web Development Services
    def get_text_block_website_design(self):
        self.scroll_to_element(Locators.text_block_website_design_locator)
        text = self.get_text_block_from_page_all(Locators.text_block_website_design_locator)
        return text


    # Метод для получения заголовка блока
    def get_title_block_custom_design_solutions(self):
        # Сначала сделаем скролл к элементу
        self.scroll_to_element(Locators.title_block_custom_design_solutions_locator)
        title = self.get_title_block_from_page_all(Locators.title_block_custom_design_solutions_locator)
        return title


    # тянем данные из названия блока App and Web Development Services
    def get_text_block_custom_design_solutions(self):
        self.scroll_to_element(Locators.text_block_custom_design_solutions_locator)
        text = self.get_text_block_from_page_all(Locators.text_block_custom_design_solutions_locator)
        return text