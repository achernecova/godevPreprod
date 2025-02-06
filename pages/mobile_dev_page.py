import logging

from selenium.webdriver.common.by import By

from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement
from pages.base_page import BasePage

class MobileDevPage(BasePage):
    logging.basicConfig(level=logging.INFO)

    locators = {
        "button_in_card_select_locator": (By.XPATH, "//*[@class='info-card selected']//button"),
        "button_in_faq_locator": (By.XPATH, "//*[@class='faq-section']//button"),
        "input_name_locator": (By.XPATH, "//*[@class='request-offer-inputs']//input[@name='name']"),
        "input_email_locator": (By.XPATH, "//*[@class='request-offer-inputs']//input[@name='email']"),
        "input_comment_locator": (By.XPATH, "//*[@class='form-textarea']//*[@placeholder='Comment']"),
        "button_click_locator": (By.XPATH, "//*[@class='request-offer-bottom']//button"),
        "button_banner_locator": (By.XPATH, "//*[@class='banner']//button"),
        "topping_dev_button_locator": (By.XPATH, "//label[@class='topping'][@for='t11']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/mobile-development/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

    def get_popup(self):
        return PopupElement(self.driver)

    def click_button_banner(self):
        button_banner = self.wait_for_element(self.locators["button_banner_locator"])
        self.scroll_to_element(button_banner)
        button_banner.click()

    def click_button_in_card_select(self):
        button_in_card_select = self.wait_for_element(self.locators["button_in_card_select_locator"])
        self.scroll_to_element(button_in_card_select)
        button_in_card_select.click()

    def click_button_in_faq(self):
        button_in_faq = self.wait_for_element(self.locators["button_in_faq_locator"])
        self.scroll_to_element(button_in_faq)
        button_in_faq.click()



