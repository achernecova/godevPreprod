import logging
import os

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage, put_a_secret
from test.locators import Locators


class WebDevelopPage(BasePage):

    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.team_card_more = None
        self.driver = driver
        self.subURL = os.getenv('WEBSITE_DEV', 'services/website-development/')



    @allure.step("Открытие страницы лендинга по URL: services/website-development/")
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

    def get_project_service_element(self):
        from page_elements.project_service_element import ProjectServiceElement
        return ProjectServiceElement(self.driver)


    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        logging.info('move cursor to element')

        wait = WebDriverWait(self.driver, 10)

        # Убедитесь, что элемент доступен
        locator = Locators.get_button_more_locator(index)
        self.team_card_more = wait.until(EC.presence_of_element_located(locator))

        if not self.team_card_more:
            raise ValueError(f"Кнопка 'More' по индексу {index} не найдена.")

        element = self.scroll_new(locator)  # Передаем locator вместо элемента

        # Используем JavaScript для клика по элементу
        self.driver.execute_script("arguments[0].click();", element)

        title_page = self.get_title_page()  # title_page теперь строка
        assert self.get_url() == page_url, f"Ожидался URL '{page_url}', но получен '{self.get_url()}'"
        assert title_page == page_title, f"Ожидался заголовок '{page_title}', но получен '{title_page}'"


    def click_button_in_faq(self):
        try:
            button_in_faq = self.scroll_new(Locators.button_in_faq_locator)
            if button_in_faq and button_in_faq.is_displayed() and button_in_faq.is_enabled():
                self.driver.execute_script("arguments[0].click();", button_in_faq)  # Используем JavaScript для клика
            else:
                print("Button is not available for clicking.")
        except Exception as e:
            print(f"Error clicking button: {str(e)}")
            raise  # Повторно выбрасываем исключение для дальнейшей обработки

    def get_popup(self):
        return PopupElement(self.driver)

    def get_data_card_website(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('WEBSITE_DEV', 'services/website-development/')
        self.get_data_card_(self.get_card_data, 'data_card_block_packages.json',
                            'web_site_develop_card_data', url)

    # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('WEBSITE_DEV', 'services/website-development/')
        self.get_data_advant_carousel(self.get_data_advant_section_carousel, 'advant_section_carousel.json',
                                      'advant_section_website', url)

    # получение данных с карточек с отзывами
    def get_data_review(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('WEBSITE_DEV', 'services/website-development/')
        self.get_data_review_(self.get_reviews_data_from_page, 'carousel_of_review.json', 'reviews-wrapper', url)

    # метод для faq
    def get_data_faq_card(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('WEBSITE_DEV', 'services/website-development/')
        self.get_data_card_with_type_project(
            'faq_block_data.json',
            self.get_data_faq_tiles_new,
            'faq_website_dev',
            "//*[@class='accordeon-body']",
            ".//*[@class='accordeon-question']",
            ".//*[@class='accordeon-subject-text']",
            url)

    # метод для черно-белых карточек
    def get_data_card_tiles_website(self):
        base_url = put_a_secret()
        url = base_url + os.getenv('WEBSITE_DEV', 'services/website-development/')
        self.get_data_card_with_type_project(
            'data_card_block_packages.json',
            self.get_data_faq_tiles_new,
            'tiles_section_card_data_website',
            "//*[contains(@class, 'tile w-')]",
            ".//h3",
            ".//span",
            url)
