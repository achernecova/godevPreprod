from selenium.webdriver.support import expected_conditions as EC
from page_elements import form_page
from page_elements.block_count_elements import CountElements
from page_elements.form_page import FormPage
from page_elements.meta_data_page import MetaData

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_elements.popup_element import PopupElement
from pages.B2BPage import B2BPage
from pages.EComPage import EComPage
from pages.mobile_dev_page import MobileDevPage
from pages.euro_vpn_project import project_euro_vpn
from pages.project_find_a_builder import project_find_a_builder
from pages.project_mint_link import project_mint_link
from pages.project_sls import project_sls
from pages.project_vegan_hotel import project_vegan_hotel
from pages.support_page import support_page
from pages.web_design_page import web_design_page
from pages.WebDevServicesPage import WebDevServicesPage
from pages.WebDevelopPage import WebDevelopPage
from pages.web_outstaff_page import web_outstaff_page


class MainPage:

    def __init__(self, driver):
        self.count_card_count = None
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/')

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

    def click_button_banner(self):
        button_banner = self.driver.find_element(By.XPATH, "//*[@class='banner']//button")
        button_banner.click()

    def click_topping_dev_banner(self):
        topping_dev_button = self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t11']")
        topping_dev_button.click()

    def input_name_in_banner(self):
        input_name = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='name']")
        input_name.send_keys("Test name")

    def input_email_in_banner(self):
        input_email = self.driver.find_element(By.XPATH, "//*[@class='request-offer-inputs']//input[@name='email']")
        input_email.send_keys("testPochta@test.ru")

    def input_comment_in_banner(self):
        input_comment = self.driver.find_element(By.XPATH, "//*[@class='form-textarea']//*[@placeholder='Comment']")
        input_comment.send_keys("Тестовый комментарий")

    def click_button_in_banner(self):
        button_click = self.driver.find_element(By.XPATH, "//*[@class='request-offer-bottom']//button")
        button_click.click()

    def click_button_in_header(self):
        button_header_click = self.driver.find_element(By.XPATH, "//*[@class='right']//button")
        button_header_click.click()

    def click_topping_analysts_banner(self):
        topping_analysts_button = self.driver.find_element(By.XPATH, "//label[@class='topping'][@for='t14']")
        topping_analysts_button.click()



    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def click_button_more_mobile_card(self):
        button_more_mobile_card = self.driver.find_element(By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/mobile-development/']")
        self.scroll_to_element(button_more_mobile_card)
        button_more_mobile_card.click()

    def click_button_more_web_site_dev_card(self):
        button_more_web_site_dev_card = self.driver.find_element(By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/website-development/']")
        self.scroll_to_element(button_more_web_site_dev_card)
        button_more_web_site_dev_card.click()

    def click_button_more_supp_card(self):
        button_more_supp_card = self.driver.find_element(By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/tech-support/']")
        self.scroll_to_element(button_more_supp_card)
        button_more_supp_card.click()

    def click_button_more_web_dev_card(self):
        button_more_web_dev_card = self.driver.find_element(By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/web-development/']")
        self.scroll_to_element(button_more_web_dev_card)
        button_more_web_dev_card.click()

    def click_button_more_ecom_card(self):
        button_more_ecom_card = self.driver.find_element(By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/website-development/e-commerce/']")
        self.scroll_to_element(button_more_ecom_card)
        button_more_ecom_card.click()

    def click_button_more_design_card(self):
        button_more_design_card = self.driver.find_element(By.XPATH, "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/website-design-and-development-services/']")
        self.scroll_to_element(button_more_design_card)
        button_more_design_card.click()

    def click_button_more_outstaff_card(self):
        print('move cursor to element')
        button_more_outstaff_card = self.driver.find_element(By.XPATH,
                                                              "//*[@class='service-item']//a[@href='https://dev.godev.agency/services/outstaffing-and-outsourcing-of-it-specialists/']")
        self.scroll_to_element(button_more_outstaff_card)
        button_more_outstaff_card.click()

    def click_button_more_b2b_card(self):
        print('move cursor to element')
        element_more_b2b = self.driver.find_element(By.XPATH,
                                                  "//*[@class='service-item']"+"//a[@href='https://dev.godev.agency/services/website-development/b2b/']")
        self.scroll_to_element(element_more_b2b)
        element_more_b2b.click()

    def click_button_more_section_outstaff(self):
        print('move cursor to element')
        element_more_section_outstaff = self.driver.find_element(By.XPATH, "//*[@class='section-header type-base ']//a")
        self.scroll_to_element(element_more_section_outstaff)
        element_more_section_outstaff.click()

    def click_euro_vpn_project(self):
        print('move cursor to element')
        euro_vpn_project = self.driver.find_element(By.XPATH, "(//*[@class='projects-title'])[1]")
        self.scroll_to_element(euro_vpn_project)
        euro_vpn_project.click()

    def click_vegan_hotel_project(self):
        print('move cursor to element')
        vegan_hotel_project = self.driver.find_element(By.XPATH, "(//*[@class='projects-title'])[2]")
        self.scroll_to_element(vegan_hotel_project)
        vegan_hotel_project.click()

    def click_find_a_builder_project(self):
        print('move cursor to element')
        find_a_builder_project = self.driver.find_element(By.XPATH, "(//*[@class='projects-title'])[3]")
        self.scroll_to_element(find_a_builder_project)
        find_a_builder_project.click()

    def click_mint_link_project(self):
        print('move cursor to element')
        mint_link_project = self.driver.find_element(By.XPATH, "(//*[@class='projects-title'])[5]")
        self.scroll_to_element(mint_link_project)
        mint_link_project.click()

    def click_sls_project(self):
        print('move cursor to element')
        sls_project = self.driver.find_element(By.XPATH, "(//*[@class='projects-title'])[4]")
        self.scroll_to_element(sls_project)
        sls_project.click()

    def click_project(self, index):
        print('move cursor to element')
        project = self.driver.find_element(By.XPATH, "(//*[@class='projects-title'])["+index+"]")
        self.scroll_to_element(project)
        project.click()

    def popup_success_displayed(self, timeout=10):
        try:
            # Ожидание видимости элемента с указанным XPath
            popup_success = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@class='sendmail-popup success']"))
            )
            return popup_success.is_displayed()
        except (NoSuchElementException, TimeoutException):
            # Если элемент не найден или не виден в течение указанного времени, возвращаем False
            return False

    def test_click_card_and_open_page(self, card_type, expected_url, expected_title):
        if card_type == "website_dev":
            self.click_button_more_web_site_dev_card()
            page = WebDevelopPage(self.driver)
        elif card_type == "support":
            self.click_button_more_supp_card()
            page = support_page(self.driver)
        elif card_type == "web_development":
            self.click_button_more_web_dev_card()
            page = WebDevServicesPage(self.driver)
        elif card_type == "e_commerce":
            self.click_button_more_ecom_card()
            page = EComPage(self.driver)
        elif card_type == "website_design":
            self.click_button_more_design_card()
            page = web_design_page(self.driver)
        elif card_type == "outstaffing" or card_type == "section_outstaffing":
            self.click_button_more_outstaff_card()
            page = web_outstaff_page(self.driver)
        elif card_type == "b2b":
            self.click_button_more_b2b_card()
            page = B2BPage(self.driver)
        elif card_type == "mobile_dev":
            self.click_button_more_mobile_card()
            page = MobileDevPage(self.driver)
        else:
            raise ValueError("Неверный тип карточки")

        assert self.get_url() == expected_url, f"Ожидался URL '{expected_url}', но получен '{self.driver.current_url}'"
        assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"

    def test_click_project_and_open_page(self, project_type, expected_url, expected_title):
        if project_type == "euro_VPN":
            self.click_euro_vpn_project()
            page = project_euro_vpn(self.driver)
        elif project_type == "vegan_hotel":
            self.click_vegan_hotel_project()
            page = project_vegan_hotel(self.driver)
        elif project_type == "find_a_builder":
            self.click_find_a_builder_project()
            page = project_find_a_builder(self.driver)
        elif project_type == "sls":
            self.click_sls_project()
            page = project_sls(self.driver)
        elif project_type == "mint_link":
            self.click_mint_link_project()
            page = project_mint_link(self.driver)
        else:
            raise ValueError("Неверный тип карточки")
        assert page.get_url() == expected_url, f"Ожидался URL '{expected_url}', но получен '{self.driver.current_url}'"
        assert page.get_title_page() == expected_title, f"Получен Title: {page.get_title_page()}"



    def check_packages_data(self, project_type, experience, bullits, price, index):
        print('move cursor to element')
        team_card = self.driver.find_element(By.XPATH, "(//*[@class='team-card'])["+index+"]")
        self.scroll_to_element(team_card)
        self.project_title = self.driver.find_element(By.XPATH, "(//*[@class='team-card-title']//*[@class='exp'])["+index+"]")
        self.project_bullits = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='level'])["+index+"]")
        self.project_name = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//*[@class='spec fs24'])[" + index + "]")
        self.project_price = self.driver.find_element(By.XPATH, "(//*[@class='price'])[" + index + "]")
        assert self.project_title.text == experience, f"Ожидался заголовок '{experience}', но получен '{self.project_title.text}'"
        assert self.project_bullits.text == bullits, f"Ожидался заголовок '{bullits}', но получен '{self.project_bullits.text}'"
        assert self.project_name.text == project_type, f"Ожидался заголовок '{project_type}', но получен '{self.project_name.text}'"
        assert self.project_price.text == price, f"Ожидался заголовок '{price}', но получен '{self.project_price.text}'"

    def click_more_packages_and_data_pages(self, index, page_url, page_title):
        print('move cursor to element')
        self.team_card_more = self.driver.find_element(By.XPATH, "(//*[@class='team-card']//a[@class='more'])["+index+"]")
        self.scroll_to_element(self.team_card_more)
        self.team_card_more.click()
        self.title_page = self.driver.find_element(By.XPATH, "//h1")
        assert self.get_url() == page_url, f"Ожидался заголовок '{page_url}', но получен '{self.get_url()}'"
        assert self.title_page.text == page_title, f"Ожидался заголовок '{page_title}', но получен '{self.title_page.text}'"
