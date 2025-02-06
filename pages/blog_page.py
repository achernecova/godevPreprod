import logging

from selenium.webdriver.common.by import By

from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage


class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('blog/')  # Добавляем под-URL

    def get_date_blog(self):
        date_blog = self.driver.find_element(By.XPATH, "//*[@class= 'blog-single-banner__date']")
        return date_blog.text

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


    def click_block_page(self, index, side, page_url, page_title, date_blog):
        logging.info('move cursor to element')
        self.close_modal_popup()

        block_class = 'blog__block-right' if side == 'right' else 'blog__block-left--item'
        element = self.driver.find_element(By.XPATH, f"(//*[contains(@class, '{block_class}')])[{index}]")

        self.scroll_to_element(element)
        self._click_element(element)

        title_page = self.driver.find_element(By.XPATH, "//h1")

        assert self.get_url() == page_url, f"Ожидался URL '{page_url}', но получен '{self.get_url()}'"
        assert title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{title_page.text}'"
        assert self.get_date_blog() == date_blog, f"Ожидалась дата '{date_blog}', но получен '{self.get_date_blog()}'"