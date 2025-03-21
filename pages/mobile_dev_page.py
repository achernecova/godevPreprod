import logging
import os

import allure

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage
from test.locators import Locators


class MobileDevPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('MOBILE_PAGE', 'services/mobile-development/')  # Значение по умолчанию


    @allure.step("Открытие мобильной страницы по URL: services/mobile-development/")
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

    def get_popup(self):
        return PopupElement(self.driver)


    def click_button_get_in_touch(self):
        try:
            button = self.scroll_new(Locators.button_in_card_select_locator)
            if button and button.is_displayed() and button.is_enabled():
                self.driver.execute_script("arguments[0].click();", button)  # Используем JavaScript для клика
            else:
                print("Button is not available for clicking.")
        except Exception as e:
            print(f"Error clicking button: {str(e)}")
            raise  # Повторно выбрасываем исключение для дальнейшей обработки


    @allure.step("Скролл до кнопки Get in touch в блоке Development cost")
    def click_button_in_develop_table(self):
        try:
            button = self.scroll_new(Locators.button_in_card_select_locator)
            if button and button.is_displayed() and button.is_enabled():
                self.driver.execute_script("arguments[0].click();", button)  # Используем JavaScript для клика
            else:
                print("Button is not available for clicking.")
        except Exception as e:
            print(f"Error clicking button: {str(e)}")
            raise  # Повторно выбрасываем исключение для дальнейшей обработки


    # Метод для получения заголовка блока
    @allure.step("Получение заголовка из блока What we do")
    def get_title_block_what_we_do(self):
        self.scroll_new(Locators.title_block_app_and_web_development_services_locator)
        title = self.get_title_block_from_page_all(Locators.title_block_app_and_web_development_services_locator)
        return title


    # тянем данные из названия блока What we do
    @allure.step("Получение текста из блока What we do")
    def get_text_block_what_we_do(self):
        self.scroll_new(Locators.text_block_app_and_web_development_services_locator)
        text = self.get_text_block_from_page_all(Locators.text_block_app_and_web_development_services_locator)
        return text


    # Метод для получения заголовка блока Stages of creating
    @allure.step("Получение заголовка из блока Stages of creating")
    def get_title_block_stages_of_creating(self):
        self.scroll_to_element(Locators.title_block_stages_of_creating_locator)
        title = self.get_title_block_from_page_all(Locators.title_block_stages_of_creating_locator)
        return title


    # тянем данные из названия блока Stages of creating
    @allure.step("Получение текста из блока Stages of creating")
    def get_text_block_stages_of_creating(self):
        self.scroll_new(Locators.text_block_stages_of_creating_locator)
        text = self.get_text_block_from_page_all(Locators.text_block_stages_of_creating_locator)
        return text


# метод для черно-белых карточек
    def get_data_card_tiles_mobile(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('MOBILE_PAGE', 'services/mobile-development/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_mobile',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)

    # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('MOBILE_PAGE', 'services/mobile-development/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                      'advant_card_mobile', url)


# метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_mobile(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('MOBILE_PAGE', 'services/mobile-development/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_mobile',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

# метод для faq
    def get_data_faq_card(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('MOBILE_PAGE', 'services/mobile-development/')
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_mobile',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)