from test.locators import Locators


class ProjectEuroVpn:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/projects/information-security-service/')

    def get_title_page(self):
        title_page = self.driver.find_element(*Locators.title_page)
        return title_page.text