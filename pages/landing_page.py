from pages.base_page import BasePage
from constants import URLs, subURLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/development-of-a-landing-page/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)

        # метод для цветных карточек
    def get_data_card_tile_squad(self):
        url = URLs.MAIN_PAGE + subURLs.LANDING  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tile_squad, 'data_card_block_packages.json',
                                                 'tile_squad', url)

        # метод для черно-белых карточек с кружками и порядковыми номерами
    def get_data_card_how_it_staff_landing(self):
        url = URLs.MAIN_PAGE+subURLs.LANDING  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_card_data_tiles_card, 'section_how_it_staff_tiles.json',
                                                 'how_it_staff_landing', url)

        # метод для карусели адвант
    def get_data_advant_carousel_card(self):
        url = URLs.MAIN_PAGE+subURLs.LANDING
        self.get_data_advant_carousel(self.get_data_advant_section_carousel,'advant_section_carousel.json', 'advant_section_landing', url)