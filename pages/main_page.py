import logging

import requests
from bs4 import BeautifulSoup

from constants import URLs, subURLs
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.menu_element import MenuElement
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage
from test.locators import Locators
from utils.data_loader import load_file


class MainPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.driver = driver

    def click_button_banner(self):
        click_button_banner = self.driver.find_element(*Locators.click_button_banner)
        click_button_banner.click()

    def open(self):
        super().open('')  # Добавляем под-URL

    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_menu_element(self):
        return MenuElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        self.team_card_more = self.driver.find_element(*Locators.get_team_card_more_locator(index))
        self.scroll_to_element(self.team_card_more)
        self.team_card_more.click()
        self.title_page = self.driver.find_element(*Locators.title_page)
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"


    def get_data_title_carousel(self):
        # грузим данные из json
        data = load_file('carousel_of_review.json')

        # получаем описания со страницы
        title_block_from_page = self.get_title_block_from_page(URLs.MAIN_PAGE)

        # берем данные из секции reviews_wrapper
        reviews_wrapper = data['reviews-wrapper']
        # отладочное.
        logging.info(f"Заголовок из JSON: " + reviews_wrapper['title'])
        logging.info(f"Заголовок на странице: {title_block_from_page}")
        # проверяем данные
        assert reviews_wrapper['title'] in title_block_from_page, \
            f"Заголовок не найден на странице: {reviews_wrapper['title']}"


    # тянем данные из названия блока
    def get_title_block_from_page(self, url):
        title_element = self.driver.find_element(*Locators.title_element)

        if title_element is not None:
            title_text = title_element.text.strip()
            logging.info(f"Заголовок на странице: '{title_text}'")
            return title_text
        else:
            logging.error('Ошибка!!! Заголовок не найден.')
            return 'Ошибка!!!'


    # Объединяем три метода в один
    def get_reviews_data_from_page(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение всех элементов с классом 'review-card'
        reviews_data = []
        type_section = soup.find_all(class_='review-card')

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

    # переделываем метод
    def get_data_carousel_reviews(self):
        # Загрузите данные из JSON
        data = load_file('carousel_of_review.json')

        # получаем данные из блока карусели на странице
        reviews_data_from_page = self.get_reviews_data_from_page(URLs.MAIN_PAGE)
        logging.info(f'Полученные данные с страницы: {reviews_data_from_page}')

        # смотрим, что каждое описание из JSON присутствует на странице
        descriptions = data['reviews-wrapper']['descriptions']
        logging.info(f'Заголовок из JSON: {str(descriptions)}')

        for desc in descriptions:
            print("Компания: " + str({desc['author_company']}))
            print("Автор: " + str({desc['author_name']}))
            print("Текст отзыва: " + str({desc['text']}))
            assert desc['text'] in [review['text'] for review in reviews_data_from_page], f"Текст не найден на странице: {desc['text']}"
            assert desc['author_company'].strip() in [review['author_company'] for review in reviews_data_from_page], f"Организация не найдена на странице: {desc['author_company']}"
            assert desc['author_name'] in [review['author_name'] for review in reviews_data_from_page], f"Автор не найден на странице: {desc['author_name']}"



# метод для черно-белых карточек
    def get_data_card_tiles_main(self):
        url = URLs.MAIN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tiles, 'data_card_block_packages.json',
                                    'tiles_section_card_data_main', url)

# метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_main(self):
        url = URLs.MAIN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tiles_card, 'section_how_it_staff_tiles.json',
                                    'how_it_staff_main', url)



# метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = URLs.MAIN_PAGE
        self.get_data_advant_carousel(self.get_data_advant_section_carousel,'advant_section_carousel.json','advant_section', url)