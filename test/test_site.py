
from pages.homePage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product = ProductPage(driver)
    product.check_title_is('Samsung galaxy s6')

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    homepage.check_products_count(2)
