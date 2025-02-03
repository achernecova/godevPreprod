from selenium.webdriver.common.by import By
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData
from page_elements.popup_element import PopupElement

from pages.base_page import BasePage
from pages.euro_vpn_project import ProjectEuroVpn
from pages.project_find_a_builder import ProjectFindFBuilder
from pages.project_mint_link import ProjectMintLink
from pages.project_sls import ProjectSls
from pages.project_vegan_hotel import ProjectVeganHotel

class SupportPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/tech-support/')  # Добавляем под-URL

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_title_page(self):
        title_page = self.driver.find_element(By.XPATH, "//h1")
        return title_page.text

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
        button_tariff = self.driver.find_element(By.XPATH, "(//*[@class='service-last-row']//button)[1]")
        self.scroll_to_element(button_tariff)
        button_tariff.click()



