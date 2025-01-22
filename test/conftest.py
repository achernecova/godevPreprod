from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    print ("Before test")
    yield driver
    #driver.close()
    driver.quit()