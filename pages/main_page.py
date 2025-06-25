import logging
import os
import time
from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.menu_element import MenuElement
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage, put_a_secret
from test.locators import Locators
from utils.data_loader import load_file


class MainPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.driver = driver

    @allure.step("Открытие главной страницы")
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

    @allure.step(
        "Проверяем заголовок и урл после клика по кнопке More")
    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')
        locator = Locators.get_team_card_more_locator(index)
        self.scroll_to_element(locator)  # Передаем локатор на скролл

        # Явное ожидание, что элемент станет кликабельным
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        WebDriverWait(self.driver, 5).until(lambda d: self.is_element_in_viewport(button))

        self.team_card_more = self.driver.find_element(*locator)  # Найти элемент
        self.driver.execute_script("arguments[0].click();", self.team_card_more)

        # Получаем заголовок страницы
        self.title_page = self.driver.find_element(*Locators.title_page)

        # Проверяем совпадение URL и заголовка
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"


    @allure.step(
        "Проверяем заголовок из карусели")
    def get_data_title_carousel(self):
        # грузим данные из json
        data = load_file('carousel_of_review.json')
        # получаем описания со страницы
        title_block_from_page = self.get_title_block_from_page_all(Locators.title_element)
        # берем данные из секции reviews_wrapper
        reviews_wrapper = data['reviews-wrapper']
        # отладочное.
        logging.info(f"Заголовок из JSON: " + reviews_wrapper['title'])
        logging.info(f"Заголовок на странице: {title_block_from_page}")
        # проверяем данные
        assert reviews_wrapper['title'] in title_block_from_page, \
            f"Заголовок не найден на странице: {reviews_wrapper['title']}"

    # получение данных с карточек с отзывами
    def get_data_review(self):
        base_url = put_a_secret()
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json',
                              'reviews-wrapper', base_url)

    # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        base_url = put_a_secret()
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                      'advant_section', base_url)

    @allure.step(
        "Получаем заголовок блока")
    def get_title_block(self, locator):
        # Сначала сделаем скролл к элементу
        self.scroll_to_element(locator)
        title = self.get_title_block_from_page_all(locator)
        return title

    @allure.step(
        "Проверяем текст из карусели")
    def get_text_block(self, locator):
        text = self.get_text_block_from_page_all(locator)
        return text

    # Используем объединенные методы
    def get_title_block_app_and_web_development_services(self):
        return self.get_title_block(Locators.title_block_app_and_web_development_services_locator)

    def get_text_block_app_and_web_development_services(self):
        return self.get_text_block(Locators.text_block_app_and_web_development_services_locator)

    def get_title_block_it_staff(self):
        return self.get_title_block(Locators.title_block_custom_design_solutions_locator)

    def get_text_block_it_staff(self):
        return self.get_text_block(Locators.text_block_it_staff_locator)

    @allure.step(
        "тянем заголовок из блока Web Development Process")
    def get_title_block_web_dev_process(self):
        return self.get_title_block(Locators.title_block_website_dev_locator)

    @allure.step(
        "тянем текст из блока Web Development Process")
    def get_text_block_web_dev_process(self):
        return self.get_text_block(Locators.text_block_website_dev_locator)

    @allure.step(
        "тянем заголовок из блока Digital Agency Godev")
    def get_title_block_digital_agency_godev(self):
        return self.get_title_block(Locators.title_block_digital_agency_godev_locator)

    @allure.step(
        "тянем текст из блока Digital Agency Godev")
    def get_text_block_digital_agency_godev(self):
        return self.get_text_block(Locators.text_block_digital_agency_godev_locator)

    """
    Метод для определения атрибутов шрифта блока: цвет, сам шрифт, размер
    click_body_element() - метод для клика в пустой области страницы.
    Тянем данные из json файла, в который внесены все шрифты с атрибутикой. 
    Вытаскиваем данные со страницы через обращения к атрибутам (например, value_of_css_property("color"))
    """
    @allure.step(
        "загружаем данные из json и тянем данные со страницы через обращение к атрибутам элемента")
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