from allure_commons._allure import link, feature
import pytest
from pages.landing_page import LandingPage

from utils.data_loader import load_package_data_main
from utils.page_factory import get_page_instance


@feature('Проверка данных в карточках блока Web Development Process')
def test_landing_page_web_development_process_data_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_card_tile_squad()



@feature('Проверка данных в карточках блока How a landing page helps your business')
def test_landing_page_why_do_you_need_data_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_card_how_it_staff_landing()


@feature('Проверка данных в карточках блока Work process')
def test_landing_page_web_development_process_data_assert(driver):
    landing_page_test = LandingPage(driver)
    landing_page_test.open()
    landing_page_test.get_data_advant_carousel_card()