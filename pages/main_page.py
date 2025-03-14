import logging
import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import URLs
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


    @allure.step(
        "Кликаем по кнопке в баннере")
    def click_button_banner(self):
        click_button_banner = self.driver.find_element(*Locators.click_button_banner)
        click_button_banner.click()


    @allure.step(
        "Кликаем по кнопке Get in touch")
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
        self.close_modal_popup()
        self.scroll_to_element(locator)  # Передаем локатор на скролл
        time.sleep(3)
        # Явное ожидание, что элемент станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

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
        url = URLs.MAIN_PAGE
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json',
                              'reviews-wrapper', url)

    # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = URLs.MAIN_PAGE
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                      'advant_section', url)

    # метод для черно-белых карточек
    def get_data_card_tiles_main(self):
        url = URLs.MAIN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_main',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_main(self):
        url = URLs.MAIN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_main',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

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
        self.scroll_to_element(locator)
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
    def get_title_block_web_dev_process (self):
        return self.get_title_block(Locators.title_block_website_dev_locator)


    @allure.step(
        "тянем текст из блока Web Development Process")
    def get_text_block_web_dev_process (self):
        return self.get_text_block(Locators.text_block_website_dev_locator)


    @allure.step(
        "тянем заголовок из блока Digital Agency Godev")
    def get_title_block_digital_agency_godev (self):
        return self.get_title_block(Locators.title_block_digital_agency_godev_locator)


    @allure.step(
        "тянем текст из блока Digital Agency Godev")
    def get_text_block_digital_agency_godev (self):
        return self.get_text_block(Locators.text_block_digital_agency_godev_locator)


    def get_data_card_app_and_web_services_main(self):
        url = URLs.MAIN_PAGE  # Укажите нужный URL
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'app_and_web_services_main',
            "//*[@class='service-item']",
            ".//*[@class='service-descr']",
            './/h3',
            url)