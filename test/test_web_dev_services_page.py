import allure
import pytest
from allure_commons._allure import feature

from pages.web_dev_services_page import WebDevServicesPage

# тест с мета-тегами вынесен в main_page_test

@feature('Количество элементов в блоке')
def test_web_dev_serv_page_count_card_services(driver):
    web_dev_serv_page = WebDevServicesPage(driver)
    web_dev_serv_page.open()
    blocks = web_dev_serv_page.get_count_elements()
    blocks.count_cards_assert("web_dev_services", 12)

@pytest.mark.parametrize("index, project_type, price", [
    (0, "Web App development", "3000 $\nfrom"),
    (1, "Design and redesign", "1000 $\nfrom"),
    (2, "E-Commerce Web Development", "3000 $\nfrom "),
    (3, "CMS-based projects", "2000 $\nfrom "),
    (4, "Technical assistance and web project scaling", "600 $\nfrom "),
    (5, "Frontend development", "30 $\n/ hour"),
    (6, "Backend development", "30 $\n/ hour"),
    (7, "UI design", "1000 $\nfrom "),
    (8, "UX development", "1000 $\nfrom "),
    (9, "Performance optimization", "600 $\nfrom "),
    (10, "Web App security", "100 $\nfrom "),
    (11, "Testing", "28 $\n/ hour")
])
def test_web_dev_serv_page_data_card_packages(driver, index, project_type, price):
    web_dev_serv_page = WebDevServicesPage(driver)
    web_dev_serv_page.open()
    blocks = web_dev_serv_page.get_count_elements()
    blocks.check_packages_data_services(index, project_type, price)



@allure.feature('Проверка данных в карточках блока Advantages of choosing Godev for website development')
def test_web_dev_serv_page_benefits_count_cards_assert(driver):
    web_dev_serv_page = WebDevServicesPage(driver)
    web_dev_serv_page.open()
    web_dev_serv_page.get_data_card_tiles_webdev()



@allure.feature('Проверка данных в FAQ')
def test_web_dev_serv_page_faq_data_assert(driver):
    web_dev_serv_page = WebDevServicesPage(driver)
    web_dev_serv_page.open()
    web_dev_serv_page.get_data_faq_card()