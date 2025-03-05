import logging
from lxml import html
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from constants import URLs
from test.locators import Locators
from utils.data_loader import load_file


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
        self.URL = URLs.MAIN_PAGE
        self.driver = driver

    def open(self, suburl=''):
        self.driver.get(URLs.MAIN_PAGE + suburl)

    def close_modal_popup(self):
        close_modal = self.driver.find_element(*Locators.close_modal)
        close_modal.click()

    def _click_element(self, locator: tuple[str, str]):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logging.info(f"Clicked on element: {locator}")
        except (NoSuchElementException, TimeoutException):
            logging.error(f"Element {locator} not found or not clickable.")

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_title_page(self):
        title_page = self.driver.find_element(*Locators.title_page)
        return title_page.text

    def popup_success_displayed(self, timeout=10):
        try:
            # Ожидание видимости элемента с указанным XPath
            popup_success = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(Locators.popup_success)
            )
            return popup_success.is_displayed()
        except (NoSuchElementException, TimeoutException):
            # Если элемент не найден или не виден в течение указанного времени, возвращаем False
            return False

    def create_index_mapping(self):
        index_mapping = {}
        elements = self.driver.find_elements(*Locators.elements_in_card)
        for index, element in enumerate(elements):
            project_type = element.find_element(*Locators.project_type_with_experience).text.strip()
            index_mapping[project_type] = index  # предполагая, что project_type уникален
        print("Индекс маппинг:", index_mapping)  # Отладочное сообщение
        return index_mapping

    def create_index_mapping_not_experience(self):
        index_mapping = {}
        elements = self.driver.find_elements(*Locators.elements_in_card)
        for index, element in enumerate(elements):
            project_type = element.find_element(*Locators.project_type_not_experience).text.strip()
            index_mapping[project_type] = index  # предполагая, что project_type уникален
        return index_mapping


# проверка карточек с экспириенсем, буллитами, ценой и текстом
    def check_packages_data(self, project_type, experience, bullits, price, text):
        logging.info('move cursor to element')
        index_mapping = self.create_index_mapping()
        print("Индекс маппинг:", index_mapping)  # Отладочное сообщение

        if project_type not in index_mapping:
            raise ValueError(
                f"Project type {project_type} not found on the page. Available types: {list(index_mapping.keys())}")

        index = index_mapping[project_type]
        print('Индекс: ', index)  # Отладочное сообщение

        if index < 0:
            raise ValueError(f"Index {index} is out of bounds. Project type: {project_type}")

        wait = WebDriverWait(self.driver, 10)
        team_card = wait.until(
            EC.presence_of_element_located(Locators.get_check_packages_data_not_experience_locator(index)))
        self.scroll_to_element(team_card)

        attributes = {
            'spec fs24': project_type,
            'exp': experience,
            'level': bullits,
            'price': price,
            'text': text
        }

        for attr, expected in attributes.items():
            if attr == 'text':
                element =  self.driver.find_element(By.XPATH, "(//*[@class='team-card']//p)" + str([index+1]))
                print(element.text)
                assert element.text == expected, f"Ожидался текст: '{expected}', но получен '{element.text}'"
            else:
                element = self.driver.find_element(*Locators.get_data_with_attr_and_index_locator(attr, index))
                print(element.text)
                assert element.text == expected, f"Ожидался заголовок: '{expected}', но получен '{element.text}'"






    # проверка карточек без экспириенса и текста
    def check_packages_data_not_text(self, project_type, bullits, price):
        logging.info('move cursor to element')
        index_mapping = self.create_index_mapping_not_experience()
        print("Индекс маппинг:", index_mapping)  # Отладочное сообщение

        if project_type not in index_mapping:
            raise ValueError(
                f"Project type {project_type} not found on the page. Available types: {list(index_mapping.keys())}")

        index = index_mapping[project_type]
        print("Индекс:", index)  # Отладочное сообщение

        if index < 0:
            raise ValueError(f"Index {index} is out of bounds. Project type: {project_type}")

        wait = WebDriverWait(self.driver, 10)
        team_card = wait.until(
            EC.presence_of_element_located(Locators.get_check_packages_data_not_experience_locator(index)))
        self.scroll_to_element(team_card)

        attributes = {
            'spec fs22': project_type,
            'level': bullits,
            'price': price
        }

        for attr, expected in attributes.items():
            element = self.driver.find_element(*Locators.get_data_with_attr_and_index_locator(attr, index))
            print(element.text)
            assert element.text == expected, f"Ожидался заголовок: '{expected}', но получен '{element.text}'"


# метод для извлечения данных
    def get_card_data_tiles(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение всех элементов с классами, содержащими 'tile w-'
        team_data = []
        type_section = soup.select("[class*='tile w-']")  # Используем селектор для поиска классов

        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'tile w-'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'tile w-'")

        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'tile w-'")
            return team_data  # Возвращаем пустой список, если ничего не найдено

        for section in type_section:
            # Извлечение project_type из текущего элемента
            project_type_element = section.select_one("h3")  # Извлекаем h3 внутри текущего элемента
            project_type = project_type_element.get_text(strip=True) if project_type_element else 'Не найдено'

            # Извлечение text из элементов span внутри текущего элемента
            text_section = section.select_one("span")  # Находим span внутри текущего элемента
            text = text_section.get_text(strip=True) if text_section else 'Не найдено'

            # Удаление нежелательных символов из text
            text = text.replace('\u2028', '')  # Удаляем символ разрыва строки
            text = text.replace('\n', ' ').replace('\r', '')  # Удаляем переносы строк

            logging.info(f"project_type: {project_type}, text: {text}")

            team_data.append({
                'project_type': project_type,
                'text': text
            })

        return team_data


# метод для извлечения данных для черно-белых карточек с кружками и порядковыми номерами
    def get_card_data_tiles_card(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга

        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath("//*[@class='card']")  # Используем XPath для поиска классов

        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'card'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'card'")

        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'card'")
            return team_data  # Возвращаем пустой список, если ничего не найдено

        lokator = './/p'
        for section in type_section:
            # Извлечение project_type из текущего элемента
            project_type_element = section.xpath(".//h3[@class='card-title']")  # Используем XPath
            project_type = project_type_element[0].text_content().strip() if project_type_element else 'Не найдено'

            # Извлечение text из элементов p внутри текущего элемента
            text_section = section.xpath(lokator)  # Используем XPath
            text = text_section[0].text_content().strip() if text_section else 'Не найдено'

            # Удаление нежелательных символов из text
            text = text.replace('\u2028', '')  # Удаляем символ разрыва строки
            text = text.replace('\n', ' ').replace('\r', '')  # Удаляем переносы строк

            logging.info(f"project_type: {project_type}, text: {text}")

            team_data.append({
                'project_type': project_type,
                'text': text
            })

        return team_data





# метод для извлечения данных для faq
    def get_data_faq(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга

        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath("//*[@class='accordeon-body']")  # Используем XPath для поиска классов

        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'accordeon-body'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'accordeon-body'")

        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'accordeon-body'")
            return team_data  # Возвращаем пустой список, если ничего не найдено

        for section in type_section:
            # Извлечение project_type из текущего элемента
            project_type_element = section.xpath(".//*[@class='accordeon-question']")  # Используем XPath
            project_type = project_type_element[0].text_content().strip() if project_type_element else 'Не найдено'

            project_type = project_type.replace('â', '’')
            project_type = str(project_type.replace('\u2028', '')
                            .replace('\x80\x99', '')
                            .replace('Â\xa0',' '))  # Удаляем символ разрыва строки

            # Извлечение text из элементов p внутри текущего элемента
            text_section = section.xpath(".//*[@class='accordeon-subject-text']")  # Используем XPath
            text = text_section[0].text_content().strip() if text_section else 'Не найдено'

            # Обрабатываем
            text = text.replace('\u2028', '')  # Удаляем символ разрыва строки
            text = (text.replace('\x80\x99', '')
                    .replace('Â\xa0', '’')
                    .replace('â', '’'))
            text = (text.replace('\n', ' ')
                    .replace('\r', '')
                    .replace('\xa0', ' '))

            logging.info(f"project_type: {project_type}, text: {text}")

            team_data.append({
                'project_type': project_type,
                'text': text
            })

        return team_data


# метод для извлечения данных для карточек из карусели
    def get_data_advant_section_carousel(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга

        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath("//*[@class='advant-card-content']")  # Используем XPath для поиска классов

        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-card-content'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-card-content'")

        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'advant-card-content'")
            return team_data  # Возвращаем пустой список, если ничего не найдено

        for section in type_section:
            # Извлечение project_type из текущего элемента
            project_type_element = section.xpath(".//*[@class='advant-title']")  # Используем XPath
            project_type = project_type_element[0].text_content().strip() if project_type_element else 'Не найдено'


            # Извлечение text из элементов span внутри текущего элемента
            text_section = section.xpath(".//span")  # Используем XPath
            text = text_section[0].text_content().strip() if text_section else 'Не найдено'

            # Обрабатываем
            text = text.replace('\u2028', '')  # Удаляем символ разрыва строки
            text = (text.replace('\x80\x99', '')
                    .replace('Â\xa0', '’')
                    .replace('â', '’'))
            text = (text.replace('\n', ' ')
                    .replace('\r', '')
                    .replace('\xa0', ' '))

            logging.info(f"advant_title: {project_type}, advant_text: {text}")

            team_data.append({
                'advant_title': project_type,
                'advant_text': text
            })

        return team_data


# делаем универсальный метод куда передаем параметры: урл, data[] (т.е.название блока из json)
# метод для карусели адвант
    def get_data_advant_carousel(self, url_method, file_load, json_key, url):
        # Загрузите данные из JSON
        data = load_file(file_load)

        # Получаем данные из блока карусели на странице
        card_data_from_page = url_method(url)

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_from_page:
            print(review)

        # Смотрим, что каждое описание из advant_section_e_com присутствует на странице
        descriptions = data[json_key]['descriptions']

        # Выводим данные из JSON
        print("Данные из JSON:")
        for desc in descriptions:
            print(desc)

        for desc in descriptions:
            # Обработаем каждое описание
            found = any(
                review['advant_title'].strip() == desc['advant_title'].strip() and
                review['advant_text'].strip() == desc['advant_text'].strip()
                for review in card_data_from_page
            )

            assert found, f"Данные из JSON не найдены на странице для: {desc['advant_title']} | {desc['advant_text']} "


# метод для faq
 # переделываем метод
    def get_data_card_with_type_project(self, url_method, file_load, json_key, url):
        # Загрузите данные из JSON
        data = load_file(file_load)

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = url_method(url)

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_data_from_page:
            print(review)

        # Смотрим, что каждое описание из e_com_card_data присутствует на странице
        descriptions = data[json_key]['descriptions']

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
            experience = section.find(class_='exp').get_text(strip=True)
            level = section.find(class_='level').get_text(strip=True)
            project_type = section.find(class_='spec fs24').get_text(strip=True)
            price = section.find(class_='price').get_text(strip=True).replace('\xa0', ' ')
            text = section.find('p').get_text(strip=True)

            logging.info(
                f"project_type: {project_type}, level: {level}, exp: {experience}, price: {price}, text: {text}")

            team_data.append({
                'exp': experience,
                'level': level,
                'project_type': project_type,
                'price': price,
                'text': text
            })

        return team_data

  # переделываем метод
    def get_data_card_(self, url_method, file_load, json_key, url):
        # Загрузите данные из JSON
        data = load_file(file_load)

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = url_method(url)

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_data_from_page:
            print(review)

        # Смотрим, что каждое описание из cms_card_data присутствует на странице
        descriptions = data[json_key]['descriptions']

        # Выводим данные из JSON
        print("Данные из JSON:")
        for desc in descriptions:
            print(desc)

        for desc in descriptions:
            # Обработаем каждое описание из cms_card_data
            # Проверяем все
            found = any(
                review['project_type'].strip() == desc['project_type'].strip() and
                review['exp'].strip() == desc['exp'].strip() and
                review['level'].strip() == desc['level'].strip() and
                review['price'].strip() == desc['price'].strip() and
                review['text'].strip() == desc['text'].strip()
                for review in card_data_data_from_page
            )

            assert found, f"Данные из JSON не найдены на странице для: {desc['project_type']} | {desc['exp']} | {desc['level']} | {desc['price']} | {desc['text']}"

    def get_card_data_tile_squad(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение всех элементов с классом 'tile-squad-item card'
        team_data = []
        type_section = soup.find_all(class_='tile-squad-item card')

        logging.info(f"Найдено {len(type_section)} элементов с классом 'tile-squad-item card'")

        for section in type_section:
            # Извлечение данных
            title = section.find('h3').get_text(strip=True)
            #title_project = section.xpath('.//h3').get_text(strip=True)
            #title = title_project[0].text_content().strip() if title_project else 'Не найдено'
            text = section.find(class_='tile-squad-descr').get_text(strip=True)

            logging.info(
                f"project_type: {title}, text: {text}")

            team_data.append({
                'project_type': title,
                'text': text
            })

        return team_data

