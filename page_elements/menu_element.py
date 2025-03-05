from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from test.locators import Locators


class MenuElement(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "menu_service_locator": (By.XPATH, "//*[@class='menu-wrapper']//a[@href= 'https://dev.godev.agency/services/']"),
        "menu_project_locator": (By.XPATH, "//*[@class='menu-wrapper']//a[@href= 'https://dev.godev.agency/projects/']"),
        "menu_reviews_locator": (By.XPATH, "//*[@class='menu-wrapper']//a[@href= 'https://dev.godev.agency/reviews/']"),
        "menu_contacts_locator": (By.XPATH, "//*[@class='menu-wrapper']//a[@href= 'https://dev.godev.agency/contacts/']"),
        "submenu_outstaff_outsource_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/']"),
        "submenu_mobile_development_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/mobile-development/']"),
        "submenu_web_site_dev_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/website-development/']"),
        "submenu_web_development_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/web-development/']"),
        "submenu_tech_support_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/tech-support/']"),
        "submenu_e_com_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/website-development/e-commerce/']"),
        "submenu_cms_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/website-development/cms/']"),
        "submenu_framework_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/website-development/framework/']"),
        "submenu_b2b_locator": (By.XPATH, "//*[@href= 'https://dev.godev.agency/services/website-development/b2b/']"),
        "submenu_landing_locator": (By.XPATH, "//*[@href= '/services/development-of-a-landing-page/']")
    }

    def click_menu_service(self):
        self._click_element(self.locators["menu_service_locator"])

    def click_menu_project(self):
        self._click_element(self.locators["menu_project_locator"])

    def click_menu_reviews(self):
        self._click_element(self.locators["menu_reviews_locator"])

    def click_menu_contacts(self):
        self._click_element(self.locators["menu_contacts_locator"])

    def click_submenu_outstaff(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        self._click_element(self.locators["submenu_outstaff_outsource_locator"])

    def click_submenu_mobile_dev(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        self._click_element(self.locators["submenu_mobile_development_locator"])

    def click_submenu_web_site_dev(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        self._click_element(self.locators["submenu_web_site_dev_locator"])

    def click_submenu_web_dev(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        self._click_element(self.locators["submenu_web_development_locator"])

    def click_submenu_tech_support(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        self._click_element(self.locators["submenu_tech_support_locator"])

    def click_submenu_e_com(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        submenu_web_site_dev_locator = self.wait_for_element(self.locators["submenu_web_site_dev_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        action.move_to_element(submenu_web_site_dev_locator).perform()
        self._click_element(self.locators["submenu_e_com_locator"])

    def click_submenu_cms(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        submenu_web_site_dev_locator = self.wait_for_element(self.locators["submenu_web_site_dev_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        action.move_to_element(submenu_web_site_dev_locator).perform()
        self._click_element(self.locators["submenu_cms_locator"])

    def click_submenu_framework(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        submenu_web_site_dev_locator = self.wait_for_element(self.locators["submenu_web_site_dev_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        action.move_to_element(submenu_web_site_dev_locator).perform()
        self._click_element(self.locators["submenu_framework_locator"])

    def click_submenu_b2b(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        submenu_web_site_dev_locator = self.wait_for_element(self.locators["submenu_web_site_dev_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        action.move_to_element(submenu_web_site_dev_locator).perform()
        self._click_element(self.locators["submenu_b2b_locator"])


    def click_submenu_landing(self):
        menu_service_locator = self.wait_for_element(self.locators["menu_service_locator"])
        submenu_web_site_dev_locator = self.wait_for_element(self.locators["submenu_web_site_dev_locator"])
        action = ActionChains(self.driver)
        action.move_to_element(menu_service_locator).perform()
        action.move_to_element(submenu_web_site_dev_locator).perform()
        element = self.driver.find_element(*Locators.button_landing_locator)
        element.click()
        #self._click_element(element)
