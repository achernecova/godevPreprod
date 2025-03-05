import logging

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from constants import URLs, subURLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class WebDevelopPage(BasePage):

    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.team_card_more = None
        self.driver = driver

    def open(self):
        super().open('services/website-development/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        wait = WebDriverWait(self.driver, 10)

        # Убедитесь, что элемент доступен
        self.team_card_more = wait.until(EC.presence_of_element_located(Locators.get_button_more_locator(index)))
        if not self.team_card_more:
            raise ValueError(f"Кнопка 'больше' по индексу {index} не найдена.")

        self.scroll_to_element(self.team_card_more)
        self.team_card_more.click()


        title_page = self.get_title_page()  # title_page теперь строка
        assert self.get_url() == page_url, f"Ожидался URL '{page_url}', но получен '{self.get_url()}'"
        assert title_page == page_title, f"Ожидался заголовок '{page_title}', но получен '{title_page}'"


 # переделываем метод
    def get_data_card_website(self):
        # Загрузите данные из JSON
        data = load_file('data_card_block_packages.json')

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = self.get_card_data(URLs.MAIN_PAGE + subURLs.WEBSITE_DEV)

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_data_from_page:
            print(review)

        # Смотрим, что каждое описание из cms_card_data присутствует на странице
        descriptions = data['web_site_develop_card_data']['descriptions']

        # Выводим данные из JSON
        print("Данные из JSON:")
        for desc in descriptions:
            print(desc)

        errors = []  # Список для хранения ошибок

        for desc in descriptions:
            # Обработаем каждое описание из b2b_card_data
            # Проверяем все
            found = any(
                review['project_type'].strip() == desc['project_type'].strip() and
                review['exp'].strip() == desc['exp'].strip() and
                review['level'].strip() == desc['level'].strip() and
                review['price'].strip() == desc['price'].strip() and
                review['text'].strip() == desc['text'].strip()
                for review in card_data_data_from_page
            )

            if not found:
                errors.append(
                    f"Данные из JSON не найдены на странице для: {desc['project_type']} | {desc['exp']} | {desc['level']} | {desc['price']} | {desc['text']}")

        # Если есть ошибки, выводим их
        if errors:
            print("Ошибки:")
            for error in errors:
                print(error)
            # Можно также вызвать исключение, если это необходимо
            raise AssertionError("Некоторые данные не были найдены на странице.")

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
            project_type = section.find(class_='spec fs24').get_text(strip=True)
            exp = section.find(class_='exp').get_text(strip=True)
            level = section.find(class_='level').get_text(strip=True)
            price = section.find(class_='price').get_text(strip=True).replace('\xa0', ' ')
            text = section.find('p').get_text(strip=True)

            logging.info(
                f"project_type: {project_type}, exp: {exp}, level: {level}, price: {price}, text: {text}" )

            team_data.append({
                'exp': exp,
                'level': level,
                'project_type': project_type,
                'price': price,
                'text': text
            })

        return team_data



# метод для черно-белых карточек
 # переделываем метод
    def get_data_card_tiles_website(self):
        # Загрузите данные из JSON
        data = load_file('data_card_block_packages.json')

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = self.get_card_data_tiles(URLs.MAIN_PAGE+subURLs.WEBSITE_DEV)

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_data_from_page:
            print(review)

        # Смотрим, что каждое описание из e_com_card_data присутствует на странице
        descriptions = data['tiles_section_card_data_website']['descriptions']

        # Выводим данные из JSON
        print("Данные из JSON:")
        for desc in descriptions:
            print(desc)

        for desc in descriptions:
            # Обработаем каждое описание из e_com_card_data
            # Проверяем все
            found = any(
                review['project_type'].strip() == desc['project_type'].strip() and
                review['text'].strip() == desc['text'].strip()
                for review in card_data_data_from_page
            )

            assert found, f"Данные из JSON не найдены на странице для: {desc['project_type']} | {desc['text']} "



# метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = URLs.MAIN_PAGE+subURLs.WEBSITE_DEV  # Укажите нужный URL
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json' , 'advant_section_website', url)


# метод для faq
    def get_data_faq_card(self):
        url = URLs.MAIN_PAGE + subURLs.WEBSITE_DEV  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_data_faq, 'faq_block_data.json', 'faq_website_dev', url)