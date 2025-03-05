from selenium.webdriver.common.by import By

from constants import URLs, subURLs
from page_elements.block_count_elements import CountElements
from page_elements.meta_data_page import MetaData
from pages.base_page import BasePage
from utils.data_loader import load_file


class WebDevServicesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        super().open('services/web-development/')  # Добавляем под-URL

    def get_meta_data(self):
        return MetaData(self.driver)

    def get_count_elements(self):
        return CountElements(self.driver)




# метод для черно-белых карточек
 # переделываем метод
    def get_data_card_tiles_webdev(self):
        # Загрузите данные из JSON
        data = load_file('data_card_block_packages.json')

        # Получаем данные из блока карусели на странице
        card_data_data_from_page = self.get_card_data_tiles(URLs.MAIN_PAGE+subURLs.WEB_DEV)

        # Выводим полученные данные с веб-страницы
        print("Полученные данные с веб-страницы:")
        for review in card_data_data_from_page:
            print(review)

        # Смотрим, что каждое описание из e_com_card_data присутствует на странице
        descriptions = data['tiles_section_card_data_webdev']['descriptions']

        # Выводим данные из JSON
        print("Данные из JSON:")
        for desc in descriptions:
            print(desc)

        for desc in descriptions:
            # Обработаем каждое описание из e_com_card_data
            # Проверяем все
            found = any(
                review['project_type'].strip() == desc['project_type'].strip() and
                review['text'].strip() == desc['text'].strip()
                for review in card_data_data_from_page
            )

            assert found, f"Данные из JSON не найдены на странице для: {desc['project_type']} | {desc['text']} "


# метод для faq
    def get_data_faq_card(self):
        url = URLs.MAIN_PAGE + subURLs.WEB_DEV  # Укажите нужный URL
        self.get_data_card_with_type_project(self.get_data_faq, 'faq_block_data.json', 'faq_web_dev', url)