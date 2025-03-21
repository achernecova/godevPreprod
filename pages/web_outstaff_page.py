import logging
import os

import allure
import requests
from bs4 import BeautifulSoup
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class WebOutstaffPage(BasePage):
    fake = Faker()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')


    @allure.step("Открытие страницы лендинга по URL: services/outstaffing-and-outsourcing-of-it-specialists/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL


    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)


    @allure.step("Клик по кнопке Get in touch в блоке Outstaffing and outsourcing of IT-teams")
    def click_button_outsource(self):
        try:
            button_request = self.scroll_new(Locators.button_request)
            if button_request and button_request.is_displayed() and button_request.is_enabled():
                self.driver.execute_script("arguments[0].click();", button_request)  # Используем JavaScript для клика
            else:
                print("Button is not available for clicking.")
        except Exception as e:
            print(f"Error clicking button: {str(e)}")
            raise  # Повторно выбрасываем исключение для дальнейшей обработки

    @allure.step("Проверка данных в блоке Different models of hiring IT specialists")
    def get_data_carousel(self):
        # загружаем данные из json
        data = load_file('carousel_types_of_it.json')

        # получаем описание из блока карусели на странице
        descriptions_from_page = self.get_descriptions_from_page(os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/'))

        # проверяем, что каждое описание из JSON присутствует на странице
        descriptions = data['tiles_section']['descriptions']

        # логи
        logging.info(f"Полученные данные с страницы: {descriptions_from_page}")

        for desc in descriptions:
            # логи каждого описания и заголовка из JSON
            logging.info(f"Описание из JSON: {desc['description_card']}")
            logging.info(f"Заголовок из JSON: {desc['title_card']}")

            # проверяем наличия заголовка и описания на странице
            assert desc['title_card'].strip().lower() in [item['title_card'].strip().lower() for item in
                                                          descriptions_from_page], \
                f"Заголовок не найден на странице: {desc['title_card']}"
            assert desc['description_card'].strip().lower() in [item['description_card'].strip().lower() for item in
                                                                descriptions_from_page], \
                f"Описание не найдено на странице: {desc['description_card']}"


    # тянем данные из описания карточки
    @allure.step("Получение заголовка и текста из блока Different models of hiring IT specialists")
    def get_descriptions_from_page(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Получаем все элементы с классом 'types-of-it-card' - т.е. находим карточки
        reviews_data = []
        type_section = soup.find_all(class_='types-of-it-card')

        for section in type_section:
            # извлекаем заголовок
            descr_card = section.find(class_='types-of-it-descr').get_text(strip=True)
            title_card = section.find(class_='types-of-it-title').get_text(strip=True)

            reviews_data.append({
                'title_card': title_card,
                'description_card': descr_card
            })
            print(f'Полученный заголовок: {title_card}')
            print(f'Полученное описание: {descr_card}')
        return reviews_data


   # переделываем метод
    @allure.step("Проверка данных в блоке Team and specialists")
    def get_data_team_and_spec(self):
        # Загрузите данные из JSON
        data = load_file('data_card_block_packages.json')

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = self.get_card_data(os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/'))
        logging.info(f'Полученные данные с страницы: {card_data_data_from_page}')

        # Смотрим, что каждое описание из outstaff_card_data присутствует на странице
        descriptions = data['outstaff_card_data']['descriptions']
        logging.info(f'Заголовок из JSON: {str(descriptions)}')

        for desc in descriptions:
            # Обработаем каждое описание из outstaff_card_data
            # Проверяем все
            found = any(
                review['direction'].strip().lower() == desc['direction'].strip().lower() and
                review['exp'].strip() == desc['exp'].strip() and
                review['level'].strip() == desc['level'].strip() and
                review['price'].strip() == desc['price'].strip() and
                review['text'].strip() == desc['text'].strip()
                for review in card_data_data_from_page
            )

            assert found, f"Данные из JSON не найдены на странице для: {desc['direction']} | {desc['exp']} | {desc['level']} | {desc['price']}"



    # Объединяем три метода в один
    @allure.step("Получение данных в карточках блока Team and specialists")
    def get_card_data(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение всех элементов с классом 'team-card'
        team_data = []
        type_section = soup.find_all(class_='team-card')  # Измените на 'team-card'

        print(f"Найдено {len(type_section)} элементов с классом 'team-card'")  # Отладочный вывод

        for section in type_section:
            # Извлечение данных
            experience = section.find(class_='exp').get_text(strip=True)
            level = section.find(class_='level').get_text(strip=True)
            direction = section.find(class_='spec fs24').get_text(strip=True)
            price = section.find(class_='price').get_text(strip=True)
            text = section.find('p').get_text(strip=True)

            print(
                f"direction: {direction}, level: {level}, exp: {experience}, price: {price}, text: {text}")  # Отладочный вывод

            team_data.append({
                'exp': experience,
                'level': level,
                'direction': direction,
                'price': price,
                'text': text
            })

        return team_data


# метод для черно-белых карточек
    def get_data_card_tiles_outstaff(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_outstaff',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)


# метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_outstaff(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_outstaff',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

        # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_convenient_outstaff(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'convenient_of_outstaffing',
            "//*[@class='work-card']",
            ".//span[not(@class)]",
            ".//span[@class='h3']",
             url)

# метод для faq
    def get_data_faq_card_new(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_outstaff',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)


# метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel,'advant_section_carousel.json' , 'advant_section_outstaff', url)


    @allure.step("Клик по кнопке Get in touch")
    def click_button_get_in_touch(self):
        # ждем видимость блока
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.block_get_in_touch_locator)
        )
        # крутим страницу попиксельно до элемента
        position = element.location['y']
        self.driver.execute_script("window.scrollTo(0, arguments[0]);", position)
        # Дополнительное ожидание видимости кнопки
        click_button_banner = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.button_get_in_touch_locator)
        )
        # дополнительно проверяем видимость
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return arguments[0].getBoundingClientRect().top >= 0;",
                                                 click_button_banner)
        )
        # клик по кнопке через js
        self.driver.execute_script("arguments[0].click();", click_button_banner)


    def get_popup(self):
        return PopupElement(self.driver)

    # тянем заголовок из названия блока Digital Agency Godev
    def get_title_block_convenient (self):
        return self.get_title_block(Locators.title_convenient_locator)


    @allure.step("Получаем заголовок блока")
    def get_title_block(self, locator):
        # Сначала сделаем скролл к элементу
        self.scroll_to_element(locator)
        title = self.get_title_block_from_page_all(locator)
        return title

    @allure.step("Клик по кнопке Ask a Question в блоке FAQ")
    def click_button_in_faq(self):
        # ждем видимость блока
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.button_in_faq_locator)
        )
        # крутим страницу попиксельно до элемента
        position = element.location['y']
        self.driver.execute_script("window.scrollTo(0, arguments[0]);", position)
        # Дополнительное ожидание видимости кнопки
        click_button_faq = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.button_in_faq_locator)
        )
        # дополнительно проверяем видимость
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return arguments[0].getBoundingClientRect().top >= 0;",
                                                 click_button_faq)
        )
        # клик по кнопке через js
        self.driver.execute_script("arguments[0].click();", click_button_faq)