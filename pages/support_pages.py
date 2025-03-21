import logging
import os

import allure

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage
from test.locators import Locators


class SupportPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subURL = os.getenv('SUPPORT_PAGE', 'services/tech-support/')


    def get_popup(self):
        return PopupElement(self.driver)

    @allure.step("Открытие страницы лендинга по URL: services/tech-support/")
    def open(self, sub_url=None):
        """Открывает мобильную страницу. Если sub_url не передан, используется subURL по умолчанию."""
        if sub_url is None:  # Если sub_url не указан, используем стандартный
            sub_url = self.subURL
        allure.step(f"Открытие мобильной страницы по URL: {sub_url}")
        logging.info(f"Открываем страницу: {sub_url}")
        super().open(sub_url)  # Вызов метода open() из базового класса с под-URL


    def get_form_page(self):
        return FormPage(self.driver)

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_popup_element(self):
        return PopupElement(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)

    def click_button_tariff_table(self):
        try:
            button_tariff = self.scroll_new(Locators.button_tariff)
            if button_tariff and button_tariff.is_displayed() and button_tariff.is_enabled():
                self.driver.execute_script("arguments[0].click();", button_tariff)  # Используем JavaScript для клика
            else:
                print("Button is not available for clicking.")
        except Exception as e:
            print(f"Error clicking button: {str(e)}")
            raise  # Повторно выбрасываем исключение для дальнейшей обработки

# метод для черно-белых карточек
    def get_data_card_tiles_support(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('SUPPORT_PAGE', 'services/tech-support/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_support',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)


# метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_support(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('SUPPORT_PAGE', 'services/tech-support/')
        self.get_data_card_with_type_project(
            'section_how_it_staff_tiles.json',
            self.get_card_data_tiles_card,
            'how_it_staff_support',
            "//*[@class='card']",
            './/p',
            ".//h3[@class='card-title']",
            url)

# метод для faq
    def get_data_faq_card(self):
        url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/') + os.getenv('SUPPORT_PAGE', 'services/tech-support/')
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_support',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)