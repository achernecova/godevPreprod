import logging

from selenium.webdriver.common.by import By

from pages.b2b_page import B2BPage
from pages.base_page import BasePage
from pages.e_com_page import EComPage
from pages.euro_vpn_project import ProjectEuroVpn
from pages.mobile_dev_page import MobileDevPage
from pages.project_find_a_builder import ProjectFindFBuilder
from pages.project_mint_link import ProjectMintLink
from pages.project_sls import ProjectSls
from pages.project_vegan_hotel import ProjectVeganHotel
from pages.support_pages import SupportPage
from pages.web_design_page import WebDesignPage
from pages.web_dev_services_page import WebDevServicesPage
from pages.web_develop_page import WebDevelopPage
from pages.web_outstaff_page import WebOutstaffPage


class ProjectServiceElement(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "button_banner_locator": (By.XPATH, "//*[@class='banner']//button"),
        "topping_dev_button": (By.XPATH, "//label[@class='topping'][@for='t11']"),
        "button_more_mobile_locator": (By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/mobile-development/']"),
        "button_more_web_site_dev_locator": (By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/website-development/']"),
        "button_more_supp_locator": (By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/tech-support/']"),
        "button_more_web_dev_locator": (By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/web-development/']"),
        "button_more_ecom_locator": (By.XPATH,"//*[@class='service-item']//a[@href='https://dev.godev.agency/services/website-development/e-commerce/']"),
        "button_more_design_locator": (By.XPATH,"//*[@class='service-item']//a[@href='https://dev.godev.agency/services/website-design-and-development-services/']"),
        "button_more_outstaff_locator": (By.XPATH,"//*[@class='service-item']//a[@href='https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/']"),
        "button_more_b2b_locator": (By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/website-development/b2b/']"),
        "button_more_section_outstaff": (By.XPATH, "//*[@class='section-header type-base ']//a"),

        "button_project_mint_link_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/projects/mint-links/']"),
        "button_project_sls_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/projects/swift-logistic-solutions/']"),
        "button_project_find_a_builder_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/projects/find-a-builder/']"),
        "button_project_vegan_hotel_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/projects/vegan-hotel/']"),
        "button_project_euro_VPN_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/projects/information-security-service/']"),
    }


    def test_click_card_and_open_page(self, card_type, expected_url, expected_title):
        self.close_modal_popup()
        card_mapping = {
            "website_dev": (self.click_button_more_web_site_dev_card, WebDevelopPage),
            "support": (self.click_button_more_supp_card, SupportPage),
            "web_development": (self.click_button_more_web_dev_card, WebDevServicesPage),
            "e_commerce": (self.click_button_more_ecom_card, EComPage),
            "website_design": (self.click_button_more_design_card, WebDesignPage),
            "outstaffing": (self.click_button_more_outstaff_card, WebOutstaffPage),
            "b2b": (self.click_button_more_b2b_card, B2BPage),
            "mobile_dev": (self.click_button_more_mobile_card, MobileDevPage),
            "section_outstaffing": (self.click_button_more_outstaff_card, WebOutstaffPage),

            "mint_link": (self.click_project_mint_link, ProjectMintLink),
            "sls": (self.click_project_sls, ProjectSls),
            "find_a_builder": (self.click_project_find_a_builder, ProjectFindFBuilder),
            "vegan_hotel": (self.click_project_vegan_hotel, ProjectVeganHotel),
            "euro_VPN": (self.click_project_euro_VPN, ProjectEuroVpn)

        }
        if card_type not in card_mapping:
            raise ValueError("Неверный тип карточки")
        click_method, page_class = card_mapping[card_type]
        click_method()
        page = page_class(self.driver)
        assert self.driver.current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{self.driver.current_url}'"
        assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

    def click_project_mint_link(self):
        button_project_mint_link = self.wait_for_element(self.locators["button_project_mint_link_locator"])
        self.scroll_to_element(button_project_mint_link)
        button_project_mint_link.click()

    def click_project_sls(self):
        button_project_sls = self.wait_for_element(self.locators["button_project_sls_locator"])
        self.scroll_to_element(button_project_sls)
        button_project_sls.click()

    def click_project_find_a_builder(self):
        button_project_find_a_builder = self.wait_for_element(self.locators["button_project_find_a_builder_locator"])
        self.scroll_to_element(button_project_find_a_builder)
        button_project_find_a_builder.click()

    def click_project_vegan_hotel(self):
        button_project_vegan_hotel = self.wait_for_element(self.locators["button_project_vegan_hotel_locator"])
        self.scroll_to_element(button_project_vegan_hotel)
        button_project_vegan_hotel.click()

    def click_project_euro_VPN(self):
        button_project_euro_VPN = self.wait_for_element(self.locators["button_project_euro_VPN_locator"])
        self.scroll_to_element(button_project_euro_VPN)
        button_project_euro_VPN.click()

    def click_button_more_mobile_card(self):
        mobile_card_button = self.wait_for_element(self.locators["button_more_mobile_locator"])
        self.scroll_to_element(mobile_card_button)
        mobile_card_button.click()

    def click_button_more_web_site_dev_card(self):
        button_more_web_site_dev_card = self.wait_for_element(self.locators["button_more_web_site_dev_locator"])
        self.scroll_to_element(button_more_web_site_dev_card)
        button_more_web_site_dev_card.click()

    def click_button_more_supp_card(self):
        button_more_supp_card = self.wait_for_element(self.locators["button_more_supp_locator"])
        self.scroll_to_element(button_more_supp_card)
        button_more_supp_card.click()

    def click_button_more_web_dev_card(self):
        button_more_web_dev_card = self.wait_for_element(self.locators["button_more_web_dev_locator"])
        self.scroll_to_element(button_more_web_dev_card)
        button_more_web_dev_card.click()

    def click_button_more_ecom_card(self):
        button_more_ecom_card = self.wait_for_element(self.locators["button_more_ecom_locator"])
        self.scroll_to_element(button_more_ecom_card)
        button_more_ecom_card.click()

    def click_button_more_design_card(self):
        button_more_design_card = self.wait_for_element(self.locators["button_more_design_locator"])
        self.scroll_to_element(button_more_design_card)
        button_more_design_card.click()

    def click_button_more_outstaff_card(self):
        button_more_outstaff_card = self.wait_for_element(self.locators["button_more_outstaff_locator"])
        self.scroll_to_element(button_more_outstaff_card)
        button_more_outstaff_card.click()

    def click_button_more_b2b_card(self):
        logging.info('move cursor to element')
        element_more_b2b = self.wait_for_element(self.locators["button_more_b2b_locator"])
        self.scroll_to_element(element_more_b2b)
        element_more_b2b.click()
