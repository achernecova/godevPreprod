import logging
import os
from time import sleep

import allure
import requests
from bs4 import BeautifulSoup
from lxml import html
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test.locators import Locators
from utils.data_loader import load_file


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver, base_url=None):
        # Если base_url не передан, используем значение из переменной окружения
        self.URL = base_url or os.getenv('MAIN_PAGE', 'https://dev.godev.agency/')  # Значение по умолчанию
        self.driver = driver

    def open(self, suburl=''):
        full_url = self.URL + suburl
        logging.info(f"Открываем страницу: {full_url}")
        self.driver.get(full_url)

    def get_base_url(self):
        base_url = put_a_secret()
        sub_url = getattr(self, 'subURL', '')
        return base_url + sub_url

    """
    Новый метод для связывания данных на странице (в карточках) и в json
    how_it_staff_b2b - блок с черно-белыми карточками с кружками и порядковыми номерами
    card_tiles_b2b - блок с черно-белыми 3д карточками
    ...
    """
    def get_data_card(self, card_type):
        config = {
            'tiles_cms': {
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_cms',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'how_it_staff_cms': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_cms',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'section_it_staff_main': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'app_and_web_services_main',
                'locator_block': "//*[@class='service-item']",
                'locator_element': ".//*[@class='service-descr']",
                'locator_section': './/h3'
            },
            'tiles_main': {
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_main',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span"
            },
            'how_it_staff_main': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_main',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']"
            },
            'how_it_staff_b2b': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'how_it_staff_b2b',
                'locator_block': "//*[@class='card']",
                'locator_element': ".//h3[@class='card-title']",
                'locator_section': './/p',
            },
            'card_tiles_b2b': {
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_b2b',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'tiles_icon_d2c': {
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_icon_card_data_d2c',
                'locator_block': "//*[@class='tiles icons']//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'tiles_img_d2c': {
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_d2c',
                'locator_block': "//*[@class='tiles images']//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'accordeon_faq_design': {
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_design',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'how_it_staff_design': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_design',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'tiles_e_com': { # метод для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_e_com',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'faq_frame': {
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_framework',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'advant_frame': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'advantages_of_outsourcing_framework',
                'locator_block': "//*[@class='advantages-outsourcing__item']",
                'locator_element': ".//*[@class='advantages-outsourcing__text']",
                'locator_section': ".//*[@class='advantages-outsourcing__title']",
            },
            'how_it_staff_frame': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_framework',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'tile_squad_landing': {  # для цветных карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'tile_squad',
                'locator_block': "//*[@class='tile-squad-item card']",
                'locator_element': ".//h3",
                'locator_section': ".//*[@class='tile-squad-descr']",
            },
            'how_it_staff_landing': {  # для черно-белых карточек с кружками и порядковыми номерами
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_landing',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'tiles_landing': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_landing',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'card_tiles_mobile': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_mobile',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'how_it_staff_mobile': {  # для черно-белых карточек с кружками и порядковыми номерами
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_mobile',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'faq_card_mobile': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_mobile',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'card_tiles_outstaff': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_outstaff',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'how_it_staff_outstaff': {  # для черно-белых карточек с кружками и порядковыми номерами
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_outstaff',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'convenient_of_outstaff': {  # для черно-белых карточек
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'convenient_of_outstaffing',
                'locator_block': "//*[@class='work-card']",
                'locator_element': ".//span[not(@class)]",
                'locator_section': ".//span[@class='h3']",
            },
            'faq_outstaff': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_outstaff',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'tiles_react': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_react',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'how_it_staff_react': {  # для черно-белых карточек с кружками и порядковыми номерами
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_react',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'app_and_web_services_react': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'app_and_web_services_react',
                'locator_block': "//*[@class='service-item']",
                'locator_element': ".//*[@class='service-descr']",
                'locator_section': './/h3',
            },
            'advant_of_outsource_react': {
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'advantages_of_outsourcing_react',
                'locator_block': "//*[@class='advantages-outsourcing__item']",
                'locator_element': ".//*[@class='advantages-outsourcing__text']",
                'locator_section': ".//*[@class='advantages-outsourcing__title']",
            },
            'card_best_framework_react': {  # для черно-белых карточек с кружками и порядковыми номерами
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'best_framework_card_blocks_react',
                'locator_block': "//*[contains(@class, 'best-frameworks__item ')]",
                'locator_element': ".//*[@class='best-frameworks__item-text']",
                'locator_section': ".//*[@class='best-frameworks__item-title']",
            },
            'faq_card_react': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_reactjs',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'card_tiles_saas': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_saas',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'how_it_staff_saas': {  # для черно-белых карточек с кружками и порядковыми номерами
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'how_it_staff_saas',
                'locator_block': "//*[@class='card']",
                'locator_element': ".//h3[@class='card-title']",
                'locator_section': './/p',
            },
            'faq_card_saas': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_web_saas',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'app_and_web_services_advant': {  # для черно-белых карточек
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
                'locator_element': ".//*[@class='service-descr']",
                'locator_section': './/h3',
            },
            'card_tiles_support': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_support',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'how_it_staff_support': {  # для черно-белых карточек с кружками и порядковыми номерами
                'file_load': 'section_how_it_staff_tiles.json',
                'url_method': self.get_card_data_tiles_card,
                'json_key': 'how_it_staff_support',
                'locator_block': "//*[@class='card']",
                'locator_element': './/p',
                'locator_section': ".//h3[@class='card-title']",
            },
            'faq_card_support': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_support',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'faq_card_symfony': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_symfony',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'card_tiles_web_dev_services': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_webdev',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'faq_card_web_dev_services': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_web_dev',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            },
            'tiles_website': {  # для черно-белых карточек
                'file_load': 'data_card_block_packages.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'tiles_section_card_data_website',
                'locator_block': "//*[contains(@class, 'tile w-')]",
                'locator_element': ".//h3",
                'locator_section': ".//span",
            },
            'faq_website': {  # для faq
                'file_load': 'faq_block_data.json',
                'url_method': self.get_data_faq_tiles_new,
                'json_key': 'faq_website_dev',
                'locator_block': "//*[@class='accordeon-body']",
                'locator_element': ".//*[@class='accordeon-question']",
                'locator_section': ".//*[@class='accordeon-subject-text']",
            }
        }

        if card_type not in config:
            raise ValueError(f"Такого блока не существует: {card_type}")

        conf = config[card_type]
        url = self.get_base_url()

        self.get_data_card_with_type_project(
            conf['file_load'],
            conf['url_method'],
            conf['json_key'],
            conf['locator_block'],
            conf['locator_element'],
            conf['locator_section'],
            url
        )


    @allure.step("Закрытие окна кеш-куки")
    def close_modal_popup(self):
        close_modal = self.driver.find_element(*Locators.close_modal)
        close_modal.click()

    @allure.step("Клик по элементу")
    def _click_element(self, locator: tuple[str, str]):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logging.info(f"Clicked on element: {locator}")
        except (NoSuchElementException, TimeoutException):
            logging.error(f"Element {locator} not found or not clickable.")

    def scroll_new(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)  # Ждем, пока элемент станет видимым
        )
        element = self.driver.find_element(*locator)  # Убедитесь, что locator корректен
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # Прокрутка до элемента
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)  # Ждем, пока элемент станет кликабельным
        )
        return element  # Возвращаем элемент

    # Метод для скролла до элемента
    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        # Ждём, пока элемент станет видимым
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        # Прокручиваем элемент в центр окна браузера
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        # Ждём, пока элемент станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        # Дополнительно можно проверить, что элемент виден в viewport
        WebDriverWait(self.driver, 5).until(lambda d: self.is_element_in_viewport(element))

    def is_element_in_viewport(self, element):
        # Возвращает True, если элемент видим в viewport
        return self.driver.execute_script(
            """
            var elem = arguments[0],
                box = elem.getBoundingClientRect(),
                cx = box.left + box.width / 2,
                cy = box.top + box.height / 2,
                e = document.elementFromPoint(cx, cy);
            return e === elem || elem.contains(e);
            """, element)

    @allure.step("Ожидаем пока элемент станет видимым")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Получение текущего урла")
    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step("Получение заголовка")
    def get_title_page(self):
        title_page = self.driver.find_element(*Locators.title_page)
        return title_page.text

    @allure.step("Получение признака отображения окна успешности отправки заявки")
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
    @allure.step("Проверка списка данных из блока с экспириенсем, буллитами, ценой и текстом")
    def check_packages_data(self, project_type, experience, bullits, price, text):
        logging.info('move cursor to element')
        index_mapping = self.create_index_mapping()
        if project_type not in index_mapping:
            raise ValueError(
                f"Project type {project_type} not found on the page. Available types: {list(index_mapping.keys())}")
        index = index_mapping[project_type]
        if index < 0:
            raise ValueError(f"Index {index} is out of bounds. Project type: {project_type}")
        # Используем правильный локатор
        locator = (By.XPATH, f"//*[contains(@class, 'team-card')][{index + 1}]")
        # team_card_new = self.driver.find_element(*locator)
        # Теперь передаем локатор в scroll_to_element
        self.scroll_to_element(locator)
        attributes = {
            'spec fs24': project_type,
            'exp': experience,
            'level': bullits,
            'price': price,
            'text': text
        }
        for attr, expected in attributes.items():
            if attr == 'text':
                element = self.driver.find_element(By.XPATH, f"((//*[@class='team-card']//p)[{index + 1}])")
                assert element.text == expected, f"Expected text: '{expected}', but got '{element.text}'"
            else:
                locator = Locators.get_data_with_attr_and_index_locator(attr, index)
                print(f"Locator for attr '{attr}' at index {index}: {locator}")
                assert locator is not None, f"Locator is None for attr '{attr}' and index {index}"

                try:
                    element = self.driver.find_element(*locator)
                    assert element.text == expected, f"Expected header: '{expected}', but got '{element.text}'"
                except NoSuchElementException:
                    raise AssertionError(f"Element with attribute '{attr}' and index {index} not found.")

    # метод для извлечения данных для черно-белых карточек с кружками и порядковыми номерами
    @staticmethod
    @allure.step("Получение списка данных из блока с черно-белыми карточками с кружками и порядковым номером")
    def get_card_data_tiles_card(url, locator_block, locator_element, locator_section):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга
        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath(locator_block)  # Используем XPath для поиска классов
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими {locator_block}")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими {locator_block}")
        if not type_section:
            logging.warning(f"Не найдено элементов с классами, содержащими {locator_block}")
            return team_data  # Возвращаем пустой список, если ничего не найдено
        for section in type_section:
            # Извлечение project_type из текущего элемента
            project_type_element = section.xpath(locator_section)  # Используем XPath
            project_type = project_type_element[0].text_content().strip() if project_type_element else 'Не найдено'
            # Извлечение text из элементов p внутри текущего элемента
            text_section = section.xpath(locator_element)  # Используем XPath
            text = text_section[0].text_content().strip() if text_section else 'Не найдено'
            # Удаление нежелательных символов из text
            text = text.replace('\u2028', '')  # Удаляем символ разрыва строки
            text = text.replace('\n', ' ').replace('\r', '').replace('â\x80\x99', '’')  # Удаляем переносы строк
            logging.info(f"project_type: {project_type}, text: {text}")
            team_data.append({
                'project_type': project_type,
                'text': text
            })
        return team_data

    # метод для faq
    @staticmethod
    @allure.step(
        "Проверка получения корректных данных из блока Boost your business with a landing page и сравнение с данными из json")
    def get_data_card_with_type_project(file_load, url_method, json_key, locator_block, locator_element,
                                        locator_section, url):
        # Загрузите данные из JSON
        data = load_file(file_load)
        # Получаем данные из блока карусели на странице
        card_data_data_from_page = url_method(url, locator_block, locator_element, locator_section)
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

    # метод для карточек rates
    @staticmethod
    @allure.step("Проверка данных в карточках блока Rates")
    def get_data_card_with_type_project_rates(url_method, file_load, json_key, url):
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
                review['text'].strip() == desc['text'].strip() and
                review['price'].strip() == desc['price'].strip()
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
    @staticmethod
    def get_data_card_name_price_text_button_more(url_method, file_load, json_key, url):
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
        errors = []  # Список для хранения ошибок
        for desc in descriptions:
            # Обработаем каждое описание из cms_card_data
            # проверяем все
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
            raise AssertionError("Некоторые данные не были найдены на странице.")

    @staticmethod
    def get_card_data_tile_squad(url):
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
            text = section.find(class_='tile-squad-descr').get_text(strip=True)
            logging.info(
                f"project_type: {title}, text: {text}")
            team_data.append({
                'project_type': title,
                'text': text
            })
        return team_data

    # метод для извлечения данных из карточек rates
    @allure.step("Извлекаем данные со страницы из блока Rates")
    def get_card_data_rates(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)
        team_data = []
        type_section = tree.xpath("//*[contains(@class, 'tarif-item')]")
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'tarif-item '")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'tarif-item '")
        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'tarif-item '")
            return team_data
        for section in type_section:
            project_type_element = section.xpath(".//*[@class='tarif-name']//span/text()")
            project_type = project_type_element[0].strip() if project_type_element else 'Не найдено'

            price_section = section.xpath(".//*[@class='tarif-price']//span/text()")
            price_text = price_section[0].strip() if price_section else 'Не найдено'
            price_text = price_text.replace('\u2028', '').replace('\n', ' ').replace('\r', '')

            price_section_text = section.xpath(".//*[@class='tarif-descr']//span/text()")
            text = price_section_text[0].strip() if price_section_text else 'Не найдено'
            text = text.replace('\u2028', '').replace('\n', ' ').replace('\r', '').replace('â\x80\x99', '’')

            logging.info(f"project_type: {project_type}, price: {price_text}, text: {text}")
            team_data.append({
                'project_type': project_type,
                'price': price_text,
                'text': text
            })
        return team_data

    # Объединяем три метода в один
    @allure.step("Получаем данные из блока с отзывами")
    def get_reviews_data_from_page(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')
        element_new = 'review-card'
        # Извлечение всех элементов с классом 'review-card'
        reviews_data = []
        type_section = soup.find_all(class_=element_new)
        for section in type_section:
            # Извлечение текста отзыва
            text = section.find(class_='review-text').get_text(strip=True)
            # Извлечение названия организации
            author_company = section.find(class_='author-company').get_text(strip=True)
            # Извлечение имени автора
            author_name = section.find(class_='author-name').get_text(strip=True)
            reviews_data.append({
                'text': text,
                'author_company': author_company,
                'author_name': author_name
            })
        return reviews_data

    # проверка данных с карусели с отзывами
    @allure.step("Проверяем данные из карусели с отзывами на корректность")
    def get_data_review_(self, url_method, file_load, json_key, url):
        # Загрузите данные из JSON
        data = load_file(file_load)
        # получаем данные из блока карусели на странице
        reviews_data_from_page = url_method(url)
        logging.info(f'Полученные данные с страницы: {reviews_data_from_page}')

        # смотрим, что каждое описание из JSON присутствует на странице
        descriptions = data[json_key]['descriptions']
        logging.info(f'Заголовок из JSON: {str(descriptions)}')

        for desc in descriptions:
            print("Компания: " + str({desc['author_company']}))
            print("Автор: " + str({desc['author_name']}))
            print("Текст отзыва: " + str({desc['text']}))
            assert desc['text'] in [review['text'] for review in
                                    reviews_data_from_page], f"Текст не найден на странице: {desc['text']}"
            assert desc['author_company'].strip() in [review['author_company'] for review in
                                                      reviews_data_from_page], f"Организация не найдена на странице: {desc['author_company']}"
            assert desc['author_name'] in [review['author_name'] for review in
                                           reviews_data_from_page], f"Автор не найден на странице: {desc['author_name']}"

    # метод для извлечения данных для faq - для всех страниц
    @allure.step("Получаем данные из блока FAQ")
    def get_data_faq_tiles_new(self, url, locator_block, locator_element, locator_section):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга
        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath(locator_block)  # Используем XPath для поиска классов
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими '{locator_block}'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими '{locator_block}'")
        if not type_section:
            logging.warning(f"Не найдено элементов с классами, содержащими '{locator_block}'")
            return team_data  # Возвращаем пустой список, если ничего не найдено
        for section in type_section:
            # Извлечение project_type из текущего элемента
            project_type_element = section.xpath(locator_element)  # Используем XPath
            project_type = project_type_element[0].text_content().strip() if project_type_element else 'Не найдено'
            project_type = project_type.replace('â', '’')
            project_type = str(project_type.replace('\u2028', '')
                               .replace('\x80\x99', '')
                                .replace('’\x80\x94 ', ' — ')
                                .replace('’\x80\x93', '–')
                               .replace('Â\xa0', ' '))  # Удаляем символ разрыва строки
            # Извлечение text из элементов p внутри текущего элемента
            text_section = section.xpath(locator_section)  # Используем XPath
            text = text_section[0].text_content().strip() if text_section else 'Не найдено'
            # Обрабатываем
            text = text.replace('\u2028', '')  # Удаляем символ разрыва строки
            text = (text.replace('\x80\x99', '')
                    .replace('Â\xa0', '’')
                    .replace('â', '’')
                    .replace('’\x80\x94 ', '— ')
                    .replace('’\x80\x93', '–'))
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
    @allure.step("Получаем данные из карточек карусели")
    def get_data_advant_section_carousel(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга
        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath(
            "//*[contains(@class, 'swiper-slide grabbable')]//*[@class='advant-card']")  # Используем XPath для поиска классов
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-card-content'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'swiper-slide grabbable // advant-card'")
        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'swiper-slide grabbable // advant-card'")
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


    # метод для извлечения данных для карточек из карусели
    @allure.step("Получаем данные из карточек карусели c icons")
    def get_data_advant_section_carousel_icons(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга
        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath(
            "//*[@class='advant-section']//*[contains(@class, ' swiper icons')]")  # Используем XPath для поиска классов
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими ' swiper icons'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими ' swiper icons // advant-card'")
        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими ' swiper icons // advant-card'")
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
    @allure.step("Проверка данных из блока для карусели advant")
    def get_data_advant_carousel(self, url_method, file_load, json_key, url):
        # Загрузите данные из JSON
        data = load_file(file_load)
        # Получаем данные из блока карусели на странице
        card_data_from_page = url_method(url)
        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_from_page:
            print(review)
        # Смотрим, что каждое описание из advant_section_<> присутствует на странице
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

    @allure.step("Получаем заголовок блока")
    def get_title_block_from_page_all(self, locator):
        method, value = locator
        title_element = self.driver.find_element(method, value)
        if title_element is not None:
            title_text = title_element.text.strip()
            logging.info(f"Заголовок на странице: '{title_text}'")
            return title_text
        else:
            logging.error('Ошибка!!! Заголовок не найден.')
            return 'Ошибка!!!'

    @allure.step("Клик по кнопке Ask a Question в блоке FAQ")
    def click_button_in_faq(self):
        self.click_body_element()
        element = self.driver.find_element(*Locators.button_in_faq_locator)
        try:
            # Прокрутка к элементу (используем уже найденный элемент)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # Находим и закрываем модальное окно (важно, чтобы это не мешало клику на основной кнопке)
            button_close_modal = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.close_modal)
            )
            button_close_modal.click()
            element.click()  # Кликаем на уже найденный элемент
        except Exception as e:
            print(f"Error clicking button: {str(e)}")
            raise  # Повторно выбрасываем исключение для дальнейшей обработки

    # тянем текст из блока
    @allure.step("Получаем текст блока")
    def get_text_block_from_page_all(self, locator):
        method, value = locator
        try:
            # Выведем HTML для отладки
            # print(self.driver.page_source)

            text_element = self.driver.find_element(method, value)
            text = text_element.text.strip()
            logging.info(f"Текст на странице: '{text}'")
            return text
        except:
            logging.error('Ошибка!!! Текст не найден.')
            return 'Ошибка!!!'

    # метод для извлечения данных для карточек из карусели
    @allure.step("Получаем данные из карточек блока")
    def get_data_advant_section_card(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга
        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath("//*[contains(@class, 'advant-card ')]")  # Используем XPath для поиска классов
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-card '")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-card '")
        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'advant-card '")
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

    # метод для извлечения данных для карточек из карусели с серебряными картинками
    @allure.step("Получаем данные из карточек карусели")
    def get_data_advant_section_carousel_d2c(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга
        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath(
            "//*[contains(@class, 'advant-slider swiper images')]//*[@class='advant-card']")  # Используем XPath для поиска классов
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-slider swiper images'")
        print(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-slider swiper images // advant-card'")
        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'swiper-slide grabbable // advant-card'")
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

        # метод для извлечения данных для карточек из карусели с серебряными картинками

    @allure.step("Получаем данные из карточек карусели")
    def get_data_advant_section_carousel_d2c_icons(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        tree = html.fromstring(response.content)  # Используем lxml для парсинга
        # Извлечение всех элементов с классами, содержащими 'card'
        team_data = []
        type_section = tree.xpath(
            "//*[contains(@class, 'advant-slider swiper icons')]//*[@class='advant-card']")  # Используем XPath для поиска классов
        logging.info(f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-slider swiper images'")
        print(
            f"Найдено {len(type_section)} элементов с классами, содержащими 'advant-slider swiper images // advant-card'")
        if not type_section:
            logging.warning("Не найдено элементов с классами, содержащими 'swiper-slide grabbable // advant-card'")
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

    def click_body_element(self):
        element = self.driver.find_element(*Locators.body_element)
        element.click()

    """
    Метод для клика по кнопку Get in touch в баннере (в верху страницы).
    После оптимизации - скрипты запускаются только по клику в любую область экрана. 
    Чтобы обойти это - используем клик по любой области экрана, иначе скрипты не запускаются и селениум не видит кнопки, 
    соответственно выбрасывает исключение
    click_body_element() - метод для клика в пустой области страницы.
    Locators.close_modal - специально делаем метод для ожидания кликабельности окна куков, чтобы убедиться, что у нас запустились скрипты. Не удалять!         
    """
    @allure.step("Кликаем по кнопке в баннере")
    def click_button_banner(self):
        self.click_body_element()
        # Находим элемент с помощью правильного метода
        click_button_banner = self.driver.find_element(*Locators.button_banner_page_locator)

        # Используем новый метод для прокрутки
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_button_banner)

        # Находим элемент и ждем его кликабельности
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.close_modal)
        )
        # Кликаем по элементу
        self.driver.execute_script("arguments[0].click();", click_button_banner)

    def get_title_block(self, locator):
        self.click_body_element()
        wait = WebDriverWait(self.driver, 15)
        try:
            # Ждем появления элемента и его видимости
            title_element = wait.until(EC.visibility_of_element_located(locator))
            # Скроллим к элементу
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", title_element)
            # Получаем текст элемента
            title = self.get_title_block_from_page_all(locator)
            print(title)
            return title
        except TimeoutException:
            print("Элемент не найден или не стал видимым за отведенное время.")
            raise

    def get_text_block(self, locator):
        self.click_body_element()
        self.scroll_to_element(locator)
        text = self.get_text_block_from_page_all(locator)
        return text




def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования
        format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщения
        handlers=[
            logging.FileHandler("app.log"),  # Запись логов в файл
            logging.StreamHandler()  # Вывод логов в консоль
        ]
    )


def put_a_secret():
    # Получаем значение окружения
    environment = os.getenv('ENVIRONMENT',
                            'development')  # Значение по умолчанию - development (второе значение - production)
    # Определяем базовый URL в зависимости от окружения
    if environment == 'production':
        base_url = os.getenv('PROD_PAGE', 'https://godev.agency/')  # Значение по умолчанию для прод окружения
    else:
        base_url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/')  # Значение по умолчанию для дев окружения
    return base_url

